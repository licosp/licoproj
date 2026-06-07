import type { Plugin } from "@opencode-ai/plugin";
import { exec } from "child_process";
import { randomUUID } from "crypto";
import * as fs from "fs";
import * as path from "path";
import { promisify } from "util";

const execAsync = promisify(exec);

/**
 * [Execution Timing]
 * Called *every time* an event is fired, right before passing data to Python.
 *
 * Safely writes the event data to a temporary file (JSON) and returns
 * a UUID-based file path to completely prevent race conditions.
 */
function createPayloadFile(event: any, eventsDir: string): string {
  const eventId = randomUUID();
  const payloadFile = path.join(eventsDir, `event_payload_${eventId}.json`);
  const payload = JSON.stringify(event, null, 2);

  fs.writeFileSync(payloadFile, payload);
  return payloadFile;
}

/**
 * Returns a JST (+09:00) formatted timestamp: YYYY-MM-DDTHH:MM:SS+09:00
 */
function getTimestamp(): string {
  const d = new Date();
  d.setUTCHours(d.getUTCHours() + 9);
  return `${d.toISOString().substring(0, 19)}+09:00`;
}

/**
 * Helper to safely log TS-side fallback errors.
 */
function logError(logFile: string, label: string, error: any): void {
  const timestamp = getTimestamp();
  const errorMsg = `[${timestamp}] ERROR [lico_observer.plugin]\n(${label}) ${error?.message || String(error)}\n`;
  try {
    fs.appendFileSync(logFile, errorMsg);
  } catch (e) {
    // Final fallback if even the log file couldn't be created
  }
}

export const MyPlugin: Plugin = async () => {
  const workspacePath = process.cwd();
  const opencodeTempDir = path.join(workspacePath, ".temp", "opencode");
  const eventsDir = path.join(opencodeTempDir, "events");
  const logFile = path.join(opencodeTempDir, "plugin-debug.log");

  try {
    // One-time initialization. Delegation of directory creation and log resetting to Python.
    await execAsync(`uv run lico-observer-opencode --init`);
  } catch (error: any) {
    logError(logFile, "Initialization Error", error);
  }

  return {
    event: async ({ event }) => {
      try {
        // Filter out word-by-word spam (delta) and non-message events
        if (
          event.type === "message.part.delta" ||
          !event.type.includes("message")
        ) {
          return;
        }

        // Create a JSON payload file for each event
        const payloadFile = createPayloadFile(event, eventsDir);

        // Pass the file path to Python and execute. (Silence on success, catch on failure)
        const cmd = `uv run lico-observer-opencode '${payloadFile}'`;
        await execAsync(cmd);

        // (Note: We intentionally do NOT delete the JSON file here to preserve a debuggable audit trail of the session)
      } catch (error: any) {
        logError(logFile, "Error", error);
      }
    },
  };
};

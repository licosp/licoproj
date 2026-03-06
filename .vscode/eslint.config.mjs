import js from "@eslint/js";
import prettierConfig from "eslint-config-prettier";
import html from "eslint-plugin-html";
import importPlugin from "eslint-plugin-import";
import prettierPlugin from "eslint-plugin-prettier";
import fs from "fs"; // ファイル読み込み用に追加
import globals from "globals";
import yaml from "js-yaml"; // YAMLパース用に追加

const prettierrc = yaml.load(
  fs.readFileSync("./.vscode/.prettierrc.yaml", "utf8")
);

export default [
  {
    ignores: [
      "**/node_modules/**",
      "**/.venv/**",
      "**/.temp/**",
      "**/.trash/**",
      "**/dist/**",
    ],
  },
  {
    files: ["**/*.js", "**/*.html"],
    plugins: {
      html,
      import: importPlugin,
      prettier: prettierPlugin,
    },
    languageOptions: {
      globals: {
        ...globals.browser,
        ...globals.node,
        ...globals.es2021,
      },
      ecmaVersion: "latest",
      sourceType: "module",
    },
    rules: {
      ...js.configs.recommended.rules,

      ...prettierConfig.rules,

      "prettier/prettier": ["error", prettierrc],

      "no-unused-vars": ["error", { args: "all", vars: "all" }],
      "no-console": "error",
      "no-var": "error",
      "prefer-const": "error",
      eqeqeq: ["error", "always"],
      curly: ["error", "all"],

      "no-eval": "error",
      "no-implied-eval": "error",
      "no-return-assign": "error",
      "no-sequences": "error",
      yoda: ["error", "never"],

      complexity: ["error", 10],
      "max-depth": ["error", 4],
      semi: ["error", "always"],
      quotes: ["error", "double"],
      "max-len": [
        "error",
        {
          code: 79,
          tabWidth: 2,
          ignoreUrls: true,
          ignoreStrings: true,
          ignoreTemplateLiterals: true,
        },
      ],
    },
  },
];

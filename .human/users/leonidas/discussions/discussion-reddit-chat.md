---
ai_visible: true
language: en
author: leonidas
tag: [reddit, discussion, chat]
related:
  https://www.reddit.com/user/Plenty-Candidate-882/: user
  https://chat.reddit.com/room/!4bwU9LA_MUzNyACBT84d5IIkVYBl2TJimModV3bDOso%3Areddit.com: 0000
---

# The discussion on Reddit.

## User

- identifier: `Plenty-Candidate-882`

## Comments

### 0000

#### 0000, 4bwU9LA_MUzNyACBT84d5IIkVYBl2TJimModV3bDOso

##### 0000-0000

I try to keep a single AI conversation going for as long as possible, managing up to three agents at once (limited by Antigravity’s three-slot system). Even though different models have their own strengths, I treat them essentially as generalists. To me, a long conversation is the agent’s history—it’s full of successes and failures that I periodically document for future versions of myself or other AIs. I maintain all the behavioral rules and the underlying data structures in a single, unified repository.

##### 0000-0001

The "three-slot system" refers to the token priority limits for AI models. (I recommend using Gemini Pro, Gemini Flash, and Claude Opus for these slots.)

Switching the AI model for an active agent can cause significant issues, so I typically stick with 1 to 3 fixed agents for my work.

As I mentioned in this link, using multiple agents in parallel within a single IDE instance often leads to conversation reloading when switching between them. For long conversations, this reload can take several minutes.
https://www.reddit.com/r/google_antigravity/comments/1q8lakw/comment/nyqasqf/

The best solution I've found is "1 IDE Instance = 1 Agent". I open each IDE window using a specific 'workspace configuration file' (.code-workspace). While it's a bit tedious to manually select the correct AI model from the dropdown for each instance, it's the most stable setup.

I've developed all my workflows and rules myself. I suggest consulting with your agent to design a directory structure that fits your project's specific goals. You can see an example in my repository here:
https://github.com/licosp/licoproj/tree/main/.agent/rules

As for 'Skills,' I believe it's best to wait until you're fully comfortable with your custom workspace. I personally use Skills to create a primitive communication system between agents. (It's complicated, so I won't explain it here.)

I don't use any special extensions for Antigravity itself—I keep it mostly default. I only use a simple extension to visualize token usage, which is non-intrusive and doesn't affect the workspace at all.

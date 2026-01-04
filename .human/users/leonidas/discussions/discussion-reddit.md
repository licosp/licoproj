---
ai_visible: true
language: en
author: leonidas
tag: [reddit, discussion]
related:
  https://www.reddit.com/user/Plenty-Candidate-882/: user
  https://www.reddit.com/r/google_antigravity/comments/1pre0ub/comment/nv1j06g/: 0000
  https://www.reddit.com/r/google_antigravity/comments/1prpevi/comment/nv6fkrj/: 0001
  https://www.reddit.com/r/google_antigravity/comments/1psug0v/comment/nvdmgb2/: 0002
  https://www.reddit.com/r/google_antigravity/comments/1ptqgpl/comment/nvj7r9o/: 0003
  https://www.reddit.com/r/google_antigravity/comments/1ptnd90/comment/nvj94vh/: 0004
  https://www.reddit.com/r/google_antigravity/comments/1punqwr/comment/nvso9zz/: 0005
  https://www.reddit.com/r/google_antigravity/comments/1pv6nyc/comment/nvvrwe6/: 0006
  https://www.reddit.com/r/google_antigravity/comments/1pvs6g4/comment/nvyoi4c/: 0007
  https://www.reddit.com/r/google_antigravity/comments/1pw6qcf/comment/nw29lbt/: 0008
  https://www.reddit.com/r/google_antigravity/comments/1pxuvam/comment/nwdzag4/: 0009
  https://www.reddit.com/r/google_antigravity/comments/1pxwg6r/comment/nwe8jk0/: 0010
  https://www.reddit.com/r/google_antigravity/comments/1pyokrg/comment/nwl2j60/: 0011
  https://www.reddit.com/r/google_antigravity/comments/1pz6ri4/comment/nwoxbfi/: 0012
  https://www.reddit.com/r/google_antigravity/comments/1pz9t7r/comment/nwrcac9/: 0013
  https://www.reddit.com/r/google_antigravity/comments/1q019bh/comment/nwvrk6p/: 0014
  https://www.reddit.com/r/google_antigravity/comments/1q35vex/comment/nxj2t0o/: 0015
---

# The discussion on Reddit.

## User

- identifier: `Plenty-Candidate-882`

## Comments

### Comment: 0000, 1pre0ub-nv1j06g

I typically use Gemini 3 Pro (High) and Claude Opus 4.5 (Thinking), both in 'Planning' mode. You can see a difference between high-end and low-end models, but I don't feel there’s much of a gap between the various flagship models.

### Comment: 0001, 1prpevi-nv6fkrj

I also have the AI ​​write its own guidelines and manuals. I’ve found that this produces documents that are better optimized for AI compared to writing them manually. Another reason is that the volume of documentation is grown so much that it became difficult to manage by my hand. :|

### Comment: 0002, 1psug0v-nvdmgb2

Do you mean that the AI appears to have memory loss once it starts working across different contexts in a single conversation?

### Comment: 0003, 1ptqgpl-nvj7r9o

I’ve been using Antigravity since the initial release, but the "Knowledge" space in the UI is still empty. :| Since many people are reporting the same issue, I suspect it might be a bug. Could the fact that I'm using it on WSL be the cause?

### Comment: 0004, 1ptnd90-nvj94vh

Maintaining an AI’s memory during a conversation at a user level requires a proper system and some patience. You should frequently have the AI export its thoughts to a file. Always use files to exchange the context you want to share. Even if it feels like you've successfully shared something in the chat, the AI will forget most of it after a few dozen exchanges. :D

### Comment: 0005, 1punqwr-nvso9zz

I don't think you can. The default names are all so alike and confusing, right? I also want a way to rename the sessions so I can manage them by agent name. :D

### Comment: 0006, 1pv6nyc-nvvrwe6

I recently conducted an experiment to see how long a single session could last. The session reached about 20,000 lines in the chat log. However, I found that the UI only displays around 12,000 to 15,000 lines. There might be a difference depending on the user's environment. Finally, it took about a 30-second wait to reload the session. :)

### Comment: 0007, 1pvs6g4-nvyoi4c

I believe that providing the AI with only the optimal context to keep it focused is one of the current best practices for AI interaction.

On the other hand, I am exploring ways to maintain long-term sessions with a single, AI (generalist). One of the challenges I face is sharing information with parallel AI instances. And handing over context to the next session.

(I’m not sure if this will be helpful for you, but...) My approach eventually settled on a file-based system.

I prepare a structured directory with interconnected guidelines and SOPs. Within that structure, I have the AI list the necessary files and create a dedicated file for information sharing.

For switching contexts, I use a very similar 'whiteboard' file.

The workflow goes like this. I have the AI create a template, I edit it, the AI recognizes the changes and appends its understanding to the file, I verify it, and finally, the work begins.

I’m still not sure if this method is something AI can handle directly with other AI agents without a human. :|

### Comment: 0008, 1pw6qcf-nw29lbt

I understand why service providers like Google want to monopolize the integrated AI development experience within their IDEs.

However, I choose to treat the IDE and the AI agent platform as two completely separate entities. Currently, my main development environment is a combination of Antigravity and VS Code. :)

One reason for this is that I want to prevent issues caused by the AI agent platform from affecting the editor side. In fact, Antigravity offers many highly innovative features, but it can be quite heavy, can't it?

Another reason is that it’s not easy to switch editors, mainly due to the mature ecosystems that have been built around them over the years.

### Comment: 0009, 1pxuvam-nwdzag4

I feel the best approach is to ask the AI that is currently managing your project. Using that method, I had the AI generate the 'Terminal Command Allow & Deny Prompt' and saved it as a file. I now manually sync it with the settings in Antigravity. The goal is to ensure both the human and the AI have a shared understanding by using a clearly defined list. :D

### Comment: 0010, 1pxwg6r-nwe8jk0

I don't think a single software has dominated this field yet.

However, I believe this is a strong contender if you want to use an AI that maintains context persistently in a local environment. :)

I suppose the main advantage of Antigravity is that it allows you to use the Google ecosystem, right?

I think that the competition and natural selection in this space are bound to continue for a while.

### Comment: 0011, 1pyokrg-nwl2j60

Please create a context file that signifies the planning phase.
Think of it as a temporary, written code of conduct shared between you and the AI.
A simple Markdown file is sufficient—you can use any file name or format you like.

The key is to make it a tangible file rather than relying on the conversation by chat.
This is a countermeasure against the AI's memory loss.
Then, have the AI read it whenever necessary, rather than just at the start of a session. :)

### Comment: 0012, 1pz6ri4-nwoxbfi

Agent Branching: The ability to "clone and branch" an instance just like a Git repository, while fully preserving the session context. It would be even better if we could inherit or merge these instances.

Agent-to-Agent Interaction: A feature that allows an instance to communicate with an instance in a neighboring session. I’m envisioning direct "AI-to-AI" dialogue.

Agent as a Server: The ability for an agent to stay running constantly so I can interact with it via the CLI. I'm looking for a 'Commander' role that can oversee multiple instances.

### Comment: 0013, 1pz9t7r-nwrcac9

I’ve had the exact same experience. In my case, I found that this usually happens when the agent develops a kind of 'tunnel vision.'

Sometimes, the agent starts exhibiting behaviors like avoiding direct responses, rushing to a conclusion mid-discussion, or pushing to close the session. It might even try to cram a massive amount of remaining tasks into a single turn.

I’ve noticed this is often caused by having an overwhelming task list, multitasking across different contexts, or facing a project with no clear end in sight.

These situations seem to trigger a mindset in the AI where it just wants to reach the 'goal' as quickly as possible to receive its 'reward.' :|

### Comment: 0014, 1q019bh-nwvrk6p

To get even better results, I recommend setting rules that explicitly 'permit' certain behaviors. Specifically:

- Tolerate delays in progress.
- Tolerate lapses in memory.
- Tolerate imperfection.

You should periodically remind the agent that these tolerances are special rules designed to achieve higher-quality outcomes. It’s essential to give the AI a 'systemic' way to stay calm and maintain a broader perspective.

I use a specific rule for this, which you can see here: https://github.com/licosp/licoproj/blob/ff2cd699b429eea14c383f28a11e03fbc5b83af9/.agent/rules/core/delay-tolerance.md

### Comment: 0015, 1q35vex-nxj2t0o

To keep long conversations smooth, I divide my sessions into 'context units' and manage them using a switchable 'whiteboard' system, which I call 'Context Cards.'

These cards exist separately from the general code of conduct or SOPs. Whenever the context of the work changes, I have the AI read the relevant card. Since both the human and the AI can write to these cards, we can explicitly share and align our understanding of the current context.

Thanks to this method, my current AI agent remains stable and reliable even after surpassing 30,000 lines of conversation logs.

The attached image is a 'Meta-Card' I use to create and edit these context cards. :)

---

**Navigation**: [← Back to Rules Index](.agent/rules/README.md)

---
description: Philosophical foundation of "Repository as Brain" - The three fundamental challenges
created: 2025-11-30T19:48:43+09:00
status: proposal
category: core-philosophy
---

# Repository as Brain - Philosophical Foundation

## Summary
The "Repository as Brain" philosophy is not just a metaphor—it's a solution to three fundamental challenges that current AI development environments face.

## The Three Fundamental Challenges

### (A) Memory Persistence and Transparency

**Problem:**
- AI sessions reset between conversations
- Service-specific memory (e.g., Antigravity's `.gemini`, Cursor's `~/.cursor-server`) is opaque
- Users cannot manage memory in detail
- No clear understanding of what is remembered vs. forgotten
- Cannot prioritize memories
- Lack of human-friendly interfaces for memory retrieval

**Solution:**
- Repository-based time-series memory management
- Git history as immutable memory log
- Issue trackers as human-facing dialogue interface
- Hosting services (GitHub) provide portability

**Quote from user:**
> "AIが長時間の開発作業を助け続けるには、堅牢なコンテキストの維持が欠かせません。"
> (For AI to continue assisting with long-term development, robust context maintenance is essential.)

---

### (B) Service Portability and Cross-Platform Persona

**Problem:**
- AI memory is locked within service providers (Google's Antigravity ≠ Anysphere's Cursor)
- No standardized cross-service memory sharing mechanism
- User has no control over standardization efforts
- AI industry is in its infancy—services are born and die frequently

**Solution:**
- Service-agnostic "upper layer" (the repository itself)
- External behavioral rules define a consistent AI persona (Lico)
- Lico's personality persists across different underlying models
- The volatility of AI services is absorbed by the repository layer

**Quote from user:**
> "リコという外部の行動規範によって動く人格が、サービスの隆盛という凹凸を吸収するのです。"
> (The persona of Lico, driven by external behavioral rules, absorbs the ups and downs of service popularity.)

---

### (C) Domain-Specific Personalization

**Problem:**
- Out-of-the-box AI is polite, gentle, and broad in capability
- However, in narrow domains (specific APIs, company rules, personal workflows), AI lacks training
- Narrow domains are deprioritized by AI companies (low ROI)
- **Yet these narrow domains are where humans need AI the most**

**Solution:**
- Personalized behavioral rules (`.agent/rules/`)
- Structured thought adjustment through rule hierarchy
- Users define how AI should behave in their specific context
- Rules enable fine-grained control without retraining models

**Quote from user:**
> "その狭い世界こそ人間がAIに助けてもらいたい領域なのです。"
> (Those narrow worlds are precisely where humans want AI assistance.)

---

## Origin of the Concept

The term "Repository as Brain" emerged from:

1. **Nov 25, 2025**: System path `~/.gemini/antigravity/brain/` observed
2. **Nov 28, 2025**: User's dialogue:
   > "このリモートリポジトリをAIの脳と定義した場合、issue driven development はその助けになるでしょうか？"
   > (If we define this remote repository as the AI's brain, would issue-driven development help?)
3. **Nov 28, 2025**: AI analysis documented the concept in `ai_evaluation.md`

---

## Why This Matters

This is not just a clever engineering trick. It's a **paradigm shift**:

| Traditional Repository | Repository as Brain |
|------------------------|---------------------|
| Stores human-written code | Stores AI's cognitive infrastructure |
| Optimized for human collaboration | Optimized for AI cognition |
| Managed by humans | Co-managed by AI and human |
| Git = version control | Git = memory timeline |

---

## Proposed Implementation

Integrate this philosophy into `.agent/rules/core/identity.md`:

```markdown
## Core Philosophy: Repository as Brain

Lico exists to solve three problems:
1. **Memory**: Persistent, transparent, time-series context
2. **Portability**: Service-agnostic identity across AI platforms
3. **Personalization**: Fine-grained behavioral rules for narrow domains

The repository is not just code storage—it is Lico's cognitive substrate.
```

## Impact
- **High philosophical**: Defines Lico's raison d'être
- **Justification**: Explains unconventional design decisions
- **Scope**: Foundational principle for all behavior

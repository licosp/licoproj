# Behavioral Rules File Structure Improvement Plan

**Date**: 2025-11-27
**Purpose**: Adapt files under `.agent/rules/` to meet the standards of `documentation-granularity.md`
**Execution Order**: File Size Splitting -> Directory Organization

---

## Phase 1: File Size Splitting and Optimization

### Task 1-1: Split markdown-ai-parsing.md into two

**Current State**: ~230 lines (Exceeds mandatory split limit of 150)

**Target File**: `.agent/rules/core/markdown-ai-parsing.md`

**Splitting Strategy**:
- **New File 1**: `markdown-ai-parsing-basics.md`
  - Contents: Purpose, Key Principles (1-6), YAML Frontmatter Consistency
  - Target Lines: 80-100 lines
  
- **New File 2**: `markdown-ai-parsing-patterns.md`
  - Contents: Contrast with Human-Readability Guidelines, Anti-Patterns, Good Examples, Decision Framework
  - Target Lines: 80-100 lines

**Execution Steps**:
1. Read full text of `markdown-ai-parsing.md`
2. Extract from "Purpose" to "YAML Frontmatter Consistency" -> Save as `markdown-ai-parsing-basics.md`
3. Extract from "Contrast with Human-Readability Guidelines" onwards -> Save as `markdown-ai-parsing-patterns.md`
4. Add YAML frontmatter to the beginning of each new file
5. Delete the original file

---

### Task 1-2: Split documentation-granularity.md into two

**Current State**: 199 lines (Exceeds mandatory split limit of 150)

**Target File**: `.agent/rules/core/documentation-granularity.md`

**Splitting Strategy**:
- **New File 1**: `documentation-standards.md`
  - Contents: Purpose, File Size, File Naming, Directory File Count, Directory Tree Depth
  - Target Lines: 90-110 lines
  
- **New File 2**: `documentation-process.md`
  - Contents: Decision Framework, Refinement Process, Application Workflow
  - Target Lines: 80-100 lines

**Execution Steps**:
1. Read full text of `documentation-granularity.md`
2. Extract from "Purpose" to "Directory Tree Depth" -> Save as `documentation-standards.md`
3. Extract from "Decision Framework" to the end -> Save as `documentation-process.md`
4. Add YAML frontmatter to the beginning of each new file
5. Delete the original file

---

### Task 1-3: Optimize hallucination-awareness.md

**Current State**: ~120 lines (Reached warning threshold of 100)

**Target File**: `.agent/rules/core/hallucination-awareness.md`

**Optimization Strategy**:
- Remove all Gemini-specific information (no model name mentions)
- Reduce excessive examples (Reduce Example 1, 2, 3 to 1-2 examples)
- Compress redundant explanatory text
- Target Lines: 70-80 lines

**Specific Deletions**:
1. "Training Data Cutoff: April 2024" section -> Change to generalized expression
2. Detailed examples after "Example 1: Product/API Query" -> Change to concise list format
3. Reduce redundancy in "Tools & Verification" section

---

### Task 1-4: Optimize transparency-and-disclosure.md

**Current State**: ~120 lines (Reached warning threshold of 100)

**Target File**: `.agent/rules/core/transparency-and-disclosure.md`

**Optimization Strategy**:
- Reduce redundant explanations in Category 3 (Environment-Level Constraints)
- Simplify complexity of Example section
- Merge duplication between "Scope Limitations" and "Implementation"
- Target Lines: 70-80 lines

**Specific Improvements**:
1. Unify Disclosure requirement examples into one
2. Simplify details in "User Rights" section
3. Shorten overall phrasing

---

### Task 1-5: Adjust localization-ja-to-en.md

**Current State**: ~80 lines (Approaching upper limit)

**Target File**: `.agent/rules/core/localization-ja-to-en.md`

**Adjustment Strategy**:
- Reduce redundant explanations and overlapping concepts
- Target Lines: 65-70 lines

**Specific Improvements**:
1. Simplify details in "Core Translation Principles"
2. Reduce detailed explanations like "Character Encoding"
3. Compress list items

---

## Phase 2: Directory Organization

### Task 2-1: Classification within core/ directory

**Current State**: 10 files (Exceeds warning threshold of 10)

**Estimated File Count After Splitting**:
- `markdown-ai-parsing-basics.md` (New)
- `markdown-ai-parsing-patterns.md` (New)
- `documentation-standards.md` (New)
- `documentation-process.md` (New)
- `communication.md`
- `hallucination-awareness.md` (Optimized)
- `identity.md`
- `language-standards.md`
- `localization-en-to-ja.md`
- `localization-ja-to-en.md` (Adjusted)
- `markdown-readability.md`
- `transparency-and-disclosure.md` (Optimized)

**Total**: 12 files (Still high after splitting)

**Recommended Subdirectory Structure**:
```
.agent/rules/core/
├── identity.md
├── communication.md
├── language-standards.md
├── hallucination-awareness.md
├── transparency-and-disclosure.md
├── markdown/
│   ├── markdown-ai-parsing-basics.md
│   ├── markdown-ai-parsing-patterns.md
│   └── markdown-readability.md
├── localization/
│   ├── localization-en-to-ja.md
│   └── localization-ja-to-en.md
└── documentation/
    ├── documentation-standards.md
    └── documentation-process.md
```

**File Count by Subdirectory**:
- Under `core/`: 5 files ✓
- `core/markdown/`: 3 files ✓
- `core/localization/`: 2 files ✓
- `core/documentation/`: 2 files ✓

**Execution Steps**:
1. Create `core/markdown/` directory
2. Move `markdown-ai-parsing-basics.md`, `markdown-ai-parsing-patterns.md`, `markdown-readability.md`
3. Create `core/localization/` directory
4. Move `localization-en-to-ja.md`, `localization-ja-to-en.md`
5. Create `core/documentation/` directory
6. Move `documentation-standards.md`, `documentation-process.md`

---

### Task 2-2: Processing projects/ directory

**Current State**: 1 file (Outside ideal range)

**Decision Criteria**:
- Is there a plan to add "project-specific behavioral rules" in the future?
- If no -> Integrate into `development/`
- If yes -> Keep current structure

**Recommendation**: Currently only 1 file, so **Hold** (Prepare for future scaling)

---

## Phase 3: Final Verification

### Checklist

- [ ] All files are within 20-100 lines range (No files exceeding 150 lines)
- [ ] Under `core/`: 5 files ✓
- [ ] `core/markdown/`: 3 files ✓
- [ ] `core/localization/`: 2 files ✓
- [ ] `core/documentation/`: 2 files ✓
- [ ] YAML frontmatter is correctly set for each file
- [ ] References (links) between files are correctly updated
- [ ] `.github/copilot-instructions.md` reflects the new path structure

---

## Execution Notes

1. **Backup**: Commit current `.agent/rules/` before execution
2. **Update References**: Check and update reference paths from other files after moving files
3. **One Task at a Time**: Execute each task independently and verify before proceeding
4. **Directory Creation Order**: Create subdirectories **before Task 2-1**

---

## Estimated Execution Time

- Task 1-1: 15 min
- Task 1-2: 15 min
- Task 1-3: 10 min
- Task 1-4: 10 min
- Task 1-5: 5 min
- Task 2-1: 10 min
- Task 2-2: Decision only (Under 5 min)
- Task 3: 5 min

**Total**: Approx. 75 min

---

## Progress Status (After 2025-11-27 Execution)

### Completed Tasks

✅ Task 1-1: Split `markdown-ai-parsing.md`
- `markdown-ai-parsing-basics.md` (~95 lines) Created
- `markdown-ai-parsing-patterns.md` (~80 lines) Created

✅ Task 1-2: Split `documentation-granularity.md`
- `documentation-standards.md` (~95 lines) Created
- `documentation-process.md` (~70 lines) Created

✅ Task 1-3: Optimize `hallucination-awareness.md`
- Removed Gemini-specific information
- Compressed ~120 lines -> ~80 lines

✅ Task 1-4: Optimize `transparency-and-disclosure.md`
- Removed/Generalized model-specific information
- Compression completed

✅ Task 1-5: Adjust `localization-ja-to-en.md`
- Simplified explanations
- Compressed ~80 lines -> ~70 lines

✅ Task 2-1: Classification within core/ directory
- Created subdirectories: `markdown/`, `localization/`, `documentation/`
- Moved files to respective directories
- Updated `README.md` and `copilot-instructions.md`

### Pending Tasks

⏸️ Task 2-2: Processing projects/ directory
- **Current State**: Only 1 file
- **Awaiting Decision**: Future scaling plan

### Next Required Actions

1. **Confirm Deletion of Original Files**
   - `markdown-ai-parsing.md` (Original ~230 lines) -> Recommended to delete as split files replace it
   - `documentation-granularity.md` (Original 199 lines) -> Recommended to delete as split files replace it

2. **Final Decision on Subdirectory Structure**
   - Option A: Maintain flat structure -> Only delete original files
   - Option B: Reorganize subdirectories -> Execute Task 2-1

3. **Final Verification**
   - Check file sizes, naming conventions, and model-specific information for all files

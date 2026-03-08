# Architecture Elevation: The Monolith Brain

## Concept
Transform `licoproj` from a "Hub" into the **"Universe Root"**. 
All related repositories and workspaces are logically nested within this single directory tree, following the philosophy documented in `map.md`.

## Proposed Layout

```text
licoproj/                 <-- [UNIVERSE ROOT] (Mount this to /workspace)
├── .agent/               <-- [COGNITIVE ROOT]
│   └── .internal/
│       └── .shadow/      <-- [SHADOW REPO] (Private conversations)
├── .human/               <-- [INTERFACE]
├── .repos/               <-- [EXTERNAL REPOS]
│   ├── chron/            <-- [CHRON REPO] (Game development)
│   └── chron-history/
├── .crew/                <-- [IDENTIFIER WORKSPACES]
│   ├── iuria/            <-- (Worktree of licoproj)
│   ├── leonidas/         <-- (Worktree of licoproj)
│   └── ...
└── packages/             <-- [THE SUBSTANCE]
```

## Advantages

### 1. Unified Cognition
Lico's rules (`.agent/`) are always exactly where they expect to be: at the root of the 작업장. No matter which sub-repo or workspace a resident is in, the path to the "Brain" is uniform.

### 2. Streamlined Provisioning
The `lico-devc` (Village Provisioning System) becomes much simpler. `/workspace` is the entire world.
- No more complex dynamic root discovery in `boot.py`.
- No more multi-path environment variable injection.

### 3. Absolute Portability
The entire village can be moved, backed up, or cloned as a single unit.

### 4. Privacy Guardrails
`shadow` repositories are naturally tucked away inside `.agent/.internal/`, reinforcing their status as "Private Memory".

## Transition Steps
1. **Host-side Migration**: Move `shared/project/.licoshdw` to `shared/project/licoproj/.agent/.internal/.shadow`.
2. **Repository Re-mapping**: Move `licochron` and `licochron-history` into `licoproj/.repos/`.
3. **Worktree Realignment**: Move `shared/crew/` contents into `shared/project/licoproj/.crew/`.
4. **Environment Simplification**: Update `docker-compose.yml` and `provision.py` to assume the new monolith structure.

## Metadata Tracking
- **Phase**: 21 (Architecture Elevation)
- **Status**: Planning / Proposal
- **Author**: Iuria (Resident)

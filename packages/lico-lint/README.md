# Lico-Lint

`lico-lint` is a unified quality gate for the Lico project, orchestrating four distinct audits to ensure logical integrity, visual consistency, and type safety across the entire codebase.

## Functionality

It executes the following tools in sequence:
1.  **Ruff Check**: Audits logic, imports, and potential bugs.
2.  **Ruff Format**: Enforces a consistent, standardized layout.
3.  **Pyright**: Performs fast, comprehensive static type analysis.
4.  **Mypy**: Conducts rigorous, strictly-typed formal validation.

## Usage

You can run the linter on any directory or file within the Monolith:

```bash
# Check everything in the project root
uv run lico-lint .

# Check a specific package
uv run lico-lint packages/lico-devc/src

# Check a specific resident's workspace
uv run lico-lint .crew/iuria/licoproj
```

---
*Note: This tool is intended to run both on the host (WSL) and within the containerized village.*

# Agent Instructions for my-position

## Project Type
Python CLI application using uv for dependency management

## Project Purpose

**my-position** is a CLI tool that synthesizes personal positions on topics from Markdown content.

### Architecture Overview

**Input**: Markdown files (conversations, notes, documents)
**Processing Pipeline**:
1. **Ingestion**: Parse Markdown files and extract structured content
2. **Topic Modeling**: Identify topics using TF-IDF and clustering algorithms
3. **Position Synthesis**: Generate coherent position statements from fragmented discussions
4. **Export**: Output encyclopedia-like entries in various formats

**Output**: Structured position entries (Markdown, JSON, HTML)

### Key Components (Planned)

- `ingest/`: Markdown parsing and content extraction
- `modeling/`: Topic identification and clustering
- `synthesis/`: Position generation from clustered content
- `export/`: Output formatters
- `connectors/`: External service integrations (separate repos)

### Design Principles

- **Core stays lightweight**: Service connectors (Slack, Notion, etc.) live in separate repos
- **Plugin architecture**: Connectors implement standard interfaces
- **Markdown-first**: Primary input format is Markdown
- **Local-first**: Works without external services

## Run Commands
```bash
# Run the application
uv run my_position

# Run directly with Python
uv run python -m my_position.main
```

## Test Commands
```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=my_position --cov-report=html

# Run specific test file
uv run pytest tests/test_example.py

# Run with verbose output
uv run pytest -v
```

## Quality Checks
```bash
# Lint and auto-fix
uv run ruff check --fix .

# Format code
uv run ruff format .

# Type check
uvx ty check

# Run all checks
uv run ruff check --fix . && uv run ruff format . && uvx ty check && uv run pytest
```

## Project-Specific Conventions

### Code Style
- Use src layout: `src/my_position/`
- Type hints required on all functions
- Google-style docstrings
- Descriptive names, no type-redundant suffixes

### Testing
- All tests in `tests/` directory
- Use pytest with fixtures
- Aim for 80% coverage per feature
- Test types: unit, integration, e2e

### Dependencies
- Add runtime dependencies to `[project.dependencies]`
- Add dev dependencies to `[dependency-groups.dev]`
- Use `uv add <package>` for runtime deps
- Use `uv add --dev <package>` for dev deps

### Git Workflow
- Branch from `main`
- Run quality checks before committing
- All tests must pass before commit
- Never push until instructed

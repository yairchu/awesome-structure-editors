# Awesome Structure Editors Repository

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the information here.

This is an "awesome list" repository that curates structural/projectional code editor projects. It contains a README.md with organized tables of projects, their properties, descriptions, and metadata.

## Working Effectively

### Essential Setup
- Python 3.x is required (available as `python`)
- Node.js and npm are required (available as `node` and `npm`)  
- GitHub CLI is required for statistics updates (available as `gh`)
- All dependencies are pre-installed in the environment

### Primary Validation Workflow
- **Always run `npx awesome-lint` before committing changes** - this validates the awesome list format
- `npx awesome-lint` takes ~2 seconds after initial package download (first run ~30-60 seconds)
- NEVER CANCEL: First run takes 30-60 seconds to download packages. Set timeout to 120+ seconds for safety
- The linter checks:
  - Proper awesome badge format
  - Table of contents structure
  - Link formatting and alphabetical ordering
  - Project description standards
  - Required heading formats

### Statistics Update Script
- `python update-stats.py` updates GitHub stars and last update information
- **Requires GitHub token**: Script will fail with "GH_TOKEN environment variable" error without authentication
- In GitHub Actions, this runs with automated token
- For local development, you need `gh auth login` or set `GH_TOKEN` environment variable
- **Do not run this script without proper GitHub authentication** - document this limitation in contributions

## Validation Process

### Testing Changes
- Always validate README.md changes with `npx awesome-lint`
- The linter will show specific errors with line numbers if formatting is incorrect
- Example error output includes missing badges, incorrect headings, or malformed tables
- **Always run linting after any README.md modifications**

### Manual Validation Scenarios
When making changes to the repository, always test these scenarios:
1. **Basic validation**: Run `npx awesome-lint` and verify it passes
2. **Error detection**: Introduce a deliberate formatting error and verify the linter catches it
3. **Restore and re-validate**: Fix the error and confirm the linter passes again

## Repository Structure

### Key Files
```
/home/runner/work/awesome-structure-editors/awesome-structure-editors/
├── README.md                   # Main content - curated list (149 lines)
├── update-stats.py             # Python script to update GitHub statistics  
├── .github/workflows/main.yml  # CI workflow that runs awesome-lint
├── contributing.md             # Contribution guidelines
├── code-of-conduct.md          # Code of conduct
└── LICENSE                     # CC0 license
```

### Content Structure in README.md
- **Main sections**: Structural code editor projects, Blocks Programming Editors, Spreadsheet-based projects, Other notable projects, Resources
- **Project tables**: Include columns for Project name, Properties (emoji flags), Description, Written in, Stars, Updated year
- **Property flags**: 💵 Commercial, 🎓 Academic, ♡ Donations, 📖 Uses text files, ⌨️ Text editing UX, 👶 New language, λ Functional, etc.

## Common Tasks

### Adding New Projects
1. Determine correct section (active vs concluded projects)
2. Follow table format exactly: `| [Name](url) | flags | description | language | stars | year |`
3. Use appropriate emoji flags from the legend
4. Maintain alphabetical ordering within star count groups
5. **Always run `npx awesome-lint` to validate formatting**

### Editing Existing Entries  
1. Preserve table structure and alignment
2. Update year only if there's significant project activity
3. Don't manually update star counts - use `update-stats.py` instead
4. **Always run `npx awesome-lint` to validate changes**

### Updating Statistics
- **Manual approach**: Run `python update-stats.py` with proper GitHub authentication
- **Automated approach**: Statistics are updated via GitHub Actions workflow
- **Do not manually edit star counts** - they will be overwritten by the update script

## Build and Test Commands

### Linting (Primary Validation)
```bash
npx awesome-lint
```
- **Timing**: 2 seconds after packages downloaded, first run 30-60 seconds
- **NEVER CANCEL**: Set timeout to 120+ seconds for safety
- **Exit codes**: 0 = success, non-zero = validation errors
- **Always run this before committing changes**

### Statistics Update
```bash
python update-stats.py
```
- **Requirements**: Needs GitHub token authentication
- **Timing**: Variable depending on number of projects (~2-5 minutes)
- **Will fail without authentication** - document this in any error reports

### Git Operations
```bash
git status
git add README.md
git commit -m "Add new project: ProjectName"
```

## Troubleshooting

### Common Linting Errors
- "Main heading must be in title case" - Check README.md first line
- "Missing Awesome badge" - Verify badge format in header
- "Missing or invalid Table of Contents" - Check TOC section format
- Table formatting errors - Verify pipe alignment and required columns

### Update Script Issues  
- "GH_TOKEN environment variable" error - Authentication required
- API rate limiting - Wait and retry, or use authenticated requests
- Network timeouts - Normal for large number of projects

### Contributing Workflow
1. Edit README.md following existing patterns
2. Run `npx awesome-lint` to validate (NEVER CANCEL - wait for completion)
3. Fix any linting errors shown
4. Commit changes with descriptive message
5. Statistics will be updated automatically via CI

## Environment Information

### Pre-installed Tools
- Python 3.12.3
- Node.js (latest)
- npm (latest) 
- GitHub CLI 2.78.0+
- All required Python modules (json, datetime, subprocess, sys)

### File Locations
- Repository root: `/home/runner/work/awesome-structure-editors/awesome-structure-editors`
- Always use absolute paths when referencing files in this repository

## Critical Reminders
- **NEVER CANCEL** the `npx awesome-lint` command - it may take 30-60 seconds on first run
- **Always validate with awesome-lint** before committing README.md changes  
- **Do not manually edit star counts** - use the update script or let CI handle it
- **GitHub authentication required** for statistics updates - document failures appropriately
- **Preserve existing formatting** when making edits - this is a curated list with specific standards
# Optional alternative: the Mintlify multi-repo GitHub Action

**The primary setup for this site is Mintlify's native multi-repo support** (see the repo README). Use the action only if the project is not on an Enterprise plan, or if you would rather manage sources in a file than in the dashboard.

These files are parked here so they stay inactive. GitHub only runs workflows in `.github/workflows/`.

## Turn it on

1. In the dashboard, remove the four API repos from **Git settings** (leave only this repo).
2. Copy the files into place and make the action's base config:
   ```bash
   cp .github/multirepo-action-alternative/mintlify-multirepo.yml .github/mintlify-multirepo.yml
   cp .github/multirepo-action-alternative/multirepo.yml          .github/workflows/multirepo.yml
   cp docs.json docs.base.json     # the action reads docs.base.json and generates docs.json
   ```
3. In **Settings > Actions > General**, tick **Allow GitHub Actions to create and approve pull requests** (or set `mode: push` in the workflow).
4. Run **Combine docs** from the Actions tab (or wait for the hourly schedule). It copies each API's `docs/` folder into a folder named after the repo and rewrites `docs.json`.
5. Optional: add a `DOCS_DISPATCH_TOKEN` secret to each API repo so the `Notify docs repository` workflow can trigger a sync on every docs change.

## Known differences from native multi-repo

- The action only prefixes the `openapi` **source file** path. Generated endpoint pages stay in `api-reference/...` (shared by all four APIs) instead of `<repo>/api-reference/...`. If you use the action, set `"openapi": { "source": "openapi.json", "directory": "<repo>/api-reference" }` in each child `docs.json`.
- Links in the child docs already include the repo prefix (for example `/todo-api/quickstart`), and the action leaves links that start with a destination folder untouched.
- Untested: this path has not been run end to end.

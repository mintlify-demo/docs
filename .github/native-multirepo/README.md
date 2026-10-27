# Parked: native multi-repo setup

`docs.native.json` is the `docs.json` used with Mintlify's **native multi-repository projects** (Enterprise, sources added in Git settings). It is parked here because the sources option was not available in this project's Git settings, so the site currently uses the **multirepo GitHub Action** instead.

## Current setup (action)

- `docs.base.json`: hand-edited site config. It has the `sourceRef` entries.
- `.github/mintlify-multirepo.yml` + `.github/workflows/multirepo.yml`: the action copies each API repo's `docs/` into a folder named after the repo, then **generates `docs.json`** from `docs.base.json` and pushes to `main`.
- **Don't edit `docs.json` or the API folders by hand.** The next sync overwrites them. Edit `docs.base.json` or the API repos.

## Switch back to native multi-repo

1. Delete `.github/workflows/multirepo.yml`, `.github/mintlify-multirepo.yml`, `.mintlify-multirepo.json`, `docs.base.json`, the generated `docs.json`, and the four copied API folders (`merge-sort-api/`, `calculator-api/`, `todo-api/`, `text-utils-api/`).
2. `cp .github/native-multirepo/docs.native.json docs.json`
3. In each API repo's `docs/docs.json`, change the `openapi` object to the string form `"openapi": "openapi.json"`. (With the action, the children set `directory: "<repo>/api-reference"` themselves because the action doesn't prefix generated pages.)
4. In the Mintlify dashboard, add the four repos as sources (docs path `docs`, URL paths `merge-sort-api`, `calculator-api`, `todo-api`, `text-utils-api`).

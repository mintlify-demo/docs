# Mintlify Demo (docs)

The central docs repo for the **mintlify-demo** org: a showcase site for Mintlify account executives. It holds the site settings (`docs.json`), the landing page, guides, the component and AI showcase pages, and the changelog. Each example API keeps its own docs in its own repository and is pulled in by the **mintlify/multirepo-action** GitHub Action.

## How it fits together

- `docs.base.json` is the hand-edited site config (theme, colors, logo, navigation). Each API tab uses `{ "sourceRef": "mintlify-demo/<repo>" }` to mark where that repo's navigation goes.
- The [multirepo GitHub Action](.github/workflows/multirepo.yml) runs hourly, on demand, and when an API repo sends a `docs-updated` event. It copies each API repo's `docs/` folder into a folder named after the repo, generates **`docs.json`**, and pushes to `main`. Mintlify then redeploys.
- Each API repo's `docs/docs.json` has a `navigation.pages` list: **Get started**, **Guides**, and an **API reference** group generated from the committed `docs/openapi.json`.
- **Don't edit `docs.json` or the four API folders here.** The next sync overwrites them. Edit `docs.base.json` or the API repos.

| Repo | Docs folder | URL path |
| --- | --- | --- |
| `mintlify-demo/docs` (this repo) | `/` | `/` |
| `mintlify-demo/merge-sort-api` | `docs/` | `/merge-sort-api` |
| `mintlify-demo/calculator-api` | `docs/` | `/calculator-api` |
| `mintlify-demo/todo-api` | `docs/` | `/todo-api` |
| `mintlify-demo/text-utils-api` | `docs/` | `/text-utils-api` |

Sync now: `gh workflow run "Combine docs" -R mintlify-demo/docs`

## Native multi-repo (parked)

If Enterprise multi-repo gets enabled, see [`.github/native-multirepo/`](.github/native-multirepo/README.md) for the saved `docs.json` and the steps to switch back.

## Preview everything locally

Clone all five repos side by side, then:

```bash
npm i -g mint
python3 scripts/preview_merged.py     # builds ./.preview with every API's docs merged in (reads docs.base.json)
cd .preview && mint dev
```

`mint validate` and `mint broken-links` both work inside `.preview`.

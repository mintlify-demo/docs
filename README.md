# Mintlify Demo (docs)

The central docs repo for the **mintlify-demo** org: a showcase site for Mintlify account executives. It holds the site settings (`docs.json`), the landing page, guides, the component and AI showcase pages, and the changelog. Each example API keeps its own docs in its own repository and is pulled in with Mintlify's **multi-repository projects**.

| Repo | Docs folder | URL path |
| --- | --- | --- |
| `mintlify-demo/docs` (this repo, **base source**) | `/` | `/` |
| `mintlify-demo/merge-sort-api` | `docs/` | `/merge-sort-api` |
| `mintlify-demo/calculator-api` | `docs/` | `/calculator-api` |
| `mintlify-demo/todo-api` | `docs/` | `/todo-api` |
| `mintlify-demo/text-utils-api` | `docs/` | `/text-utils-api` |

## How it fits together

- `docs.json` here is the base config. Each API tab uses `{ "sourceRef": "mintlify-demo/<repo>" }` to drop that repo's navigation into place. Mintlify prefixes its pages with the repo's URL path.
- Each API repo's `docs/docs.json` has a `navigation.pages` list: a **Get started** group, a **Guides** group, and an **API reference** group generated from the committed `docs/openapi.json`.
- Links inside child docs include the repo prefix (for example `/todo-api/quickstart`), so they work once merged.

## Connect it to Mintlify (native multi-repo, Enterprise)

In the dashboard, open **Git settings** and add one source per repository:

| Repository | Branch | docs.json in subdirectory | URL path |
| --- | --- | --- | --- |
| `mintlify-demo/docs` (set as **Base**) | `main` | off | _(empty, or `/`)_ |
| `mintlify-demo/merge-sort-api` | `main` | `docs` | `merge-sort-api` |
| `mintlify-demo/calculator-api` | `main` | `docs` | `calculator-api` |
| `mintlify-demo/todo-api` | `main` | `docs` | `todo-api` |
| `mintlify-demo/text-utils-api` | `main` | `docs` | `text-utils-api` |

The Mintlify GitHub app must have access to all five repos.

## Preview everything locally

Clone all five repos side by side, then:

```bash
npm i -g mint
python3 scripts/preview_merged.py     # builds ./.preview with every API's docs merged in
cd .preview && mint dev
```

`mint validate` and `mint broken-links` both work inside `.preview`. Run in this repo alone, `mint validate` passes, but `mint broken-links` reports links to the API pages, which live in the other repos.

## Optional: multirepo GitHub Action

If you can't use native multi-repo, see [`.github/multirepo-action-alternative/`](.github/multirepo-action-alternative/README.md).

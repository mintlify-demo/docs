# Mintlify Demo (docs)

The docs repo for the **mintlify-demo** org: a showcase site for Mintlify account executives. **All** docs live here: the site settings (`docs.json`), the landing page, guides, showcase pages, the changelog, es/fr translations, and the docs for each example API.

| Folder | What it is | Code lives in |
| --- | --- | --- |
| `/` (`index`, `quickstart`, `showcase/`, `changelog`) | Site pages (public) | - |
| `es/`, `fr/` | Spanish and French translations of the site pages. The API docs stay in English | - |
| `merge-sort-api/` | Pages + `openapi.json` | [merge-sort-api](https://github.com/mintlify-demo/merge-sort-api) |
| `calculator-api/` | Pages + `openapi.v2.json` / `openapi.v1.json` (version switcher) + full `openapi.json` | [calculator-api](https://github.com/mintlify-demo/calculator-api) |
| `todo-api/` | Pages + `openapi.json`, `schema.graphql` (GraphQL), `asyncapi.yaml` (WebSocket), `sdk-artifacts/python` (Sphinx JSON for the SDK reference) | [todo-api](https://github.com/mintlify-demo/todo-api) |
| `text-utils-api/` | Pages + `openapi.json` | [text-utils-api](https://github.com/mintlify-demo/text-utils-api) |

URLs are `/<api-name>/...`, as before. API pages have no `public: true`, so they need a login. Site pages are `public: true`.

## How docs stay in sync with code
The API repos hold only code and tests. Mintlify's **Update from code changes** automation watches them. When a PR changes an API, the automation opens a PR here that updates that API's pages and spec. The nightly demo reset closes open bot PRs and reverts merged ones; it never force-pushes this repo (see `mintlify-demo/demo-kit`).

## Regenerating a spec by hand
Each API serves its spec at `http://localhost:8000/openapi.json`. Run the API, then:

```bash
curl -s localhost:8000/openapi.json | python3 -m json.tool > merge-sort-api/openapi.json
```

## Preview
```bash
npm i -g mint
mint dev
```

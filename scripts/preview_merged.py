#!/usr/bin/env python3
"""Build a local, merged copy of the whole site for `mint dev` / `mint validate`.

In production, the mintlify/multirepo-action GitHub Action stitches the
repositories together (see .github/workflows/multirepo.yml). This script does
the same thing on your laptop so you can preview before pushing.

It expects the repos to be cloned side by side:

    mintlify-demo/
      docs/              <- this repo
      merge-sort-api/
      calculator-api/
      todo-api/
      text-utils-api/

Usage:   python scripts/preview_merged.py [--parent ..] [--out .preview]
Then:    cd .preview && mint dev
"""
import argparse
import json
import shutil
from pathlib import Path

REPOS = ["merge-sort-api", "calculator-api", "todo-api", "text-utils-api"]
OWNER = "mintlify-demo"


def prefix_navigation(node, dest):
    """Prefix every page path and openapi path in a child's navigation with its URL path."""
    if isinstance(node, list):
        return [prefix_navigation(n, dest) for n in node]
    if not isinstance(node, dict):
        return node
    out = {}
    for key, value in node.items():
        if key == "pages" and isinstance(value, list):
            out[key] = [f"{dest}/{p}" if isinstance(p, str) else prefix_navigation(p, dest) for p in value]
        elif key == "openapi" and isinstance(value, dict) and isinstance(value.get("source"), str):
            # Like the action: prefix the spec path, leave `directory` alone.
            out[key] = {**value, "source": f"{dest}/{value['source']}"}
        elif key == "openapi" and isinstance(value, str):
            out[key] = f"{dest}/{value}"
        else:
            out[key] = prefix_navigation(value, dest)
    return out


def replace_source_refs(node, navs):
    """Replace {"sourceRef": "owner/repo"} entries with the child's navigation."""
    if isinstance(node, list):
        result = []
        for item in node:
            if isinstance(item, dict) and "sourceRef" in item:
                result.extend(navs[item["sourceRef"]])
            else:
                result.append(replace_source_refs(item, navs))
        return result
    if isinstance(node, dict):
        return {k: replace_source_refs(v, navs) for k, v in node.items()}
    return node


def main():
    here = Path(__file__).resolve().parent.parent
    ap = argparse.ArgumentParser()
    ap.add_argument("--parent", default=str(here.parent), help="folder that contains the cloned repos")
    ap.add_argument("--out", default=str(here / ".preview"))
    args = ap.parse_args()
    parent, out = Path(args.parent), Path(args.out)

    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(
        here, out,
        ignore=shutil.ignore_patterns(".git", ".github", ".preview", "scripts", "README.md", "node_modules"),
    )

    navs = {}
    for repo in REPOS:
        docs_dir = parent / repo / "docs"
        child = json.loads((docs_dir / "docs.json").read_text())
        shutil.copytree(
            docs_dir, out / repo,
            ignore=shutil.ignore_patterns("docs.json", ".*", "node_modules"),
        )
        nav = child["navigation"]
        items = nav.get("pages") or nav.get("groups")
        navs[f"{OWNER}/{repo}"] = prefix_navigation(items, repo)

    base = json.loads((here / "docs.base.json").read_text())
    merged = replace_source_refs(base, navs)
    (out / "docs.json").write_text(json.dumps(merged, indent=2) + "\n")
    print(f"Merged site written to {out}\nNext: cd {out.name} && mint dev")


if __name__ == "__main__":
    main()

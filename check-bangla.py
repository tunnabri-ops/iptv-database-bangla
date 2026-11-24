#!/usr/bin/env python3
"""Validate channels-bangla.csv against the iptv-org/database schema.

Checks (from upstream data/channels.csv):
- header matches upstream exactly
- every id ends with .bd and country is BD
- no duplicate ids, no empty name
- launched date, if present, is YYYY-MM-DD
Usage: python3 check-bangla.py
"""
import csv
import re
import sys

EXPECTED_HEADER = [
    "id", "name", "alt_names", "network", "owners", "country",
    "categories", "is_nsfw", "launched", "closed", "replaced_by", "website",
]

errors = []
with open("channels-bangla.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    if reader.fieldnames != EXPECTED_HEADER:
        errors.append(f"header mismatch: {reader.fieldnames}")
    seen = set()
    for n, row in enumerate(reader, start=2):
        cid = row["id"]
        if not cid.endswith(".bd"):
            errors.append(f"line {n}: id {cid!r} does not end with .bd")
        if row["country"] != "BD":
            errors.append(f"line {n}: country is {row['country']!r}, expected BD")
        if not row["name"].strip():
            errors.append(f"line {n}: empty name")
        if cid in seen:
            errors.append(f"line {n}: duplicate id {cid}")
        seen.add(cid)
        if row["launched"] and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", row["launched"]):
            errors.append(f"line {n}: bad launched date {row['launched']!r}")

if errors:
    print(f"FAIL: {len(errors)} problem(s)")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print(f"OK: {len(seen)} Bangladeshi channels, schema matches upstream.")

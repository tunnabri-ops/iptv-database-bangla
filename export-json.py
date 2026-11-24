#!/usr/bin/env python3
"""Export channels-bangla.csv to channels-bangla.json (same data, JSON form).

Usage: python3 export-json.py
Reads channels-bangla.csv next to this script, writes channels-bangla.json.
"""
import csv
import json
import pathlib

HERE = pathlib.Path(__file__).parent
rows = list(csv.DictReader(open(HERE / "channels-bangla.csv", encoding="utf-8")))
with open(HERE / "channels-bangla.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)
print(f"{len(rows)} channels written to channels-bangla.json")

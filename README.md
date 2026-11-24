# 📺 IPTV Database Bangla

[![Bangla](https://img.shields.io/badge/UI-Bangla%20%2B%20English-orange)](#)

**25 Bangladeshi TV channels in one CSV file, with a validator and a JSON export — ready to use in any IPTV or EPG project.**

> বাংলা সংস্করণ নিচে আছে। / Bangla version below.

## ✨ Features

- `channels-bangla.csv` — 25 Bangladeshi channels with their official ids, names, networks, owners, categories, launch dates and websites: NTV, Somoy News TV, ATN Bangla, ATN News, Bangla Vision, Channel 24, Channel I, Deepto TV, Ekattor TV, Ekushey TV, Independent TV, Jamuna TV, Maasranga TV, My TV, RTV, SATV, Boishakhi TV, BTV National, BTV World, DBC News, Gazi TV, Mohona TV, News24, Asian TV, Bijoy TV.
- `check-bangla.py` — validates the CSV before you use it: correct header columns, every id ending in `.bd`, country `BD`, no duplicate ids, no empty names, launch dates in `YYYY-MM-DD` format.
- `export-json.py` — converts the same 25 channels to `channels-bangla.json` for apps that prefer JSON.
- Channel ids checked against the live channel list — the easy-to-mistake ones are already right (Somoy TV is `SomoyNewsTV.bd`, Channel i is `ChannelI.bd`, BTV is `BTVNational.bd`, Ekushey TV is `EkusheyTV.bd`, Gazi TV is `GaziTV.bd`).

## 🚀 How to use

```bash
# Validate the channel list
python3 check-bangla.py

# Export the same data as JSON
python3 export-json.py
# → writes channels-bangla.json (25 channels)
```

Feed `channels-bangla.csv` (or the JSON) to any playlist builder or EPG grabber that reads channel data — the columns are `id, name, alt_names, network, owners, country, categories, is_nsfw, launched, closed, replaced_by, website`.

## ⚠️ Honest limits

- This is channel data only — no stream URLs. A channel being in the list does not mean its stream is online; check that a channel is still on air before putting it in a playlist.
- The list is a snapshot of 25 channels. New channels are added by editing the CSV and running the checker — the checker catches a wrong id before it breaks a playlist or EPG grab.
- Channel details (owners, launch dates, websites) can change over time; re-check a row if something looks out of date.

## 🇧🇩 বাংলা

**IPTV Database বাংলা — ২৫টা বাংলাদেশি চ্যানেলের ডেটাবেস।**

- `channels-bangla.csv` — ২৫টা চ্যানেলের আইডি, নাম, নেটওয়ার্ক, মালিক, ক্যাটাগরি, শুরুর তারিখ আর ওয়েবসাইট।
- `check-bangla.py` — ফাইলটা ঠিক আছে কি না যাচাই করে (ভুল আইডি থাকলে আগেই ধরে)।
- `export-json.py` — একই ডেটা JSON আকারে বানায়।
- শুধু চ্যানেলের তথ্য আছে, স্ট্রিমের লিংক নেই — প্লেলিস্টে দেওয়ার আগে চ্যানেলটা এখনো চলে কি না দেখে নিন।

## 📄 License

MIT — use it however you like; credit is appreciated.

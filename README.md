# IPTV Database Bangla — বাংলাদেশি চ্যানেলের ডেটাবেস

Bangla-first subset of the iptv-org channel database, built on **iptv-org/database**.

- **Original repo:** https://github.com/iptv-org/database (user-editable database for TV channels — 31,000+ channels in CSV, used by iptv-org/iptv and iptv-org/epg)

## কী আছে / What is inside

- `channels-bangla.csv` — 25 Bangladeshi channels copied **exactly** from upstream `data/channels.csv` (same columns, same values): NTV, Somoy News TV, ATN Bangla, ATN News, Bangla Vision, Channel 24, Channel I, Deepto TV, Ekattor TV, Ekushey TV, Independent TV, Jamuna TV, Maasranga TV, My TV, RTV, SATV, Boishakhi TV, BTV National, BTV World, DBC News, Gazi TV, Mohona TV, News24, Asian TV, Bijoy TV.
- `check-bangla.py` — validates the Bangla CSV against the upstream schema (header columns, `.bd` ids, country `BD`, no duplicates).

## যা ঠিক করা হয়েছে / What was fixed

- Upstream has 31,857 channels in one giant CSV — finding the Bangladeshi ones means grepping a 31k-line file. This repo ships the ready-made Bangla slice, so a Bangla IPTV/EPG project can use it directly.
- Upstream channel ids are easy to get wrong from memory (e.g. Somoy TV is `SomoyNewsTV.bd`, not `SomoyTV.bd`; Channel i is `ChannelI.bd`; BTV is `BTVNational.bd`). Every id here was matched against the live upstream CSV, and the checker script catches a wrong id before it breaks a playlist or EPG grab.
- No fake channels: the 5 guessed ids that were not in upstream were replaced with the real ones.

## ব্যবহার / How to use

```bash
# Validate the Bangla slice
python3 check-bangla.py

# Use it in your own iptv-org workflow (same CSV format as upstream)
# e.g. feed it to an EPG grabber or a playlist builder that reads data/channels.csv
```

Contributing a missing Bangladeshi channel: copy its row from upstream `data/channels.csv`, keep the column order, run the checker, and open a PR upstream too — see `CONTRIBUTING.md` in iptv-org/database.

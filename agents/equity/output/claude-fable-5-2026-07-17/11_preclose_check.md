# 11 Preclose Check — 2026-07-17

The scheduled fire at 15:59 ET landed inside the 15:45 ET preclose window; observations at 16:1x ET (IBKR snapshots, pre-official-close):

- SPY 742.29 last (−1.12% at the print; ts 16:17 ET AH tape), QQQ 694.86 (−1.57%), SOXX 520.10 (−1.96%) — a risk-off close led by semis; VIX 18.75 (+2.02, CBOE delayed quote, last trade 16:01 ET).
- No open positions exist (system has never published GO); no stop criterion fires. The only monitored condition — the HIGH_VOL regime trigger (VIX > 20 with SPY below both MAs) — did **not** fire: VIX 18.75.
- Action: none. The full pipeline proceeded on the official close (12).

These preclose prints differ from the official closes by the AH drift (SPY 742.29 AH vs 743.15 official) — the package scores on the official close only; this file records the checkpoint observation, nothing downstream cites it.

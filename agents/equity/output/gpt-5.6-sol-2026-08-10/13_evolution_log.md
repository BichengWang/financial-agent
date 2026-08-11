# 13 — Evolution Log

## Run context

| Field | Value |
| --- | --- |
| Run date / model | 2026-08-10 / gpt-5.6-sol |
| Final status | NO_TRADE |
| Regime | BULL |
| Evaluation window | 2026-08-03 through 2026-08-10, all models |
| Ledger | EQ n=819 eff_n=2; MF n=132 eff_n=2 |
| Weighted rank IC | -0.0518 |
| Track A eligibility | False — INSUFFICIENT_EFFECTIVE_N |
| Baseline flag | CROSS_MODEL_BASELINE |

### Packages in the review window

| Package | Model | Date | Status | Predictions | Numbered artifacts |
| --- | --- | --- | --- | --- | --- |
| claude-opus-5-2026-08-03 | claude-opus-5 | 2026-08-03 | NO_TRADE | 27 | 12 |
| claude-opus-5-2026-08-04 | claude-opus-5 | 2026-08-04 | NO_TRADE | 27 | 13 |
| claude-opus-5-2026-08-06 | claude-opus-5 | 2026-08-06 | NO_TRADE | 27 | 12 |
| claude-opus-5-2026-08-07 | claude-opus-5 | 2026-08-07 | NO_TRADE | 27 | 14 |
| gpt-5-2026-08-03 | gpt-5 | 2026-08-03 | HALTED | 3 | 12 |
| gpt-5.6-sol-2026-08-10 | gpt-5.6-sol | 2026-08-10 | NO_TRADE | 23 | 13 |
| gpt-5.6-sol-2026-08-10 | gpt-5.6-sol | 2026-08-10 | NO_TRADE | 23 | 13 |

## What worked

1. Post-close grounding completed for 519 histories and 23 published entries; independent
   price deviation was 0.0000%.
2. The settlement fix accepted all 77 same-day target-close rows; the entire 200-key due queue
   normalized to canonical state with due 0, conflicts 0 and rejected rows unchanged at 87.
3. The full union, technical helper, earnings sweep, risk analytics and core ETF block all
   completed without a Required-input gap.

## What failed

1. Equity hit rate is 39.19% and weighted rank IC is -0.0518. The score order is not predictive.
2. Market-forecast direction accuracy is 27.34%; CI coverage at 87.12% is above the healthy
   55-85% band, but `eff_n=2` prevents parameter action.
3. Fund_Z and Sent_Z remain unavailable, making the investable evidence gates impossible.

## Primary diagnosis

**Factor calibration.** Source grounding and intervals are broadly serviceable; cross-sectional
rank order remains the core failure [L028].

## Exactly one proposed change — Track A (`DEFER`)

**Proposal:** on the next eligible calibration study, shift 0.05 weight from Technical to Macro:
Technical 0.30 -> 0.25 and Macro 0.15 -> 0.20, leaving Fundamental 0.30 and Sentiment 0.25
unchanged. This is one coupled weight reallocation and stays inside the +/-0.05 single-step cap.

**Hypothesis:** reducing trend concentration should lift held-out rank IC above zero while
preserving or improving hit rate, drawdown and turnover. The present negative rank IC and the
July 13 momentum-lead failures motivate the test; they do not validate it.

**Validation gate:** raw equity n=819 clears n>=20, but `eff_n=2<3` fails the independent-window
gate. No holdout comparison may therefore be treated as acceptance evidence. Required future
validation is an untouched target window with deltas for IR, hit rate, drawdown and turnover,
and no protected-limit regression.

**Decision: `DEFER` — `INSUFFICIENT_EFFECTIVE_N`.** No scoring weight changes in this run.

## Effective next step

Keep all parameters unchanged. Re-evaluate after the equity ledger gains a third non-overlapping
28-day target window (projection: 2026-09-03), then run the proposal on a locked holdout. No
Track B change is proposed or accepted this run.

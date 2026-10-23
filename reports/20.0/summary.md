# OCA → 20.0 migration status

Generated 2026-10-23 00:50 UTC · 47 repos · 2245 modules tracked

## Totals

| status | modules |
|---|---:|
| todo | 945 |
| skipped-relevancy | 32 |
| claimed-by-others | 45 |
| blocked-by-deps | 552 |
| merged-in-fork | 130 |
| ready-for-upstream-pr | 541 |

## Changes since last run

_none_
## Per repo

| repo | todo | skipped-relevancy | claimed-by-others | blocked-by-deps | merged-in-fork | ready-for-upstream-pr |
|---|---:|---:|---:|---:|---:|---:|
| [account-analytic](account-analytic.csv) | 24 | 0 | 0 | 2 | 5 | 8 |
| [account-financial-reporting](account-financial-reporting.csv) | 5 | 0 | 0 | 1 | 4 | 1 |
| [account-financial-tools](account-financial-tools.csv) | 18 | 0 | 0 | 11 | 3 | 18 |
| [account-invoicing](account-invoicing.csv) | 42 | 2 | 0 | 11 | 9 | 26 |
| [account-reconcile](account-reconcile.csv) | 16 | 0 | 1 | 1 | 0 | 1 |
| [bank-payment](bank-payment.csv) | 10 | 0 | 2 | 9 | 0 | 1 |
| [bank-statement-import](bank-statement-import.csv) | 9 | 0 | 7 | 9 | 0 | 0 |
| [commission](commission.csv) | 0 | 5 | 0 | 8 | 2 | 1 |
| [connector](connector.csv) | 2 | 0 | 0 | 2 | 1 | 1 |
| [connector-telephony](connector-telephony.csv) | 3 | 0 | 0 | 1 | 0 | 0 |
| [contract](contract.csv) | 10 | 0 | 0 | 16 | 7 | 2 |
| [crm](crm.csv) | 12 | 0 | 1 | 3 | 5 | 13 |
| [delivery-carrier](delivery-carrier.csv) | 33 | 1 | 1 | 22 | 3 | 9 |
| [dms](dms.csv) | 1 | 0 | 0 | 9 | 0 | 0 |
| [e-commerce](e-commerce.csv) | 10 | 2 | 0 | 11 | 10 | 32 |
| [edi](edi.csv) | 7 | 3 | 0 | 27 | 2 | 2 |
| [field-service](field-service.csv) | 1 | 1 | 0 | 50 | 0 | 1 |
| [geospatial](geospatial.csv) | 3 | 0 | 0 | 9 | 0 | 1 |
| [helpdesk](helpdesk.csv) | 21 | 0 | 1 | 15 | 0 | 0 |
| [hr](hr.csv) | 13 | 0 | 1 | 14 | 1 | 9 |
| [knowledge](knowledge.csv) | 12 | 0 | 2 | 2 | 0 | 1 |
| [management-system](management-system.csv) | 4 | 0 | 0 | 34 | 0 | 1 |
| [manufacture](manufacture.csv) | 42 | 0 | 0 | 15 | 0 | 15 |
| [mis-builder](mis-builder.csv) | 0 | 0 | 0 | 0 | 3 | 0 |
| [multi-company](multi-company.csv) | 20 | 0 | 5 | 3 | 0 | 2 |
| [partner-contact](partner-contact.csv) | 42 | 2 | 3 | 7 | 15 | 47 |
| [payroll](payroll.csv) | 2 | 0 | 2 | 2 | 0 | 0 |
| [pos](pos.csv) | 45 | 2 | 1 | 12 | 1 | 2 |
| [product-attribute](product-attribute.csv) | 61 | 1 | 0 | 19 | 4 | 38 |
| [project](project.csv) | 28 | 1 | 1 | 6 | 4 | 38 |
| [purchase-workflow](purchase-workflow.csv) | 55 | 2 | 1 | 25 | 6 | 41 |
| [queue](queue.csv) | 4 | 0 | 2 | 1 | 1 | 1 |
| [report-print-send](report-print-send.csv) | 1 | 0 | 0 | 9 | 0 | 0 |
| [reporting-engine](reporting-engine.csv) | 14 | 0 | 1 | 5 | 4 | 15 |
| [sale-workflow](sale-workflow.csv) | 75 | 2 | 1 | 41 | 23 | 65 |
| [server-auth](server-auth.csv) | 13 | 0 | 4 | 7 | 1 | 8 |
| [server-backend](server-backend.csv) | 10 | 0 | 0 | 2 | 2 | 4 |
| [server-tools](server-tools.csv) | 28 | 0 | 3 | 7 | 2 | 26 |
| [server-ux](server-ux.csv) | 11 | 0 | 1 | 8 | 0 | 15 |
| [social](social.csv) | 50 | 1 | 0 | 15 | 0 | 1 |
| [stock-logistics-barcode](stock-logistics-barcode.csv) | 4 | 0 | 0 | 4 | 0 | 0 |
| [stock-logistics-warehouse](stock-logistics-warehouse.csv) | 48 | 3 | 0 | 34 | 2 | 14 |
| [stock-logistics-workflow](stock-logistics-workflow.csv) | 66 | 2 | 0 | 46 | 7 | 30 |
| [timesheet](timesheet.csv) | 13 | 0 | 1 | 9 | 1 | 13 |
| [vertical-hotel](vertical-hotel.csv) | 1 | 0 | 0 | 5 | 0 | 0 |
| [web](web.csv) | 33 | 1 | 1 | 2 | 2 | 33 |
| [website](website.csv) | 23 | 1 | 2 | 1 | 0 | 5 |

## Notes from this run

- 2026-10-23 (first full run): the Actions workflow had never produced a scan — `report.py` crashed on `diff_report.csv` (KeyError 'status'); fixed in 2da2ca0, workflow re-run manually, 47 repos / 2245 modules scanned (the "changes since last run" above is empty only because the scan commit precedes the verdicts commit; vs. the scan: 32 todo/blocked → skipped-relevancy, 2245 new candidates).
- Relevancy: 1529 verdicts recorded (1497 relevant, 17 native-in-target, 15 deprecated-upstream). Please eyeball the 32 skips (`relevancy` ≠ relevant in the CSVs; e.g. commission/* renamed to *_oca, edi Factur-X/UBL import now core, partner_title_* and stock_valuation_layer_* models gone in 19.0); `overrides.csv` reinstates any.
- Migration NOT run: 25 candidates were ready (base_tier_validation, dms, mail_tracking, mail_activity_board, account_chart_update, sale_blanket_order, web_widget_bokeh_chart, jsonifier, …) but this scheduled session cannot reach the BADEP forks (no `add_repo` tool; git push and API return 403 for BADEP/web — only BADEP/addons and BADEP/oca-migration-tools are attached) and cannot install pre-commit / odoo-module-migrator (pypi.org is not an allowed domain, so `bootstrap.sh` fails).
- Needs a human: (1) give the scheduled task access to all BADEP fork repos (or run it from a session where add_repo works), (2) allow pypi.org and files.pythonhosted.org for the session's network, (3) the task fired Thu 23:30 UTC, i.e. before the Friday 09:00 UTC Actions cron — move it to ~11:00 UTC Friday so the scan is fresh.
- Repair / merge: nothing to do — no fork PR with failing CI (`ci` column is empty everywhere; the 671 modules already merged-in-fork / ready-for-upstream-pr come from earlier work and have no open PR).
- OCA pages re-read: migration wiki for 20.0 (last edit 2026-09-08) and the AI policy (merged 2026-07-18, `Assisted-by:` trailer, no `Co-authored-by:` for tools, no unsupervised agents) — nothing new beyond what the scripts already do.

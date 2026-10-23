# OCA → 20.0 migration status

Generated 2026-10-23 17:17 UTC · 47 repos · 2246 modules tracked

## Totals

| status | modules |
|---|---:|
| todo | 924 |
| skipped-relevancy | 32 |
| claimed-by-others | 39 |
| blocked-by-deps | 574 |
| merged-in-fork | 126 |
| ready-for-upstream-pr | 551 |

## Changes since last run

### claimed-by-others → blocked-by-deps (1)
- sale-workflow/sales_team_security_crm

### claimed-by-others → todo (5)
- server-tools/auto_backup
- server-tools/autovacuum_message_attachment
- server-tools/field_vector
- server-ux/announcement
- web/web_disable_export_group

### todo → blocked-by-deps (19)
- account-financial-tools/account_asset_compute_batch
- account-financial-tools/account_asset_low_value
- account-financial-tools/account_asset_management_stock_lot
- account-financial-tools/account_asset_number
- account-financial-tools/account_asset_transfer
- account-financial-tools/account_bank_statement_chatter
- account-financial-tools/account_dashboard_banner_mis_builder
- sale-workflow/pricelist_cache
- sale-workflow/sale_cancel_confirm
- sale-workflow/sale_invoice_delivery_state
- sale-workflow/sale_order_invoicing_picking_filter
- sale-workflow/sale_order_lot_selection
- sale-workflow/sale_partner_utm_source
- sale-workflow/sale_product_identification
- sale-workflow/sale_product_set_packaging_qty
- sale-workflow/sale_resource_booking
- sale-workflow/sale_triple_discount
- server-tools/attachment_queue
- web/web_responsive_company_color

### todo → ready-for-upstream-pr (8)
- account-financial-tools/account_chart_update
- dms/dms
- sale-workflow/sale_blanket_order
- server-tools/jsonifier
- server-ux/base_tier_validation
- social/mail_activity_board
- social/mail_tracking
- web/web_widget_bokeh_chart

## Per repo

| repo | todo | skipped-relevancy | claimed-by-others | blocked-by-deps | merged-in-fork | ready-for-upstream-pr |
|---|---:|---:|---:|---:|---:|---:|
| [account-analytic](account-analytic.csv) | 25 | 0 | 0 | 2 | 4 | 9 |
| [account-financial-reporting](account-financial-reporting.csv) | 5 | 0 | 0 | 1 | 4 | 1 |
| [account-financial-tools](account-financial-tools.csv) | 10 | 0 | 0 | 18 | 3 | 19 |
| [account-invoicing](account-invoicing.csv) | 42 | 2 | 0 | 11 | 8 | 27 |
| [account-reconcile](account-reconcile.csv) | 16 | 0 | 1 | 1 | 0 | 1 |
| [bank-payment](bank-payment.csv) | 10 | 0 | 2 | 9 | 0 | 1 |
| [bank-statement-import](bank-statement-import.csv) | 9 | 0 | 7 | 9 | 0 | 0 |
| [commission](commission.csv) | 0 | 5 | 0 | 8 | 2 | 1 |
| [connector](connector.csv) | 2 | 0 | 0 | 2 | 1 | 1 |
| [connector-telephony](connector-telephony.csv) | 3 | 0 | 0 | 1 | 0 | 0 |
| [contract](contract.csv) | 10 | 0 | 0 | 16 | 7 | 2 |
| [crm](crm.csv) | 12 | 0 | 1 | 3 | 5 | 13 |
| [delivery-carrier](delivery-carrier.csv) | 33 | 1 | 1 | 22 | 3 | 9 |
| [dms](dms.csv) | 0 | 0 | 0 | 9 | 0 | 1 |
| [e-commerce](e-commerce.csv) | 10 | 2 | 0 | 11 | 10 | 32 |
| [edi](edi.csv) | 7 | 3 | 0 | 27 | 2 | 2 |
| [field-service](field-service.csv) | 1 | 1 | 0 | 50 | 0 | 1 |
| [geospatial](geospatial.csv) | 3 | 0 | 0 | 9 | 0 | 1 |
| [helpdesk](helpdesk.csv) | 21 | 0 | 1 | 15 | 0 | 0 |
| [hr](hr.csv) | 13 | 0 | 1 | 14 | 1 | 9 |
| [knowledge](knowledge.csv) | 12 | 0 | 2 | 2 | 0 | 1 |
| [management-system](management-system.csv) | 4 | 0 | 0 | 34 | 0 | 1 |
| [manufacture](manufacture.csv) | 42 | 0 | 0 | 16 | 0 | 15 |
| [mis-builder](mis-builder.csv) | 0 | 0 | 0 | 0 | 3 | 0 |
| [multi-company](multi-company.csv) | 20 | 0 | 5 | 3 | 0 | 2 |
| [partner-contact](partner-contact.csv) | 43 | 2 | 3 | 6 | 15 | 47 |
| [payroll](payroll.csv) | 2 | 0 | 2 | 2 | 0 | 0 |
| [pos](pos.csv) | 45 | 2 | 1 | 12 | 1 | 2 |
| [product-attribute](product-attribute.csv) | 61 | 1 | 0 | 19 | 4 | 38 |
| [project](project.csv) | 29 | 1 | 1 | 6 | 4 | 38 |
| [purchase-workflow](purchase-workflow.csv) | 55 | 2 | 1 | 25 | 5 | 42 |
| [queue](queue.csv) | 4 | 0 | 2 | 1 | 1 | 1 |
| [report-print-send](report-print-send.csv) | 1 | 0 | 0 | 9 | 0 | 0 |
| [reporting-engine](reporting-engine.csv) | 14 | 0 | 1 | 5 | 4 | 15 |
| [sale-workflow](sale-workflow.csv) | 63 | 2 | 0 | 53 | 23 | 66 |
| [server-auth](server-auth.csv) | 13 | 0 | 4 | 7 | 1 | 8 |
| [server-backend](server-backend.csv) | 10 | 0 | 0 | 2 | 2 | 4 |
| [server-tools](server-tools.csv) | 29 | 0 | 0 | 8 | 2 | 26 |
| [server-ux](server-ux.csv) | 11 | 0 | 0 | 8 | 0 | 16 |
| [social](social.csv) | 48 | 1 | 0 | 15 | 0 | 3 |
| [stock-logistics-barcode](stock-logistics-barcode.csv) | 4 | 0 | 0 | 4 | 0 | 0 |
| [stock-logistics-warehouse](stock-logistics-warehouse.csv) | 47 | 3 | 0 | 35 | 2 | 13 |
| [stock-logistics-workflow](stock-logistics-workflow.csv) | 66 | 2 | 0 | 46 | 7 | 30 |
| [timesheet](timesheet.csv) | 13 | 0 | 1 | 9 | 1 | 13 |
| [vertical-hotel](vertical-hotel.csv) | 1 | 0 | 0 | 5 | 0 | 0 |
| [web](web.csv) | 32 | 1 | 0 | 3 | 1 | 35 |
| [website](website.csv) | 23 | 1 | 2 | 1 | 0 | 5 |

## Notes from this run

- Earlier scheduled run (11:08 UTC): relevancy done (1529 verdicts); migration blocked (no add_repo, 403 on forks, pypi.org unresolved).
- Interactive run (16:40-17:45 UTC): 3 new relevancy verdicts (all relevant); 8 modules migrated, 16 not started (stopped on request).
- Migrated and merged into fork 20.0 on request, before CI: base_tier_validation, dms, mail_tracking, mail_activity_board, sale_blanket_order, account_chart_update, web_widget_bokeh_chart, jsonifier.
- Needs a human: 7 of those were built without pre-commit/odoo-module-migrator; rebuild with REBUILD=1 before any OCA PR (only mail_activity_board is complete). "ready-for-upstream-pr" is not true for any of them yet.
- dms and mail_tracking keep an old-style version (20.0.1.1.6 / 20.0.1.0.5); fixed by the rebuild.
- account_chart_update, web_widget_bokeh_chart, jsonifier: merge conflicts in other modules (fork 20.0 behind OCA/20.0); OCA side taken.
- Tooling fixed: human commit identity (config.migrate.commit_identity, exit 13 guard), version reset to 20.0.1.0.0, migrator capped at its last supported version (19.0), REBUILD=1.
- Sandbox: pypi.org, files.pythonhosted.org, registry.npmjs.org must be removed from NO_PROXY/no_proxy/npm_config_noproxy; PRs via REST (no GraphQL).
- Branches first pushed with a Claude identity were rewritten (author/committer Khalid Hazam).
- Live 20.0 wiki does not mention the selection_badge split noted in GUIDELINES.md: to confirm.


# OCA → 20.0 migration status

Generated 2026-10-26 23:00 UTC · 47 repos · 2250 modules tracked

## Totals

| status | modules |
|---|---:|
| todo | 938 |
| skipped-relevancy | 33 |
| claimed-by-others | 76 |
| blocked-by-deps | 502 |
| pr-to-fork | 25 |
| merged-in-fork | 129 |
| ready-for-upstream-pr | 547 |

## Changes since last run

### ready-for-upstream-pr → merged-in-fork (3)
- account-analytic/purchase_analytic
- account-invoicing/account_invoice_transmit_method
- web/web_m2x_options_manager

### todo → blocked-by-deps (25)
- account-analytic/purchase_request_analytic
- account-analytic/sale_analytic
- account-financial-tools/account_dashboard_banner_mis_builder
- account-financial-tools/account_fiscal_month
- account-financial-tools/account_move_budget
- account-financial-tools/account_move_line_purchase_info
- account-invoicing/account_invoice_auto_send_by_email
- account-invoicing/product_customerinfo_invoice
- account-reconcile/account_reconcile_oca_add_default_filters
- account-reconcile/account_reconcile_oca_queue
- delivery-carrier/delivery_carrier_report_to_printer
- edi/account_invoice_export_job
- partner-contact/partner_noncommercial
- project/project_task_stock_product_set
- reporting-engine/report_async
- sale-workflow/pricelist_cache
- sale-workflow/sale_block_no_stock
- sale-workflow/sale_cancel_confirm
- sale-workflow/sale_invoice_policy
- sale-workflow/sale_order_invoicing_picking_filter
- sale-workflow/sale_order_product_availability_inline
- sale-workflow/sale_stock_line_sequence
- stock-logistics-warehouse/stock_demand_estimate_matrix
- stock-logistics-warehouse/stock_exception
- stock-logistics-warehouse/stock_inventory_preparation_filter

### todo → pr-to-fork (25)
- account-analytic/account_analytic_distribution_manual
- account-analytic/account_analytic_parent
- account-financial-tools/account_loan
- account-invoicing/account_manual_currency
- account-reconcile/account_mass_reconcile
- account-reconcile/account_reconcile_model_oca
- delivery-carrier/delivery_package_number
- edi/account_einvoice_generate
- knowledge/attachment_preview
- partner-contact/partner_email_check
- pos/pos_order_to_sale_order
- project/project_timesheet_time_control
- reporting-engine/bi_view_editor
- sale-workflow/sale_procurement_group_by_line
- social/mail_attach_existing_attachment
- social/mail_autosubscribe
- social/mail_debrand
- social/mail_gateway
- social/mail_outbound_static
- social/mass_mailing_partner
- stock-logistics-warehouse/account_move_line_stock_info
- web/web_theme_classic
- web/web_tree_dynamic_colored_field
- web/web_widget_open_tab
- website/website_odoo_debranding

## Per repo

| repo | todo | skipped-relevancy | claimed-by-others | blocked-by-deps | pr-to-fork | merged-in-fork | ready-for-upstream-pr |
|---|---:|---:|---:|---:|---:|---:|---:|
| [account-analytic](account-analytic.csv) | 21 | 0 | 0 | 4 | 2 | 5 | 8 |
| [account-financial-reporting](account-financial-reporting.csv) | 5 | 0 | 0 | 1 | 0 | 4 | 1 |
| [account-financial-tools](account-financial-tools.csv) | 14 | 0 | 0 | 13 | 1 | 3 | 19 |
| [account-invoicing](account-invoicing.csv) | 39 | 2 | 1 | 12 | 1 | 9 | 26 |
| [account-reconcile](account-reconcile.csv) | 12 | 0 | 1 | 3 | 2 | 0 | 1 |
| [bank-payment](bank-payment.csv) | 10 | 0 | 2 | 9 | 0 | 0 | 1 |
| [bank-statement-import](bank-statement-import.csv) | 9 | 0 | 7 | 9 | 0 | 0 | 0 |
| [commission](commission.csv) | 0 | 5 | 0 | 8 | 0 | 2 | 1 |
| [connector](connector.csv) | 2 | 0 | 0 | 2 | 0 | 1 | 1 |
| [connector-telephony](connector-telephony.csv) | 3 | 0 | 0 | 1 | 0 | 0 | 0 |
| [contract](contract.csv) | 10 | 0 | 1 | 15 | 0 | 7 | 2 |
| [crm](crm.csv) | 12 | 0 | 1 | 3 | 0 | 5 | 13 |
| [delivery-carrier](delivery-carrier.csv) | 32 | 1 | 1 | 22 | 1 | 3 | 9 |
| [dms](dms.csv) | 0 | 0 | 0 | 9 | 0 | 0 | 1 |
| [e-commerce](e-commerce.csv) | 10 | 3 | 0 | 11 | 0 | 10 | 32 |
| [edi](edi.csv) | 5 | 3 | 0 | 28 | 1 | 2 | 2 |
| [field-service](field-service.csv) | 1 | 1 | 0 | 50 | 0 | 0 | 1 |
| [geospatial](geospatial.csv) | 3 | 0 | 0 | 9 | 0 | 0 | 1 |
| [helpdesk](helpdesk.csv) | 22 | 0 | 1 | 14 | 0 | 0 | 0 |
| [hr](hr.csv) | 13 | 0 | 1 | 14 | 0 | 1 | 9 |
| [knowledge](knowledge.csv) | 11 | 0 | 2 | 2 | 1 | 0 | 1 |
| [management-system](management-system.csv) | 19 | 0 | 15 | 4 | 0 | 0 | 1 |
| [manufacture](manufacture.csv) | 42 | 0 | 1 | 16 | 0 | 0 | 15 |
| [mis-builder](mis-builder.csv) | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| [multi-company](multi-company.csv) | 20 | 0 | 5 | 3 | 0 | 0 | 2 |
| [partner-contact](partner-contact.csv) | 42 | 2 | 4 | 5 | 1 | 15 | 47 |
| [payroll](payroll.csv) | 2 | 0 | 2 | 2 | 0 | 0 | 0 |
| [pos](pos.csv) | 45 | 2 | 1 | 12 | 1 | 1 | 2 |
| [product-attribute](product-attribute.csv) | 63 | 1 | 0 | 17 | 0 | 4 | 38 |
| [project](project.csv) | 27 | 1 | 1 | 7 | 1 | 4 | 37 |
| [purchase-workflow](purchase-workflow.csv) | 57 | 2 | 2 | 22 | 0 | 5 | 42 |
| [queue](queue.csv) | 4 | 0 | 2 | 1 | 0 | 1 | 1 |
| [report-print-send](report-print-send.csv) | 6 | 0 | 1 | 3 | 0 | 0 | 0 |
| [reporting-engine](reporting-engine.csv) | 12 | 0 | 1 | 6 | 1 | 4 | 15 |
| [sale-workflow](sale-workflow.csv) | 68 | 2 | 3 | 44 | 1 | 23 | 66 |
| [server-auth](server-auth.csv) | 13 | 0 | 4 | 7 | 0 | 1 | 8 |
| [server-backend](server-backend.csv) | 10 | 0 | 0 | 2 | 0 | 2 | 4 |
| [server-tools](server-tools.csv) | 26 | 0 | 4 | 7 | 0 | 2 | 26 |
| [server-ux](server-ux.csv) | 11 | 0 | 1 | 7 | 0 | 0 | 16 |
| [social](social.csv) | 42 | 1 | 0 | 16 | 6 | 0 | 3 |
| [stock-logistics-barcode](stock-logistics-barcode.csv) | 4 | 0 | 2 | 2 | 0 | 0 | 0 |
| [stock-logistics-warehouse](stock-logistics-warehouse.csv) | 51 | 3 | 1 | 29 | 1 | 2 | 13 |
| [stock-logistics-workflow](stock-logistics-workflow.csv) | 73 | 2 | 2 | 37 | 0 | 7 | 30 |
| [timesheet](timesheet.csv) | 13 | 0 | 1 | 9 | 0 | 1 | 13 |
| [vertical-hotel](vertical-hotel.csv) | 2 | 0 | 2 | 2 | 0 | 0 | 0 |
| [web](web.csv) | 29 | 1 | 1 | 2 | 3 | 2 | 34 |
| [website](website.csv) | 23 | 1 | 2 | 1 | 1 | 0 | 5 |

## Notes from this run

- 2026-10-26, interactive run on the maintainer's machine (local clones, `gh` authenticated). Relevancy: 4 relevant, 1 native-in-target (`website_sale_category_smart_button`).
- Migrated 25 modules (the cap), all exit 0, no conflicts, no dependency PRs; one `[20.0][MIG]` PR each on the BADEP forks (status `pr-to-fork`).
- Review: 8 formatting-only, 17 reviewed by subagents, no unexplained changes, nothing reverted. Core API changes found were required by 20.0 (`models.Constraint`, `group_ids`, `fields.Domain`, `env.context`).
- Wiki changed 2026-10-23, two tasks `migrate_module.sh` does not do: ACL/`ir.rule` to `ir.access`, and `_test_user_groups = None` on `BaseCommon` tests. Pending on account_loan, account_analytic_distribution_manual, mail_gateway, delivery_package_number, account_move_line_stock_info, project_timesheet_time_control, attachment_preview.
- Human decision: add those two tasks to the list in `docs/GUIDELINES.md` and to `migrate_module.sh`.
- BLOCKER: CI cannot run on any of the 16 forks (Actions enabled but 0 workflows registered, 0 runs ever). `ci` stays empty, so no repair round and no merge into the forks' 20.0 this run. Enable Actions in each fork's Actions tab, then close/reopen the PRs.
- Forks already hold many older `20.0-mig-*` branches from earlier work; none touched by this run.


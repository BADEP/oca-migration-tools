# OCA → 20.0 migration status

Generated 2026-10-28 23:41 UTC · 47 repos · 2249 modules tracked

## Totals

| status | modules |
|---|---:|
| todo | 987 |
| skipped-relevancy | 33 |
| claimed-by-others | 87 |
| blocked-by-deps | 446 |
| pr-to-fork | 25 |
| merged-in-fork | 126 |
| ready-for-upstream-pr | 545 |

## Changes since last run

### CI failing on our fork PR (23)
- account-analytic/account_analytic_distribution_manual https://github.com/BADEP/account-analytic/pull/15
- account-analytic/account_analytic_parent https://github.com/BADEP/account-analytic/pull/16
- account-financial-tools/account_loan https://github.com/BADEP/account-financial-tools/pull/24
- account-invoicing/account_manual_currency https://github.com/BADEP/account-invoicing/pull/36
- account-reconcile/account_mass_reconcile https://github.com/BADEP/account-reconcile/pull/3
- account-reconcile/account_reconcile_model_oca https://github.com/BADEP/account-reconcile/pull/2
- delivery-carrier/delivery_package_number https://github.com/BADEP/delivery-carrier/pull/13
- edi/account_einvoice_generate https://github.com/BADEP/edi/pull/5
- knowledge/attachment_preview https://github.com/BADEP/knowledge/pull/2
- partner-contact/partner_email_check https://github.com/BADEP/partner-contact/pull/63
- pos/pos_order_to_sale_order https://github.com/BADEP/pos/pull/4
- reporting-engine/bi_view_editor https://github.com/BADEP/reporting-engine/pull/20
- sale-workflow/sale_procurement_group_by_line https://github.com/BADEP/sale-workflow/pull/91
- social/mail_attach_existing_attachment https://github.com/BADEP/social/pull/7
- social/mail_autosubscribe https://github.com/BADEP/social/pull/9
- social/mail_debrand https://github.com/BADEP/social/pull/6
- social/mail_gateway https://github.com/BADEP/social/pull/8
- social/mail_outbound_static https://github.com/BADEP/social/pull/5
- social/mass_mailing_partner https://github.com/BADEP/social/pull/4
- web/web_theme_classic https://github.com/BADEP/web/pull/40
- web/web_tree_dynamic_colored_field https://github.com/BADEP/web/pull/38
- web/web_widget_open_tab https://github.com/BADEP/web/pull/39
- website/website_odoo_debranding https://github.com/BADEP/website/pull/6

### in-progress → pr-to-fork (25)
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
| [account-analytic](account-analytic.csv) | 23 | 0 | 0 | 2 | 2 | 4 | 9 |
| [account-financial-reporting](account-financial-reporting.csv) | 5 | 0 | 0 | 1 | 0 | 4 | 1 |
| [account-financial-tools](account-financial-tools.csv) | 18 | 0 | 2 | 7 | 1 | 3 | 19 |
| [account-invoicing](account-invoicing.csv) | 43 | 2 | 1 | 10 | 1 | 8 | 27 |
| [account-reconcile](account-reconcile.csv) | 14 | 0 | 1 | 1 | 2 | 0 | 1 |
| [bank-payment](bank-payment.csv) | 11 | 0 | 4 | 6 | 0 | 0 | 1 |
| [bank-statement-import](bank-statement-import.csv) | 9 | 0 | 7 | 9 | 0 | 0 | 0 |
| [commission](commission.csv) | 0 | 5 | 0 | 8 | 0 | 2 | 1 |
| [connector](connector.csv) | 2 | 0 | 0 | 2 | 0 | 1 | 1 |
| [connector-telephony](connector-telephony.csv) | 3 | 0 | 0 | 1 | 0 | 0 | 0 |
| [contract](contract.csv) | 13 | 0 | 3 | 10 | 0 | 7 | 2 |
| [crm](crm.csv) | 12 | 0 | 1 | 3 | 0 | 5 | 13 |
| [delivery-carrier](delivery-carrier.csv) | 33 | 1 | 1 | 22 | 1 | 3 | 9 |
| [dms](dms.csv) | 5 | 0 | 1 | 3 | 0 | 0 | 1 |
| [e-commerce](e-commerce.csv) | 10 | 3 | 0 | 11 | 0 | 10 | 32 |
| [edi](edi.csv) | 6 | 3 | 0 | 27 | 1 | 2 | 2 |
| [field-service](field-service.csv) | 1 | 1 | 0 | 50 | 0 | 0 | 1 |
| [geospatial](geospatial.csv) | 3 | 0 | 0 | 9 | 0 | 0 | 1 |
| [helpdesk](helpdesk.csv) | 22 | 0 | 1 | 14 | 0 | 0 | 0 |
| [hr](hr.csv) | 13 | 0 | 1 | 14 | 0 | 1 | 9 |
| [knowledge](knowledge.csv) | 11 | 0 | 2 | 2 | 1 | 0 | 1 |
| [management-system](management-system.csv) | 19 | 0 | 15 | 4 | 0 | 0 | 1 |
| [manufacture](manufacture.csv) | 43 | 0 | 2 | 14 | 0 | 0 | 15 |
| [mis-builder](mis-builder.csv) | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| [multi-company](multi-company.csv) | 20 | 0 | 5 | 3 | 0 | 0 | 2 |
| [partner-contact](partner-contact.csv) | 43 | 2 | 4 | 4 | 1 | 15 | 47 |
| [payroll](payroll.csv) | 2 | 0 | 2 | 2 | 0 | 0 | 0 |
| [pos](pos.csv) | 45 | 2 | 1 | 12 | 1 | 1 | 2 |
| [product-attribute](product-attribute.csv) | 63 | 1 | 0 | 18 | 0 | 4 | 35 |
| [project](project.csv) | 30 | 1 | 1 | 4 | 1 | 4 | 37 |
| [purchase-workflow](purchase-workflow.csv) | 59 | 2 | 3 | 19 | 0 | 5 | 42 |
| [queue](queue.csv) | 5 | 0 | 2 | 0 | 0 | 1 | 1 |
| [report-print-send](report-print-send.csv) | 5 | 0 | 3 | 2 | 0 | 0 | 0 |
| [reporting-engine](reporting-engine.csv) | 13 | 0 | 1 | 5 | 1 | 4 | 15 |
| [sale-workflow](sale-workflow.csv) | 81 | 2 | 3 | 31 | 1 | 23 | 66 |
| [server-auth](server-auth.csv) | 13 | 0 | 4 | 7 | 0 | 1 | 8 |
| [server-backend](server-backend.csv) | 10 | 0 | 0 | 2 | 0 | 2 | 4 |
| [server-tools](server-tools.csv) | 26 | 0 | 4 | 7 | 0 | 2 | 26 |
| [server-ux](server-ux.csv) | 11 | 0 | 1 | 7 | 0 | 0 | 16 |
| [social](social.csv) | 42 | 1 | 0 | 16 | 6 | 0 | 3 |
| [stock-logistics-barcode](stock-logistics-barcode.csv) | 5 | 0 | 2 | 1 | 0 | 0 | 0 |
| [stock-logistics-warehouse](stock-logistics-warehouse.csv) | 55 | 3 | 1 | 25 | 1 | 2 | 13 |
| [stock-logistics-workflow](stock-logistics-workflow.csv) | 73 | 2 | 2 | 37 | 0 | 7 | 30 |
| [timesheet](timesheet.csv) | 13 | 0 | 1 | 9 | 0 | 1 | 13 |
| [vertical-hotel](vertical-hotel.csv) | 2 | 0 | 2 | 2 | 0 | 0 | 0 |
| [web](web.csv) | 29 | 1 | 1 | 2 | 3 | 1 | 33 |
| [website](website.csv) | 23 | 1 | 2 | 1 | 1 | 0 | 5 |

## Notes from this run


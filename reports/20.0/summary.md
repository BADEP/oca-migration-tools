# OCA → 20.0 migration status

Generated 2026-10-30 12:08 UTC · 47 repos · 2247 modules tracked

## Totals

| status | modules |
|---|---:|
| todo | 977 |
| skipped-relevancy | 33 |
| claimed-by-others | 104 |
| blocked-by-deps | 443 |
| pr-to-fork | 25 |
| merged-in-fork | 125 |
| ready-for-upstream-pr | 540 |

## Changes since last run

### blocked-by-deps → claimed-by-others (5)
- dms/web_editor_media_dialog_dms
- manufacture/mrp_multi_level
- server-auth/vault_share
- vertical-hotel/hotel_restaurant
- vertical-hotel/report_hotel_restaurant

### blocked-by-deps → todo (5)
- account-analytic/account_analytic_parent_plan_restrict
- manufacture/mrp_multi_level_consume_safety_stock
- manufacture/mrp_multi_level_estimate
- sale-workflow/sale_product_catalog_extended
- server-ux/server_action_mass_edit_onchange

### merged-in-fork → ready-for-upstream-pr (1)
- queue/test_queue_job

### new candidates (4)
- contract/contract_line_defer
- contract/contract_line_defer_successor
- contract/product_contract_line_defer
- social/social_media_x_sync

### removed from report (6)
- partner-contact/partner_contact_department
- purchase-workflow/purchase_all_shipments
- queue/queue_job
- web/web_quick_start_screen
- web/web_refresher
- web/web_widget_numeric_step

### todo → blocked-by-deps (5)
- edi/account_invoice_export_job
- manufacture/mrp_production_serial_matrix_queue_job
- sale-workflow/pricelist_cache
- sale-workflow/sale_order_product_recommendation_packaging_default
- stock-logistics-barcode/stock_barcodes

### todo → claimed-by-others (12)
- account-analytic/account_analytic_line_commercial_partner
- account-analytic/mrp_stock_analytic
- account-financial-tools/account_move_budget
- dms/hr_dms_field
- manufacture/mrp_warehouse_calendar
- purchase-workflow/purchase_lot
- sale-workflow/sale_order_lot_generator
- server-auth/vault
- stock-logistics-workflow/sale_stock_picking_invoice_link
- vertical-hotel/report_hotel_reservation
- web/web_filter_header_button
- web/web_pivot_computed_measure

## Per repo

| repo | todo | skipped-relevancy | claimed-by-others | blocked-by-deps | pr-to-fork | merged-in-fork | ready-for-upstream-pr |
|---|---:|---:|---:|---:|---:|---:|---:|
| [account-analytic](account-analytic.csv) | 22 | 0 | 2 | 1 | 2 | 4 | 9 |
| [account-financial-reporting](account-financial-reporting.csv) | 5 | 0 | 0 | 1 | 0 | 4 | 1 |
| [account-financial-tools](account-financial-tools.csv) | 17 | 0 | 3 | 7 | 1 | 3 | 19 |
| [account-invoicing](account-invoicing.csv) | 43 | 2 | 1 | 10 | 1 | 8 | 27 |
| [account-reconcile](account-reconcile.csv) | 14 | 0 | 1 | 1 | 2 | 0 | 1 |
| [bank-payment](bank-payment.csv) | 11 | 0 | 4 | 6 | 0 | 0 | 1 |
| [bank-statement-import](bank-statement-import.csv) | 9 | 0 | 7 | 9 | 0 | 0 | 0 |
| [commission](commission.csv) | 0 | 5 | 0 | 8 | 0 | 2 | 1 |
| [connector](connector.csv) | 2 | 0 | 0 | 2 | 0 | 1 | 1 |
| [connector-telephony](connector-telephony.csv) | 3 | 0 | 0 | 1 | 0 | 0 | 0 |
| [contract](contract.csv) | 15 | 0 | 3 | 11 | 0 | 7 | 2 |
| [crm](crm.csv) | 12 | 0 | 1 | 3 | 0 | 5 | 13 |
| [delivery-carrier](delivery-carrier.csv) | 33 | 1 | 1 | 22 | 1 | 3 | 9 |
| [dms](dms.csv) | 4 | 0 | 3 | 2 | 0 | 0 | 1 |
| [e-commerce](e-commerce.csv) | 10 | 3 | 0 | 11 | 0 | 10 | 32 |
| [edi](edi.csv) | 5 | 3 | 0 | 28 | 1 | 2 | 2 |
| [field-service](field-service.csv) | 1 | 1 | 0 | 50 | 0 | 0 | 1 |
| [geospatial](geospatial.csv) | 3 | 0 | 0 | 9 | 0 | 0 | 1 |
| [helpdesk](helpdesk.csv) | 22 | 0 | 1 | 14 | 0 | 0 | 0 |
| [hr](hr.csv) | 13 | 0 | 1 | 14 | 0 | 1 | 9 |
| [knowledge](knowledge.csv) | 11 | 0 | 2 | 2 | 1 | 0 | 1 |
| [management-system](management-system.csv) | 19 | 0 | 15 | 4 | 0 | 0 | 1 |
| [manufacture](manufacture.csv) | 43 | 0 | 4 | 12 | 0 | 0 | 15 |
| [mis-builder](mis-builder.csv) | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| [multi-company](multi-company.csv) | 20 | 0 | 5 | 3 | 0 | 0 | 2 |
| [partner-contact](partner-contact.csv) | 43 | 2 | 4 | 4 | 1 | 15 | 46 |
| [payroll](payroll.csv) | 2 | 0 | 2 | 2 | 0 | 0 | 0 |
| [pos](pos.csv) | 45 | 2 | 1 | 12 | 1 | 1 | 2 |
| [product-attribute](product-attribute.csv) | 63 | 1 | 0 | 18 | 0 | 4 | 35 |
| [project](project.csv) | 30 | 1 | 1 | 4 | 1 | 4 | 37 |
| [purchase-workflow](purchase-workflow.csv) | 58 | 2 | 4 | 19 | 0 | 5 | 41 |
| [queue](queue.csv) | 5 | 0 | 2 | 0 | 0 | 0 | 1 |
| [report-print-send](report-print-send.csv) | 5 | 0 | 3 | 2 | 0 | 0 | 0 |
| [reporting-engine](reporting-engine.csv) | 13 | 0 | 1 | 5 | 1 | 4 | 15 |
| [sale-workflow](sale-workflow.csv) | 79 | 2 | 4 | 32 | 1 | 23 | 66 |
| [server-auth](server-auth.csv) | 12 | 0 | 6 | 6 | 0 | 1 | 8 |
| [server-backend](server-backend.csv) | 10 | 0 | 0 | 2 | 0 | 2 | 4 |
| [server-tools](server-tools.csv) | 26 | 0 | 4 | 7 | 0 | 2 | 26 |
| [server-ux](server-ux.csv) | 12 | 0 | 1 | 6 | 0 | 0 | 16 |
| [social](social.csv) | 42 | 1 | 0 | 17 | 6 | 0 | 3 |
| [stock-logistics-barcode](stock-logistics-barcode.csv) | 4 | 0 | 2 | 2 | 0 | 0 | 0 |
| [stock-logistics-warehouse](stock-logistics-warehouse.csv) | 55 | 3 | 1 | 25 | 1 | 2 | 13 |
| [stock-logistics-workflow](stock-logistics-workflow.csv) | 72 | 2 | 3 | 37 | 0 | 7 | 30 |
| [timesheet](timesheet.csv) | 13 | 0 | 1 | 9 | 0 | 1 | 13 |
| [vertical-hotel](vertical-hotel.csv) | 1 | 0 | 5 | 0 | 0 | 0 | 0 |
| [web](web.csv) | 27 | 1 | 3 | 2 | 3 | 1 | 30 |
| [website](website.csv) | 23 | 1 | 2 | 1 | 1 | 0 | 5 |

## Notes from this run


# OCA → 20.0 migration status

Generated 2026-11-06 13:23 UTC · 47 repos · 2243 modules tracked

## Totals

| status | modules |
|---|---:|
| todo | 991 |
| skipped-relevancy | 31 |
| claimed-by-others | 124 |
| blocked-by-deps | 417 |
| pr-to-fork | 25 |
| merged-in-fork | 120 |
| ready-for-upstream-pr | 535 |

## Changes since last run

### blocked-by-deps → claimed-by-others (6)
- commission/sale_commission_oca
- geospatial/base_geoengine_demo
- geospatial/geoengine_partner
- hr/hr_contract_reference
- hr/hr_employee_ppe
- hr/hr_job_category

### blocked-by-deps → todo (28)
- account-financial-tools/account_chart_update_code_digits
- account-financial-tools/account_chart_update_l10n_eu_oss
- account-invoicing/account_invoice_transmit_method_substitution_rule
- bank-payment/account_banking_mandate_sale_contact
- commission/commission_formula_oca
- commission/sale_commission_margin_oca
- commission/sale_commission_oca_product_criteria
- commission/sale_commission_pricelist_oca
- commission/sale_commission_salesman
- connector/connector_base_product
- connector/test_connector
- contract/contract_transmit_method
- crm/crm_partner_employee_quantity
- delivery-carrier/delivery_dachser
- edi/base_ebill_payment_contract
- geospatial/geoengine_base_geolocalize
- hr/hr_employee_document_from_applicant
- hr/hr_personal_equipment_stock
- multi-company/product_multi_company_stock
- pos/pos_product_multi_barcode
- product-attribute/product_state_active
- product-attribute/product_state_stock_base
- purchase-workflow/purchase_stock_line_sequence
- sale-workflow/pricelist_cache_rest
- sale-workflow/sale_order_transmit_method
- stock-logistics-warehouse/stock_product_qty_by_packaging
- stock-logistics-workflow/stock_picking_consolidation_priority
- stock-logistics-workflow/stock_picking_group_by_partner_by_carrier

### claimed-by-others → blocked-by-deps (1)
- sale-workflow/sale_order_lot_generator

### claimed-by-others → todo (2)
- payroll/payroll
- sale-workflow/sale_order_lot_selection

### merged-in-fork → ready-for-upstream-pr (5)
- partner-contact/partner_title_contacts
- project/project_task_product_stock
- project/project_task_pull_request_state
- purchase-workflow/purchase_triple_discount
- sale-workflow/sale_product_set

### new candidates (12)
- account-reconcile/account_move_line_reconcile_manual
- manufacture/mrp_bom_line_net_qty
- manufacture/mrp_production_unique_lot
- multi-company/product_category_company
- multi-company/purchase_sale_lot_intercompany
- purchase-workflow/purchase_order_line_import_sheet_file
- sale-workflow/sale_partner_sale_contact
- sale-workflow/sale_partner_sale_contact_on_project
- sale-workflow/sale_partner_sale_contact_website_sale
- server-tools/base_sequence_template
- stock-logistics-workflow/stock_readonly
- timesheet/hr_timesheet_sheet_activity

### removed from report (16)
- account-invoicing/account_invoice_triple_discount
- edi/account_invoice_import_facturx
- edi/account_invoice_import_ubl
- partner-contact/partner_category_security
- partner-contact/partner_title
- product-attribute/product_set
- project/project_task_default_stage
- project/project_task_product
- project/project_task_pull_request
- purchase-workflow/purchase_order_internal_note
- server-tools/auto_backup
- server-tools/base_cron_exclusion
- stock-logistics-warehouse/stock_warehouse_calendar
- stock-logistics-workflow/stock_picking_sale_order_link
- stock-logistics-workflow/stock_restrict_lot
- web/web_filter_header_button

### todo → blocked-by-deps (4)
- payroll/payroll_contract_advantages
- payroll/payroll_rule_time_parameter
- project/project_task_stock_product_set
- stock-logistics-warehouse/stock_lot_catalog_sale

### todo → claimed-by-others (18)
- bank-payment/account_banking_mandate_sale
- bank-payment/account_banking_sepa_direct_debit
- bank-payment/account_payment_order_grouped_output
- connector/connector
- geospatial/base_geoengine
- hr/hr_personal_equipment_request
- multi-company/account_multicompany_easy_creation
- multi-company/product_multi_company
- multi-company/product_tax_multicompany_default
- pos/pos_config_logo
- product-attribute/product_attribute_value_menu
- product-attribute/product_packaging_calculator
- stock-logistics-barcode/product_multi_barcode
- stock-logistics-warehouse/stock_location_lockdown
- stock-logistics-warehouse/stock_move_quantity_product_uom
- stock-logistics-warehouse/stock_warehouse_out_pull
- timesheet/hr_employee_cost_history
- timesheet/hr_timesheet_amount_security

## Per repo

| repo | todo | skipped-relevancy | claimed-by-others | blocked-by-deps | pr-to-fork | merged-in-fork | ready-for-upstream-pr |
|---|---:|---:|---:|---:|---:|---:|---:|
| [account-analytic](account-analytic.csv) | 22 | 0 | 2 | 1 | 2 | 4 | 9 |
| [account-financial-reporting](account-financial-reporting.csv) | 5 | 0 | 0 | 1 | 0 | 4 | 1 |
| [account-financial-tools](account-financial-tools.csv) | 19 | 0 | 3 | 5 | 1 | 3 | 19 |
| [account-invoicing](account-invoicing.csv) | 43 | 2 | 2 | 9 | 1 | 8 | 26 |
| [account-reconcile](account-reconcile.csv) | 15 | 0 | 1 | 1 | 2 | 0 | 1 |
| [bank-payment](bank-payment.csv) | 9 | 0 | 7 | 5 | 0 | 0 | 1 |
| [bank-statement-import](bank-statement-import.csv) | 9 | 0 | 7 | 9 | 0 | 0 | 0 |
| [commission](commission.csv) | 5 | 5 | 1 | 2 | 0 | 2 | 1 |
| [connector](connector.csv) | 3 | 0 | 1 | 0 | 0 | 1 | 1 |
| [connector-telephony](connector-telephony.csv) | 3 | 0 | 0 | 1 | 0 | 0 | 0 |
| [contract](contract.csv) | 16 | 0 | 3 | 10 | 0 | 7 | 2 |
| [crm](crm.csv) | 13 | 0 | 1 | 2 | 0 | 5 | 13 |
| [delivery-carrier](delivery-carrier.csv) | 34 | 1 | 1 | 21 | 1 | 3 | 9 |
| [dms](dms.csv) | 4 | 0 | 3 | 2 | 0 | 0 | 1 |
| [e-commerce](e-commerce.csv) | 10 | 3 | 0 | 11 | 0 | 10 | 32 |
| [edi](edi.csv) | 6 | 1 | 0 | 27 | 1 | 2 | 2 |
| [field-service](field-service.csv) | 1 | 1 | 0 | 50 | 0 | 0 | 1 |
| [geospatial](geospatial.csv) | 3 | 0 | 3 | 6 | 0 | 0 | 1 |
| [helpdesk](helpdesk.csv) | 22 | 0 | 1 | 14 | 0 | 0 | 0 |
| [hr](hr.csv) | 14 | 0 | 5 | 9 | 0 | 1 | 9 |
| [knowledge](knowledge.csv) | 11 | 0 | 2 | 2 | 1 | 0 | 1 |
| [management-system](management-system.csv) | 19 | 0 | 15 | 4 | 0 | 0 | 1 |
| [manufacture](manufacture.csv) | 44 | 0 | 5 | 12 | 0 | 0 | 15 |
| [mis-builder](mis-builder.csv) | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| [multi-company](multi-company.csv) | 19 | 0 | 8 | 3 | 0 | 0 | 2 |
| [partner-contact](partner-contact.csv) | 43 | 2 | 3 | 4 | 1 | 14 | 46 |
| [payroll](payroll.csv) | 1 | 0 | 1 | 4 | 0 | 0 | 0 |
| [pos](pos.csv) | 45 | 2 | 2 | 11 | 1 | 1 | 2 |
| [product-attribute](product-attribute.csv) | 63 | 1 | 2 | 16 | 0 | 4 | 34 |
| [project](project.csv) | 29 | 1 | 1 | 5 | 1 | 2 | 36 |
| [purchase-workflow](purchase-workflow.csv) | 60 | 2 | 3 | 18 | 0 | 4 | 42 |
| [queue](queue.csv) | 5 | 0 | 2 | 0 | 0 | 0 | 1 |
| [report-print-send](report-print-send.csv) | 5 | 0 | 3 | 2 | 0 | 0 | 0 |
| [reporting-engine](reporting-engine.csv) | 13 | 0 | 1 | 5 | 1 | 4 | 15 |
| [sale-workflow](sale-workflow.csv) | 82 | 2 | 3 | 33 | 1 | 22 | 67 |
| [server-auth](server-auth.csv) | 12 | 0 | 6 | 6 | 0 | 1 | 8 |
| [server-backend](server-backend.csv) | 10 | 0 | 0 | 2 | 0 | 2 | 4 |
| [server-tools](server-tools.csv) | 28 | 0 | 3 | 6 | 0 | 2 | 25 |
| [server-ux](server-ux.csv) | 12 | 0 | 1 | 6 | 0 | 0 | 16 |
| [social](social.csv) | 42 | 1 | 0 | 17 | 6 | 0 | 3 |
| [stock-logistics-barcode](stock-logistics-barcode.csv) | 3 | 0 | 3 | 2 | 0 | 0 | 0 |
| [stock-logistics-warehouse](stock-logistics-warehouse.csv) | 52 | 3 | 4 | 25 | 1 | 2 | 12 |
| [stock-logistics-workflow](stock-logistics-workflow.csv) | 75 | 2 | 3 | 35 | 0 | 7 | 28 |
| [timesheet](timesheet.csv) | 11 | 0 | 3 | 10 | 0 | 1 | 13 |
| [vertical-hotel](vertical-hotel.csv) | 1 | 0 | 5 | 0 | 0 | 0 | 0 |
| [web](web.csv) | 27 | 1 | 2 | 2 | 3 | 1 | 30 |
| [website](website.csv) | 23 | 1 | 2 | 1 | 1 | 0 | 5 |

## Notes from this run


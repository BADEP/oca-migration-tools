# OCA → 20.0 migration status

Generated 2026-11-20 12:46 UTC · 47 repos · 2218 modules tracked

## Totals

| status | modules |
|---|---:|
| todo | 1012 |
| skipped-relevancy | 31 |
| claimed-by-others | 195 |
| blocked-by-deps | 336 |
| pr-to-fork | 24 |
| merged-in-fork | 106 |
| ready-for-upstream-pr | 514 |

## Changes since last run

### blocked-by-deps → claimed-by-others (18)
- bank-payment/account_payment_purchase_stock
- delivery-carrier/delivery_schenker
- dms/dms_user_role
- field-service/fieldservice_agreement
- field-service/fieldservice_availability
- field-service/fieldservice_equipment_stock
- field-service/fieldservice_equipment_warranty
- field-service/fieldservice_google_map
- field-service/fieldservice_repair
- field-service/fieldservice_sale
- field-service/fieldservice_sale_agreement
- field-service/fieldservice_sale_agreement_equipment_stock
- field-service/fieldservice_sale_recurring
- field-service/fieldservice_sale_stock
- field-service/fieldservice_sign
- field-service/fieldservice_timesheet
- sale-workflow/sale_start_end_dates
- stock-logistics-workflow/stock_move_valuation_usage

### blocked-by-deps → todo (29)
- account-invoicing/sale_stock_picking_invoicing
- bank-statement-import/account_statement_import_online_gocardless
- bank-statement-import/account_statement_import_online_paypal
- bank-statement-import/account_statement_import_online_plaid
- bank-statement-import/account_statement_import_online_ponto
- bank-statement-import/account_statement_import_online_qonto
- bank-statement-import/account_statement_import_online_stripe
- delivery-carrier/delivery_correos_express
- delivery-carrier/delivery_state_manual
- field-service/fieldservice_account_analytic
- field-service/fieldservice_account_payment
- field-service/fieldservice_agreement_repair
- field-service/fieldservice_equipment_stock_return
- field-service/fieldservice_fleet
- field-service/fieldservice_sale_recurring_agreement
- field-service/fieldservice_sale_stock_route
- field-service/fieldservice_subcontracting
- helpdesk/helpdesk_mgmt_fieldservice_equipment_warranty
- helpdesk/helpdesk_mgmt_fieldservice_project
- helpdesk/helpdesk_mgmt_project_domain
- helpdesk/helpdesk_mgmt_sale_project
- knowledge/document_page_access_group_user_role
- multi-company/purchase_sale_note_intercompany
- multi-company/purchase_sale_stock_inter_company
- purchase-workflow/purchase_force_invoiced_quantity
- sale-workflow/sale_probability_amount
- server-backend/base_user_role_activity
- server-backend/base_user_role_profile
- stock-logistics-workflow/stock_picking_return_lot

### merged-in-fork → ready-for-upstream-pr (3)
- account-financial-reporting/partner_statement
- account-financial-tools/account_asset_management
- crm/crm_industry

### new candidates (18)
- contract/contract_invoice_force_date
- contract/contract_invoice_force_date_queue
- e-commerce/website_sale_partner_sale_contact
- e-commerce/website_sale_product_catalog_public_category
- field-service/fieldservice_appointment_confirmation
- hr/hr_user_role_activity
- manufacture/mrp_subcontracting_resupply_status
- partner-contact/partner_address_format_domestic
- product-attribute/product_supplierinfo_multi_code
- purchase-workflow/purchase_order_accrual_accounting_date
- purchase-workflow/purchase_work_acceptance_tier_validation
- sale-workflow/sale_delivery_address_picking_update
- sale-workflow/sale_order_add_consumed_components
- sale-workflow/sale_order_line_smartbutton
- server-ux/base_line_numbering
- stock-logistics-barcode/stock_barcodes_picking_batch
- stock-logistics-workflow/stock_move_position
- stock-logistics-workflow/stock_picking_batch_move_position

### removed from report (24)
- account-analytic/account_analytic_line_commercial_partner
- account-financial-reporting/account_tax_balance
- account-invoicing/portal_account_personal_data_only
- delivery-carrier/delivery_package_number
- delivery-carrier/delivery_state
- dms/dms_field
- dms/hr_dms_field
- manufacture/mrp_production_unique_lot
- manufacture/mrp_subcontracting_purchase_link
- multi-company/base_multi_company
- partner-contact/partner_employee_quantity
- partner-contact/partner_industry_secondary
- project/project_task_pull_request_state
- purchase-workflow/purchase_order_line_menu
- purchase-workflow/purchase_order_line_price_unit_digits
- reporting-engine/report_xlsx_helper
- sale-workflow/portal_sale_personal_data_only
- sale-workflow/sale_order_archive
- sale-workflow/sale_order_line_menu
- server-tools/upgrade_analysis
- server-ux/developer_menu
- server-ux/server_action_mass_edit
- stock-logistics-workflow/stock_account_product_run_fifo_hook
- timesheet/hr_timesheet_amount_security

### todo → claimed-by-others (44)
- account-analytic/analytic_hr_department_restriction
- account-invoicing/account_invoice_subscription_per_contact
- bank-payment/account_payment_purchase
- bank-statement-import/account_statement_import_camt54
- bank-statement-import/account_statement_import_online
- dms/dms_auto_classification
- field-service/fieldservice_account
- field-service/fieldservice_activity
- field-service/fieldservice_calendar
- field-service/fieldservice_crm
- field-service/fieldservice_expense
- field-service/fieldservice_kanban_info
- field-service/fieldservice_portal
- field-service/fieldservice_project
- field-service/fieldservice_purchase
- field-service/fieldservice_recurring
- field-service/fieldservice_route
- field-service/fieldservice_size
- field-service/fieldservice_skill
- field-service/fieldservice_stage_server_action
- field-service/fieldservice_stage_validation
- field-service/fieldservice_stock
- field-service/fieldservice_timeline
- field-service/fieldservice_vehicle
- helpdesk/helpdesk_mgmt_activity
- helpdesk/helpdesk_mgmt_crm
- helpdesk/helpdesk_mgmt_merge
- helpdesk/helpdesk_mgmt_project
- helpdesk/helpdesk_mgmt_rating
- helpdesk/helpdesk_mgmt_sale
- hr/hr_employee_bank_restrict
- knowledge/document_page_access_group
- knowledge/document_page_partner
- knowledge/document_page_product
- multi-company/crm_lost_reason_multi_company
- multi-company/crm_stage_multi_company
- multi-company/purchase_sale_inter_company
- partner-contact/partner_affiliate
- queue/queue_job_subscribe
- sale-workflow/sale_invoice_policy
- sale-workflow/sale_mrp_bom
- web/web_save_discard_button
- web/web_toggle_chatter
- web/web_widget_image_download

## Per repo

| repo | todo | skipped-relevancy | claimed-by-others | blocked-by-deps | pr-to-fork | merged-in-fork | ready-for-upstream-pr |
|---|---:|---:|---:|---:|---:|---:|---:|
| [account-analytic](account-analytic.csv) | 20 | 0 | 4 | 1 | 2 | 4 | 8 |
| [account-financial-reporting](account-financial-reporting.csv) | 5 | 0 | 0 | 1 | 0 | 2 | 2 |
| [account-financial-tools](account-financial-tools.csv) | 20 | 0 | 3 | 4 | 1 | 2 | 19 |
| [account-invoicing](account-invoicing.csv) | 43 | 2 | 3 | 8 | 1 | 7 | 26 |
| [account-reconcile](account-reconcile.csv) | 15 | 0 | 1 | 1 | 2 | 0 | 1 |
| [bank-payment](bank-payment.csv) | 8 | 0 | 9 | 4 | 0 | 0 | 1 |
| [bank-statement-import](bank-statement-import.csv) | 13 | 0 | 9 | 3 | 0 | 0 | 0 |
| [commission](commission.csv) | 5 | 5 | 1 | 2 | 0 | 2 | 1 |
| [connector](connector.csv) | 3 | 0 | 1 | 0 | 0 | 1 | 1 |
| [connector-telephony](connector-telephony.csv) | 3 | 0 | 0 | 1 | 0 | 0 | 0 |
| [contract](contract.csv) | 17 | 0 | 3 | 11 | 0 | 7 | 2 |
| [crm](crm.csv) | 13 | 0 | 1 | 2 | 0 | 4 | 12 |
| [delivery-carrier](delivery-carrier.csv) | 35 | 1 | 2 | 18 | 0 | 3 | 9 |
| [dms](dms.csv) | 3 | 0 | 2 | 1 | 0 | 0 | 0 |
| [e-commerce](e-commerce.csv) | 10 | 3 | 1 | 12 | 0 | 10 | 31 |
| [edi](edi.csv) | 7 | 1 | 0 | 26 | 1 | 2 | 2 |
| [field-service](field-service.csv) | 15 | 1 | 32 | 5 | 0 | 0 | 1 |
| [geospatial](geospatial.csv) | 3 | 0 | 3 | 6 | 0 | 0 | 1 |
| [helpdesk](helpdesk.csv) | 23 | 0 | 7 | 9 | 0 | 0 | 0 |
| [hr](hr.csv) | 13 | 0 | 6 | 10 | 0 | 1 | 9 |
| [knowledge](knowledge.csv) | 7 | 0 | 7 | 0 | 1 | 0 | 0 |
| [management-system](management-system.csv) | 20 | 0 | 15 | 3 | 0 | 0 | 1 |
| [manufacture](manufacture.csv) | 45 | 0 | 3 | 12 | 0 | 0 | 14 |
| [mis-builder](mis-builder.csv) | 0 | 0 | 0 | 0 | 0 | 2 | 1 |
| [multi-company](multi-company.csv) | 18 | 0 | 10 | 1 | 0 | 0 | 2 |
| [partner-contact](partner-contact.csv) | 43 | 2 | 4 | 4 | 1 | 10 | 47 |
| [payroll](payroll.csv) | 1 | 0 | 1 | 5 | 0 | 0 | 0 |
| [pos](pos.csv) | 45 | 2 | 2 | 11 | 1 | 1 | 2 |
| [product-attribute](product-attribute.csv) | 63 | 1 | 6 | 14 | 0 | 4 | 34 |
| [project](project.csv) | 29 | 1 | 2 | 4 | 1 | 1 | 34 |
| [purchase-workflow](purchase-workflow.csv) | 59 | 2 | 5 | 18 | 0 | 4 | 40 |
| [queue](queue.csv) | 4 | 0 | 3 | 0 | 0 | 0 | 1 |
| [report-print-send](report-print-send.csv) | 5 | 0 | 3 | 2 | 0 | 0 | 0 |
| [reporting-engine](reporting-engine.csv) | 13 | 0 | 2 | 4 | 1 | 2 | 14 |
| [sale-workflow](sale-workflow.csv) | 86 | 2 | 8 | 27 | 1 | 21 | 63 |
| [server-auth](server-auth.csv) | 11 | 0 | 7 | 6 | 0 | 1 | 8 |
| [server-backend](server-backend.csv) | 12 | 0 | 0 | 0 | 0 | 2 | 4 |
| [server-tools](server-tools.csv) | 26 | 0 | 5 | 6 | 0 | 2 | 24 |
| [server-ux](server-ux.csv) | 13 | 0 | 1 | 6 | 0 | 0 | 13 |
| [social](social.csv) | 42 | 1 | 0 | 17 | 6 | 0 | 3 |
| [stock-logistics-barcode](stock-logistics-barcode.csv) | 4 | 0 | 3 | 3 | 0 | 0 | 0 |
| [stock-logistics-warehouse](stock-logistics-warehouse.csv) | 51 | 3 | 3 | 26 | 1 | 2 | 12 |
| [stock-logistics-workflow](stock-logistics-workflow.csv) | 75 | 2 | 4 | 36 | 0 | 7 | 26 |
| [timesheet](timesheet.csv) | 18 | 0 | 2 | 3 | 0 | 1 | 13 |
| [vertical-hotel](vertical-hotel.csv) | 1 | 0 | 5 | 0 | 0 | 0 | 0 |
| [web](web.csv) | 24 | 1 | 4 | 2 | 3 | 1 | 27 |
| [website](website.csv) | 23 | 1 | 2 | 1 | 1 | 0 | 5 |

## Notes from this run


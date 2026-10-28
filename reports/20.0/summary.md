# OCA → 20.0 migration status

Generated 2026-10-28 19:52 UTC · 47 repos · 2249 modules tracked

## Totals

| status | modules |
|---|---:|
| todo | 987 |
| skipped-relevancy | 33 |
| claimed-by-others | 87 |
| blocked-by-deps | 446 |
| in-progress | 25 |
| merged-in-fork | 126 |
| ready-for-upstream-pr | 545 |

## Changes since last run

### blocked-by-deps → claimed-by-others (6)
- account-financial-tools/account_move_line_purchase_info
- account-financial-tools/account_move_line_sale_info
- contract/contract_termination
- dms/dms_field
- manufacture/mrp_production_quant_manual_assign
- report-print-send/printer_zpl2

### blocked-by-deps → todo (53)
- account-analytic/purchase_request_analytic
- account-analytic/sale_analytic
- account-financial-tools/account_dashboard_banner_mis_builder
- account-financial-tools/account_fiscal_month
- account-financial-tools/account_move_budget
- account-financial-tools/purchase_unreconciled
- account-invoicing/account_invoice_auto_send_by_email
- account-invoicing/product_customerinfo_invoice
- account-reconcile/account_reconcile_oca_add_default_filters
- account-reconcile/account_reconcile_oca_queue
- bank-payment/account_banking_mandate_contact
- bank-payment/account_banking_mandate_sale
- bank-payment/account_banking_sepa_direct_debit
- contract/contract_mandate
- contract/contract_price_revision
- contract/contract_sale_payment_mode
- contract/product_contract
- delivery-carrier/delivery_carrier_report_to_printer
- dms/dms_attachment_link
- dms/dms_auto_classification
- dms/dms_field_auto_classification
- dms/dms_file_sequence
- dms/hr_dms_field
- edi/account_invoice_export_job
- manufacture/mrp_mass_production_order
- partner-contact/partner_noncommercial
- project/project_task_code_portal
- project/project_task_stock_product_set
- project/website_project_task_code
- purchase-workflow/product_supplierinfo_qty_multiplier
- purchase-workflow/purchase_order_approval_block
- purchase-workflow/purchase_transport_mode
- queue/test_queue_job_batch
- reporting-engine/report_async
- sale-workflow/pricelist_cache
- sale-workflow/sale_automatic_workflow_auto_assign
- sale-workflow/sale_automatic_workflow_force_invoiced
- sale-workflow/sale_automatic_workflow_payment_mode
- sale-workflow/sale_automatic_workflow_periodicity
- sale-workflow/sale_automatic_workflow_stock
- sale-workflow/sale_block_no_stock
- sale-workflow/sale_cancel_confirm
- sale-workflow/sale_invoice_policy
- sale-workflow/sale_order_invoicing_picking_filter
- sale-workflow/sale_order_product_availability_inline
- sale-workflow/sale_order_product_recommendation_packaging_default
- sale-workflow/sale_stock_line_sequence
- stock-logistics-barcode/stock_barcodes
- stock-logistics-warehouse/stock_demand_estimate_matrix
- stock-logistics-warehouse/stock_exception
- stock-logistics-warehouse/stock_inventory_preparation_filter
- stock-logistics-warehouse/stock_vertical_lift
- web/web_notify_channel_message

### merged-in-fork → ready-for-upstream-pr (3)
- account-analytic/purchase_analytic
- account-invoicing/account_invoice_transmit_method
- web/web_m2x_options_manager

### new candidates (4)
- account-invoicing/account_invoice_ar_ap_by_journal
- account-invoicing/account_invoice_supplier_self_invoice
- delivery-carrier/delivery_fee_deposit
- product-attribute/product_supplierinfo_incoterm

### pr-to-fork → in-progress (25)
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

### removed from report (5)
- product-attribute/product_attribute_value_avoid_auto_fill
- product-attribute/product_code_mandatory
- product-attribute/product_manufacturer
- web/web_dialog_size
- web/web_responsive

### todo → blocked-by-deps (1)
- web/web_responsive_company_color

### todo → claimed-by-others (5)
- bank-payment/account_banking_mandate
- bank-payment/account_payment_sale
- contract/contract_line_successor
- purchase-workflow/purchase_order_internal_note
- report-print-send/base_report_to_printer_cups

## Per repo

| repo | todo | skipped-relevancy | claimed-by-others | blocked-by-deps | in-progress | merged-in-fork | ready-for-upstream-pr |
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


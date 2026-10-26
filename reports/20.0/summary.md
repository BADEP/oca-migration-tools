# OCA → 20.0 migration status

Generated 2026-10-26 22:22 UTC · 47 repos · 2250 modules tracked

## Totals

| status | modules |
|---|---:|
| todo | 989 |
| skipped-relevancy | 32 |
| claimed-by-others | 76 |
| blocked-by-deps | 477 |
| merged-in-fork | 126 |
| ready-for-upstream-pr | 550 |

## Changes since last run

### blocked-by-deps → claimed-by-others (20)
- management-system/document_page_procedure
- management-system/document_page_quality_manual
- management-system/document_page_work_instruction
- management-system/mgmtsystem_action
- management-system/mgmtsystem_audit
- management-system/mgmtsystem_hazard
- management-system/mgmtsystem_manual
- management-system/mgmtsystem_nonconformity
- management-system/mgmtsystem_nonconformity_hr
- management-system/mgmtsystem_quality
- management-system/mgmtsystem_review
- management-system/mgmtsystem_risk
- management-system/mgmtsystem_survey
- purchase-workflow/purchase_invoice_plan
- sale-workflow/sale_order_lot_selection
- sale-workflow/sale_triple_discount
- sale-workflow/sales_team_security_crm
- stock-logistics-barcode/barcodes_generator_product
- vertical-hotel/hotel_housekeeping
- vertical-hotel/hotel_reservation

### blocked-by-deps → todo (78)
- account-financial-tools/account_asset_compute_batch
- account-financial-tools/account_asset_low_value
- account-financial-tools/account_asset_management_stock_lot
- account-financial-tools/account_asset_number
- account-financial-tools/account_asset_transfer
- account-financial-tools/account_bank_statement_chatter
- account-financial-tools/account_dashboard_banner_mis_builder
- account-financial-tools/account_fiscal_year_auto_create
- account-financial-tools/account_move_fiscal_year
- account-invoicing/account_invoice_refund_link_sale
- contract/contract_sale_generation
- delivery-carrier/delivery_carrier_report_to_printer
- helpdesk/helpdesk_mgmtsystem_nonconformity
- management-system/document_page_environment_manual
- management-system/document_page_environmental_aspect
- management-system/document_page_health_safety_manual
- management-system/mgmtsystem_action_efficacy
- management-system/mgmtsystem_action_template
- management-system/mgmtsystem_environment
- management-system/mgmtsystem_hazard_risk
- management-system/mgmtsystem_info_security_manual
- management-system/mgmtsystem_information_security
- management-system/mgmtsystem_nonconformity_hazard
- management-system/mgmtsystem_nonconformity_maintenance_equipment
- management-system/mgmtsystem_nonconformity_mrp
- management-system/mgmtsystem_nonconformity_product
- management-system/mgmtsystem_nonconformity_repair
- management-system/mgmtsystem_objective
- management-system/mgmtsystem_review_survey
- management-system/mgmtsystem_security_event
- partner-contact/partner_stage_only_confirmed
- partner-contact/partner_tier_validation
- product-attribute/product_logistics_uom_total_weight
- product-attribute/product_packaging_dimension
- purchase-workflow/purchase_order_line_sequence
- purchase-workflow/purchase_work_acceptance_invoice_plan
- report-print-send/base_report_to_label_printer
- report-print-send/base_report_to_printer_cups
- report-print-send/base_report_to_printer_mail
- report-print-send/base_report_to_printer_qztray
- report-print-send/base_report_to_printer_websocket
- report-print-send/printing_auto_base
- sale-workflow/pricelist_cache
- sale-workflow/sale_block_no_stock
- sale-workflow/sale_cancel_confirm
- sale-workflow/sale_invoice_delivery_state
- sale-workflow/sale_invoice_policy
- sale-workflow/sale_order_general_discount_triple
- sale-workflow/sale_order_invoicing_picking_filter
- sale-workflow/sale_order_lot_generator
- sale-workflow/sale_partner_utm_source
- sale-workflow/sale_product_identification
- sale-workflow/sale_product_set_packaging_qty
- sale-workflow/sale_resource_booking
- sale-workflow/sale_stock_line_sequence
- server-tools/attachment_queue
- server-ux/document_quick_access
- stock-logistics-barcode/barcodes_generator_location
- stock-logistics-warehouse/stock_cycle_count
- stock-logistics-warehouse/stock_inventory_location_state
- stock-logistics-warehouse/stock_inventory_lockdown
- stock-logistics-warehouse/stock_inventory_preparation_filter
- stock-logistics-warehouse/stock_inventory_restriction
- stock-logistics-warehouse/stock_inventory_verification_request
- stock-logistics-warehouse/stock_location_bin_name
- stock-logistics-warehouse/stock_lot_catalog_sale
- stock-logistics-warehouse/stock_quant_reservation_info_mrp
- stock-logistics-workflow/purchase_stock_picking_backorder_policy
- stock-logistics-workflow/sale_line_returned_qty_mrp
- stock-logistics-workflow/sale_stock_picking_backorder_policy
- stock-logistics-workflow/sale_stock_picking_reservation_policy
- stock-logistics-workflow/sale_stock_restocking_fee_invoicing
- stock-logistics-workflow/stock_picking_origin_reference_purchase
- stock-logistics-workflow/stock_picking_origin_reference_sale
- stock-logistics-workflow/stock_split_picking_dimension
- stock-logistics-workflow/stock_split_picking_kit
- vertical-hotel/report_hotel_reservation
- web/web_responsive_company_color

### new candidates (5)
- e-commerce/website_sale_category_smart_button
- manufacture/quality_control_product_manufacturer
- pos/pos_sale_order_print
- social/social_media_x
- website/website_recaptcha_v2

### removed from report (1)
- project/project_department

### todo → claimed-by-others (17)
- account-invoicing/account_invoice_discount_amount
- contract/contract_sale
- management-system/mgmtsystem
- management-system/mgmtsystem_kpi
- manufacture/account_move_line_mrp_info
- partner-contact/partner_category_security
- report-print-send/base_report_to_printer
- server-tools/auto_backup
- server-tools/autovacuum_message_attachment
- server-tools/field_vector
- server-tools/sentry_client
- server-ux/announcement
- stock-logistics-barcode/barcodes_generator_abstract
- stock-logistics-warehouse/stock_quant_reservation_info
- stock-logistics-workflow/stock_interwarehouse_transfer
- stock-logistics-workflow/stock_picking_origin_state
- web/web_disable_export_group

## Per repo

| repo | todo | skipped-relevancy | claimed-by-others | blocked-by-deps | merged-in-fork | ready-for-upstream-pr |
|---|---:|---:|---:|---:|---:|---:|
| [account-analytic](account-analytic.csv) | 25 | 0 | 0 | 2 | 4 | 9 |
| [account-financial-reporting](account-financial-reporting.csv) | 5 | 0 | 0 | 1 | 4 | 1 |
| [account-financial-tools](account-financial-tools.csv) | 19 | 0 | 0 | 9 | 3 | 19 |
| [account-invoicing](account-invoicing.csv) | 42 | 2 | 1 | 10 | 8 | 27 |
| [account-reconcile](account-reconcile.csv) | 16 | 0 | 1 | 1 | 0 | 1 |
| [bank-payment](bank-payment.csv) | 10 | 0 | 2 | 9 | 0 | 1 |
| [bank-statement-import](bank-statement-import.csv) | 9 | 0 | 7 | 9 | 0 | 0 |
| [commission](commission.csv) | 0 | 5 | 0 | 8 | 2 | 1 |
| [connector](connector.csv) | 2 | 0 | 0 | 2 | 1 | 1 |
| [connector-telephony](connector-telephony.csv) | 3 | 0 | 0 | 1 | 0 | 0 |
| [contract](contract.csv) | 10 | 0 | 1 | 15 | 7 | 2 |
| [crm](crm.csv) | 12 | 0 | 1 | 3 | 5 | 13 |
| [delivery-carrier](delivery-carrier.csv) | 34 | 1 | 1 | 21 | 3 | 9 |
| [dms](dms.csv) | 0 | 0 | 0 | 9 | 0 | 1 |
| [e-commerce](e-commerce.csv) | 11 | 2 | 0 | 11 | 10 | 32 |
| [edi](edi.csv) | 7 | 3 | 0 | 27 | 2 | 2 |
| [field-service](field-service.csv) | 1 | 1 | 0 | 50 | 0 | 1 |
| [geospatial](geospatial.csv) | 3 | 0 | 0 | 9 | 0 | 1 |
| [helpdesk](helpdesk.csv) | 22 | 0 | 1 | 14 | 0 | 0 |
| [hr](hr.csv) | 13 | 0 | 1 | 14 | 1 | 9 |
| [knowledge](knowledge.csv) | 12 | 0 | 2 | 2 | 0 | 1 |
| [management-system](management-system.csv) | 19 | 0 | 15 | 4 | 0 | 1 |
| [manufacture](manufacture.csv) | 42 | 0 | 1 | 16 | 0 | 15 |
| [mis-builder](mis-builder.csv) | 0 | 0 | 0 | 0 | 3 | 0 |
| [multi-company](multi-company.csv) | 20 | 0 | 5 | 3 | 0 | 2 |
| [partner-contact](partner-contact.csv) | 44 | 2 | 4 | 4 | 15 | 47 |
| [payroll](payroll.csv) | 2 | 0 | 2 | 2 | 0 | 0 |
| [pos](pos.csv) | 46 | 2 | 1 | 12 | 1 | 2 |
| [product-attribute](product-attribute.csv) | 63 | 1 | 0 | 17 | 4 | 38 |
| [project](project.csv) | 29 | 1 | 1 | 6 | 4 | 37 |
| [purchase-workflow](purchase-workflow.csv) | 57 | 2 | 2 | 22 | 5 | 42 |
| [queue](queue.csv) | 4 | 0 | 2 | 1 | 1 | 1 |
| [report-print-send](report-print-send.csv) | 6 | 0 | 1 | 3 | 0 | 0 |
| [reporting-engine](reporting-engine.csv) | 14 | 0 | 1 | 5 | 4 | 15 |
| [sale-workflow](sale-workflow.csv) | 76 | 2 | 3 | 37 | 23 | 66 |
| [server-auth](server-auth.csv) | 13 | 0 | 4 | 7 | 1 | 8 |
| [server-backend](server-backend.csv) | 10 | 0 | 0 | 2 | 2 | 4 |
| [server-tools](server-tools.csv) | 26 | 0 | 4 | 7 | 2 | 26 |
| [server-ux](server-ux.csv) | 11 | 0 | 1 | 7 | 0 | 16 |
| [social](social.csv) | 48 | 1 | 0 | 16 | 0 | 3 |
| [stock-logistics-barcode](stock-logistics-barcode.csv) | 4 | 0 | 2 | 2 | 0 | 0 |
| [stock-logistics-warehouse](stock-logistics-warehouse.csv) | 55 | 3 | 1 | 26 | 2 | 13 |
| [stock-logistics-workflow](stock-logistics-workflow.csv) | 73 | 2 | 2 | 37 | 7 | 30 |
| [timesheet](timesheet.csv) | 13 | 0 | 1 | 9 | 1 | 13 |
| [vertical-hotel](vertical-hotel.csv) | 2 | 0 | 2 | 2 | 0 | 0 |
| [web](web.csv) | 32 | 1 | 1 | 2 | 1 | 35 |
| [website](website.csv) | 24 | 1 | 2 | 1 | 0 | 5 |

## Notes from this run


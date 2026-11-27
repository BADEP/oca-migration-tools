# OCA → 20.0 migration status

Generated 2026-11-27 12:59 UTC · 47 repos · 2204 modules tracked

## Totals

| status | modules |
|---|---:|
| todo | 1018 |
| skipped-relevancy | 31 |
| claimed-by-others | 199 |
| blocked-by-deps | 322 |
| pr-to-fork | 24 |
| merged-in-fork | 106 |
| ready-for-upstream-pr | 504 |

## Changes since last run

### blocked-by-deps → todo (15)
- account-invoicing/partner_invoicing_mode_monthly
- crm/crm_claim_type
- delivery-carrier/delivery_cttexpress
- delivery-carrier/delivery_ups_oca
- edi/base_import_pdf_by_template_account
- edi/base_ubl_parse
- edi/test_base_import_pdf_by_template
- management-system/mgmtsystem_claim
- multi-company/purchase_sale_lot_intercompany
- pos/pos_user_restrict_stripe_bypass_user
- project/project_group_hr_timesheet
- project/sale_project_task_description_template
- purchase-workflow/procurement_purchase_sale_no_grouping
- purchase-workflow/purchase_work_acceptance_evaluation
- purchase-workflow/purchase_work_acceptance_late_fines

### new candidates (7)
- contract/subscription_oca_rating
- e-commerce/website_sale_product_publish_date
- helpdesk/helpdesk_mgmt_partner_dashboard
- product-attribute/product_cost_security_purchase
- sale-workflow/sale_order_merge
- sale-workflow/sale_stock_qty_by_warehouse
- server-backend/base_external_dbsource_sap_hana

### removed from report (20)
- account-analytic/analytic_hr_department_restriction
- account-invoicing/account_invoice_refund_link
- account-invoicing/account_invoice_tax_required
- dms/dms_auto_classification
- dms/dms_field_auto_classification
- knowledge/document_page_partner
- manufacture/mrp_subcontracting_resupply_status
- multi-company/account_multicompany_easy_creation
- multi-company/crm_tag_multi_company
- multi-company/partner_category_multi_company
- multi-company/product_multi_company
- pos/pos_config_logo
- project/project_administrator_restricted_visibility
- reporting-engine/report_qweb_parameter
- server-tools/scheduler_error_mailer
- timesheet/hr_timesheet_autofill_project_off
- timesheet/hr_timesheet_task_domain
- timesheet/sale_timesheet_invoice_link
- web/web_dark_mode
- web/web_remember_tree_column_width

### todo → claimed-by-others (12)
- account-financial-tools/account_lock_to_date
- account-invoicing/account_invoice_date_due
- account-invoicing/account_invoice_refund_reason
- delivery-carrier/delivery_price_method
- edi/base_import_pdf_by_template
- knowledge/document_page_reference
- multi-company/purchase_sale_stock_inter_company
- partner-contact/partner_second_lastname
- pos/pos_order_remove_line
- pos/pos_user_restriction
- purchase-workflow/purchase_requisition_line_description
- purchase-workflow/purchase_work_acceptance

## Per repo

| repo | todo | skipped-relevancy | claimed-by-others | blocked-by-deps | pr-to-fork | merged-in-fork | ready-for-upstream-pr |
|---|---:|---:|---:|---:|---:|---:|---:|
| [account-analytic](account-analytic.csv) | 20 | 0 | 3 | 1 | 2 | 4 | 8 |
| [account-financial-reporting](account-financial-reporting.csv) | 5 | 0 | 0 | 1 | 0 | 2 | 2 |
| [account-financial-tools](account-financial-tools.csv) | 19 | 0 | 4 | 4 | 1 | 2 | 19 |
| [account-invoicing](account-invoicing.csv) | 42 | 2 | 4 | 7 | 1 | 7 | 25 |
| [account-reconcile](account-reconcile.csv) | 15 | 0 | 1 | 1 | 2 | 0 | 1 |
| [bank-payment](bank-payment.csv) | 8 | 0 | 9 | 4 | 0 | 0 | 1 |
| [bank-statement-import](bank-statement-import.csv) | 13 | 0 | 9 | 3 | 0 | 0 | 0 |
| [commission](commission.csv) | 5 | 5 | 1 | 2 | 0 | 2 | 1 |
| [connector](connector.csv) | 3 | 0 | 1 | 0 | 0 | 1 | 1 |
| [connector-telephony](connector-telephony.csv) | 3 | 0 | 0 | 1 | 0 | 0 | 0 |
| [contract](contract.csv) | 17 | 0 | 3 | 12 | 0 | 7 | 2 |
| [crm](crm.csv) | 14 | 0 | 1 | 1 | 0 | 4 | 12 |
| [delivery-carrier](delivery-carrier.csv) | 36 | 1 | 3 | 16 | 0 | 3 | 9 |
| [dms](dms.csv) | 2 | 0 | 1 | 1 | 0 | 0 | 0 |
| [e-commerce](e-commerce.csv) | 11 | 3 | 1 | 12 | 0 | 10 | 31 |
| [edi](edi.csv) | 9 | 1 | 1 | 23 | 1 | 2 | 2 |
| [field-service](field-service.csv) | 15 | 1 | 32 | 5 | 0 | 0 | 1 |
| [geospatial](geospatial.csv) | 3 | 0 | 3 | 6 | 0 | 0 | 1 |
| [helpdesk](helpdesk.csv) | 24 | 0 | 7 | 9 | 0 | 0 | 0 |
| [hr](hr.csv) | 13 | 0 | 6 | 10 | 0 | 1 | 9 |
| [knowledge](knowledge.csv) | 6 | 0 | 7 | 0 | 1 | 0 | 0 |
| [management-system](management-system.csv) | 21 | 0 | 15 | 2 | 0 | 0 | 1 |
| [manufacture](manufacture.csv) | 45 | 0 | 2 | 12 | 0 | 0 | 14 |
| [mis-builder](mis-builder.csv) | 0 | 0 | 0 | 0 | 0 | 2 | 1 |
| [multi-company](multi-company.csv) | 16 | 0 | 9 | 0 | 0 | 0 | 2 |
| [partner-contact](partner-contact.csv) | 42 | 2 | 5 | 4 | 1 | 10 | 47 |
| [payroll](payroll.csv) | 1 | 0 | 1 | 5 | 0 | 0 | 0 |
| [pos](pos.csv) | 44 | 2 | 3 | 10 | 1 | 1 | 2 |
| [product-attribute](product-attribute.csv) | 64 | 1 | 6 | 14 | 0 | 4 | 33 |
| [project](project.csv) | 31 | 1 | 2 | 2 | 1 | 1 | 33 |
| [purchase-workflow](purchase-workflow.csv) | 60 | 2 | 7 | 15 | 0 | 4 | 40 |
| [queue](queue.csv) | 4 | 0 | 3 | 0 | 0 | 0 | 1 |
| [report-print-send](report-print-send.csv) | 5 | 0 | 3 | 2 | 0 | 0 | 0 |
| [reporting-engine](reporting-engine.csv) | 13 | 0 | 2 | 4 | 1 | 2 | 13 |
| [sale-workflow](sale-workflow.csv) | 88 | 2 | 8 | 27 | 1 | 21 | 63 |
| [server-auth](server-auth.csv) | 11 | 0 | 7 | 6 | 0 | 1 | 8 |
| [server-backend](server-backend.csv) | 13 | 0 | 0 | 0 | 0 | 2 | 4 |
| [server-tools](server-tools.csv) | 26 | 0 | 5 | 6 | 0 | 2 | 23 |
| [server-ux](server-ux.csv) | 13 | 0 | 1 | 6 | 0 | 0 | 13 |
| [social](social.csv) | 42 | 1 | 0 | 17 | 6 | 0 | 3 |
| [stock-logistics-barcode](stock-logistics-barcode.csv) | 4 | 0 | 3 | 3 | 0 | 0 | 0 |
| [stock-logistics-warehouse](stock-logistics-warehouse.csv) | 51 | 3 | 3 | 26 | 1 | 2 | 12 |
| [stock-logistics-workflow](stock-logistics-workflow.csv) | 75 | 2 | 4 | 36 | 0 | 7 | 26 |
| [timesheet](timesheet.csv) | 18 | 0 | 2 | 3 | 0 | 1 | 10 |
| [vertical-hotel](vertical-hotel.csv) | 1 | 0 | 5 | 0 | 0 | 0 | 0 |
| [web](web.csv) | 24 | 1 | 4 | 2 | 3 | 1 | 25 |
| [website](website.csv) | 23 | 1 | 2 | 1 | 1 | 0 | 5 |

## Notes from this run


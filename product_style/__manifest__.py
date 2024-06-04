{
    "name": "Product Style",
    "summary": "Add product style",
    "version": "1.0",
    "application": True,
    "installable": True,
    "depends":['mail','sale','base','product'],
    "data":["views/product_style_view.xml",
            "security/ir.model.access.csv",
            "views/salesperson_report_views.xml",
            "reports/invoice_report_templates.xml",
            ]
    ,
    "license":"LGPL-3"
}
{
    "name": "Remove Odoo Branding",
    "version": "17.0.1.0.0",
    "category": "Customization",
    "summary": "Removes Odoo branding from website, backend, and email templates",
    "author": "Andres Letto",
    "depends": ["web", "mail", "website"],
    "data": [
        "views/email_templates.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "remove_odoo_branding/static/src/xml/remove_odoo_footer.xml",
        ],
        "web.assets_backend": [
            "remove_odoo_branding/static/src/xml/remove_odoo_backend.xml",
        ],
    },
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}

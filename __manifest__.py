{
    "name": "Remove Odoo Branding",
    "version": "17.0.1.0.0",
    "category": "Customization",
    "summary": "Remueve branding de Odoo del sitio web y plantillas de email",
    "author": "Tu Nombre o Empresa",
    "depends": ["web", "mail", "website"],
    "data": [
        "views/email_templates.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "remove_odoo_branding/static/src/xml/remove_odoo_footer.xml",
        ],
    },
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}

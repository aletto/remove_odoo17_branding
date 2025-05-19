# remove_odoo_branding
This module removes Odoo 17 CE branding from website, email templates and backend.

# Installation:

This module removes Odoo branding from:

- Website footer
- Email template headers and footers
- Backend footer
- Help menu links in the user dropdown

## Features

- Removes "Powered by Odoo" from website footer
- Cleans Odoo links from email templates
- Hides Odoo footer and help links in the backend

## Installation

1. Copy the folder `remove_odoo_branding/` into your custom addons directory.
2. Restart the Odoo server:
   ```bash
   ./odoo-bin -d your_database -u remove_odoo_branding
3.  Activate Developer Mode in your Odoo instance.
4.  Go to Apps > Update Apps List, and click Update.
5.  Search for Remove Odoo Branding and install the module.
5.  Refresh your website and backend to see the changes.

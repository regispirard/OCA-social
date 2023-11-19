# Copyright 2023 TINCID (Régis Pirard)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Mail Activity Team Auto Assignment",
    "summary": "Add rules on Activity Teams to automatically assign activities",
    "version": "16.0.1.0.0",
    "development_status": "Alpha",
    "category": "Social Network",
    "website": "https://github.com/OCA/social",
    "author": "TINCID, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "installable": True,
    "depends": ["mail_activity_team"],
    "data": [
        "security/ir.model.access.csv",
        "views/mail_activity_team_views.xml",
    ],
    "assets": {},
}

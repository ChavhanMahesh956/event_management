{
    "name": "Event Management",
    "version": "0.1",
    "website": "https://www.mahesh.com",
    "author": "Mahesh",
    "description": """
        Event Management Company
    """,
    "category": "Bussines",
    "depends": ["product", "sale", "purchase", "base", "contacts", "mail"],
    "data": [
        "security/ir.model.access.csv",
        "security/security.xml",
        "wizards/event_report_wizard.xml",
        "views/event_view.xml",
        "views/organizer_view.xml",
        "views/attendee_view.xml",
        "views/registration_view.xml",
        "views/menuitem.xml",
    ],
    "demo": [],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}

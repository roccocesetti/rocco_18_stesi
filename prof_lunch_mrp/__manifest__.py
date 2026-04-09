# -*- coding: utf-8 -*-
{
    "name": "prof_lunch_mrp",
    "version": "18.0.1.0.0",
    "category": "mrp",
    "summary": "lunch reorder production",
    "license": "LGPL-3",
    "author": "Rocco Cesetti (custom)",
    "depends": [ "stock",'mrp'],
    "data": [
        "security/ir.model.access.csv",
        "views/mo_overview_wizard_views.xml",
    ],

    "installable": True,
    "application": False,
}

# -*- coding: utf-8 -*-
{
    'name': "empresas",

    'summary': """
        Módulo de empresas""",

    'author': "Alejandro",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        'views/views.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'aplication': 'True',

    'assets': {
        'web.assets_common': [
            'empresas_contratadoras/static/src/scss/style1.scss',
            'empresas_contratadoras/static/src/scss/style2.scss',
        ]
    }
}

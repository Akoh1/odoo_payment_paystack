# -*- coding: utf-8 -*-
{
    'name': "Paystack Payment Acquirer",
    'category': 'Accounting/Payment Acquirers',
    'sequence': -100,
    'summary': 'Payment Acquirer: Custom Paystack Implementation',
    'author': 'Samuel Akoh <ojima.asm@gmail.com>',
    'description': """Custom Paystack Payment Acquirer""",
    'depends': ['payment'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/payment_views.xml',
        'views/payment_templates.xml',
        'data/payment_acquirer_data.xml',
    ],
    'images': ['static/description/icon.png'],
    'application': True,
    'uninstall_hook': 'uninstall_hook',
    'installable': True,
    # 'assets': {
    #     'web.assets_frontend': [
    #         'payment_stripe/static/src/js/payment_form.js',
    #     ],
    # },
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    # 'depends': ['base'],

    # # always loaded
    # 'data': [
    #     # 'security/ir.model.access.csv',
    #     'views/views.xml',
    #     'views/templates.xml',
    # ],
    # # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}

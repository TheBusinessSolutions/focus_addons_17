{
    'name': 'Sales/Invoice Total Amount Exchange',
    'version': '17.0.1.0.0',
    'summary': 'Add exchange rate and total amount fields to Sales Orders and Invoices',
    'author': "JD DEVS",
    'license': 'LGPL-3',
    'category': 'Sales',
    'application': False,
    'installable': True,
    'depends': [
        'base',
        'sale_management',  # replaces 'sale'
        'account',
        'product',
    ],
    'data': [
        'views/views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'currency_exchange_rate_amount_/static/src/js/tax_total_new_widget.js',
        ],
        'web.assets_qweb': [
            'currency_exchange_rate_amount_/static/src/xml/total_tax_json_widget_template.xml',
            'currency_exchange_rate_amount_/static/src/xml/tax_total_tmpl_inherit.xml',
        ],
    },
    'images': ['static/description/assets/screenshots/banner.png'],
}

# -*- coding: utf-8 -*-
{
    'name': "ekanur",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','web','report_xlsx'],


    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/kelompokbarang_view.xml',
        'views/barang_view.xml',
        'views/person_view.xml',
        'views/kasir_view.xml',
        'views/gudang_view.xml',
        'views/keamanan_view.xml',
        'views/kelompokgrooming_view.xml',
        'views/grooming_view.xml', 
        'views/customer_view.xml', 
        'views/supplier_view.xml',
        'views/owner_view.xml',
        'views/penjualan_view.xml',
        'report/daftar_penjualanpdf.xml',
        'report/daftar_supplierpdf.xml',
        'report/report.xml',
        'wizzard/barangdatang_wizzard_view.xml',
    ],
   
}

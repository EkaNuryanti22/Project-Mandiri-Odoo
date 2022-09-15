from crypt import methods
import json


import json

from odoo import http, models, fields
from odoo.http import request


class Ekanur(http.Controller):
    @http.route('/ekanur/getbarang', auth='public', method=['GET'])
    def getBarang(self, **kw):
        # Mengambil semua barang dari table barang
        barang = request.env['ekanur.barang'].search([])
        items = []

        for item in barang:
            items.append({
                'nama_barang': item.name,
                'harga_jual': item.harga_jual,
                'stok': item.stok
            })
        
        return json.dumps(items)

        from crypt import methods
import json


import json

from odoo import http, models, fields
from odoo.http import request


class Ekanur(http.Controller):
    @http.route('/ekanur/getbarang', auth='public', method=['GET'])
    def getBarang(self, **kw):
        # Mengambil semua barang dari table barang
        barang = request.env['ekanur.barang'].search([])
        items = []

        for item in barang:
            items.append({
                'nama_barang': item.name,
                'harga_jual': item.harga_jual,
                'stok': item.stok
            })
        
        return json.dumps(items)

		# Perubhannya di sini
    @http.route('/ekanur/getsupplier', auth='public', method=['GET'])
    def getSupplier(self, **kw):
        supplier = request.env['ekanur.supplier'].search([])
        items = []

        for item in supplier:
            items.append({
                'nama_toko': item.name,
                'alamat': item.alamat,
                'no_telepon': item.no_telp,
                'barang_id': item.barang_id[0].name
            })
        
        return json.dumps(items)
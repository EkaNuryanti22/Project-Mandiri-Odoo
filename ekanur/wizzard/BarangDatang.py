from odoo import api, fields, models


'''
Membuat model BarangDarang yang inherit
ke Transient Model, Odoo 14 ke atas harus
di daftarkan di security
'''
class BarangDatang(models.TransientModel):
    _name = 'ekanur.barangdatang'

    barang_ids = fields.Many2one(comodel_name='ekanur.barang', string='Nama Barang', required=True)
    jumlah = fields.Integer(string='Jumlah', required=False)

    def button_barang_datang(self):
        for line in self:
            self.env['ekanur.barang'].search([('id', '=', line.barang_ids.id)]).write(
                {'stok': line.barang_ids.stok +  line.jumlah}
            )
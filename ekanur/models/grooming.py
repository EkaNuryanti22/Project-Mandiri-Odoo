from odoo import api, fields, models

class grooming(models.Model):
    _name = 'ekanur.grooming'
    _description = 'New Description'

    name = fields.Char(string='Jenis Grooming')
    harga_biasa = fields.Integer(string='Harga Biasa', required=True)
    harga_anti_jamur = fields.Integer(string='Harga Anti Jamur', required=True)
    harga_anti_kutu = fields.Integer(string='Harga Anti Kutu', required=True)
    # Perubahannya ada di sini
    kelompokgrooming_id = fields.Many2one(comodel_name='ekanur.kelompokgrooming',
                                        string='kelompok grooming')
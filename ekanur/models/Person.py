from odoo import api, fields, models


class Person(models.Model):
    _name = 'ekanur.person'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    tgl_lahir = fields.Datetime(string='Tanggal Lahir')


class Kasir(models.Model):
    _name = 'ekanur.kasir'
    _inherit = 'ekanur.person'
    _description = 'New Description'

    id_kasir = fields.Char(string='ID Kasir')


class keamanan(models.Model):
    _name = 'ekanur.keamanan'
    _inherit = 'ekanur.person'
    _description = 'New Description'

    id_keamanan = fields.Char(string='ID keamanan')

class gudang(models.Model):
    _name = 'ekanur.gudang'
    _inherit = 'ekanur.person'
    _description = 'New Description'

    id_gudang = fields.Char(string='ID gudang')
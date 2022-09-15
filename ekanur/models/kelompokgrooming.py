from odoo import api, fields, models


class kelompokgrooming(models.Model):
    _name = 'ekanur.kelompokgrooming'
    _description = 'New Description'


    name = fields.Char(string='Nama Kelompok Grooming')
    kode_kelompok = fields.Char(string='Kode Kelompok Grooming')
    kode_ruang = fields.Char(string='Kode Ruang')
# Perubahannya from odoo import api, fields, models


class kelompokgrooming(models.Model):
    _name = 'ekanur.kelompokgrooming'
    _description = 'New Description'

    name = fields.Selection([
        ('grooming sehat', 'Grooming Sehat'),
        ('grooming anti kutu', 'Grooming Anti Kutu'),
        ('grooming anti jamur', 'Grooming Anti Jamur'),
        
    ], string='Nama Kelompok')

    kode_kelompok = fields.Char(string='Kode Kelompok')
    
    @api.onchange('name')
    def _onchange_kode_kelompok(self):
        if self.name == 'grooming sehat':
            self.kode_kelompok = 'GS1'
        elif self.name == 'grooming anti kutu':
            self.kode_kelompok = 'GK1'
        elif self.name == 'grooming anti jamur':
            self.kode_kelompok = 'GJ1'
        

    kode_ruang = fields.Char(string='Kode Ruang')
    grooming_ids = fields.One2many(comodel_name='ekanur.grooming',
                                inverse_name='kelompokgrooming_id',
                                string='Daftar Grooming')
    jml_item = fields.Char(compute='_compute_jml_item', string='Jumlah')
    
		# Perubahannya di sini
    @api.depends('grooming_ids')
    def _compute_jml_item(self):
        for record in self:
            a = self.env['ekanur.grooming'].search([('kelompokgrooming_id', '=', record.id)]).mapped('name')
            b = len(a)
            record.jml_item = b
            record.daftar = a
    
    daftar = fields.Char(string='Daftar isi')
    grooming_ids = fields.One2many(comodel_name='ekanur.grooming',
                                inverse_name='kelompokgrooming_id',
                                string='Daftar Grooming')
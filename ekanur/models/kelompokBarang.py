from odoo import api, fields, models


class KelompokBarang(models.Model):
    _name = 'ekanur.kelompokbarang'
    _description = 'New Description'


    name = fields.Char(string='Nama Kelompok Barang')
    kode_kelompok = fields.Char(string='Kode Kelompok Barang')
    kode_rak = fields.Char(string='Kode Rak')
# Perubahannya from odoo import api, fields, models


class KelompokBarang(models.Model):
    _name = 'ekanur.kelompokbarang'
    _description = 'New Description'

    name = fields.Selection([
        ('makanan basah', 'Makanan Basah'),
        ('makanan kering', 'Makanan Kering'),
        ('minuman', 'Minuman'),
        ('aksesoris', 'Aksesoris'),
        
    ], string='Nama Kelompok')

    kode_kelompok = fields.Char(string='Kode Kelompok')
    
    @api.onchange('name')
    def _onchange_kode_kelompok(self):
        if self.name == 'makanan basah':
            self.kode_kelompok = 'MB1'
        elif self.name == 'makanan kering':
            self.kode_kelompok = 'MK1'
        elif self.name == 'minuman':
            self.kode_kelompok = 'MI1'
        elif self.name == 'aksesoris':
            self.kode_kelompok = 'AK1'
        

    kode_rak = fields.Char(string='Kode Rak')
    barang_ids = fields.One2many(comodel_name='ekanur.barang',
                                inverse_name='kelompokbarang_id',
                                string='Daftar Barang')
    jml_item = fields.Char(compute='_compute_jml_item', string='Jumlah')
    
		# Perubahannya di sini
    @api.depends('barang_ids')
    def _compute_jml_item(self):
        for record in self:
            a = self.env['ekanur.barang'].search([('kelompokbarang_id', '=', record.id)]).mapped('name')
            b = len(a)
            record.jml_item = b
            record.daftar = a
    
    daftar = fields.Char(string='Daftar isi')
    barang_ids = fields.One2many(comodel_name='ekanur.barang',
                                inverse_name='kelompokbarang_id',
                                string='Daftar Barang')
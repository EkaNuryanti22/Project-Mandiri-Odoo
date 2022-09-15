from odoo import api, fields, models


class customer(models.Model):
    _inherit = 'res.partner'
    _description = 'customer'

    point = fields.Integer(string='Point')
    level = fields.Char(string='Level')
    
    
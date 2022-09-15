from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'New Description'

    is_customer = fields.Boolean(string='Is customer')
    is_owner = fields.Boolean(string='Is owner')
    poin = fields.Integer(string='Poin')
    level = fields.Char(string='Level')
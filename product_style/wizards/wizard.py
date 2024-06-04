from odoo import fields, api, models, _
from odoo.exceptions import ValidationError


class SalespersonReportWizard(models.TransientModel):
    _name = 'salesperson.report.wizard'

    user_ids = fields.Many2many('res.users', string='Salespersons', domain=[('share', '=', False)])

    def show_orders(self):
        action = self.env.ref('sale.action_orders').read()[0]
        action['domain'] = [('user_id', 'in', self.user_ids.ids)]
        return action
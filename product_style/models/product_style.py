from odoo import fields, api, models, _
from odoo.exceptions import ValidationError
import base64
import io
from datetime import datetime
from xlsxwriter.workbook import Workbook
import xlwt


class ProductStyle(models.Model):
    _name = "product.style"
    _description = "styles for fashion"

    name = fields.Char(string="name")
    code = fields.Integer(string="code", unique=True)

    @api.constrains('code')
    def _unique_check(self):
        for record in self:
            if self.search_count([('code', '=', record.code)]) > 1:
                raise ValidationError(_("code should be unique"))


    class ProductStyleMenu(models.Model):
        _inherit = 'sale.order'

        styles = fields.Many2one('product.style', string='Product Style')

    class Products(models.Model):
        _inherit = "product.template"

        styles = fields.Many2one('product.style', string="Product piles")

    class SaleOrderLine(models.Model):
        _inherit = "sale.order.line"

        superduper = fields.Many2one('product.style',string="Product styles")

        @api.onchange('product_id')
        def onchange_product(self):
            if self.product_id:
                self.superduper = self.product_template_id.styles

        @api.onchange('product_id')
        def _onchange_product_id(self):
            if self.order_id.partner_id.filter_products_so:
                domain = [('pricelist_id', '=', self.order_id.pricelist_id.id)]
                return {'domain': {'product_id': domain}}




    class SaleOrder(models.Model):
        _inherit = 'sale.order'

        customer_rating = fields.Selection(related="partner_id.customer_rank", string="Customer Rating", store=True)

class ResPartner(models.Model):

    _inherit = 'res.partner'
    customer_rank = fields.Selection(
        [
            ('one_star', 'One Star'),
            ('two_star', 'Two Star'),
            ('three_star', 'Three Star'),
            ('four_star', 'Four Star'),
            ('five_star', 'Five Star')
        ],
        string="Customer Rating")
    filter_products_so = fields.Boolean(string='Filter Products in SO Based on Pricelist')

    # @api.constrains('phone')
    # def _check_phone(self):
    #     for record in self:
    #         if record.phone:
    #             if not record.phone.isdigit() or len(record.phone) != 10:
    #                 raise ValidationError("Phone number must be 10 digits long")

    @api.model
    def create(self, vals):
        if 'phone' in vals and vals['phone']:
            if not vals['phone'].isdigit() or len(vals['phone']) != 10:
                raise ValidationError("Phone number must be 10 digits long")
            vals['phone'] = '-'.join([vals['phone'][i:i + 3] for i in range(0, len(vals['phone']), 3)])
        return super(ResPartner, self).create(vals)

    def write(self, vals):
        if 'phone' in vals and vals['phone']:
            if not vals['phone'].isdigit() or len(vals['phone']) != 10:
                raise ValidationError("Phone number must be 10 digits long")
            vals['phone'] = '-'.join([vals['phone'][i:i + 3] for i in range(0, len(vals['phone']), 3)])
        return super(ResPartner, self).write(vals)


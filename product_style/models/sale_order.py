from lxml import etree
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super(SaleOrder, self).fields_view_get(view_id, view_type, toolbar, submenu)
        doc = etree.XML(res['arch'])
        for node in doc.xpath("//field[@name='partner_id']"):
            node.set('domain', "[('is_company','=',True)]")
        res['arch'] = etree.tostring(doc)
        return res
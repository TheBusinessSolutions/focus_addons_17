from odoo import api, fields, models,_
from odoo.osv import expression
import json
from lxml import etree


class ProductTemplate(models.Model):
    _inherit = "product.template"
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('approve', 'Approve')
    ], string='Status', readonly=True, index=True, copy=False, tracking=True, default='draft')

    def button_draft(self):
        self.write({'state': 'draft'})
        
    def button_approve(self):
        self.write({'state': 'approve'})

    @api.model
    def get_view(self, view_id=None, view_type=False, **options):
        result = super(ProductTemplate,self).get_view(view_id=view_id, view_type=view_type, **options)
        doc = etree.XML(result['arch'])
        sub_fields = []

        if view_type == 'form':
            for node in doc.xpath("//field"):
                field_name = node.get('name')

                if field_name in self._fields and self._fields[field_name].type == "one2many":
                    tree_view_nodes = node.xpath(".//tree/field")
                    for sub_node in tree_view_nodes:
                        sub_node.set('readonly', "parent.state != 'draft'")
                        sub_fields.append(sub_node)

            for field in doc.xpath("//field"):
                field_name = field.get('name')
                header_fields = ['qty_available', 'uom_name', 'virtual_available','nbr_moves_in','nbr_moves_out','sales_count','purchased_product_qty']
                if field not in sub_fields:
                    field.set('readonly', "state != 'draft'")
                if field_name in header_fields:
                    field.set('readonly', "1")

        result['arch'] = etree.tostring(doc, encoding='unicode')
        return result

class Product(models.Model):
    _inherit = "product.product"

    state = fields.Selection(related="product_tmpl_id.state")

    def button_draft(self):
        self.write({'state': 'draft'})

    def button_approve(self):
        self.write({'state': 'approve'})


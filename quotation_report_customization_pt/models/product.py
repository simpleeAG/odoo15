from odoo import fields, models, _

class ProductProduct(models.Model):
    _inherit = 'product.product'

    # description_sale = fields.Html(string='Description', required=True, translate=True)
    description_sale = fields.Html(
        'Sales Description', translate=True,
        help="A description of the Product that you want to communicate to your customers. "
             "This description will be copied to every Sales Order, Delivery Order and Customer Invoice/Credit Note")

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    name = fields.Html(string='Description', required=True, translate=True)
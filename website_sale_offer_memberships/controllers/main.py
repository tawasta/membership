from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request


class WebsiteSale(WebsiteSale):
    def _get_shop_payment_values(self, order, **kwargs):
        render_values = super(WebsiteSale, self)._get_shop_payment_values(
            order, **kwargs
        )
        print(render_values)
        is_membership = False
        for line in order.order_line:
            if line.product_id.membership:
                is_membership = True

        if is_membership is False:
            membership_categ_id = (
                request.env["product.public.category"]
                .sudo()
                .search([("parent_id", "=", False), ("name", "ilike", "jäsenyys")])
            )
            categ_href = "/shop/category/%s" % membership_categ_id.id
            render_values.update(
                {"show_membership_info": True, "categ_href": categ_href}
            )

        return render_values

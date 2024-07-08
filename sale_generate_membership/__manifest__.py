##############################################################################
#
#    Author: Tawasta
#    Copyright 2020 Oy Tawasta OS Technologies Ltd. (https://tawasta.fi)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see http://www.gnu.org/licenses/agpl.html
#
##############################################################################
{
    "name": "Sale Create Membership",
    "summary": "Sale Create Membership",
    "version": "14.0.1.2.1",
    "category": "Website",
    "website": "https://gitlab.com/tawasta/odoo/membership",
    "author": "Tawasta",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {"python": [], "bin": []},
    "depends": [
        "membership_product",
        "sale",
        "membership",
        "contract_invoice_address",
        "product_variant_variant_company",
        "product_variant_sale_price",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/template.xml",
        "views/contract.xml",
        "views/family_member_consent.xml",
        "views/product_template_view.xml",
        "views/sale_order.xml",
        "views/templates.xml",
    ],
    "demo": [],
}

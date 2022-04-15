# -*- coding: utf-8 -*-
# from odoo import http


# class PaymentPaystack(http.Controller):
#     @http.route('/payment_paystack/payment_paystack', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/payment_paystack/payment_paystack/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('payment_paystack.listing', {
#             'root': '/payment_paystack/payment_paystack',
#             'objects': http.request.env['payment_paystack.payment_paystack'].search([]),
#         })

#     @http.route('/payment_paystack/payment_paystack/objects/<model("payment_paystack.payment_paystack"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('payment_paystack.object', {
#             'object': obj
#         })

# coding: utf-8
import requests, json, logging
from tokenize import group
from werkzeug.urls import url_join

# from .currencies import SUPPORTED_CURRENCIES

from odoo import api, fields, service, models, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)

class PaymentAcquirer(models.Model):
    _inherit = 'payment.acquirer'
    
    provider = fields.Selection(
        selection_add=[('paystack', "Paystack")], ondelete={'paystack': 'cascade'})
    # provider = fields.Selection(selection_add=[('flutterwave', 'Flutterwave')], ondelete={'flutterwave': 'set default'})
    pstack_public_key = fields.Char(required_if_provider='rave', groups='base.group_user')
    pstack_secret_key = fields.Char(required_if_provider='rave', groups='base.group_user')
    # rave_secret_hash = fields.Char(required_if_provider='rave', groups='base.group_user', string="Flutterwave Secret Hash")
    environment = fields.Char(required_if_provider='paystack', groups='base.group_user')

    @api.model
    def _get_paystack_api_url(self):
        self.ensure_one()
        """ PaystackURLs"""
        return 'https://api.paystack.co'
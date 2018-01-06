# -*- coding: utf-8 -*-
from odoo import http

# class Supermodulo(http.Controller):
#     @http.route('/supermodulo/supermodulo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/supermodulo/supermodulo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('supermodulo.listing', {
#             'root': '/supermodulo/supermodulo',
#             'objects': http.request.env['supermodulo.supermodulo'].search([]),
#         })

#     @http.route('/supermodulo/supermodulo/objects/<model("supermodulo.supermodulo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('supermodulo.object', {
#             'object': obj
#         })
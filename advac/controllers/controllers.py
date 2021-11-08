# -*- coding: utf-8 -*-
# from odoo import http


# class Advac(http.Controller):
#     @http.route('/advac/advac/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/advac/advac/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('advac.listing', {
#             'root': '/advac/advac',
#             'objects': http.request.env['advac.advac'].search([]),
#         })

#     @http.route('/advac/advac/objects/<model("advac.advac"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('advac.object', {
#             'object': obj
#         })

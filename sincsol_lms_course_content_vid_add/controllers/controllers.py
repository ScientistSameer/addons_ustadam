# -*- coding: utf-8 -*-
# from odoo import http


# class AddonsUstadam/sincsolLmsCourseContentVidAdd(http.Controller):
#     @http.route('/addons_ustadam/sincsol_lms_course_content_vid_add/addons_ustadam/sincsol_lms_course_content_vid_add', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addons_ustadam/sincsol_lms_course_content_vid_add/addons_ustadam/sincsol_lms_course_content_vid_add/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('addons_ustadam/sincsol_lms_course_content_vid_add.listing', {
#             'root': '/addons_ustadam/sincsol_lms_course_content_vid_add/addons_ustadam/sincsol_lms_course_content_vid_add',
#             'objects': http.request.env['addons_ustadam/sincsol_lms_course_content_vid_add.addons_ustadam/sincsol_lms_course_content_vid_add'].search([]),
#         })

#     @http.route('/addons_ustadam/sincsol_lms_course_content_vid_add/addons_ustadam/sincsol_lms_course_content_vid_add/objects/<model("addons_ustadam/sincsol_lms_course_content_vid_add.addons_ustadam/sincsol_lms_course_content_vid_add"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addons_ustadam/sincsol_lms_course_content_vid_add.object', {
#             'object': obj
#         })


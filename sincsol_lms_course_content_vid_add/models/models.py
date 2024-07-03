# models/course_content.py
from odoo import models, fields

class CourseContent(models.Model):
    _name = 'ustadam.course_content'
    _description = 'Course Content'

    text = fields.Text(string='Text')
    youtube_url = fields.Char(string='YouTube URL')
    course_id = fields.Many2one('ustadam.course', string='Course')

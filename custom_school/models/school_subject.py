from odoo import models, fields, api

class SchoolSubject(models.Model):
    _name = 'school.subject'
    _description = ' School Subject'
    
    name = fields.Char(string="Name")
    credits = fields.Integer(string="Credits")
    max_students = fields.Integer(string="Max Students")
    active=fields.Boolean(string='Active')
    teacher_id = fields.Many2one('school.teacher',string='Teacher')
    student_ids=fields.Many2many('school.student',string="Students")
from odoo import models, fields, api

class SchoolTeacher(models.Model):
    _name = 'school.teacher'
    _description = ' School Teacher'
    
    name = fields.Char(string="Name")
    profile = fields.Text(string="Text")
    subject_ids=fields.One2many('school.subject','teacher_id',string="Subjects")
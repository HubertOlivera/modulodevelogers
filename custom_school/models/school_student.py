import datetime
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = ' School Student'
    
    name = fields.Char(string="Name")
    birth_date = fields.Date(string="Date")
    date = fields.Date(string='Date', default=fields.Date.today(), help="Date")
    age = fields.Integer(string="Age",compute='_get_age',)
    final_exam_grade=fields.Float(string='Final Exam Grade')
    subject_ids=fields.Many2many('school.subject',string="Subjects")
    
            
    @api.depends('birth_date')
    def _get_age(self):
        if self.birth_date:
            d1 = self.birth_date
            d2 = datetime.date.today()
            self.age = relativedelta(d2, d1).years
        else:
            self.age=1
    
    


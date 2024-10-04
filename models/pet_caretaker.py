from odoo import fields, models, api

class PetCaretaker(models.Model):
    _name = 'pet.caretaker'
    _description = 'Pet Caretaker'

    name = fields.Char(string='Name')
    experience_years = fields.Integer(string='Years of experience', default=1)
    specialty_ids = fields.Many2many('pet', string='Specialties')
    phone = fields.Char(string='Phone', required=True)
    email= fields.Char(string='Email')
    
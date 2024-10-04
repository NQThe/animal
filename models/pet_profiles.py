from odoo import fields, models, api

class PetProfile(models.Model):
    _name = 'pet.profile'
    _description = 'Pet Profile'

    name = fields.Char("Pet Name", required=True)
    birth_date = fields.Integer("Date of birth", default=1)
    
    species = fields.Many2one('pet', string='Species_ids')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ],string='Gender', default='male')
    
    
    pet_owner = fields.Char(string="Pet Owner")
    phone_owner = fields.Char(string="Phone", required=True)
    email_owner = fields.Char(string="Email")
    address_owner = fields.Char(string="Address")
    
    Pet_image = fields.Image(string="Pet Image")
    
    
    
    
    
    
    
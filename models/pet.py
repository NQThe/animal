from odoo import fields, models, api

class Pet(models.Model):
    _name = 'pet'
    
    
    name = fields.Char(string='pet', required=True)
    color =fields.Integer(string='Color')
    
    species_id_profile = fields.One2many('pet.profile','species', string='species')
    
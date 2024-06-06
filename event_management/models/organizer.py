from odoo import api, fields, models
from odoo.exceptions import ValidationError

class OrganizerModel(models.Model):
    _name = "event.organizer"
    _description = "Organizer Management System "
    
    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    end_date = fields.Datetime(string="End Date")
    user_id = fields.Many2one('res.users', string='User', readonly=True, ondelete='set null')
    event_ids = fields.Many2many('event.event', string="Event IDS")
    
    
    
    @api.model
    def create(self, vals):
            if 'email' not in vals:
                raise ValidationError("Email is required to create a user.")

            user_vals = {
                'name': vals.get('name'),
                'email': vals.get('email'),
                'is_company': False,
                'active': True,
            }
            new_user = self.env['res.users'].create(user_vals)
            
            vals['user_id'] = new_user.id

            return super(OrganizerModel, self).create(vals)
    
    

    
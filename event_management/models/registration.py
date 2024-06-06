from odoo import api, fields, models


class RegistrationModel(models.Model):
    _name = "event.registration"
    _rec_name = "attendee_id"
    _description = "Registration Management System "

    attendee_id = fields.Many2one("event.attendee", string="Attendee ID")
    event_id = fields.Many2one("event.event", string="Event ID")
    registraion_date = fields.Datetime(string="Registration Date")
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("confirmed", "Confirmed"),
            ("cancelled", "Cancelled"),
        ],
        string="Status",
        default="draft",
    )

    def action_confirm(self):
        self.state = "confirmed"

    def action_cancel(self):
        self.state = "cancelled"

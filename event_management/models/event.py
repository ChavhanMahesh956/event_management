from odoo import api, fields, models


class EventModel(models.Model):
    _name = "event.event"
    _description = "Event Management System "

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    start_date = fields.Datetime(string="Start Date")
    end_date = fields.Datetime(string="End Date")
    organizer_id = fields.Many2one("event.organizer", string="Organizer ID")
    duration = fields.Float(string="Duration", compute="_compute_duration", store=True)
    attendee_ids = fields.Many2many("event.registration", string="Attendee IDs")



    @api.depends("start_date", "end_date")
    def _compute_duration(self):
        for rec in self:
            if rec.start_date and rec.end_date:
                start_date = fields.Date.from_string(rec.start_date)
                end_date = fields.Date.from_string(rec.end_date)
                duration = (end_date - start_date).days
                rec.duration = float(duration)
            else:
                rec.duration = 0.0
                



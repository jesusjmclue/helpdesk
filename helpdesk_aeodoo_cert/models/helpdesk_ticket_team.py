from odoo import api, fields, models


class HelpdeskTeam(models.Model):
    _name = "helpdesk.ticket.team"
    _inherit = "helpdesk.ticket.team"

    use_timesheet = fields.Boolean(string="Use timesheet?")
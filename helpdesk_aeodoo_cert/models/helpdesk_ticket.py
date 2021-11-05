from odoo import _, api, fields, models, tools
from odoo.exceptions import AccessError


class HelpdeskTicket(models.Model):
    _name = "helpdesk.ticket"
    _inherit = "helpdesk.ticket"

    timesheet_ids = fields.One2many(
        comodel_name="account.analytic.line",
        inverse_name="ticket_id",
        string="Timesheet lines"
    )

    total_hours = fields.Float(
        string="Total hours",
        compute="_compute_total_hours"
    )

    use_timesheet = fields.Boolean(
        related="team_id.use_timesheet",
        store=True
    )

    @api.depends('timesheet_ids')
    def _compute_total_hours(self):
        self.ensure_one()
        hours = 0
        for timesheet in self.timesheet_ids:
            hours = hours + timesheet.unit_amount
        self.total_hours = hours
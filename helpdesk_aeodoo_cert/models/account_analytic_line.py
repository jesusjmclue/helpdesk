from odoo import _, api, fields, models, tools
from odoo.exceptions import AccessError


class AccountAnalyticLine(models.Model):
    _name = "account.analytic.line"
    _inherit = "account.analytic.line"

    ticket_id = fields.Many2one(
        comodel_name="helpdesk.ticket"
    )

    employee_cost = fields.Monetary(
        string="Employee Cost",
        compute="_compute_employee_cost",
    )

    @api.depends('ticket_id')
    def _compute_employee_cost(self):
        self.ensure_one()
        timesheet_cost = self.env['hr.employee'].search([('id', '=', self.employee_id.id)]).timesheet_cost
        self.employee_cost = self.unit_amount * timesheet_cost
# Copyright 2018-22 ForgeFlow S.L.
# Copyright 2021 Sodexis
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class MailActivityTeamRule(models.Model):
    _name = "mail.activity.team.rule"
    _description = "Mail Activity Team Rule"

    name = fields.Char()
    sequence = fields.Integer(default=1)
    active = fields.Boolean(default=True)
    team_id = fields.Many2one(
        comodel_name="mail.activity.team",
        required="True",
        string="Team",
    )
    team_member_id = fields.Many2one(
        comodel_name="res.users",
        required="True",
        string="Team Member",
    )
    rule_model = fields.Many2one(
        comodel_name="ir.model",
        string="Model",
    )
    rule_domain = fields.Char(
        required="True",
        string="Rule",
    )

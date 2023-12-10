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
    team_member_ids = fields.Many2many(
        related="team_id.member_ids",
        readonly=True,
    )
    team_model_ids = fields.Many2many(
        related="team_id.res_model_ids",
        readonly=True,
    )
    team_member_id = fields.Many2one(
        comodel_name="res.users",
        required="True",
        string="Team Member",
        domain="[('id','in',team_member_ids)]",
    )
    activity_model_ids = fields.Many2many(
        comodel_name="ir.model",
        compute="_compute_activity_model_ids",
    )
    rule_model = fields.Many2one(
        comodel_name="ir.model",
        string="Model",
        domain="[('id','in',team_model_ids or activity_model_ids)]",
    )
    rule_domain = fields.Char(
        required="True",
        string="Rule",
    )

    def _compute_activity_model_ids(self):
        for rule in self:
            rule.activity_model_ids = (
                self.env["ir.model"]
                .sudo()
                .search(["&", ("is_mail_thread", "=", True), ("transient", "=", False)])
            )

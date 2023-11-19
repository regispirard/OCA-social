# Copyright 2018-22 ForgeFlow S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models
from odoo.tools.safe_eval import safe_eval


class MailActivity(models.Model):
    _inherit = "mail.activity"

    @api.onchange("team_id")
    def _onchange_team_id(self):
        if not self.team_id.id:
            return super()._onchange_team_id()
        team_rules_domain = [
            ("team_id", "=", self.team_id.id),
            "|",
            ("rule_model", "=", self.res_model_id.id),
            ("rule_model", "=", False),
        ]
        team_rules = self.env["mail.activity.team.rule"].search(
            team_rules_domain, order="sequence ASC"
        )
        if team_rules:
            record = self.env[self.res_model].search([("id", "=", self.res_id)])
            for rule in team_rules:
                # test if the rule applies to the record related to the activity
                # the first rule which applies will be selected
                if record.filtered_domain(safe_eval(rule.rule_domain)):
                    # if the rule applies, assign to the user of the rule
                    self.user_id = rule.team_member_id
                    return
        # Fall back to original activity_tem on_change_team_id if no rule applies
        return super()._onchange_team_id()

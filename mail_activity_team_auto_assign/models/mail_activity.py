# Copyright 2018-22 ForgeFlow S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from odoo import api, models
from odoo.tools.safe_eval import safe_eval

_logger = logging.getLogger(__name__)


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
            # record to which the activity is related
            record = self.env[self.res_model].search([("id", "=", self.res_id)])
            try:
                for rule in team_rules:
                    # the first rule which applies to the record will be selected
                    if record.filtered_domain(safe_eval(rule.rule_domain)):
                        # if the rule applies, assign activity to the user
                        self.user_id = rule.team_member_id
                        return
            except KeyError:
                # this exception can happen if the domain on the rule is not well defined
                _logger.warning("Error with rule domain %s", rule.rule_domain)
        # Fall back to original activity_team on_change_team_id if no rule applies
        return super()._onchange_team_id()

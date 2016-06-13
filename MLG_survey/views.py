# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Game(Page):

    form_model = models.Player
    form_fields = ['g_pref_stage',
                   'g_pref_rk_1',
                   'g_pref_rk_2',
                   'g_pref_rk_3']

class Demographics(Page):

    form_model = models.Player
    form_fields = ['q_age',
                  'q_gender',
                  'q_gender',
                  'q_estrato',
                  'q_graduated',
                  'q_career_1',
                  'q_career_2',
                  'q_postgraduate',
                  'q_master_1',
                  'q_master_2',
                  'q_game_part',
                  'q_part_time']

class Preferences(Page):

    form_model = models.Player
    form_fields = ['p_risk',
                   'p_compet_1',
                   'p_compet_2',
                   'p_compet_3',
                   'p_compet_4',
                   'p_compet_5',
                   'p_compet_6']

class Preferences_II(Page):

    form_model = models.Player
    form_fields = ['p_trust_1',
                   'p_trust_2',
                   'p_trust_3',
                   'p_trust_4',
                   'p_trust_5']

    def before_next_page(self):
        self.player.set_payoff()

class Payment_info(Page):

    def vars_for_template(self):
        self.player.set_payoff()
        participant = self.player.participant
        return {
            'redemption_code': participant.label or participant.code,
        }


page_sequence = [
    Game,
    Demographics,
    Preferences,
    Preferences_II,
    Payment_info
]

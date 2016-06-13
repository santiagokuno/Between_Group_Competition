# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Contribute(Page):

    """Player: Choose how much to extract"""

    form_model = models.Player
    form_fields = ['extraction']

    timeout_submission = {'extraction': c(Constants.endowment/2)}

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()

    body_text = "Esperando la decisión de sus compañeros"

class Results_2WaitPage(WaitPage):

    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.subsession.set_ranking_g()

    body_text = "Esperando la decisión de sus compañeros"

class Results_6WaitPage(WaitPage):

    wait_for_all_groups = True

    body_text = "Calculando rankings de los grupos y los pagos finales"

class Results_2(Page):
    #pass
    def vars_for_template(self):
        self.player.the_ranking()
        return{
            'player_1': self.subsession.rank_p_1,
            'player_2': self.subsession.rank_p_2,
            'player_3': self.subsession.rank_p_3,
            'player_4': self.subsession.rank_p_4,
            'player_5': self.subsession.rank_p_5,
            'player_6': self.subsession.rank_p_6,
            'multiplicador_uno': self.subsession.multi_uno,
            'multiplicador_dos': self.subsession.multi_dos,
            'multiplicador_tres': self.subsession.multi_tres,
            'participante': self.player.participant,
            'partici_2': self.player.auxiliar,
            'Fondo_Comun': 5*Constants.players_per_group - self.group.total_extraction,
            'Ganancias_grupo' : self.group.total_payment,
            'Ganancias_parciales' : self.player.partial_pay,
            'Pago_final' : self.player.payoff,
            }


page_sequence = [
    Contribute,
    ResultsWaitPage,
    Results_2WaitPage,
    Results_6WaitPage,
    Results_2
]

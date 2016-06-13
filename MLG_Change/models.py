# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'MLG_Change'
    players_per_group = None
    num_rounds = 1

    question_correct_1 = '6.5'
    question_correct_2 = '7.2'

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    question_1 = models.CharField(
        choices=[
            ('1.0', '1.0'),
            ('4.0', '4.0'),
            ('6.5', '6.5'),
            ('7.2', '7.2'),
            ('12.0', '12.0'),
        ]
    )

    question_2 = models.CharField(
        choices=[
            ('1.0', '1.0'),
            ('4.0', '4.0'),
            ('6.5', '6.5'),
            ('7.2', '7.2'),
            ('12.0', '12.0'),
        ]
    )

    def question_correct_1(self):
        return self.question_1 == Constants.question_correct_1

    def question_correct_2(self):
        return self.question_2 == Constants.question_correct_2

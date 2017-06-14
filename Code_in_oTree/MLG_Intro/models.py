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

author = 'Santiago GC'

doc = """
The Introduction to our game
"""

class Constants(BaseConstants):
    name_in_url = 'MLG_Intro'
    players_per_group = None
    num_rounds = 1

    question_correct = '6.5'

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    question = models.CharField(
        choices=[
            ('3.0', '3.0'),
            ('6.0', '6.0'),
            ('6.5', '6.5'),
            ('9.5', '9.5'),
            ('13.0', '13.0'),
        ]
    )

    def question_correct(self):
        return self.question == Constants.question_correct

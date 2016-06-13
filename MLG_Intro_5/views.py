# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Intro_I(Page):
    pass

class Intro_II(Page):
    pass

class Intro_III(Page):

    form_model = models.Player
    form_fields = ['question']

class Intro_IV(Page):
    pass

class Espera(WaitPage):

    wait_for_all_groups = True

    body_text = "Esperando que sus compañeros terminen de revisar las instrucciones."

class Begin(Page):
    pass

page_sequence = [
    Intro_I,
    Intro_II,
    Intro_III,
    Intro_IV,
    Espera,
    Begin
]

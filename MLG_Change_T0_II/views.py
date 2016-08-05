# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Cambio(Page):
    pass

class Pregunta(Page):

    form_model = models.Player
    form_fields = ['question_1']

class Respuesta(Page):
    pass

class Espera(WaitPage):

    wait_for_all_groups = True

    body_text = "Esperando que sus compañeros terminen de revisar las instrucciones."

class Begin(Page):
    pass

page_sequence = [
    Cambio,
    Pregunta,
    Respuesta,
    Espera,
    Begin
]

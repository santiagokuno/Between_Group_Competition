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
    name_in_url = 'MLG_survey'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    def set_payoff(self):
        """Calculate payoff, which is zero for the survey"""
        self.payoff = 0

    q_age = models.PositiveIntegerField(verbose_name='¿Cuál es su edad?',
                                        choices=range(13, 50),
                                        initial=None)
    q_gender = models.CharField(initial=None,
                                choices=['Hombre', 'Mujer'],
                                verbose_name='¿Cuál es su género?',
                                widget=widgets.RadioSelect())
    q_estrato = models.PositiveIntegerField(verbose_name='¿En cuál estrato está ubicada su casa?',
                                        choices=range(1, 7),
                                        initial=None)
    q_game_part = models.CharField(initial=None,
                                choices=['SI', 'NO'],
                                verbose_name='¿Ha participado en actividades similares a ésta (experimentos económicos)?',
                                widget=widgets.RadioSelect())
    q_part_time = models.PositiveIntegerField(verbose_name='¿En cuántas actividades como ésta ha participado? (escriba "0" si en ninguno)')
    q_graduated = models.CharField(initial=None,
                                choices=['SI', 'NO'],
                                verbose_name='¿Está usted graduado de pregrado?',
                                widget=widgets.RadioSelect())
    q_career_1 = models.CharField(max_length=20,
                                  verbose_name='¿De cuál carrera (pregrado) se graduó o cuál está cursando? (escriba "ninguna" si no aplica)')
    q_career_2 = models.CharField(max_length=20,
                                  verbose_name='¿De cuál otra carrera (pregrado) se graduó o está cursando? (escriba "ninguna" si no aplica)')
    q_postgraduate = models.CharField(initial=None,
                                choices=['SI', 'NO'],
                                verbose_name='¿Está usted estudiando o se graduó de posgrado?',
                                widget=widgets.RadioSelect())
    q_master_1 = models.CharField(max_length=20,
                                  verbose_name='¿De cuál carrera (posgrado) se graduó o cuál está cursando? (escriba "ninguna" si no aplica)')
    q_master_2 = models.CharField(max_length=20,
                                  verbose_name='¿De cuál otra carrera (posgrado) se graduó o está cursando? (escriba "ninguna" si no aplica)')

    p_risk = models.PositiveIntegerField(verbose_name='Por favor señale una opción',
                                        choices=range(1, 11),
                                        initial=None,
                                        widget=widgets.RadioSelect())
    p_compet_1 = models.PositiveIntegerField(verbose_name='Las notas deberían basarse solo en el desempeño individual, no en trabajos en grupo',
                                             choices=[
                                                 (1, 'Absolutamente de acuerdo'),
                                                 (2, 'De acuerdo'),
                                                 (3, 'En desacuerdo'),
                                                 (4, 'Muy en desacuerdo')
                                             ],
                                             initial=None,
                                             widget=widgets.RadioSelect())
    p_compet_2 = models.PositiveIntegerField(verbose_name='El trabajo en grupo no es bueno porque permite que algunos no trabajen (free-riders)',
                                             choices=[
                                                 (1, 'Absolutamente de acuerdo'),
                                                 (2, 'De acuerdo'),
                                                 (3, 'En desacuerdo'),
                                                 (4, 'Muy en desacuerdo')
                                             ],
                                             initial=None,
                                             widget=widgets.RadioSelect())
    p_compet_3 = models.PositiveIntegerField(verbose_name='El trabajo en grupo permite desarrollar habilidades para trabajar con los demás',
                                             choices=[
                                                 (1, 'Absolutamente de acuerdo'),
                                                 (2, 'De acuerdo'),
                                                 (3, 'En desacuerdo'),
                                                 (4, 'Muy en desacuerdo')
                                             ],
                                             initial=None,
                                             widget=widgets.RadioSelect())
    p_compet_4 = models.PositiveIntegerField(verbose_name='Las habilidades que más se valoran en el mercado laborar son las individuales',
                                             choices=[
                                                 (1, 'Absolutamente de acuerdo'),
                                                 (2, 'De acuerdo'),
                                                 (3, 'En desacuerdo'),
                                                 (4, 'Muy en desacuerdo')
                                             ],
                                             initial=None,
                                             widget=widgets.RadioSelect())
    p_compet_5 = models.PositiveIntegerField(verbose_name='Me gustaría tener más cursos de solo Aprobado/Reprobado para no preocuparme por las notas',
                                             choices=[
                                                 (1, 'Absolutamente de acuerdo'),
                                                 (2, 'De acuerdo'),
                                                 (3, 'En desacuerdo'),
                                                 (4, 'Muy en desacuerdo')
                                             ],
                                             initial=None,
                                             widget=widgets.RadioSelect())
    p_compet_6 = models.PositiveIntegerField(verbose_name='En un trabajo en gupo, cómo prefiero ser calificado en una sustentación',
                                             choices=[
                                                 (3, 'La nota sea individual'),
                                                 (1, 'La nota sea el promedio de las sustentaciones del grupo'),
                                                 (2, '50% individual y 50% el promedio de los demás')
                                             ],
                                             initial=None,
                                             widget=widgets.RadioSelect())


    g_pref_stage = models.PositiveIntegerField(verbose_name='¿Cuál etapa del juego le gustó más?',
                                             choices=[
                                                 (1, 'La primera'),
                                                 (2, 'la segunda'),
                                                 (3, 'la tercera')
                                             ],
                                             initial=None,
                                             widget=widgets.RadioSelect())
    g_pref_rk_1 = models.PositiveIntegerField(verbose_name='En la PRIMERA etapa del juego, ¿qué información era más importante para decidir que hacer?',
                                             choices=[
                                                 (1, 'Mi posición individual con respecto a los demás jugadores'),
                                                 (2, 'La posición de mi grupo con respecto a los demás grupos'),
                                                 (3, 'Ambos eran igual de importantes importantes')
                                             ],
                                             initial=None,
                                             widget=widgets.RadioSelect())

    g_pref_rk_2 = models.PositiveIntegerField(verbose_name='En la SEGUNDA etapa del juego, ¿qué información era más importante para decidir que hacer?',
                                             choices=[
                                                 (1, 'Mi posición individual con respecto a los demás jugadores'),
                                                 (2, 'La posición de mi grupo con respecto a los demás grupos'),
                                                 (3, 'Ambos eran igual de importantes importantes')
                                             ],
                                             initial=None,
                                             widget=widgets.RadioSelect())

    g_pref_rk_3 = models.PositiveIntegerField(verbose_name='En la TERCERA etapa del juego, ¿qué información era más importante para decidir que hacer?',
                                             choices=[
                                                 (1, 'Mi posición individual con respecto a los demás jugadores'),
                                                 (2, 'La posición de mi grupo con respecto a los demás grupos'),
                                                 (3, 'Ambos eran igual de importantes importantes')
                                             ],
                                             initial=None,
                                             widget=widgets.RadioSelect())

    p_trust_1 = models.PositiveIntegerField(verbose_name='La mayor parte de las personas en la Universidad son honestas y se puede confiar en ellas',
                                             choices=[
                                                 (1, 'Absolutamente de acuerdo'),
                                                 (2, 'De acuerdo'),
                                                 (3, 'En desacuerdo'),
                                                 (4, 'Muy en desacuerdo')
                                             ],
                                             initial=None,
                                             widget=widgets.RadioSelect())

    p_trust_2 = models.PositiveIntegerField(verbose_name='Las personas en la Universidad por lo general se preocupan por su propio beneficio',
                                             choices=[
                                                 (1, 'Absolutamente de acuerdo'),
                                                 (2, 'De acuerdo'),
                                                 (3, 'En desacuerdo'),
                                                 (4, 'Muy en desacuerdo')
                                             ],
                                             initial=None,
                                             widget=widgets.RadioSelect())

    p_trust_3 = models.PositiveIntegerField(verbose_name='Se puede confiar más en las personas de esta Universidad que las de otras universidades',
                                             choices=[
                                                 (1, 'Absolutamente de acuerdo'),
                                                 (2, 'De acuerdo'),
                                                 (3, 'En desacuerdo'),
                                                 (4, 'Muy en desacuerdo')
                                             ],
                                             initial=None,
                                             widget=widgets.RadioSelect())

    p_trust_4 = models.PositiveIntegerField(verbose_name='En esta Universidad hay que estar alerta, de otra manera alguien se puede aprovechar de uno',
                                             choices=[
                                                 (1, 'Absolutamente de acuerdo'),
                                                 (2, 'De acuerdo'),
                                                 (3, 'En desacuerdo'),
                                                 (4, 'Muy en desacuerdo')
                                             ],
                                             initial=None,
                                             widget=widgets.RadioSelect())

    p_trust_5 = models.PositiveIntegerField(verbose_name='En esta Universidad si alguien tiene un problema, siempre hay alguien para ayudarlo',
                                             choices=[
                                                 (1, 'Absolutamente de acuerdo'),
                                                 (2, 'De acuerdo'),
                                                 (3, 'En desacuerdo'),
                                                 (4, 'Muy en desacuerdo')
                                             ],
                                             initial=None,
                                             widget=widgets.RadioSelect())
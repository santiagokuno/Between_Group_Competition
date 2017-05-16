import os
from os import environ

import dj_database_url
from boto.mturk import qualification

import otree.settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
else:
    DEBUG = True

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'otree'

SECRET_KEY = 'otreerules'

PAGE_FOOTER = ''

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}

AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')

REAL_WORLD_CURRENCY_CODE = 'COL'
USE_POINTS = True
POINTS_DECIMAL_PLACES = 1

LANGUAGE_CODE = 'es'

INSTALLED_APPS = []

DEMO_PAGE_INTRO_TEXT = """
<ul>
    <li>
        <a href="https://github.com/oTree-org/otree" target="_blank">
            Source code
        </a> for the below games.
    </li>
    <li>
        <a href="http://www.otree.org/" target="_blank">
            oTree homepage
        </a>.
    </li>
</ul>
<p>
    This is economics experiment on intra and intergroup competition.
</p>
"""

mturk_hit_settings = {
    'keywords': ['easy', 'bonus', 'choice', 'study'],
    'title': 'Title for your experiment',
    'description': 'Description for your experiment',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7*24,
    'qualification_requirements': [
    ]
}

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 200,
    'participation_fee': 5000,
    'num_bots': 12,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
}


SESSION_CONFIGS = [
       {
        'name': 'Completo_3_grupos',
        'display_name': "MLG Full (3 grupos)",
        'num_demo_participants': 12,
        'app_sequence': [
             'MLG_Intro', 'CPR_Game', 'MLG_Change', 'MLG_Game', 'MLG_Change_B', 'CPR_Game_II', 'MLG_survey'
        ],
    },
       {
        'name': 'Completo_5_grupos',
        'display_name': "MLG Full (5 grupos)",
        'num_demo_participants': 20,
        'app_sequence': [
             'MLG_Intro_5', 'CPR_Game_5', 'MLG_Change_5', 'MLG_Game_5', 'MLG_Change_B', 'CPR_Game_5_II',  'MLG_survey'
        ],
    },
       {
        'name': 'Base_3_grupos',
        'display_name': "CPR Base (3 grupos)",
        'num_demo_participants': 12,
        'app_sequence': [
             'MLG_Intro_T0', 'CPR_Game_T1', 'MLG_Change_T0', 'CPR_Game_T2', 'MLG_Change_T0_II', 'CPR_Game_T3',  'MLG_survey'
        ],
    },
]

otree.settings.augment_settings(globals())

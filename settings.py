import os
from os import environ

import dj_database_url
from boto.mturk import qualification

import otree.settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# the environment variable OTREE_PRODUCTION controls whether Django runs in
# DEBUG mode. If OTREE_PRODUCTION==1, then DEBUG=False
if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
else:
    DEBUG = True

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'otree'

# don't share this with anybody.
# Change this to something unique (e.g. mash your keyboard),
# and then delete this comment.
SECRET_KEY = 'otreerules'

PAGE_FOOTER = ''

# To use a database other than sqlite,
# set the DATABASE_URL environment variable.
# Examples:
# postgres://USER:PASSWORD@HOST:PORT/NAME
# mysql://USER:PASSWORD@HOST:PORT/NAME

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}

# AUTH_LEVEL:
# If you are launching a study and want visitors to only be able to
# play your app if you provided them with a start link, set the
# environment variable OTREE_AUTH_LEVEL to STUDY.
# If you would like to put your site online in public demo mode where
# anybody can play a demo version of your game, set OTREE_AUTH_LEVEL
# to DEMO. This will allow people to play in demo mode, but not access
# the full admin interface.

AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')


# e.g. EUR, CAD, GBP, CHF, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'COL'
USE_POINTS = True
POINTS_DECIMAL_PLACES = 1

# e.g. en-gb, de-de, it-it, fr-fr.
# see: https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'es'
#'en-us'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = []

# SENTRY_DSN = ''

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

# from here on are qualifications requirements for workers
# see description for requirements on Amazon Mechanical Turk website:
# http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_QualificationRequirementDataStructureArticle.html
# and also in docs for boto:
# https://boto.readthedocs.org/en/latest/ref/mturk.html?highlight=mturk#module-boto.mturk.qualification

mturk_hit_settings = {
    'keywords': ['easy', 'bonus', 'choice', 'study'],
    'title': 'Title for your experiment',
    'description': 'Description for your experiment',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7*24, # 7 days
    #'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    'qualification_requirements': [
        # qualification.LocaleRequirement("EqualTo", "US"),
        # qualification.PercentAssignmentsApprovedRequirement("GreaterThanOrEqualTo", 50),
        # qualification.NumberHitsApprovedRequirement("GreaterThanOrEqualTo", 5),
        # qualification.Requirement('YOUR_QUALIFICATION_ID_HERE', 'DoesNotExist')
    ]
}

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 200,
    'participation_fee': 5000,
    'num_bots': 12,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
}


SESSION_CONFIGS = [
        {
        'name': 'Instrucciones_3_grupos',
        'display_name': "Instrucciones (3 grupos)",
        'num_demo_participants': 2,
        'app_sequence': [
            'MLG_Intro'
        ],
    },
        {
        'name': 'Instrucciones_5_grupos',
        'display_name': "Instrucciones (5 grupos)",
        'num_demo_participants': 2,
        'app_sequence': [
            'MLG_Intro_5'
        ],
    },
        {
        'name': 'Instrucciones_Base_3_grupos',
        'display_name': "Instrucciones Base (3 grupos)",
        'num_demo_participants': 2,
        'app_sequence': [
            'MLG_Intro_T0'
        ],
    },
       {
        'name': 'Primera_Etapa_3_grupos',
        'display_name': "Primera_etapa (3 grupos)",
        'num_demo_participants': 12,
        'app_sequence': [
            'CPR_Game'
        ],
    },
       {
        'name': 'Primera_Etapa_5_grupos',
        'display_name': "Primera_etapa (5 grupos)",
        'num_demo_participants': 20,
        'app_sequence': [
            'CPR_Game_5'
        ],
    },
       {
        'name': 'Primera_Etapa_Base_3_grupos',
        'display_name': "Primera_etapa base (3 grupos)",
        'num_demo_participants': 12,
        'app_sequence': [
            'CPR_Game_T1'
        ],
    },
       {
        'name': 'Segunda_Etapa_Base_3_grupos',
        'display_name': "Segunda_etapa base (3 grupos)",
        'num_demo_participants': 12,
        'app_sequence': [
            'CPR_Game_T2'
        ],
    },
       {
        'name': 'Tercera_Etapa_Base_3_grupos',
        'display_name': "Tercera_etapa base (3 grupos)",
        'num_demo_participants': 12,
        'app_sequence': [
            'CPR_Game_T3'
        ],
    },
       {
        'name': 'Tercera_Etapa_3_grupos',
        'display_name': "Tercera_etapa (3 grupos)",
        'num_demo_participants': 12,
        'app_sequence': [
            'CPR_Game_II'
        ],
    },
       {
        'name': 'Tercera_Etapa_5_grupos',
        'display_name': "Tercera_etapa (5 grupos)",
        'num_demo_participants': 20,
        'app_sequence': [
            'CPR_Game_5_II'
        ],
    },
        {
        'name': 'Cambio_Regla_3_grupos',
        'display_name': "Cambio_regla (3 grupos)",
        'num_demo_participants': 2,
        'app_sequence': [
            'MLG_Change'
        ],
    },
        {
        'name': 'Cambio_Regla_5_grupos',
        'display_name': "Cambio_regla (5 grupos)",
        'num_demo_participants': 2,
        'app_sequence': [
            'MLG_Change_5'
        ],
    },
        {
        'name': 'Cambio_Regla_Base_3_grupos',
        'display_name': "Cambio regla Base (3 grupos)",
        'num_demo_participants': 2,
        'app_sequence': [
            'MLG_Change_T0'
        ],
    },
        {
        'name': 'Cambio_Regla_Base_3_grupos_II',
        'display_name': "Cambio regla Base II (3 grupos)",
        'num_demo_participants': 2,
        'app_sequence': [
            'MLG_Change_T0_II'
        ],
    },
        {
        'name': 'Cambio_Regla_3_5_grupos_II',
        'display_name': "Cambio_regla a tercer bloque",
        'num_demo_participants': 2,
        'app_sequence': [
            'MLG_Change_B'
        ],
    },
        {
        'name': 'Segunda_Etapa_3_grupos',
        'display_name': "Segunda_etapa (3 grupos)",
        'num_demo_participants': 12,
        'app_sequence': [
            'MLG_Game'
        ],
    },
        {
        'name': 'Segunda_Etapa_5_grupos',
        'display_name': "Segunda_etapa (5 grupos)",
        'num_demo_participants': 20,
        'app_sequence': [
            'MLG_Game_5'
        ],
    },
       {
        'name': 'Encuesta',
        'display_name': "Encuesta",
        'num_demo_participants': 1,
        'app_sequence': [
             'MLG_survey'
        ],
    },
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

SENTRY_DSN = 'http://7b6ef95ec90b4cddaf09ca55184f6ef1:e5fd539d433949fab29a6acc04fab93a@sentry.otree.org/13'

# anything you put after the below line will override
# oTree's default settings. Use with caution.
otree.settings.augment_settings(globals())

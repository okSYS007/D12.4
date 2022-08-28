
import logging, logging.config

DEBUG = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
        'warnFormat': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'
        },
        'errorFormat': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s'
        },
        'fileFormat': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'consoleWarn': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'warnFormat'
        },
        'consoleError': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'errorFormat'
        },
        'fileGeneral': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'NewsPaper/myapp/logging/general.log',
            'formatter': 'fileFormat'
        },
        'fileErrors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'NewsPaper/myapp/logging/errors.log',
            'formatter': 'errorFormat'
        },
        'fileSecurity': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'NewsPaper/myapp/logging/security.log',
            'formatter': 'fileFormat'
        },
    },
    'loggers': {
        'django': {
            'level': 'DEBUG',
            'handlers': ['console', 'consoleWarn', 'consoleError', 'fileGeneral', 'fileErrors', 'fileSecurity'],
            'propagate': True,
        },
        'django.request': {
            'level': 'DEBUG',
            'handlers': ['consoleError', 'fileErrors'],
            'propagate': False
        },
        'django.server': {
            'handlers': ['fileErrors'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.template': {
            'handlers': ['fileErrors'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.db_backends': {
            'handlers': ['fileErrors'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['fileSecurity'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}

logging.config.dictConfig(LOGGING)
logger = logging.getLogger('django')
logger.debug('debug log')
logger.info('info log')
logger.warning('warning log')
logger.error('error log')
logger.critical('critical log')
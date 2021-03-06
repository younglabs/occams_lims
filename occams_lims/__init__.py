from __future__ import unicode_literals
import logging
import pkg_resources

from pyramid.i18n import TranslationStringFactory
import wtforms_json; wtforms_json.init()  # monkey-patch wtforms to accept JSON data

from . import models

log = logging.getLogger('occams').getChild(__name__)

_ = TranslationStringFactory(__name__)

__prefix__ = '/lims'
__title__ = _(u'LIMS')
__version__ = pkg_resources.require(__name__)[0].version


def initdb(connectable):
    assert 'blame' in connectable.info, 'Need someone to blame!'
    models.LimsModel.metadata.create_all(connectable)


def includeme(config):

    config.registry.settings['occams.apps']['occams_lims'] = {
        'name': 'lims',
        'title': _(u'LIMS'),
        'package': 'occams_lims',
        'route': 'lims.index',
        'version': __version__
    }

    config.include('.assets')
    config.include('.routes')
    config.scan()

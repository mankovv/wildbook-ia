# -*- coding: utf-8 -*-
### __init__.py ###
# flake8: noqa
import logging
from wbia.expt import experiment_configs
from wbia.expt import experiment_drawing
from wbia.expt import test_result
from wbia.expt import harness
from wbia.expt import experiment_helpers
from wbia.expt import experiment_printres
import utool as ut

print, rrr, profile = ut.inject2(__name__, '[wbia.expt]')
logger = logging.getLogger('wbia')


def reassign_submodule_attributes(verbose=True):
    """
    why reloading all the modules doesnt do this I don't know
    """
    import sys

    if verbose and '--quiet' not in sys.argv:
        logger.info('dev reimport')
    # Self import
    import wbia.expt

    # Implicit reassignment.
    seen_ = set([])
    for tup in IMPORT_TUPLES:
        if len(tup) > 2 and tup[2]:
            continue  # dont import package names
        submodname, fromimports = tup[0:2]
        submod = getattr(wbia.expt, submodname)
        for attr in dir(submod):
            if attr.startswith('_'):
                continue
            if attr in seen_:
                # This just holds off bad behavior
                # but it does mimic normal util_import behavior
                # which is good
                continue
            seen_.add(attr)
            setattr(wbia.expt, attr, getattr(submod, attr))


def reload_subs(verbose=True):
    """Reloads wbia.expt and submodules"""
    rrr(verbose=verbose)

    def fbrrr(*args, **kwargs):
        """fallback reload"""
        pass

    getattr(experiment_configs, 'rrr', fbrrr)(verbose=verbose)
    getattr(harness, 'rrr', fbrrr)(verbose=verbose)
    getattr(experiment_helpers, 'rrr', fbrrr)(verbose=verbose)
    getattr(experiment_printres, 'rrr', fbrrr)(verbose=verbose)
    getattr(results_all, 'rrr', fbrrr)(verbose=verbose)
    getattr(results_analyzer, 'rrr', fbrrr)(verbose=verbose)
    getattr(results_organizer, 'rrr', fbrrr)(verbose=verbose)
    rrr(verbose=verbose)
    try:
        # hackish way of propogating up the new reloaded submodule attributes
        reassign_submodule_attributes(verbose=verbose)
    except Exception as ex:
        logger.info(ex)


rrrr = reload_subs

IMPORT_TUPLES = [
    ('experiment_configs', None),
    ('harness', None),
    ('experiment_helpers', None),
    ('experiment_printres', None),
    ('results_all', None),
    ('results_analyzer', None),
    ('results_organizer', None),
]
"""
Regen Command:
    cd /home/joncrall/code/wbia/wbia.expt
    makeinit.py
"""
# autogenerated __init__.py for: '/home/joncrall/code/wbia/wbia.expt'

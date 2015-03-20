#!/usr/bin/env python

import sys
from optparse import OptionParser

import django
from django.conf import settings

settings.configure()

if django.VERSION >= (1, 7):
    # New Apps loading mechanism
    django.setup()

from django_nose import NoseTestSuiteRunner


def runtests(*test_args, **kwargs):

    if not test_args:
        test_args = ['domain_name']

    test_runner = NoseTestSuiteRunner(**kwargs)

    failures = test_runner.run_tests(test_args)
    sys.exit(failures)

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('--verbosity', dest='verbosity', action='store',
                      default=1, type=int)
    parser.add_options(NoseTestSuiteRunner.options)
    (options, args) = parser.parse_args()

    runtests(*args, **options.__dict__)
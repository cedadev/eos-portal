#!/usr/bin/env python3

__author__ = "Matt Pryor"
__copyright__ = "Copyright 2020 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"

import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md")) as f:
    README = f.read()

if __name__ == "__main__":
    setup(
        name="jasmin-cloud",
        setup_requires=["setuptools_scm"],
        use_scm_version=True,
        description="API for management of tenancies in the JASMIN Cloud.",
        long_description=README,
        classifiers=[
            "Programming Language :: Python",
            "Framework :: Django",
            "Topic :: Internet :: WWW/HTTP",
            "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
        author="Matt Pryor",
        author_email="matt.pryor@stfc.ac.uk",
        url="https://github.com/cedadev/jasmin-cloud",
        keywords="web django jasmin cloud api",
        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,
        install_requires=[
            "docutils",
            "python-dateutil",
            "django",
            "djangorestframework",
            "django-settings-object",
            "jasmin-ldap",
            "pyyaml",
            "voluptuous",
            "requests",
            "rackit",
        ],
    )

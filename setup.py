# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from setuptools import setup, find_packages

import django_helpers

setup(
    name='django-helpers',
    version=django_helpers.__version__,
    packages=find_packages(),
    author='Nicolas RAMY',
    author_email='nicolas.ramy@darkelda.com',
    license='MIT',
    description='A set of context_processors, decorators, middlewares and others stuffs to develop quickly with Django',
    long_description=open('README.rst').read(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Django', ],
    url='https://github.com/nicolasramy/django-helpers',
    classifiers=[
        'Development Status :: 4 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7'
    ],
)

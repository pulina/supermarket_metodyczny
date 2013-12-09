#!/usr/bin/env python
# coding=utf-8
from setuptools import setup, find_packages

setup(
    name='Supermarket Metodyczny',
    version='0.1',
    description='Strona na której instruktorzy będą mogli zaczerpnąć wiedzę o pomysłach na realizację form dostosowanych do warunków harcerza',
    author="Szymon Kuliński",
    author_email="szymon.kulinski@zhr.pl",
    install_requires=(
        'django>=1.6,<1.7',
        'south',
        'django-admin-tools',
        'django-orderable',
        'django-js-reverse',
    ),
    packages=find_packages(),
    include_package_data=True,
)

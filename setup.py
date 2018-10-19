# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='classifier',
    version='1.0.0',
    description='Music classifier',
    long_description=readme,
    author='Alejandro Marrero',
    author_email='alemarrerodiaz@gmail.com',
    url='https://github.com/marreA/music_classifier',
    packages=find_packages(exclude=('tests', 'docs'))
)

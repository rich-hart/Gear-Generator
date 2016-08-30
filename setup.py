#!/usr/bin/env python

from setuptools import setup, find_packages

install_requires = ('dxfwrite','lxml')

setup(name='Gear_Generator',
      version='1.0',
      author='Richard Clark',
      url='https://github.com/richard-clark/Gear-Generator.git',
      packages=find_packages(),
      install_requires=install_requires,
      entry_points="""
     [console_scripts]
     gear_generator = gear:main
     """
     )


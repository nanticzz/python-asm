#!/usr/bin/env python
#This file is part of asm. The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.

import os
from setuptools import setup, find_packages
import asm


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='asm',
        version=asm.__version__,
        author='Zikzakmedia SL',
        author_email='zikzak@zikzakmedia.com',
        url="https://www.zikzakmedia.com",
        description="Python API ASM carrier",
        long_description=read('README'),
        download_url="https://bitbucket.org/zikzakmedia/python-asm",
        package_data={'asm': ['template/*']},
        packages=find_packages(),
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU Affero General Public License v3',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
            'Topic :: Software Development :: Libraries :: Python Modules',
            ],
        install_requires=[
            'genshi',
            ],
        license='GPL-3',
        extras_require={
        },
        # test_suite="asm.tests",
    )

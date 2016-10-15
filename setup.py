# -*- coding: utf8 -*-
"""
superestart.

~~~~~~~~~

A supervisord plugin used to autorestart program by specific time.
"""

from setuptools import setup

from superestart import __version__


setup(
    name="superestart",
    version=__version__,
    description="A supervisord plugin used to autorestart program by specific time",
    author="Wang Lei",
    author_email="fatelei@gmail.com",
    install_requires=[
        "supervisor==3.2.3",
        "croniter==0.3.12"
    ],
    packages=["superestart"],
    zip_safe=False,
    url="https://github.com/fatelei/superestart",
    entry_points={
        "console_scripts": [
            "superestart = superestart.main:main"
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries",
    ],
    license="BSD License"
)

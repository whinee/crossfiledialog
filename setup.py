#!/usr/bin/env python3

import sys
from distutils.core import setup

requirements: list[str] = []

if sys.platform == 'win32':
    requirements.append('pywin32')


description = 'A Python wrapper for opening files and folders with the native file dialog.'

try:
    long_description = open('README.md').read()
except:  # noqa: E722
    long_description = description



setup(
    name='crossfiledialog',
    version='0.2.0',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Maikel Wever',
    author_email='maikelwever@gmail.com',
    url='https://github.com/maikelwever/crossfiledialog/',
    packages=['crossfiledialog'],
    install_requires=requirements,
    python_requires='>=3.4',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Environment :: X11 Applications :: GTK',
        'Environment :: X11 Applications :: KDE',
        'Environment :: Win32 (MS Windows)',
        'Operating System :: OS Independent',
        'Operating System :: Microsoft',
        'Operating System :: POSIX :: Linux',
        'Topic :: Desktop Environment :: File Managers',
    ],
)

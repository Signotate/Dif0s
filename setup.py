import ez_setup
ez_setup.use_setuptools()


from setuptools import setup
from setuptools import find_packages
from signlangmtk.__about__ import *
import os


setup(
    name=__title__,
    description=__summary__,
    long_description=__long_summary__,
    version=__version__,
    packages=find_packages(),

    package_data={'signlangmtk.difos.gui':
                  ['*.ui', '*.css', '*.png', '*.ico']},
    include_package_data=True,

    author=__author__,
    author_email=__email__,
    license=__license__,

    entry_points={
        'gui_scripts': [
            'dif0s = signlangmtk.difos.__main__:main'
        ]
    },

    data_files=[
        ('share/applications', ['dif0s.desktop']),
        ('share/icons/hicolor/scalable/apps',
         ['signlangmtk/difos/gui/dif0s.svg'])
    ]
)

# setup.py

from setuptools import setup, find_packages

setup(
    name='zlibxjson',
    version='8.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'zlibxjson_command=zlibxjson.main:init',
        ],
    },
    author='Votre Nom',
    author_email='votre.email@example.com',
    description='Package ',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/votre_nom/votre_repository',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

from setuptools import setup, find_packages

setup(
    name='molecule_parser',
    url='https://github.com/mcrors/molecule_parser',
    author='Rory Houlihan',
    version=1.0,
    packages=find_packages(exclude=['*.tests', '*.tests.*', 'tests.*', 'unit_tests']),
    install_requires=[],
    setup_requires=['wheel'],
    extras_require={
        'dev': [
            'pytest',
            'pytest-pep8',
            'pytest-cov'
        ]
    }
)
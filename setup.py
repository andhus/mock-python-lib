from setuptools import setup, find_packages

VERSION = '0.0.1'

setup(
    name='mylib',
    version=VERSION,
    description=(
        'Mock python library for testing out travis and publishing to PyPI server.'
    ),
    url='https://github.com/andhus/mock-python-lib',
    license='',
    install_requires=[
        'flatdict>=3.0.0',  # random (lightweight) global PyPI lib.
    ],
    tests_require=['nose>=1.3.7'],
    extras_require={},
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]
    ),
)

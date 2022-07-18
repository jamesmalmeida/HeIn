from setuptools import setup, find_packages

setup(
    name='HeIn',
    version="0.0.1",
    url='https://github.com/jamesmalmeida/headerinjection',
    author='James Moraes de Almeida',
    author_email='james@almeida.page',

    packages = find_packages(),
    install_requires=[
        'fastapi',
        'requests',
        ],
)

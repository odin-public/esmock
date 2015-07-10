import os
from setuptools import setup, find_packages


os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='esmock',
    author='spukst3r',
    version='0.1',
    description='ElasticSearch mock server',
    url='https://github.com/spukst3r/esmock',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask==0.10.1',
        'Werkzeug==0.10.4',
        'Flask-Cors==2.0.1'
    ]
)

from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='SwarmPackagePy',
    version='0.7.2',
    author='SISDevelop',
    author_email='swarm.team.dev@gmail.com',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
)

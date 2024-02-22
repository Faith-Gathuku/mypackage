from setuptools import setup,find_packages

setup(name='my package',
    version='0.1',
    packages=find_packages(exclude=['test*']),
    license='MIT',
    descripion='EDA example python package',
    long_description=open('readme.md').read(),
    install_requires =['numpy'],
    url ="",
    author='faith',
    author_email='nyawiragathuku4@gmail.com')
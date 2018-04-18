from setuptools import setup


setup(
    name='dbshell',
    version='0.1',
    url='https://github.com/chosak/dbshell',
    license='MIT',
    author='Andy Chosak',
    author_email='andy@chosak.org',
    description='Standalone Django dbshell powered by database URLs',
    install_requires=[
        'Django',
        'dj-database-url',
    ],
    scripts=['dbshell']
)

from setuptools import setup, find_packages

setup(
    name='tomacco',
    version='0.4.3',
    author='axce1',
    author_email='axce1.github@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    description='Pomodoro Technique time',
    long_description='The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s',
    platforms='Linux',
    url='http://github.com/axce1/tomacco',
    license='WTFPL',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    entry_points={
        'console_scripts':
            ['tomacco=tomacco.main:main',
             'tomacco_cli=tomacco.tomacco_cli:main']
    }
)

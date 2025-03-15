from setuptools import setup, find_packages

setup(
    name='learnsaxs',
    version='0.0.4',
    license='MIT',
    author="Masatsuyo Takahashi",
    author_email='freesemt@gmail.com',
    packages=find_packages(),
    url='https://github.com/freesemt/learnsaxs',
    keywords='learn saxs',
    install_requires=[
          'numpy',
          'matplotlib',
      ],

)

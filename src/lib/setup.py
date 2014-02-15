from distutils.core import setup

setup(name='pbf.kao.nytowl',
      version='.1',
      description="Programmer's Best Friend Utility Extension for Nytowl",
      author='Chris Loew',
      author_email='cloew123@gmail.com',
      packages=['pbf.kao.nytowl', 'pbf.kao.nytowl.Commands', 'pbf.kao.nytowl.templates'],
      package_data = {'pbf.kao.nytowl.templates':['*']},
     )
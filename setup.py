from setuptools import setup


setup(name='enron_reader',
      version='0.21',
      description='This package makes reading emails from Enron dataset easy.',
      url='http://github.com/sparik/enron_reader',
      author='Sparik Hayrapetyan',
      author_email='sparikhayrapetyan@gmail.com',
      license='MIT',
      packages=['enron_reader'],
      include_package_data=True,
      zip_safe=False,
      scripts=['scripts/download_enron'])
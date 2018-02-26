from setuptools import setup

with open("README.rst", "r") as f:
      long_descr = f.read()

setup(name='enron_reader',
      version='0.25',
      description='This package makes reading emails from Enron dataset easy.',
      long_description=long_descr,
      url='https://github.com/zerocogtech/enron_reader',
      author='Sparik Hayrapetyan',
      author_email='sparikhayrapetyan@gmail.com',
      license='MIT',
      packages=['enron_reader'],
      include_package_data=True,
      zip_safe=False,
      scripts=['scripts/download_enron'])
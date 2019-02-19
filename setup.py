from setuptools import setup

setup(name='abs_data',
      version='0.1',
      description='Access to ABS data and correspondencies',
      url='https://github.com/varunsatish/ABS_Package',
      author='Varun Satish',
      author_email='varun.satish96@gmail.com',
      license='MIT',
      packages=setuptools.find_packages(),
      install_requires=[
          'pandas',
          'sqlalchemy',
          'sqlalchemy.orm'
      ],
      zip_safe=False)
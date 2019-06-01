from setuptools import setup, find_packages

setup(
    	name='lib-square-cipher',
	version = '3.0',
	author='Karolina Kosiorowska',
	author_email='228382@student.pwr.edu.pl',
	url='https://github.com/kkosiorowska/lib-square-cipher',
    	description='An example python package',
    	long_description=open('README.md').read(),
    	#packages=find_packages()
	packages=['cryptography', 'data']
)

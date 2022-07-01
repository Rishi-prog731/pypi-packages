from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='trying_python',
  version='0.0.1',
  description='Python module that teaches the basics of Python',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',
  author='Rishi Hariharaprasad',
  author_email='rishi.hhp@gmail.com',
  license='MIT',
  classifiers=classifiers,
  keywords='starter',
  packages=find_packages(),
  install_requires=['']
)

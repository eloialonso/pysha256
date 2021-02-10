from setuptools import setup

setup(name='pysha256',
      version='0.1',
      description='SHA256 implementation in Python. Built for my personal understanding : neither bullet-proof nor efficient.',
      url='http://github.com/bloodymosquito/pysha256',
      author='Eloi',
      author_email='',
      license='MIT',
      packages=['pysha256'],
      entry_points={
        'console_scripts': ['pysha256=pysha256.command_line:main'],
      },
      )

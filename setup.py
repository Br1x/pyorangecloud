from setuptools import setup

setup(name='pyorangecloud',
      version='1.0',
      py_modules=['pyorangecloud'],
      url='https://github.com/Orange-OpenSource/pyorangecloud',
      classifiers=[
          "Programming Language :: Python",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 2.7",
          "Topic :: Communications",
      ],
      install_requires=[requirement.rstrip(' \r\n') for requirement in open('requirements.txt').readlines()],
      )

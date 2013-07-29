from distutils.core import setup

setup(name='amiwrapper',
      version='0.1',
      description='Base class to be used for clientAsterisk/AMI applications.',
      author='Marcos Lopez',
      license='MIT',
      py_modules=['amiwrapper.amiwrapper'],
      #packages=['amiwrapper'],
      #package_dir={'amiwrapper': 'amiwrapper'},
      #include_package_data=True,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Terminals'
          ]
      )

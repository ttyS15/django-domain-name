from setuptools import setup

setup(name='django-domain-name',
      version='0.0.1',
      packages=['domain_name'],
      url='https://github.com/ttyS15/django-domain-name',
      license='Public',
      author='axeman',
      author_email='ttyS15@yandex.ru',
      description='Django models fields with some magical properties',
      setup_requires=[
          'nose>=1.0',
      ],
      tests_require=[
          'django >=1.3',
          'django-nose',
      ],
      test_suite='domain_name.tests',
      include_package_data=True,
      classifiers=[
          'Framework :: Django',
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 2.7',
      ],
)

from setuptools import setup, find_packages


setup(
    name='API',
    version='0.1.0',
    author='Devinzon, Freddy',
    author_email='test@test.com',
    packages=[
        'api/',
        'app/',
        'core/'
    ],
    url='http://pypi.python.org/',
    license=None,
    description='Backend api',
    long_description=open('README.md').read(),
    install_requires=[
        'asgiref==3.4.1',
        'Django==3.2.8',
        'django-filter==21.1',
        'djangorestframework==3.12.4',
        'Markdown==3.3.4',
        'pytz==2021.3',
        'sqlparse==0.4.2'
    ],
)

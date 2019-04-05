import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# Package dependencies
install_requires = [
    'wagtail>=1.5',
    'wagtailfontawesome',
]

# Testing dependencies
testing_extras = [
]

# Documentation dependencies
documentation_extras = [
]

setup(
    name='wagtail_blocks',
    version='0.5.2',
    packages=['wagtail_blocks'],
    include_package_data=True,
    license='MIT',
    description='A Collection of awesome Wagtail CMS stream-field blocks',
    long_description=README,
    url='https://github.com/ibrahimawadhamid/wagtail_blocks/',
    author='IbrahimAwadHamid',
    author_email='ibrahim.a.hamid@gmail.com',
    download_url = 'https://github.com/ibrahimawadhamid/wagtail_blocks/archive/V0.5.2.tar.gz',
    keywords = ['WAGTAIL', 'STREAMFIELD', 'WAGTAIL_BLOCKS', 'WAGTAIL CMS'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
    ],
    install_requires=install_requires,
    extras_require={
        'testing': testing_extras,
        'docs': documentation_extras
    },
)
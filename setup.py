import os
from setuptools import setup, find_packages

try:
    from pip._internal.req import parse_requirements
    from pip._internal.download import PipSession
except ImportError:
    from pip.req import parse_requirements
    from pip.download import PipSession

CURRENT_FILE_PATH = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE_PATH)
session = PipSession()
with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# Package dependencies
install_reqs = parse_requirements(
    os.path.join(CURRENT_DIR, "requirements.txt"), session=session)
reqs = [str(ir.req) for ir in install_reqs]

# Testing dependencies
testing_extras = [
]

# Documentation dependencies
documentation_extras = [
]

setup(
    name='wagtail_blocks',
    version=__import__('wagtail_blocks').__version__,
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='A Collection of awesome Wagtail CMS stream-field blocks and Charts',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/ibrahimawadhamid/wagtail_blocks/',
    author='IbrahimAwadHamid',
    author_email='ibrahim.a.hamid@gmail.com',
    keywords=['WAGTAIL', 'STREAMFIELD', 'WAGTAIL_BLOCKS', 'WAGTAIL CMS'],
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
    install_requires=reqs,
    extras_require={
        'testing': testing_extras,
        'docs': documentation_extras
    },
)

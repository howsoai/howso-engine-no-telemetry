import codecs
import os

from setuptools import find_namespace_packages, setup


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    name='howso-engine-no-telemetry',
    version=get_version("howso/resources/no-telemetry/version.txt"),
    description='A setuptools "extra" for the Howso Engine™.',
    long_description="""# Howso\n\n""",
    long_description_content_type='text/markdown',
    author='Howso Incorporated',
    author_email='support@howso.com',
    license='GNU Affero General Public License v3',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python :: 3'
    ],
    keywords='machine learning artificial intelligence',
    python_requires='>=3.8',
    url='',
    packages=find_namespace_packages(include=['howso.*']),
    include_package_data=True,
)

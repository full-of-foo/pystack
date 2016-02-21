from setuptools import find_packages, setup

VERSION = '1.0.0'


def read_file(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines()]


def get_version():
    import os
    build_num = os.environ.get('CIRCLE_BUILD_NUM')
    if not build_num:
        return VERSION
    return '{}.{}'.format(VERSION, build_num)

setup(
    name='pystack',
    version=get_version(),
    packages=find_packages(),
    include_package_data=True,
)

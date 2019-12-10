import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name='bitterdispute',
    version='1.1',
    author='Harvard CS207 Team 31',
    author_email='wseaton@g.harvard.edu',
    description='A step-by-step Automatic Differentiation package',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/207-of-diamonds/cs207-FinalProject',
    packages=find_packages(exclude=['tests', 'test*']),
    include_package_data=True,
    install_requires=['numpy', 'pytest', 'pytest-mock'],
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

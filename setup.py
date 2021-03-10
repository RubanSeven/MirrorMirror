# -*- coding:utf-8 -*-
"""
@author: RubanSeven
@project: MirrorMirror
"""
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="MirrorMirror",
    version="0.1.0",
    author="Hejun Zhu",
    author_email="zhuhejun2019@gmail.com",
    description="Easy to Image Augment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache",
    zip_safe=False,
    url="https://github.com/RubanSeven/MirrorMirror",
    install_requires=[
        "imgaug==0.4.0",
        "PyQt5==5.15.1"
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Indexing",
        "Topic :: Utilities",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    # packages=['MirrorMirror'],
    packages=find_packages(),
    include_package_data=True
)

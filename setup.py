from setuptools import setup,find_packages

setup(
name="wallpaperpy",
version='1.0',
author="Isaac Atia",
author_email="atiaisaac007@gmail.com",
description="Autochanging desktop wallpaper",
long_description="Change the background image automatically from \
any folder of images of your choice",
packages=find_packages(),
classifiers=[
"Development Status::3-Alpha",
"Intended Audience::Developers",
"Programming Language::Python::2.7",
"Programming Language::Python::3.5",
"License::OSI Approved::MIT License"
],
license='MIT',
entry_points={'console_scripts':['wallpaperpy=wallpaperpy.run:main' ]},
install_requires=['setuptools',]
)

from setuptools import setup, find_packages

VERSION = '0.1.2'
DESCRIPTION = 'Open Redirect Bug Finding Tool'
LONG_DESCRIPTION = 'Open Redirect Bug Finding Tool. This tool is designed to detect Open Redirect vulnerabilities.'

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="openredirectscanner",
    version=VERSION,
    author="Snega Prabhavathi",
    author_email="prabhavathisnega@gmail.com",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(include=['units', 'packages.includes']),
    entry_points={
        'console_scripts': [
            'openredirectscanner=main:main',  
        ],
    },
    install_requires=[
        'requests>=2.25.1',
        'argparse>=1.4.0',
        'termcolor>=1.1.0',
        'pyfiglet>=0.8.post1'
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)

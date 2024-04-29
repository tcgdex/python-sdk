from setuptools import find_packages
from setuptools import setup

setup(
    name="tcgdexsdk",
    version="1.0.1",
    packages=find_packages(),
    author="HellLord77",
    author_email="ratul.debnath.year@gmail.com",
    url="https://github.com/HellLord77/tcgdex-python-sdk",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    python_requires=">=3.11",
    install_requires=[
        "dacite",
    ],
    extras_require={
        "test": [
            "vcrpy",
        ]
    },
)

from setuptools import find_packages,setup


setup(
    name="sensor-fault-detection",
    version="0.0.1",
    author="Dikshant Gupta",
    author_email="guptadikshant99@gmail.com",
    packages=find_packages(),
    install_requires=["pymongo==4.2.0"]
)


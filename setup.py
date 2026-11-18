from setuptools import setup, find_packages

setup(
    name="it_inventory",
    version="1.0.0",
    description="Back-end for IT equipment inventory (Lab 4, variant 47)",
    packages=find_packages(),
    install_requires=[
        "Flask",
        "Flask-SQLAlchemy",
        "PyMySQL",
        "PyYAML",
        "cryptography",
    ],
)

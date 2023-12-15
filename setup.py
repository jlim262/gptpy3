from setuptools import setup, find_packages

setup(
    name="gptpy3",
    version="0.2",
    packages=find_packages(),
    install_requires=[
        # list your package dependencies
        'openai>=1.3.8'
    ],
    # Additional metadata about your package
)

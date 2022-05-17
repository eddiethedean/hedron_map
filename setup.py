
import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="hedron_map",
    version="0.0.0",
    description="Python package for mapping coordinates and clusters of coordinates.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/eddiethedean/hedron_map",
    author="Odos Matthews",
    author_email="odosmatthews@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.9',
    install_requires=['PyGeodesy==21.6.9', 'py-staticmaps==0.4.0']
)
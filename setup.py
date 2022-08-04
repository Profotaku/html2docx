from os import path

from setuptools import setup, find_packages

with open(path.join(path.abspath(path.dirname(__file__)), "README.md"), encoding="utf-8") as f:
    readme_description = f.read()


def read_requirements(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        return fp.read().strip().splitlines()


setup(
    name="htmldocx",
    packages=find_packages(),
    version="0.0.6 (QuillJs)",
    license="MIT License",
    description="A html to docx converter witch conserves the formatting (style, margin, padding) of the html.",
    author="pqzx",
    url="https://github.com/pqzx/html2docx",
    download_url="https://github.com/pqzx/html2docx/archive/refs/tags/v0.0.6.tar.gz",
    keywords=[
        "python",
        "convert",
        "html",
        "word",
        "office",
        "docx",
        "html",
        "QilLJs",
        "style",
        "js",
        "WYSIWYG",
        "conversion",
    ],
    install_requires=read_requirements("requirements.txt"),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    long_description=readme_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    python_requires=">=3.2, <4",
    entry_points={"console_scripts": ["htmldocx = htmldocx.__init__"]},
)

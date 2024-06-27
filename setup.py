import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    include_package_data=True,
    name='abc_xml_converter',
    version='1.0.1',
    author='Sebastian Oliver Eck',
    url="https://github.com/sebastian-eck/abc_xml_converter",
    description='ABC-XML Converter',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GNU Lesser General Public License",
    packages=setuptools.find_packages(),

    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Unix",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
    ],
    install_requires=[
        "setuptools~=69.5.1",
        "pyparsing~=3.1.1"
    ]
)
import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="excalibur", # Replace with your own username
    version="0.1.2",
    author="Ryan MacDonald, Arnav Agrawal",
    author_email="rmacdonald@astro.cornell.edu, aa687@cornell.edu",
    description="A python package to calculate atomic and molecular cross sections for exoplanet atmospheres.",

    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arnav-agrawal/excalibur-alpha",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7.6',
    install_requires = ['numpy',
                        'scipy',
                        'matplotlib',
                        'h5py',
                        'numba>=0.56',
                        'requests',
                        'bs4',
                        'tqdm',
                        'pandas',
                        'lxml'],
    zip_safe=False
)

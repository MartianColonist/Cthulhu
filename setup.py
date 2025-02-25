from setuptools import setup, find_packages
import os

setup(
    name = "Cthulhu", # Replace with your own username
    version = "1.0.0",
    description = "A python package to calculate atomic and molecular cross sections for substellar atmospheres.",
    long_description = open(os.path.join(
                            os.path.dirname(__file__), 'README.rst')).read(),
    long_description_content_type = 'text/x-rst',
    author = "Ryan MacDonald, Arnav Agrawal",
    author_email = "ryanjmac@umich.edu, aa687@cornell.edu",
    license = 'BSD 3-Clause License',
    packages = ['Cthulhu'],
    include_package_data = True,
    python_requires = '>=3.7.6',
    install_requires = ['numpy',
                        'scipy',
                        'matplotlib',
                        'h5py',
                        'numba>=0.56',
                        'requests',
                        'bs4',
                        'tqdm',
                        'pandas',
                        'lxml',
                        'hitran-api',
                        'pytest',
                        'jupyter'],
    zip_safe = False,
)

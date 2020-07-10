from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

description = 'Module for parsing binary data recieved from "ACP Feed".'

setup(
    name='acp_parser',
    version='0.1b1',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/golgor/acp_parser',
    author='Robert Nyström',
    author_email='golgafrincham@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='binary, parse, parsing',
    packages=find_packages(),
    python_requires='>=3.6, <4',
    # install_requires=[],
    # extras_require={},
    # package_data={},
    # data_files=[],
    entry_points={
        'console_scripts': ['ps_signal = acp_parser.__main__:main']
    },
)

from setuptools import setup, find_packages


setup(
    name='sbe_library',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'scapy' # for pcap files
    ],
    description='A library for working with Simple Binary Encoding (SBE)',
    author='Pedro Serrano Faria',
    author_email='pedroserrano2@gmail.com',
    url='github.com/pedrosfaria2/sbe_library',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

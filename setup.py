"""Setup file for CryptoRaid package."""
from setuptools import setup, find_packages

with open('README_ENHANCED.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cryptoraid',
    version='1.0.0',
    description='Production-ready cryptocurrency trading bot',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='CryptoRaid Contributors',
    url='https://github.com/karandeep2799-source/cryptoraid',
    packages=find_packages(),
    python_requires='>=3.9',
    install_requires=[
        'requests>=2.28.0',
        'art>=5.8',
        'pandas>=1.5.0',
        'numpy>=1.23.0',
    ],
    entry_points={
        'console_scripts': [
            'cryptoraid=main_enhanced:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Office/Business :: Financial :: Investment',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)

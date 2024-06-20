from setuptools import setup, find_packages

setup(
    name='WHAlpha191',
    version='0.1',
    packages=find_packages(),
    description='GTJA Alpha 191',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='wh',
    author_email='wendyhanmath@gmail.com',
    url='https://github.com/wendihan/Alpha-101-GTJA-191',
    install_requires=[
        "numpy",
        "pandas",
    ],
    classifiers=[
        # Choose your license as you wish
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)

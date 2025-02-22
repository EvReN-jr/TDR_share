from setuptools import setup, find_packages

setup(
    name='TopDR',
    version='0.1.0',
    description='Topological Dimension Reduction',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='BOYABATLI, Kenan Evren; YİĞT, Uğur',
    author_email='kbybtli@gmail.com; ugur.yigit@medeniyet.edu.tr',
    url='https://github.com/EvReN-jr/TDR_share',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

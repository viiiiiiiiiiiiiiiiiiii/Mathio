from setuptools import setup, find_packages

setup(
    name='Mathio',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pytest',
    ],
    description='A comprehensive mathematical library',
    long_description=open('README.md').read(),
    long_description_content_type='markdown',
    author='Vi',
    author_email='kunykunykuny6@gmail.com',
    url='https://github.com/viiiiiiiiiiiiiiiiiiii/Mathio',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

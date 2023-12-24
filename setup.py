from setuptools import setup, find_packages

setup(
    name='jewels_game',
    version='1.0',
    author='Clara Battesini',
    author_email='clarabattesini@gmail.com',
    description='A short description of your project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/clarabatt/jewels_game',
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.6',
)

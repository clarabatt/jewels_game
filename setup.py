from setuptools import setup, find_packages

setup(
    name='jewels_game',
    version='1.0',
    author='Clara Battesini',
    author_email='clarabattesini@gmail.com',
    description='A short description of your project',  # Short description
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/clarabatt/jewels_game',
    packages=find_packages(),
    include_package_data=True,
    # install_requires=[
    #     # List your project's dependencies here
    #     # e.g., 'requests>=2.25.1',
    #     # Ensure these are listed in your requirements.txt as well
    # ],
    # classifiers=[
    #     # Specify which Python versions you support
    #     'Programming Language :: Python :: 3',
    #     'License :: OSI Approved :: MIT License',  # Your project's license
    #     'Operating System :: OS Independent',
    # ],
    python_requires='>=3.6',
    # entry_points={
    #     'console_scripts': [
    #         # If you have any scripts you want to be installed as executables, list them here
    #         # e.g., 'your_script=your_project.scripts.your_script:main',
    #     ],
    # },
)

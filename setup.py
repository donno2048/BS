from setuptools import setup, find_packages
setup(
    name='backboard',
    version='1.0.5',
    description='Background noises for your keyboard typing',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/donno2048/BS',
    packages=find_packages(),
    license='MIT',
    author='Elisha Hollander',
    classifiers=['Programming Language :: Python :: 3'],
    install_requires=['pygame>=1.9.6','keyboard>=0.13.5','numpy>=1.20.3','scipy>=1.6.3'],
    entry_points={ 'console_scripts': [ 'backboard=backboard.__main__:main' ] }
)

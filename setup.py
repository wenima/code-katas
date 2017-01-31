from setuptools import setup

setup(
    name='code-katas',
    description="A selection of code katas from www.codwars.com.",
    version=0.9,
    author='Marc Kessler-Wenicker',
    author_email='marc.kesslerwenicker@gmail.com',
    license='MIT',
    package_dir={'root': 'src'},
    py_modules=['parenthesis'],
    install_requires =['ujson'],
    extras_require={
        'test': ['pytest', 'pytest-cov', 'pytest-watch', 'tox']
    },
    entry_points={
    }
)

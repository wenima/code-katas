from setuptools import setup

setup(
    name='parenthetics.py',
    description="A module to parse an input string of parenthesis.",
    version=0.9,
    author='Marc Kessler-Wenicker',
    author_email='marc.kesslerwenicker@gmail.com',
    license='MIT',
    package_dir={'root': 'src'},
    py_modules=['parenthesis'],
    install_requires =[],
    extras_require={
        'test': ['pytest', 'pytest-cov', 'pytest-watch', 'tox']
    },
    entry_points={
    }
)

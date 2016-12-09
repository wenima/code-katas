from setuptools import setup

setup(
    name='mailroom.py',
    description="A program to deal with mailroom madness.",
    version=0.1,
    author='Marc Kessler-Wenicker',
    author_email='marc.kesslerwenicker@gmail.com',
    license='MIT',
    package_dir={'root': 'src'},
    py_modules=['mailroom'],
    install_requires =[],
    extras_require={
        'test': ['pytest', 'pytest-cov', 'pytest-watch', 'tox']
    },
    entry_points={
        'console_sripts': [
            'mailroom = mailroom:mailroom'
        ]
    }
)

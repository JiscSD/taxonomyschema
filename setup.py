from setuptools import setup

setup(
    name='taxonomyschema',
    version='0.1.0',
    description='Updates the taxonomy service with schemas in repository.',
    url='https://github.com/JiscRDSS/taxonomyschema',
    install_requires=[
        "jsonschema==2.6.0",
        "requests==2.13.0"
    ],
    tests_require=[
        'pytest',
        'pytest-helpers-namespace',
        'pre-commit',
        'responses',
        'pep8',
        'autopep8'
    ],
    license='Apache',
    author='Andrew Griffiths',
    packages=['taxonomyschema'],
    entry_points={
        'console_scripts': [
            'taxonomyschema = taxonomyschema.taxonomyschema:main'
        ]
    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ],
)

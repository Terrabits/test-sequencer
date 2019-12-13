from setuptools import find_packages, setup

setup(
    name='test-sequencer',
    version='0.1.0',
    description='Test sequencer for use with Automated Test Equipment (ATE)',
    long_description=open('README.md').read().strip(),
    author='Nick Lalic',
    author_email='nick.lalic@gmail.com',
    url='http://path-to-my-packagename',
    py_modules=['test_sequencer'],
    packages=find_packages(exclude=['test']),
    package_data={'': ['*.yaml']},
    include_package_data=True,
    install_requires=[],
    extras_require={
    'dev':  [],
    'test': []
    },
    license='MIT License',
    zip_safe=False,
    keywords='RF test instrument equipment ATE',
    classifiers=['Packages', 'RF'],
    entry_points= {
        'console_scripts': []
    }
)

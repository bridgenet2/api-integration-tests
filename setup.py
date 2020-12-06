from setuptools import find_packages, setup

install_dependencies = ['requests>=2.23.0']
test_dependencies = []


setup(
    name='pronym-api-integration-tests',
    url='https://github.com/pronym-inc/pronym-api-integration-tests',
    author='Pronym',
    author_email='gregg@pronym.com',
    entry_points={},
    packages=find_packages(),
    install_requires=install_dependencies,
    tests_require=test_dependencies,
    extras_require={'test': test_dependencies},
    include_package_data=True,
    version='0.1',
    license='MIT',
    description=('Some helpful description'),
    long_description=open('README.md').read(),
)

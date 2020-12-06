from setuptools import setup, find_packages

setup(
    name='PanChemist',
    version='0.0.1',
    packages=find_packages(include=['PanChemist', 'PanChemist.*']),
    install_requires=[
        "attrs>=20.3.0",
        "certifi>=2020.12.5",
        "click>=7.1.2",
        "click-plugins>=1.1.1",
        "cligj>=0.7.1",
        "Fiona>=1.8.18",
        "geopandas>=0.8.1",
        "munch>=2.5.0",
        "mysql-connector-python>=8.0.22",
        "numpy>=1.19.4",
        "pandas>=1.1.4",
        "protobuf>=3.14.0",
        "psycopg2-binary>=2.8.6",
        "pyproj>=3.0.0.post1",
        "python-dateutil>=2.8.1",
        "pytz>=2020.4",
        "Shapely>=1.7.1",
        "six>=1.15.0",
        "spatialite>=0.0.3",
    ],
    url='https://github.com/christophertubbs/PanChemist',
    license='GPL 3.0',
    author='Christopher Tubbs',
    author_email='',
    description='Pandas-Database integration without SQLAlchemy'
)

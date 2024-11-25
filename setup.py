from setuptools import setup, find_packages

setup(
    name='marsapi',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[  
        'geojson',
        'pandas',
        'geopandas',
        'folium',        
    ],
    test_suite='tests',
    tests_require=['pytest'],
    description='Methane Data API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Manuel Montesino San Martin',
    author_email='mmontesinosanmartin@gmail.com',
    url='https://github.com/montesinoman/MARSAPI',
    license='MIT',
)
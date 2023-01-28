import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='hdf5-indexer',
                 packages=['hdf5_indexer'],
                 version='0.1.0',
                 description='Creates an index of container -> file offset of HDF5 files.',
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 license='MIT',
                 author='Jim Robinson',
                 url='https://github.com/igvteam/igv-reports',
                 keywords=['igv', 'bioinformatics', 'genomics', 'visualization', 'variant' ],
                 classifiers=[
                     'License :: OSI Approved :: MIT License',
                     'Topic :: Scientific/Engineering :: Bio-Informatics :: HDF5'
                 ],
                 install_requires=[
                     'pyfive==0.3.0', 'h5py', 'numpy'
                 ],
                 entry_points={
                     'console_scripts': [
                         'h5index=hdf5_indexer.index:main',
                         'h5extract-index=hdf5_indexer.extract_index:main'
                     ],
                 },
                 package_data={'hdf5_indexer': ['templates/*']},
                 )

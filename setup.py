import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='hdf5-indexer',
                 packages=['hdf5_indexer'],
                 version='0.5.0',
                 description='Annotates an HDF5 file with an index of container pathname -> file offset.',
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 license='MIT',
                 author='Jim Robinson',
                 url='https://github.com/igvteam/hdf5-indexer',
                 keywords=['HDF5'],
                 classifiers=[
                     'License :: OSI Approved :: MIT License',
                     'Topic :: Scientific/Engineering ::  HDF5'
                 ],
                 install_requires=[
                    'pyfive', 'h5py', 'numpy'
                 ],
                 dependency_links=["git+https://github.com/jjhelmus/pyfive.git@master#egg=pyfive"],
                 entry_points={
                     'console_scripts': [
                         'h5index=hdf5_indexer.index:main',
                         'h5extract=hdf5_indexer.extract_index:main',
                         'h5extract-offset=hdf5_indexer.extract_offset:main',
                         'h5update-offset=hdf5_indexer.update_offset:main'
                     ],
                 }
                 )

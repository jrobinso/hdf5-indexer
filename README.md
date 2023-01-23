# hdf5-indexer

Project for creating index mapping hdf5 object names -> file offsets.  These indexes can be used with
[hdf5-indexed-reader](https://github.com/jrobinso/hdf5-indexed-reader), built on [jsfive](https://github.com/usnistgov/jsfive) with the help of @bmaranville, for efficient remote URL access.

## Requirements

* pyfive==0.3.0
* certifi

## Usage

```python

python h5_indexer.indexer.py(path, output)

```

where 'path' is  the input hdf5 file path or URL, and 'output' is the file path for the created index.




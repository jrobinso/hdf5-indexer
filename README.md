# hdf5-indexer

Project for creating index mapping hdf5 object names -> file offsets.  These indexes can be used with
[hdf5-indexed-reader](https://github.com/jrobinso/hdf5-indexed-reader), an extension  
of [jsfive](https://github.com/usnistgov/jsfive), for efficient remote URL access.

## Requirements

* pyfive==0.3.0

## Usage

```python

python hdf5_indexer/indexer.py path output

```

where 'path' is  the input hdf5 file path and 'output' is the file path for the created index.





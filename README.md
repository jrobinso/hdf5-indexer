# hdf5-indexer

Tool for annotating HDF5 files with an index  mapping container paths to file offsets.   The index can be used by 
readers, such as [hdf5-indexed-reader](https://github.com/jrobinso/hdf5-indexed-reader), to directly access individual 
containers without first walking the linked list of ancestor and sibling nodes to find the container's file offset. 
The  driving use case is web based access to individual datasets from large HDF5 files (100s of GB) containing
thousands of individual datasets.  

## Limitations

The project is designed for large HDF5 files containing many datasets.  Performance will not likely be improved
for small HDF5 files  (< 100 MB) which can be read in their entirety.

The indexer is built on [pyfive](https://github.com/jjhelmus/pyfive), and the associated reader is 
built on [jsfive](https://github.com/usnistgov/jsfive), so limitations of those projects apply.  


## Installation

**Tested with Python 3.8**

```
pip install git+https://github.com/jrobinso/hdf5-indexer.git
```


## Command Line Usage

### h5index

Index an hdf5 file.  By default this utility will build an index, gzip it, and at it to the hdf5 as a top-level
dataset named "_index".   If the "_index" dataset exists it is overwitten.

```commandline
h5index inputfile <options>
```

**Arguments:**

* Required
    * __inputfile__   The hdf5 file to index
 
* Optional
    * __-o --outfile__ .  Output file path.  If provided, index json will be output to the specified file.  
    * __-n --noappend__ .  Flag - do not append index to hdf5 file.  This is not common.


## Programmatic usage

```python
import hdf5_indexer
hdf5_indexer.make_index('spleen_1chr1rep.cndb')
```

## Example

**Note: Requires python 3.8**

```commandline

wget https://www.dropbox.com/s/7hmj25az1vgaejf/spleen_1chr1rep.cndb?dl=0 -O spleen_1chr1rep.cndb
pip install git+https://github.com/jrobinso/hdf5-indexer.git
h5index spleen_1chr1rep.cndb

```

## Example notebook

An example notebook illustrating basic usage is available in [Colab](https://colab.research.google.com/drive/1zZwt8U8mYgAo3ewWZvF6CIpjL1OENNoO?usp=sharing)


## Utilities

The command line utilities below are used for test and development. 


### h5extract

To verify creation of the index use the h5extract utility.  This will extract the "_index" dataset, gunzip it, and 
print the json to stdout.  

```commandline
h5extract hdf5file
```
**Arguments:**

* Required
  * __hdf5file__   The hdf5 file to extract index from

### h5update-offset

Used to add an attribute to the root object containing the file offset to the index Dataset.   Files with this attribute can load faster as the index can be loaded directly and used, rather than searched for.   This is  only neccessary for files indexed prior to release 0.1.1. 

```commandline
h5extract h5update-offset hdf5file
```
**Arguments:**

* Required
  * __hdf5file__   The hdf5 file







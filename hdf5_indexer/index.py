import pyfive
import h5py
import argparse
import json
import numpy
import gzip


def make_index(path, outfile=None, dset_name='_index', append=True):

    '''
    Create an index mapping h5 object names -> file offset positions.  By default compressed json for the  will be inserted into
    the h5 file as a top level dataset named "_index" as compressed json.  Optionally the index json can be dumped
    to an output file.

    :param path: File path to the h5 file
    :param append: Append the index to the h5 file as a dataset.  Defaults to True
    :param dset_name: Index dataset name.  Optional, defaults to "_index".  Do not change this without good reason as reader clients might not recognize a different name
    :param outfile: Optional file path for output json
    '''

    # Walk nodes and create index.  The pyfive library is used as it gives us access to the nodes file offset.
    f = None
    try:
        f = pyfive.File(path)
        index = {}
        _index_children(f, index)
    finally:
        if f is not None:
            f.close()

    if append:
        # Convert to json and compress the result
        index_json = json.dumps(index)
        comp = gzip.compress(bytes(index_json, 'utf-8'))

        # Open file again, with h5py, and add the compressed index json as an opaque dataset
        f = h5py.File(path, 'r+')

        if dset_name in f:
            del f[dset_name]

        dt = h5py.opaque_dtype(numpy.void(comp))
        dset = f.create_dataset(dset_name, (1), dtype=dt)
        dset[0] = comp
        f.flush()
        f.close()

    # Optionally output index json to file
    if outfile is not None:
        with open(outfile, 'w') as o:
            json.dump(index, o, indent=4)


def _index_children(group, index):
    children = {}
    for key in group.keys():
        child = group.get(key)
        offset = child._dataobjects.offset
        children[key] = offset

        if hasattr(child, 'keys'):
            _index_children(child, index)
    index[group.name] = children


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='path to input hdf5 file')
    parser.add_argument('-o', '--outfile', default=None, help='path to output index (json) file')
    parser.add_argument('-n', '--noappend',  help='add index dataset to hdf5 file', action='store_true')
    parser.add_argument('-d', '--dataset', default='_index', help='dataset name')
    args = parser.parse_args()
    make_index(args.path, outfile=args.outfile, dset_name=args.dataset, append=(not args.noappend))


if __name__ == '__main__':
    main()

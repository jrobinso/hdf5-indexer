import h5py
import argparse
import gzip
import numpy

'''
Create an index dataset in an existing hdf5 file.
'''
def append_index(path, index_path, group):


    with open(index_path, 'rb') as index_file:
        index = index_file.read()
    comp = gzip.compress(index)

    f = h5py.File(path, 'r+')
    dt = h5py.opaque_dtype(numpy.void(comp))
    dset = f.create_dataset("_index", (1), dtype=dt)
    dset[0] = comp

    f.flush()
    f.close()


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path to input hdf5 file")
    parser.add_argument("index_path", help="path to index path (json) file")
    parser.add_argument("index_name", default="_index", help="name of index dataset")

    args = parser.parse_args()
    append_index(args.path, args.indexpath, args.group)


if __name__ == "__main__":
    main()

import h5py
import argparse
import gzip
import numpy


def append_index(path, index_path, dataset_name = "_index"):

    '''
    Add an index Dataset to CNDB hdf5 file
    :param path: Path to CNDB file
    :param index_path: Path to index json file
    :param dataset_name: Optional override for name of CNDB dataset.
    :return:
    '''

    with open(index_path, 'rb') as index_file:
        index = index_file.read()
    comp = gzip.compress(index)

    f = h5py.File(path, 'r+')
    dt = h5py.opaque_dtype(numpy.void(comp))
    dset = f.create_dataset(dataset_name, (1), dtype=dt)
    dset[0] = comp

    f.flush()
    f.close()


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path to input hdf5 file")
    parser.add_argument("index_path", help="path to index path (json) file")
    parser.add_argument("--dataset", default="_index", help="name of index dataset")

    args = parser.parse_args()
    append_index(args.path, args.indexpath, dataset_name=args.dataset)


if __name__ == "__main__":
    main()

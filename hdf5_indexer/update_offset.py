import h5py
import argparse
from hdf5_indexer.extract_offset import extract_offset

def update_offset(path, dset_name='_index'):

    offset = extract_offset(path, dset_name=dset_name)

    if offset is not None:
        f = h5py.File(path, 'r+')
        f.attrs.create("_index_offset", offset)
        f.flush()
        f.close()

    else:
        print("No index dataset found")



def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path to input hdf5 file")
    parser.add_argument("--dataset", default="_index", required=False, help="name of index dataset (optional, not common")

    args = parser.parse_args()
    update_offset(args.path, dset_name=args.dataset)


if __name__ == "__main__":
    main()

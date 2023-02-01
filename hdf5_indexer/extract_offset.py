import argparse
import pyfive

def extract_offset(path, dset_name='_index'):

    # find index dataset and extract offset
    f = None
    try:
        f = pyfive.File(path)
        dset = f.get(dset_name)
        if dset is None:
            print("None")
            return None
        else:
            return dset._dataobjects.offset

    finally:
        if f is not None:
            f.close()




def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path to input hdf5 file")
    parser.add_argument("--dataset", default="_index", required=False, help="name of index dataset (optional, not common")

    args = parser.parse_args()
    print(extract_offset(args.path, dset_name=args.dataset))


if __name__ == "__main__":
    main()

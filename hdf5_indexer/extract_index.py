import h5py
import argparse
import gzip


def extract_index(path, outfile = None, dataset_name = "_index"):

    '''
    Extract the index json from a CNDB file.
    :param path: Path to CNDB file
    :param outfile: Optional path to output file.  If ommitted output is printed to stdout
    :param dataset_name: Optional override for name of CNDB Dataset containing index.
    :return:
    '''

    f = h5py.File(path, 'r')
    try:
        dataset = f[dataset_name]
    except:
        dataset = None
        pass

    if dataset is None:
        print('No index found')
    else:
        comp = dataset[0]
        index_json = gzip.decompress(comp)
        if outfile is not None:
            with open(outfile, 'w') as o:
                o.write(index_json)
        else:
            print(index_json)

    f.close()


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path to input hdf5 file")
    parser.add_argument("--outfile", default=None, required=False, help="output file name for extracted json (optional)")
    parser.add_argument("--dataset", default="_index", required=False, help="name of index dataset (optional, not common")

    args = parser.parse_args()
    extract_index(args.path, outfile=args.outfile, dataset_name=args.dataset)


if __name__ == "__main__":
    main()

import h5py
import argparse
import gzip

'''
Create an index dataset from an existing index json file
'''
def extract_index(path, outfile = None, dataset_name = "_index"):


    f = h5py.File(path, 'r')
    dataset = f[dataset_name]

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

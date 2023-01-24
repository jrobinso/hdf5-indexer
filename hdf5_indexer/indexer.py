import pyfive
import argparse
import json


def make_index(path, output):

    f = pyfive.File(path)
    index = {}
    _index_children(f, index)
    with open(output, "w") as o:
        json.dump(index, o)


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
    parser.add_argument("path", help="path to input hdf5 file")
    parser.add_argument("output", help="path to output index (json) file")

    args = parser.parse_args()
    make_index(args.path, args.output)


if __name__ == "__main__":
    main()

import pyfive
import argparse
import json
from urllib.request import urlopen
import io
import ssl
import certifi

def make_index(path):

    if path.startswith("https://") :
        with urlopen(path, context=ssl.create_default_context(cafile=certifi.where())) as file:
            content = file.read()
            f = pyfive.File(io.BytesIO(content))
    else:
        f = pyfive.File(path)


    index = {}
    index_children(f, index)
    print(index)

def index_children(group, index):

    children = {}
    for key in group.keys():
        child = group.get(key)
        offset = child._dataobjects.offset
        children[key] = offset

        if hasattr(child, 'keys'):
            index_children(child, index)
    index[group.name] = children
    index_json = json.dumps(index)
    print(json)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path to input hdf5 file")
    parser.add_argument("outfile", nargs="?", default=None, help="path to output file")

    args = parser.parse_args()
    make_index(args.path)


if __name__ == "__main__":
    main()
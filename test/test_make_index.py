import unittest
import pathlib
import shutil
import hdf5_indexer
import h5py
import gzip
import json
import os

class IndexTestCase(unittest.TestCase):

    def test_make_index(self):

        h5file = str((pathlib.Path(__file__).parent / "latest.hdf5").resolve())
        h5file_indexed = str((pathlib.Path(__file__).parent / "latest.indexed.hdf5").resolve())
        shutil.copy(h5file, h5file_indexed)

        # Create the index dataset
        hdf5_indexer.make_index(h5file_indexed)

        # Open the indexed hdf5 file
        f = h5py.File(h5file_indexed, 'r')

        # Check for _index_offset attribute -- We don't need to know the value
        index_dataset_offset = f.attrs['_index_offset']
        self.assertGreater(index_dataset_offset, 0)

        # Extract index dataset
        index_dataset = f['_index']
        compressed_json = index_dataset[0]
        f.close()

        # Decompress and parse json
        json_str = gzip.decompress(compressed_json)
        index = json.loads(json_str)


        # Check known values for dataset offsets
        root_links = index['/']
        dataset1_offset = root_links['dataset1']
        self.assertEqual(dataset1_offset, 195)

        group1_links = index['/group1']
        dataset2_offset = group1_links['dataset2']
        self.assertEqual(dataset2_offset, 661)

        subgroup1_links = index['/group1/subgroup1']
        dataset3_offset = subgroup1_links['dataset3']
        self.assertEqual(dataset3_offset, 1224)

        # Cleanup
        os.remove(h5file_indexed)




if __name__ == '__main__':
    unittest.main()

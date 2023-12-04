import unittest
from product_database import make_product_database
from vendor_database import make_vendor_database
from search import query_classification
from convert import make_receiptParser, get_prompt_prefix, get_example_prompt, make_fewshot_prompt, make_model, make_chain
import pickle
import os

class product_database_test(unittest.TestCase):
# assert ideas 
#  - 
#  - 
     def test_product(self):
         make_product_database()
     
     def load_data_from_pk1_file_product(self,file_path):
        with open(file_path, 'rb') as f:
            data = pickle.load(f)
        return data
     
     def test_load_data_from_pk1_file_product(self):
        test_instance = product_database_test()
        sample_data_product = {'key': 'value'} # need to review logic
        with open('product_mapping.pk1', 'wb') as f:
            pickle.dump(sample_data_product, f)
        loaded_data_product = test_instance.load_data_from_pk1_file_product('product_mapping.pk1')

        self.assertEqual(loaded_data_product, sample_data_product)
        expected_entries = len(sample_data_product)
        actual_entries = len(loaded_data_product)
        self.assertEqual(actual_entries, expected_entries, 'failed actual entries')
        print('here')
        os.remove('product_mapping.pk1')


class vendor_database_test(unittest.TestCase):
     def test_vendor(self):
         make_vendor_database()
         return 
     def load_data_from_pk1_file_vendor(self,file_path):
        with open(file_path, 'rb') as f:
            data = pickle.load(f)
        return data
     
     def test_load_data_from_pk1_file_vendor(self):
        test_instance = vendor_database_test()
        sample_data_vendor = {'key': 'value'}
        with open('vendor_mapping.pk1', 'wb') as f:
            pickle.dump(sample_data_vendor, f)
        loaded_data_vendor = test_instance.load_data_from_pk1_file_vendor('vendor_mapping.pk1')

        self.assertEqual(loaded_data_vendor, sample_data_vendor, 'failed equal data')
        expected_entries = len(sample_data_vendor)
        actual_entries = len(loaded_data_vendor)
        self.assertEqual(actual_entries, expected_entries,'failed equal vendor')
        os.remove('vendor_mapping.pk1')

class vendor_database_test(unittest.TestCase):
# assert ideas 
#  - 
#  - 
     def test_vendor(self):
         make_vendor_database()
         return 
     def load_data_from_pk1_file_vendor(self,file_path):
        with open(file_path, 'rb') as f:
            data = pickle.load(f)
        return data
     
     def test_load_data_from_pk1_file_vendor(self):
        test_instance = vendor_database_test()
        sample_data_vendor = {'key': 'value'}
        with open('vendor_mapping.pk1', 'wb') as f:
            pickle.dump(sample_data_vendor, f)
        loaded_data_vendor = test_instance.load_data_from_pk1_file_vendor('vendor_mapping.pk1')

        self.assertEqual(loaded_data_vendor, sample_data_vendor, 'failed equal data')
        expected_entries = len(sample_data_vendor)
        actual_entries = len(loaded_data_vendor)
        self.assertEqual(actual_entries, expected_entries,'failed equal lengths')
        os.remove('vendor_mapping.pk1')

class convert_unit(unittest.TestCase):
     def test_vendor(self):
        #  make_vendor_database()
         return 
     def load_data_from_pk1_file_vendor(self,file_path):
        # with open(file_path, 'rb') as f:
        #     data = pickle.load(f)
        return data

class search_unit(unittest.TestCase): 
    def test_vendor(self):
        #  make_vendor_database()
         return 
    def load_data_from_pk1_file_vendor(self,file_path):
        # with open(file_path, 'rb') as f:
        #     data = pickle.load(f)
        return data 

class search_unit(unittest.TestCase): 
    def test_vendor(self):
         # make_vendor_database()
         return 
    def load_data_from_pk1_file_vendor(self,file_path):
        # with open(file_path, 'rb') as f:
        #     data = pickle.load(f)
        return data 

# convert
#  check number of entries in txt files against # of files in folder
#  check converted correctly with example JSON from reciepts

if __name__ == "__main__":
    unittest.main()

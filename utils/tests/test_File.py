from unittest import TestCase


class Test(TestCase):
    def test_csvfile_no_file(self):
        from utils.File import CSVFile
        self.assertIsNone(CSVFile(file_location=None).read())

    def test_csvfile_empty_file(self):
        from utils.File import CSVFile
        self.assertIsNone(CSVFile(file_location='').read())

    def test_csvfile_valid_file_no_lines(self):
        from utils.File import CSVFile
        processed_file = CSVFile(file_location="files/test_data_no_lines.csv").read()
        self.assertIsNotNone(processed_file)
        self.assertEqual(len(processed_file), 0)

    def test_csvfile_valid_file(self):
        from utils.File import CSVFile
        processed_file = CSVFile(file_location="files/test_data.csv").read()
        self.assertIsNotNone(processed_file)
        self.assertEqual(len(processed_file), 3)

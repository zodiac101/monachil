import csv

"""
Base Class for File Handling with interfaces for reading and writing files
"""


class File:

    def __init__(self, file_location):
        self.file_location = file_location

    def read(self):
        pass


"""
Class for handling CSV files
"""


class CSVFile(File):
    type = 'csv'

    def read(self):
        """
        :return: data from file
        """
        try:
            with open(self.file_location, 'r') as file:
                csv_reader = csv.reader(file, delimiter=',')
                line_count = 0
                file_data = list()
                for row in csv_reader:
                    line_count += 1

                    """
                    Skip two lines as they are not data
                    """
                    if line_count <= 2:
                        continue
                    elif line_count >= 10e10:
                        break
                    file_data.append(row)
                return file_data
        except Exception as e:
            print(e)
            return None

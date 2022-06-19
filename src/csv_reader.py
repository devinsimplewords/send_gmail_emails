import csv


class CSVReader:

    def __init__(self):
        self.csv_path = "data/email_info.csv"

    def get_email_info_from_csv(self):
        """Open CSV file and store rows in a list"""
        print("Reading '{}' file...".format(self.csv_path))
        email_info_list = []
        # open CSV file
        with open(self.csv_path, "r") as read_obj:
            csv_reader = csv.reader(read_obj)
            for idx, row in enumerate(csv_reader):
                # skip header
                if idx == 0:
                    continue

                # store row in list
                email_info_list.append(row)

        return email_info_list

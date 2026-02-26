import csv
import os
from datetime import datetime

class Database:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', newline='') as csvfile:
                csvfile.write('Date,Amount,Description\n')  # Write the header

    def add_record(self, date, amount, description):
        with open(self.filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([date, amount, description])

    def get_total(self):
        total = 0
        with open(self.filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                total += float(row['Amount'])
        return total

    def get_records(self):
        records = []
        with open(self.filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                records.append(row)
        return records

    def filter_records_by_date(self, start_date, end_date):
        filtered_records = []
        with open(self.filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                record_date = datetime.strptime(row['Date'], '%Y-%m-%d %H:%M:%S')
                if start_date <= record_date <= end_date:
                    filtered_records.append(row)
        return filtered_records
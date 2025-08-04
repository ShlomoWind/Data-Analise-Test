import pandas as pd

class DataLoader:
    def __init__(self,csv_file_path):
        self.csv = csv_file_path

#convert the csv file to a data frame
    def convert_to_data_frame(self):
        df = pd.read_csv(self.csv)
        return df
class ExporterCsv:
    def __init__(self,data_frame,path):
        self.df = data_frame
        self.path = path

    def export_to_csv(self):
        self.df.to_csv(self.path)


import json

class ExporterJson:
    def __init__(self,dictionary,path):
        self.dict = dictionary
        self.path = path

    def export_to_json(self):
        with open(self.path,'w')as f:
            json.dump(self.dict,f)

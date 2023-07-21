import json
import pickle
import os


class DataConverter:
    def __init__(self, directory, filename):
        self.directory = directory
        self.filename = filename

    def save_json_to_pickle(self):
        with open(os.path.join(self.directory, self.filename), 'r') as json_file:
            data = json.load(json_file)
        with open(os.path.join(self.directory, self.filename + '.pickle'), 'wb') as pickle_file:
            pickle.dump(data, pickle_file)


converter = DataConverter('C:\GitHub_projects\GB\Pogruzheniye v Python\seminar_10_OOP\data', 'data.json')
converter.save_json_to_pickle()

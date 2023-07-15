import pickle


def to_pickle(data, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)

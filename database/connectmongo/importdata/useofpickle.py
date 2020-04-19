import _pickle as pickle
import numpy as np
import pandas as pd
import csv

class conversionPickle(object):
    def ___init__(self, name):
        self.name = name



    def conversionOfCsvToPickle(self, csv_path, path_pickle):
        file = None
        try:
            file = pd.read_csv(csv_path, header=0)
        except Exception:
            print("Error while reading csv file")
        else:
            file = file.dropna(how='any', axis=0)
            filehandler = open(path_pickle, "wb")
            pickle.dump(file, filehandler)

    # Error
    # def convertCSVToPickle(self, csv_path, path_pickle):
    #     objects = []
    #     try:
    #         with open(csv_path, 'a') as csvfile:
    #             reader = csv.reader(csvfile)
    #             for p in reader:
    #                 objects.append(p)
    #
    #         file = open(path_pickle, "wb")
    #         pickle.dump(objects, file)
    #         file.close()
    #     except Exception:
    #         print("Exception while converting to pickke")

if __name__ == "__main__":

    csv_path = '../../data/chicagoCrimes.csv'
    output = '../../data/chiCrimes.pickle'
    # conversionPickle.convertCSVToPickle(object, csv_path=csv_path, path_pickle=output)
    conversionPickle.conversionOfCsvToPickle(object, csv_path,output)
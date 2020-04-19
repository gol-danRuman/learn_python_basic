import csv
import _pickle as pickle

class LoadData:
    # Map row to dictionary (dictionary comprehension)
    def data(column_names, row):
        return {column_names[column]: data for column, data in enumerate(row) if column < len(column_names)}


if __name__ == "__main__":
    # Map CSV file to list of dictionaries (list comprehension)
    data_path = '../../data/chiCrimes.pickle'
    column_name = ['ID', 'Case Number', 'Date', 'Block', 'IUCR', 'Primary Type', 'Description', 'Location Description', 'Arrest', 'Domestic', 'Beat', 'District', 'Ward', 'Community Area', 'FBI Code', 'X Coordinate', 'Y Coordinate', 'Year', 'Updated On', 'Latitude', 'Longitude', 'Location']
    # datas = [LoadData.data(column_name, row) for row in pickle.load(open(data_path, 'rb'))]
    data = pickle.load(open(data_path, 'rb'))
    print(type(data))
    "Data loads as DataFrame type so need to convert to array list to get objects"

    "To get the Column name as a list"
    print(list(data.columns.values))

    "To convert dataFrame to list"
    data_list = data.values
    print(data_list[0])

    datas = [LoadData.data(column_name, row) for row in data_list]

    print(datas[0])

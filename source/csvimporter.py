import csv

def load_data(foldername,modelname, delimiter):
    MODEL_PATH = 'csv/'
    with open(MODEL_PATH + foldername + '/alphabet_' + modelname + '.csv', newline='') as csvalphabet:
        reader = csv.reader(csvalphabet, delimiter=delimiter)
        alphabets = []
        for row in reader:
            symbol = row[0]
            alphabets.append(symbol)
    
    with open(MODEL_PATH + foldername + '/data_' + modelname + '.csv', newline='') as csvdata:
        reader = csv.reader(csvdata, delimiter=delimiter)
        trainingset = []
        for row in reader:
            sequence = row[0]
            trainingset.append(sequence)
    
    return alphabets, trainingset
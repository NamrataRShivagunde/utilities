import argparse
import pandas as pd
from matplotlib import pyplot as plt
from pandas.io import parsers
import numpy as np

#Get the filename and column names as argument
parser = argparse.ArgumentParser()
parser.add_argument("filename",help = "csv file name")

#reads the argument and return the csv file
def parse_argument():
    args = parser.parse_args()
    filename = args.filename
    
    read_csv_file = pd.read_csv(filename)
    return read_csv_file


def create_separate_files(csv_file):
    crossword_classes = list(csv_file.annotation.unique())
    for each_class in crossword_classes:
        filtered_dataframe_factual = csv_file.loc[csv_file['annotation'] == each_class]
        filtered_dataframe_factual= filtered_dataframe_factual[['source', 'target']]
        each_class = each_class.replace("/","_")
        each_class = each_class.replace(" ","")
        filtered_dataframe_factual.to_csv("separated_test/{}.csv".format(each_class.lower()), index= False)




if __name__ == "__main__":
    csv_file = parse_argument()
    create_separate_files(csv_file)
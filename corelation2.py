"""
import csv
import numpy as np


def getDataSource(data_path):
   cups_of_coffee = []
   hours_of_sleep = []
   with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cups_of_coffee.append(float(row["Coffee in ml"]))
            hours_of_sleep.append(float(row["sleep in hours"]))

   return {"x" : cups_of_coffee , "y":  hours_of_sleep}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between cups_of_coffee and hours_of_sleep  :-  \n--->",correlation[0,1])

def setup():
    data_path  = "corelation1.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()
"""
import csv
import numpy as np


def getDataSource(data_path):
   marks_in_percentage= []
   days_present = []
   with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))

   return {"x" : marks_in_percentage, "y": days_present }

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between cups_of_coffee and hours_of_sleep  :-  \n--->",correlation[0,1])

def setup():
    data_path  = "corelation.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()
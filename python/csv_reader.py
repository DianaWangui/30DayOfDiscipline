import csv
def csv_reader():

  with open("diana.csv", "r") as csv_file:
    reader = csv.reader(csv_file, delimiter=',')

    for row in reader:
      print(row)
if __name__ == "__main__":
  csv_reader()
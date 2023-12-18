import csv
def csv_reader():
  """Opening the csv file and reading the content separated by (,)"""
  with open("write.csv", "r") as csv_file:
    reader = csv.reader(csv_file, delimiter=',')

    """Reading row by row and printing it to stdout"""
    for row in reader:
      print(row)
if __name__ == "__main__":
  csv_reader()
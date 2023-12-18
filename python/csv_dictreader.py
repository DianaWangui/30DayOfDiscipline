import csv
def dictreader():
  """Opening csv file for reading using DictReader() function
  DictReader reads directly into a dictionary instead of reading
  directly into string like the reader() function
  """
  with open('write.csv', 'r') as file:
    reader = csv.DictReader(file)
    line_count = 0 # for keeping track of read lines

    """Reading all data in first row in the dictionary
    which are the columns header names for the data in
    the spreadsheet/table
    """
    for row in reader:
      if line_count == 0:
        print("Column names are {}".format(', '.join(row)))
        line_count += 1
        
      """Printing the data in the spreadsheet of the above columns"""  
      print(f'\t{row["F_name"]} {row["L_name"]} is {row["Rank"]}.')
      line_count += 1

    """Printing the number of lines processed in out program"""
    print(f"Processed {line_count} lines")
if __name__ == "__main__":
  dictreader()
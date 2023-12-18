import csv
def writeDict():
  """Openinf file to write in dictionary format"""
  with open('dict.csv', 'w') as f:
    fieldname = ['Name', 'dept', 'birth_month']
    writer = csv.DictWriter(f, fieldnames=fieldname)

    """Adding data into the file"""
    writer.writeheader()
    writer.writerow({'Name': 'Diana', 'dept': 'IT', 'birth_month': 'Aug'})
    writer.writerow({'Name': 'John', 'dept': 'Sales', 'birth_month': 'Nov'})
    writer.writerow({'Name': 'Kelvin', 'dept': 'Finance', 'birth_month': 'Dec'})

  print("Finished writing data")
if __name__ == "__main__":
  writeDict()

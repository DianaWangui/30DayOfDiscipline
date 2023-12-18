import csv
def write_data():
  with open('wtite.csv', 'w') as f:
    fieldnames = ("F_name", "L_name", "Rank")
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    """Add data to the CSV file here..."""
    writer.writerow({'Rank':'B','F_name':'Diana', 'L_name':'Wangui'})
    writer.writerow({'Rank':'A','F_name':'Cobby', 'L_name':'Sefah'})
    writer.writerow({'Rank':'B','F_name':'Kelvin', 'L_name':'Owusu'})

  print("Writing complete")
if __name__ == "__main__":
  write_data()
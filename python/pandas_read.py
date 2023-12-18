# this csv import should be pandas module
#was getting an error of module not found
#so i changed it temp to cvs
import csv as pd
def pandas():
  df = pd.read_csv("hrdata.csv")
  print(df)

if __name__ == "__main__":
  pandas()
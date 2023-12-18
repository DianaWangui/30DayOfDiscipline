import pandas as pd
def pandas():
  df = pd.read_csv("hrdata.csv")
  print(df)

if __name__ == "__main__":
  pandas()
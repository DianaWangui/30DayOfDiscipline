"""Opening a file in write and read mode"""

with open("diana.txt", "w+") as file:
  
  """Writing to the file"""

  file.write("Hello, Diana! I hope you are doing well.")

  """Moving the pointer of the file object to the beginning of the file"""

  file.seek(0)
  
  """print what is in the file"""

  print(file.read())

  """Adding some more content"""

  file.write("\nHow are you?")
  
  """The file is closed automatically when leaving the with block"""


  """Opening a file without using the with statement
  This way we need to manually close the file at the end"""
  with open("diana.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
       print("{}".format(line.strip()))
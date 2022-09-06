import pandas as pd
import numpy as np
import openpyxl
# Draw a new windows to reques the file yo get all data
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
file = filename


data = pd.read_excel(file,sheet_name = 0, index_col=0)
# print(data.head())
print(sheets.sheetnames)



def getsheetname(file):
    sheets  = openpyxl.load_workbook(file)

    
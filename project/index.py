import pandas as pd
import numpy as np

# Modulo para manejar pantallas
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
file = filename



tips_df = pd.read_excel(file, index_col=0)
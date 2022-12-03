import tkinter as tk
import pandas as pd
from input_page import *
from select_page import *


# app2 = SelectPage('Please input data', pd.DataFrame({'a':[1, 1]}))
# app2.mainloop()
app = InputPage('Please input data')
app.mainloop()







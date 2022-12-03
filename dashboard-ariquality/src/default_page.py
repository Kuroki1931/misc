import tkinter as tk

class Default(tk.Tk):
    def __init__(self, title=None):
        super().__init__()
        self.title('Air quality')
        self.geometry("400x300")
        # title
        label = tk.Label(self, text=title, font=('Arial', 14))
        label.grid(row=0, column=0, padx=5, pady=10)
    
    

        
       

import tkinter as tk
import pandas as pd
import default_page
import select_page

from tkinter.filedialog import askopenfilename
from dateutil import parser


class InputPage(default_page.Default):
    def __init__(self, title):
        super().__init__(title)
        self.create_widgets()

    def create_widgets(self):
        # menu
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Input", command=self.new_window)
        filemenu.add_separator()
        menubar.add_cascade(label="Menu", menu=filemenu)
        self.config(menu=menubar)
        #sensor data
        sensor_label = tk.Label(self, text='Sensors information', font=('Arial', 11))
        sensor_label.grid(row=10, column=0, padx=5, pady=10)
        sensor_textbox = tk.Entry(self, font=('Arial', 11))
        sensor_textbox.grid(row=10, column=1, padx=5, pady=10)
        def sensor_readfile():
            filename = askopenfilename()
            sensor_textbox.insert(0, str(filename))
        sensor_btn = tk.Button(self, command=sensor_readfile, text='select')
        sensor_btn.grid(row=10, column=2, padx=5, pady=10)
        #attribute data
        attribute_label = tk.Label(self, text='Attribute information', font=('Arial', 11))
        attribute_label.grid(row=20, column=0, padx=5, pady=10)
        attribute_textbox = tk.Entry(self, font=('Arial', 11))
        attribute_textbox.grid(row=20, column=1, padx=5, pady=10)
        def attribute_readfile():
            filename = askopenfilename()
            attribute_textbox.insert(0, str(filename))
        attribute_btn = tk.Button(self, command=attribute_readfile, text='select')
        attribute_btn.grid(row=20, column=2, padx=5, pady=10)
        #all sensors data
        all_sensors_label = tk.Label(self, text='All sensors information', font=('Arial', 11))
        all_sensors_label.grid(row=30, column=0, padx=5, pady=10)
        all_sensors_textbox = tk.Entry(self, font=('Arial', 11))
        all_sensors_textbox.grid(row=30, column=1, padx=5, pady=10)
        def all_sensors_readfile():
            filename = askopenfilename()
            all_sensors_textbox.insert(0, str(filename))
        all_sensors_btn = tk.Button(self, command=all_sensors_readfile, text='select')
        all_sensors_btn.grid(row=30, column=2, padx=5, pady=10)

        # read_file
        read_label = tk.Label(self, font=('Arial', 11), fg='red')
        read_label.grid(row=40, column=0, padx=5, pady=10)

        number_label = tk.Label(self, text='How many columns', font=('Arial', 11))
        number_label.grid(row=50, column=0, padx=5, pady=10)
        number_textbox = tk.Entry(self, text='0', font=('Arial', 11))
        number_textbox.grid(row=50, column=1, padx=5, pady=10)

        def combine_data(data1, data2, number):
            #read data
            data11 = data1['Timestamp;SensorID;AttributeID;Value;'].str.split(';', expand = True)
            data11.columns = ['Timestamp', 'SensorID', 'AttributeID', 'Value','']
            try:
                data11 = data11[-number:]
            except:
                read_label.config(text='column number is over')
            del data11['']

            data22 = data2['SensorID;Latitude;Longitude;Description'].str.split(';', expand = True)
            data22.columns = ['SensorID', 'Latitude', 'Longitude', 'Description']

            #Merge two tables
            data3 = pd.merge(data11,data22)
            del data3['Description']

            #Define concat function
            def concat_func(x):
                return pd.Series({
                    'SensorID':','.join(x['SensorID'].unique()),
                    'AttributeID':','.join(x['AttributeID'].unique()),
                    'Value':','.join(x['Value'].unique()),
                    'Latitude':','.join(x['Latitude'].unique()),
                    'Longitude':','.join(x['Longitude'].unique()),
                })

            data4 = data3.groupby(data3['Timestamp']).apply(concat_func).reset_index()

            del data4['AttributeID']

            data44 = data4['Value'].str.split(',', expand = True)
            data44.columns = ['O3', 'NO2', 'SO2', 'PM10','NA1','NA2','NA3','NA4']
            del data44['NA1']
            del data44['NA2']
            del data44['NA3']
            del data44['NA4']

            del data4['Value']

            dataf = pd.merge(data4,data44,left_index = True, right_index = True)
            dataf['Timestamp'] = dataf['Timestamp'].apply(lambda x: parser.parse(x))
            return dataf

        def excute():
            url1 = sensor_textbox.get()
            url2 = attribute_textbox.get()
            url3 = all_sensors_textbox.get()
            number = int(number_textbox.get())
            
            if url1=='' or url2=='' or url3=='':
                read_label.config(text='you need to select all')
                return

            try:
                sensor_data = pd.read_csv(url1, encoding='utf-8')
                # attribute_data = pd.read_csv(url2, encoding='utf-8')
                all_sensors_data = pd.read_csv(url3, encoding='utf-16')
                data = combine_data(all_sensors_data, sensor_data, number)
                print(data)
            except:
                read_label.config(text='path is wrong')
                return
        
            new_app = select_page.SelectPage('Please select parameters', data)
            new_app.mainloop()
            

        read_btn = tk.Button(self, command=excute, text='read')
        read_btn.grid(row=50, column=2, padx=5, pady=10)

    def new_window(self):
        new_app = InputPage('Please input data')
        new_app.mainloop()

    
        
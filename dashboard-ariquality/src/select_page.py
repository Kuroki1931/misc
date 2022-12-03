import tkinter as tk
import pandas as pd
import default_page
import input_page

from sklearn.metrics import r2_score
from datetime import datetime, timedelta
from default_page import *
from dateutil import parser
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


class SelectPage(default_page.Default):
    def __init__(self, title, data):
        super().__init__(title)
        self.geometry("1100x600")
        self.data = data
        self.mean_gragh_data = None
        self.corr_gragh_data = None
        self.IAQI_list = [0, 50, 100, 150, 200, 300, 400]
        self.O3_list = [0, 160, 200, 300, 400, 500, 1000]
        self.SO2_list = [0, 50, 150, 475, 800, 1600, 2100]
        self.NO2_list = [0, 40, 80, 180, 280, 565, 750]
        self.PM10_list = [0, 50, 150, 250, 350, 420, 500]
        self.Sensor_list = ['Sensor0', 'Sensor1', 'Sensor2', 'Sensor3', 'Sensor4', 'Sensor5', 'Sensor6', 'Sensor7', 'Sensor8', 'Sensor9']
        self.label_sensor_list = []
        self.create_widgets()
        

    def create_widgets(self):
        # menu
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Input", command=self.new_window)
        filemenu.add_separator()
        menubar.add_cascade(label="Menu", menu=filemenu)
        self.config(menu=menubar)

        # data duration
        start_date = str(self.data.iloc[0, 0])[:10]
        end_date = str(self.data.iloc[-1, 0])[:10]
        start_label = tk.Label(self, text='data duration {}  -  {}'.format(start_date, end_date), font=('Arial', 11))
        start_label.grid(row=1, column=0, padx=1, pady=1)

        # Basic settings
        mean_label = tk.Label(self, text='Basic Settings', font=('Arial', 11), fg='blue')
        mean_label.grid(row=2, column=0, padx=1, pady=1)
        meanspan_label = tk.Label(self, text='mean span', font=('Arial', 11))
        meanspan_label.grid(row=3, column=0, padx=1, pady=1)
        chk = tk.Checkbutton(self, text='24 hour')
        chk.grid(row=3, column=1, padx=1, pady=1)
        standardday_label = tk.Label(self, text='standard day', font=('Arial', 11))
        standardday_label.grid(row=4, column=0, padx=1, pady=1)
        standardday_textbox = tk.Entry(self, font=('Arial', 11))
        standardday_textbox.grid(row=4, column=1, padx=1, pady=1)
        timespan_label = tk.Label(self, text='time span', font=('Arial', 11))
        timespan_label.grid(row=5, column=0, padx=1, pady=1)
        timespan_textbox = tk.Entry(self, font=('Arial', 11))
        timespan_textbox.grid(row=5, column=1, padx=1, pady=1)

        #duration
        duration_label = tk.Label(self, text='duration', font=('Arial', 11))
        duration_label.grid(row=6, column=1, padx=1, pady=1)

        def excute():
            standard = standardday_textbox.get()
            timespan = int(timespan_textbox.get())

            standard_date = datetime.strptime(standard, '%Y-%m-%d')
            time_change = timedelta(days=timespan)
            start_date = str(standard_date - time_change)[:10]
            end_date = str(standard_date + time_change)[:10]
            duration_label.config(text='{}  -  {}'.format(start_date, end_date))

            data = self.data.copy()
            base = data['Timestamp'][0]
            data['Timestamp'] = data['Timestamp'] - base
            data['Timestamp'] = data['Timestamp'].apply(lambda x: x.days)
            data['O3'] = data['O3'].astype(float)
            data['NO2'] = data['NO2'].astype(float)
            data['SO2'] = data['SO2'].astype(float)
            data['PM10'] = data['PM10'].astype(float)
            standard_day = int((parser.parse(standard) - base).days)
            data = data.groupby(['Timestamp','SensorID']).mean()
            data = data.reset_index()
            extract_day_list = [i for i in range(standard_day-timespan, standard_day+timespan)]
            data = data[data['Timestamp'].isin(extract_day_list)]
            data['IAQI_O3'] = data['O3'].apply(lambda x: self.calculate_IAQI(self.IAQI_list, self.O3_list, x))
            data['IAQI_SO2'] = data['SO2'].apply(lambda x: self.calculate_IAQI(self.IAQI_list, self.SO2_list, x))
            data['IAQI_NO2'] = data['NO2'].apply(lambda x: self.calculate_IAQI(self.IAQI_list, self.NO2_list, x))
            data['IAQI_PM10'] = data['PM10'].apply(lambda x: self.calculate_IAQI(self.IAQI_list, self.PM10_list, x))
            data['AQI'] = data[['IAQI_O3', 'IAQI_SO2', 'IAQI_NO2', 'IAQI_PM10']].max(axis=1)
            print(data)

            for x, y in zip(self.label_sensor_list, self.Sensor_list):
                x.config(text=data[data['SensorID']==y]['AQI'].max())
                
            self.mean_gragh_data = data
            self.corr_gragh_data = data
        
        mean_btn = tk.Button(self, command=excute, text='read')
        mean_btn.grid(row=6, column=0, padx=5, pady=5)

        # mean_gragh 
        gragh_frame = tk.Frame(self, relief=tk.GROOVE)
        gragh_frame.grid(row=0, column=2, rowspan=15, padx=10, pady=1, sticky=tk.W+tk.E+tk.N+tk.S)
        fig = self.plot_wave(0, 0, 'mean_gragh')
        canvas = FigureCanvasTkAgg(fig, gragh_frame)
        canvas.get_tk_widget().grid(row=0, column=0)

        # mean_gragh settings
        gragh_label = tk.Label(self, text='Mean gragh Settings', font=('Arial', 11), fg='blue')
        gragh_label.grid(row=7, column=0, padx=1, pady=1)
        area_label = tk.Label(self, text='area', font=('Arial', 11))
        area_label.grid(row=8, column=0, padx=1, pady=1)
        area_textbox = tk.Entry(self, font=('Arial', 11))
        area_textbox.grid(row=8, column=1, padx=1, pady=1)

        # mean gragh create
        def mean_button():
            area = area_textbox.get()
            data = self.mean_gragh_data.copy()
            data = data[data['SensorID']==area]
            x = data['Timestamp']
            y = data['AQI']
            fig = self.plot_wave(x, y, 'mean_gragh')
            canvas = FigureCanvasTkAgg(fig, gragh_frame)
            canvas.draw()
            canvas.get_tk_widget().grid(row=0, column=0)

        gragh_btn = tk.Button(self, command=mean_button, text='create')
        gragh_btn.grid(row=9, column=0, padx=5, pady=5)  

        # correlation
        corr_frame = tk.Frame(self, relief=tk.GROOVE)
        corr_frame.grid(row=0, column=3, rowspan=10, padx=10, pady=1, sticky=tk.N+tk.S)
        fig = self.plot_plot(0, 0, 'correlation')
        canvas = FigureCanvasTkAgg(fig, corr_frame)
        canvas.get_tk_widget().grid(row=0, column=0)  

        # Corr_Gragh settings
        corr_gragh_label = tk.Label(self, text='Corr gragh Settings', font=('Arial', 11), fg='blue')
        corr_gragh_label.grid(row=10, column=0, padx=1, pady=1)
        corr_area_label1 = tk.Label(self, text='area1', font=('Arial', 11))
        corr_area_label1.grid(row=11, column=0, padx=1, pady=1)
        corr_area_textbox1 = tk.Entry(self, font=('Arial', 11))
        corr_area_textbox1.grid(row=11, column=1, padx=1, pady=1)
        corr_area_label2 = tk.Label(self, text='area2', font=('Arial', 11))
        corr_area_label2.grid(row=12, column=0, padx=1, pady=1)
        corr_area_textbox2 = tk.Entry(self, font=('Arial', 11))
        corr_area_textbox2.grid(row=12, column=1, padx=1, pady=1)

        # corr gragh create
        def corr_button():
            area1 = corr_area_textbox1.get()
            area2 = corr_area_textbox2.get()
            data = self.corr_gragh_data.copy()
            data1 = data[data['SensorID']==area1]
            y1 = data1['AQI']
            data2 = data[data['SensorID']==area2]
            y2 = data2['AQI']
            r2 = r2_score(y1, y2)
            title = 'corr_gragh ' + 'R-squared = %0.2f' % r2
            fig = self.plot_plot(y1, y2, title)
            canvas = FigureCanvasTkAgg(fig, corr_frame)
            canvas.draw()
            canvas.get_tk_widget().grid(row=0, column=0)

        gragh_btn = tk.Button(self, command=corr_button, text='create')
        gragh_btn.grid(row=13, column=0, padx=5, pady=5) 

        #table
        label_00 = tk.Label(self, text='area name', font=('Arial', 11))
        label_00.grid(row=11, column=2, padx=1, pady=1) 
        label_10 = tk.Label(self, text='Sensor0', font=('Arial', 11))
        label_10.grid(row=12, column=2, padx=1, pady=1) 
        label_20 = tk.Label(self, text='Sensor1', font=('Arial', 11))
        label_20.grid(row=13, column=2, padx=1, pady=1) 
        label_30 = tk.Label(self, text='Sensor2', font=('Arial', 11))
        label_30.grid(row=14, column=2, padx=1, pady=1) 
        label_40 = tk.Label(self, text='Sensor3', font=('Arial', 11))
        label_40.grid(row=15, column=2, padx=1, pady=1) 
        label_50 = tk.Label(self, text='Sensor4', font=('Arial', 11))
        label_50.grid(row=16, column=2, padx=1, pady=1) 
        label_60 = tk.Label(self, text='Sensor5', font=('Arial', 11))
        label_60.grid(row=17, column=2, padx=1, pady=1) 
        label_70 = tk.Label(self, text='Sensor6', font=('Arial', 11))
        label_70.grid(row=18, column=2, padx=1, pady=1) 
        label_80 = tk.Label(self, text='Sensor7', font=('Arial', 11))
        label_80.grid(row=19, column=2, padx=1, pady=1) 
        label_90 = tk.Label(self, text='Sensor8', font=('Arial', 11))
        label_90.grid(row=20, column=2, padx=1, pady=1) 
        label_100 = tk.Label(self, text='Sensor9', font=('Arial', 11))
        label_100.grid(row=21, column=2, padx=1, pady=1) 

        label_01 = tk.Label(self, text='Worst AQI', font=('Arial', 11))
        label_01.grid(row=11, column=3, padx=1, pady=1) 
        label_11 = tk.Label(self, font=('Arial', 11))
        label_11.grid(row=12, column=3, padx=1, pady=1) 
        label_21 = tk.Label(self, font=('Arial', 11))
        label_21.grid(row=13, column=3, padx=1, pady=1) 
        label_31 = tk.Label(self, font=('Arial', 11))
        label_31.grid(row=14, column=3, padx=1, pady=1) 
        label_41 = tk.Label(self, font=('Arial', 11))
        label_41.grid(row=15, column=3, padx=1, pady=1) 
        label_51 = tk.Label(self, font=('Arial', 11))
        label_51.grid(row=16, column=3, padx=1, pady=1) 
        label_61 = tk.Label(self, font=('Arial', 11))
        label_61.grid(row=17, column=3, padx=1, pady=1) 
        label_71 = tk.Label(self, font=('Arial', 11))
        label_71.grid(row=18, column=3, padx=1, pady=1) 
        label_81 = tk.Label(self, font=('Arial', 11))
        label_81.grid(row=19, column=3, padx=1, pady=1) 
        label_91 = tk.Label(self, font=('Arial', 11))
        label_91.grid(row=20, column=3, padx=1, pady=1) 
        label_101 = tk.Label(self, font=('Arial', 11))
        label_101.grid(row=21, column=3, padx=1, pady=1) 
        self.label_sensor_list = [label_11, label_21, label_31, label_41, label_51, label_61, label_71, label_81, label_91, label_101]


    def calculate_IAQI(self, list1, list2, value):
            C_p = value
            for i in range(len(list2)-1):
                if (C_p>list2[i]) & (C_p<list2[i+1]):
                    BP_Hi = list2[i+1]
                    BP_Lo = list2[i]
                    IAQI_Hi = list1[i+1]
                    IAQI_Lo = list1[i]
                    return (IAQI_Hi - IAQI_Lo)/(BP_Hi-BP_Lo)*(C_p-BP_Lo)+IAQI_Lo

    def plot_wave(self, x, y, title, marker=None):
        # Figureインスタンスを生成する。
        fig = plt.Figure(figsize=(4.5, 3.5))
    
        # 目盛を内側にする。
        plt.rcParams['xtick.direction'] = 'in'
        plt.rcParams['ytick.direction'] = 'in'
    
        # Axesを作り、グラフの上下左右に目盛線を付ける。
        ax1 = fig.add_subplot(111)
        ax1.yaxis.set_ticks_position('both')
        ax1.xaxis.set_ticks_position('both')
    
        # 軸のラベルを設定する。
        ax1.set_xlabel('date')
        ax1.set_ylabel('mean AQI')
        ax1.title.set_text(title)
    
        # データをプロットする。
        ax1.plot(x, y, marker=marker)
        return fig

    def plot_plot(self, x, y, title):
        # Figureインスタンスを生成する。
        fig = plt.Figure(figsize=(4.5, 3.5))
    
        # 目盛を内側にする。
        plt.rcParams['xtick.direction'] = 'in'
        plt.rcParams['ytick.direction'] = 'in'
    
        # Axesを作り、グラフの上下左右に目盛線を付ける。
        ax1 = fig.add_subplot(111)
        ax1.yaxis.set_ticks_position('both')
        ax1.xaxis.set_ticks_position('both')
    
        # 軸のラベルを設定する。
        ax1.set_xlabel('area1 AQI')
        ax1.set_ylabel('area2 AQI')
        ax1.title.set_text(title)

    
        # データをプロットする。
        ax1.scatter(x, y)
        return fig

    def new_window(self):
        new_app = input_page.InputPage('Please input data')
        new_app.mainloop()

    
        
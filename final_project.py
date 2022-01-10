# -*- coding: utf-8 -*-
"""Final_Project_1301194172 | 1301194314 | 1301194275

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ofkPdKdS0YUuX3G8Au5bc6_-fIKOvpx6

> FINAL PROJECT - Visualisasi Data

> Kelas    : IF - 42 - GAB04

> Kelompok : 
*   Fadhlan Mochamad Daffa Richtman ( 1301194172 )
*   Firra Millaty Suryadi ( 1301194314 )
*   Yudha Yasa Afrildzal Briano ( 1301194275 )
"""

import pandas as pd
from bokeh.plotting import figure
from bokeh.plotting import show
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, HoverTool, Select
from bokeh.models.widgets import Tabs, Panel
from bokeh.layouts import row, widgetbox

!gdown --id 1rGQ_C1fhB0kZ7B5WGrep-cY0F2XBZc6P

df = pd.read_csv("covid_19_indonesia_time_series_all.csv")
df["Date"] = pd.to_datetime(df["Date"])
data = df[df["Location"].str.contains("Indonesia")==False]
data = data[['Date', 'Location', 'Total Cases', 'Total Deaths', 'Total Recovered', 'Total Active Cases']]

lokasi = list(data.Location.unique())

col_list = list(data.columns)

def make_dataset(lokasi, feature):

    
    xs = []
    ys = []
    colors = []
    labels = []

    for i, lokasi in enumerate(lokasi):

        df = data[data['Location'] == lokasi].reset_index(drop = True)
        
        x = list(df['Date'])
        y = list(df[feature])
        
        xs.append(list(x))
        ys.append(list(y))

        colors.append(Category20_16[i])
        labels.append(lokasi)

    new_src = ColumnDataSource(data={'x': xs, 'y': ys, 'color': colors, 'label': labels})

    return new_src

def make_plot(src, feature):
    
    p = figure(plot_width = 700, plot_height = 400, 
            title = 'Covid19-Indonesia All Time Series',
            x_axis_label = 'Date', y_axis_label = 'Feature Selected')

    p.multi_line('x', 'y', color = 'color', legend_field = 'label', line_width = 2, source = src)

    return p

def update_country(attr, old, new):
    countries_to_plot = [lokasi_selection.labels[i] for i in lokasi_selection.active]

    
    new_src = make_dataset(countries_to_plot, feature_select.value)

    src.data.update(new_src.data)

def update_feature(attr, old, new):
    countries_to_plot = [lokasi_selection.labels[i] for i in lokasi_selection.active]
    
    feature = feature_select.value
    
    new_src = make_dataset(countries_to_plot, feature)

    src.data.update(new_src.data)
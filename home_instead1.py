# -*- coding: utf-8 -*-
"""
Created on Mon Mar 06 14:28:17 2017

@author: Balaganesh
"""
#importing pandas .... 

import pandas as pd

#importing numpy ....

import numpy as np

#importing seaborn for advance visualization...

import seaborn as sb
sb.set_style('whitegrid')


#importing matplotlib for adavcnce plotting...

import matplotlib.pyplot as mplt

#reading data from local machine

data = pd.read_csv('ExportedRecords.csv' , names = ['ID' , 'start' , 'end' , 'PID' , 'CID'])


#Preprocessing
#calculating the time difference to get the Number of Hours the appointment lasted..

data['start'] = pd.to_datetime(data['start'])
data['end'] = pd.to_datetime(data['end'])
TD = pd.DataFrame(data.end - data.start)
data = data.join(TD)
data.columns = ['ID' , 'start' , 'End' , 'PID' , 'CID' , 'TD']
data = data.drop('ID' , 1)

#reading the data frame / information about the dataframe

data.info()
data.describe()

# converting the timestamp values to seperate columns for clear understanding of Time driven data

time = data['start'].iloc[0]
time.dayofweek
time.year

data['hour'] = data['start'].apply(lambda time : time.hour)
data['month'] = data['start'].apply(lambda time : time.month)

#DAYOFWEEK reference {'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}....
data['day'] = data['start'].apply(lambda time : time.dayofweek)
data['year'] = data['start'].apply(lambda time : time.year)

#basic analysis count of each analysis to start knowing the dataset...

data['CID'].value_counts()
data['PID'].value_counts()
data['hour'].value_counts()
data['month'].value_counts()
data['day'].value_counts()
data['year'].value_counts()

#plotting the outcomes of the basic analysis....
# we will be using seaborn analysis to get good visualization on the extracted analysis
# 1. To see the number of appointments per day / month / hour
 
 #sb.countplot(x='month',data=data, hue ='CID',palette='viridis')
#mplt.legend(bbox_to_anchor = (1.05,1 ) , loc=2 , borderaxespad = 0.)

#number of customers apooitnment per year
d_year = data.groupby('year').count()
d_year['CID'].plot()

#numbre of customers appointment per day
d_day = data.groupby('day').count()
d_day['CID'].plot()

#number of cutomers appoitment per month
d_month = data.groupby('month').count()
d_month['CID'].plot()

#number of customers apooitnment per hour
d_hour = data.groupby('hour').count()
d_hour['CID'].plot()

#numbre of providers appoitnments per day

d_day['PID'].plot()

#number of providers appoitment per month

d_month['PID'].plot()

#number of providers apooitnment per hour

d_hour['PID'].plot()

#number of provides apooitnment per year

d_year['PID'].plot()

# Analysis deep into service providers per week and day

p_day_hour = data.groupby(by=['day' , 'hour' ]).count()['PID'].unstack()
p_day_hour.head(5)

#plotting the datarfame to get results of number of service provider appoitnment per day in a week

mplt.figure(figsize=(12,6))
sb.heatmap(p_day_hour,cmap='viridis')

sb.clustermap(p_day_hour,cmap='viridis')

#Analysis and plotting the datarfame to get results of number of service provider appoitnment per week in a month

p_month_week = data.groupby(by=['day' , 'month' ]).count()['PID'].unstack()
p_month_week.head(5)

mplt.figure(figsize=(12,6))
sb.heatmap(p_month_week,cmap='viridis')
sb.clustermap(p_month_week,cmap='viridis')

#Analysis and plotting the datarfame to get results of number of service provider appointment per month in a year

p_year_month = data.groupby(by=['month' , 'year' ]).count()['PID'].unstack()
p_year_month.head(5)
p_year_month.fillna(0)

mplt.figure(figsize=(12,6))
sb.heatmap(p_year_month,cmap='viridis')
mplt.show()


# Analysis 2
data1 = data.groupby('PID').count()
data1.reset_index(level=0 , inplace=True)
data1.describe()

data1[data1['CID'] >= ]['PID'].describe()
data1[data1['CID'] <= 42.0 ]['PID'].describe()

sb.jointplot(x = 'PID' ,y = 'CID' , data = data1  , kind = 'reg')

































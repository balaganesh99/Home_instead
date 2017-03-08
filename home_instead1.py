import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as mplt
sb.set_style('whitegrid')

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
data.isnull()
data.isna()
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
#number of customers apooitnment per year
d_year = data.groupby('year').count()
d_year.reset_index(level = 0 , inplace = True)
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

# Analysis 2
data1 = data.groupby('PID').count()
data1.reset_index(level=0 , inplace=True)
data1.describe()
sb.jointplot(x = 'PID' ,y = 'CID' , data = data1 )
data['TD'].describe()

# Analysis 2
data1 = data.groupby('PID').count()
data2 = data.groupby('CID').count()
data1.reset_index(level=0 , inplace=True)
data2.reset_index(level=0 , inplace=True)
data1.describe()
sb.jointplot(x = 'PID' ,y = 'CID' , data = data1 )
data['TD'].describe()
data_tid_max = data[data['TD'] < '430 days 10:30:00'
data_tid_max = data_tid_max[data_tid_max['TD'] < '280 days 05:30:00']
data_tid_max
data_tid_max['TD'].describe()

# analysis of each quarlite of the ideal appoitnment time for each quartile
data.describe()
data.info()
data1['PID'].describe()
data1
data2['CID'].describe()
data.describe()
data['TD'].describe()

#Quartiles of time difference to calculate the ideal time for an appoitnment 
#1st quartile
data[(data['TD'] >= '0 days 00:00:00') & (data['TD'] <= '0 days 02:55:00') ].describe()

#2nd quartile 
data[(data['TD'] > '0 days 02:55:00') & (data['TD'] <= '0 days 04:00:00') ].describe()

#3rd Quartile
data[(data['TD'] > '0 days 04:00:00') & (data['TD'] <= '0 days 06:00:00') ].describe()

#4th quartile
data[(data['TD'] > '0 days 06:00:00') & (data['TD'] <= '430 days 10:30:00') ].describe()


# number of customers each year
d_year[d_year['year'] == 2010]hour
d_year[d_year['year'] == 2011]
d_year[d_year['year'] == 2012]
d_year[d_year['year'] == 2013]
d_year[d_year['year'] == 2014]
d_year[d_year['year'] == 2015]
d_year[d_year['year'] == 2016]
d_year[d_year['year'] == 2017]































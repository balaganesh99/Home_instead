# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 16:30:43 2017

@author: Balaganesh
"""
pwd
import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
import seaborn as sb
import tokenize 

data = pd.read_csv('ExportedRecords.csv' , names = ['ID' , 'Start' , 'End' , 'PID' , 'CID'])

data.info()

from datetime import datetime

data['Start']  = pd.to_datetime(data['Start'])
data['End'] = pd.to_datetime(data['End'])

TD = pd.DataFrame (data.End - data.Start ) 

join = data.join(TD)

join.columns = ['ID' , 'Start' , 'End' , 'PID' , 'CID' , 'TD']

td = pd.DataFrame(join , columns = ['PID', 'CID' , 'TD'])

td_grp =  td.groupby('CID')

td_grp_cnt = td_grp.count()

td_grp_cnt['PID'].max()

join.describe()
join.info()




td_grp_cnt.info()

td_grp_cnt.reset_index(level = 0 ,inplace = True)

td_grp_cnt['PID'].max()

join[join['TD']  > '0 days 08:00:00.000000000']['CID']

join['TD'].max()

sb.lmplot(x= 'CID' , y = 'PID'  , data = td_grp_cnt)

sb.pairplot(td_grp_cnt)

join.describe()

join.info()
join[join['TD']  == '0 days 00:00:00']['CID']











td_grp_cnt['CID'].max()

join = data.join(TD)
join.info()

pid_grp = td.groupby('PID')


pid_grp_count = pid_grp.count()

pid_grp_count.reset_index(level = 0 , inplace = True)

pid_grp_count['CID'].max()
pid_grp_count[pid_grp_count['CID'] == 17638]['PID']

pid_grp_count.info()
pid_grp_count.describe()

join[join['TD'] > '25:00:00']['TD']

x = join['TD'].iloc[0]
x= join['TD'].str.split('days')

join['TD'] = join['TD'] / np.timedelta64(1,'s')
join['TD'] = join['TD']/60
join['TD'] = join['TD']/60
join[join['TD']> 24]['TD'].count()
join['CID'].nunique()
join['PID'].nunique()
join['PID'].value_counts().head(5)
join['CID'].value_counts().head(5)
join[join['CID'] == 29916.0]

sb.countplot(x ='PID' , data = join)












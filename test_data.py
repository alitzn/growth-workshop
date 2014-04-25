from __future__ import division
import matplotlib.pyplot as plt
from sqlalchemy import *
import numpy as np
from sklearn.linear_model import LogisticRegression
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from sklearn.metrics import confusion_matrix
from sklearn.cross_validation import train_test_split
from churndata import *
from sklearn.preprocessing import StandardScaler
from pandas import DataFrame
from pandas.core.groupby import GroupBy
from util import query_to_df
import pandas as pd


from util import campaign_to_num,event_to_num,transform_column,hist_and_show,vectorize,to_percentage,num_rows,vectorize_label,meal_to_num,to_milliseconds
db = create_engine('sqlite:///forjar.db')


metadata = MetaData(db)

Session = sessionmaker(bind=db)


session = Session()

q = session.query(Event).join(Meal,Event.Meal_Id == Meal.id).join(Users).add_entity(Meal).add_entity(Users)

df = query_to_df(session,q)

print df.columns

df['Event_date'] = pd.to_datetime(df['Event_date'])
df = df.set_index(df.Event_date)

df = df['Users_id'].groupby(df['Event_date'].map(lambda x : (x.month,x.year))cd).value_counts()




print df





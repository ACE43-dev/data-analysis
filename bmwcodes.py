import pandas as pd
dt= pd.read_csv("/content/BMW sales data (2010-2024) (1).csv")

dt.head(10)

dt.isnull().sum()
#que 1
dt.groupby('Region')['Sales_Volume'].sum()
#------------------------------------------------------------------------------------------

#que 2 

#ans: 7 series is highest sold product
dt.groupby('Model')['Sales_Volume'].sum().mode()

dt.groupby('Model')['Sales_Volume'].sum()
#------------------------------------------------------------------------------------------
# que 3
dt.groupby('Model')['Sales_Volume'].mean()
# 3 Series	5066.660065
# 5 Series	5029.947517
# 7 Series	5097.828118
# M3	5064.512576
# M5	5087.022778
# X1	5121.676149
# X3	5057.933956
# X5	5061.232226
# X6	5060.738276
# i3	5009.495236
# i8	5085.516934
#------------------------------------------------------------------------------------------

#que 4
dt.groupby('Region')['Sales_Volume'].sum().max()
#42974277
#asia
#------------------------------------------------------------------------------------------

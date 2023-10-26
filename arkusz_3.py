import pandas as pd
import numpy as np

technologies = ["Spark", "Pandas","Python", "PHP"]
fee = [25000, 20000, 15000, 18000]
duration = ['50 Days', '35 Days', '35 Days', np.nan, '30 Days', '30 Days'] #np. None
discount = [2000,1000,800,500,500]
columns = ['Courses', "Fee", "Duration", "Discount"]

df = pd.DataFrame(
    list(zip(technologies, fee, duration, discount)),
    columns=columns
)

print(df)
data2 ={'A':[1,2,3],'B':[4,5,6],'C':[7,8,9]}
df.to_excel('courses.xlsx', index=False) #zapisujedo excela i usuwa numerowanie
#df.to_excel('D//new folder//courses.xlsx') #zapisujedo excela

indeksy = ['Wiersz1', 'Wiersz2','Wiersz3']
df1=pd.DataFrame(data2, index=indeksy)
df1.to_excel('courses2.xlsx', index=True) #


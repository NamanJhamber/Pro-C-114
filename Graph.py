import numpy as np
GRE_Score_array=np.array(GRE_Score)
chances_of_admit_array=np.array(chances_of_admit)

m,c=np.polyfit(GRE_Score_array,chances_of_admit_array,1)
y=[]

for x in GRE_Score_array:
  y_value=m*x+c
  y.append(y_value)

fig=px.scatter(x=GRE_Score_array,y=chances_of_admit_array)
fig.update_layout(shapes=[
                          dict(
                              type="line",
                               y0=min(y),y1=max(y),
                               x0=min(GRE_Score_array),x1=max(GRE_Score_array)
                          )
])
fig.show()

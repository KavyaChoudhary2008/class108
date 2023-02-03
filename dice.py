import random
import plotly.express as px 
import plotly.figure_factory as ff


dice_result = []
count=[]
for i in range(0,1000):
    dice1 = random.randint(1,6)
    #print(dice1)
    dice2 = random.randint(1,6)
    #print(dice2)
    dice_sum = dice1+dice2
    #print(dice_sum)
    dice_result.append(dice_sum)
    #print(dice_result)
    count.append(i)
    #print(count)

#fig = px.bar(x=dice_result,y=count)
#fig.show()
fig=ff.create_distplot([dice_result],["Result"])
fig.show()





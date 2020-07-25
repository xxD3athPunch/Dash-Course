import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

#Generate a random seed to create data consistency
np.random.seed(56)

"""Generate some random data for the x axis... use the np.linspace
function as seen below. We are generating data with linspace, that creates
equally spaced data points. We are saying that we want the data to be
between zero and one, and we want 100 different points of data
"""
x_values = np.linspace(0,1,100)

"""Generate some random data for the y axis....use the np.random.randn 
function as seen below. We are generating 100 random points of data that
all have different spacing. 
"""

y_values = np.random.randn(100)

"""We are going to create a variable that contains all of 
the data for the chart and use this variable for better
organization"""

#trace0 is comprised of data for a scatter plot with just markers
trace0 = go.Scatter(x=x_values, y=y_values+5, 
				   mode='markers',
				   name='markers')

#trace1 is comprised of data for a line chart with no markers
trace1 = go.Scatter(x=x_values, y=y_values,
				    mode='lines',
				    name='mylines')
#trace3 is comprised of data for both a line and marker chart
trace2 = go.Scatter(x=x_values, y=y_values-5,
					mode='lines+markers',
					name='my favorite')



#Passing that chart variable into "data" which is cleaner

data = [trace0, trace1, trace2]

#Adding a Chart title to our layout
layout = go.Layout(title='Line Charts')

#Passing both the data and the layout into the figure
fig = go.Figure(data=data, layout=layout)

#Plotting that figure to display the chart that we have created
pyo.plot(fig)
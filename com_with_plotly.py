"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import plotly.plotly as py
from plotly.graph_objs import *
import time 				
import datetime
import serial

port = "/dev/USB0"

# les Donnees de la conncexion a plotly
username = ""
api_key = ""

# Initialisation d un Objet Plotly 
py.sign_in(username,api_key)

# Initialisation du graph (sans streaming)
trace1 = Scatter(
    x=[],
    y=[],
    stream={'token': '', 'maxpoints': 1000}
)
trace2 = Scatter(
    x=[],
    y=[],
    xaxis='x2',
    yaxis='y2',
    stream={'token': '', 'maxpoints': 1000}
)

trace3 = Scatter(
    x=[],
    y=[],
    xaxis='x3',
    yaxis='y3',
    stream={'token': '', 'maxpoints': 1000}
)

trace4 = Scatter(
    x=[],
    y=[],
    xaxis='x4',
    yaxis='y4',
    stream={'token': '', 'maxpoints': 1000}
)

data = Data([trace1, trace2, trace3, trace4])

layout = Layout(
    title='Paramétre Météo',
    xaxis=XAxis(
        title='Time of day',
        domain=[0, 0.45]
    ),
    yaxis=YAxis(
        title='Humidity %',
        domain=[0, 0.45]
    ),
    xaxis2=XAxis(
        title='Time of day',
        domain=[0.55, 1]
    ),
    xaxis3=XAxis(
        title='Time of day',
        domain=[0, 0.45],
        anchor='y3'
    ),
    xaxis4=XAxis(
        title='Time of day',
        
        domain=[0.55, 1],
        anchor='y4'
    ),
    yaxis2=YAxis(
        title='Temperature C',
        domain=[0, 0.45],
        anchor='x2'
    ),
    yaxis3=YAxis(
        title='Pressure Kpa',
        domain=[0.55, 1]
    ),
    yaxis4=YAxis(
        title='Relative Pressure',
        domain=[0.55, 1],
        anchor='x4'
    )
)

fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='multiple-subplots')

connexion = serial.Serial(port,9600)
connexion.flushInput()

# Initialisation de l'objet streaming Plotly 
stream1 = py.Stream('')
stream1.open()

stream2 = py.Stream('')
stream2.open()

stream3 = py.Stream('')
stream3.open()

stream4 = py.Stream('')
stream4.open()

while True:
    if(connexion.inWaiting()>0):
        value_string = connexion.readline()
        value=value_string.split(",")

        stream1.write({'x': datetime.datetime.now(), 'y': float(value[0])})
        stream2.write({'x': datetime.datetime.now(), 'y': float(value[1])})
        stream3.write({'x': datetime.datetime.now(), 'y': float(value[2])})
        stream4.write({'x': datetime.datetime.now(), 'y': float(value[3])})

        time.sleep(200)	# délais entre deux envois

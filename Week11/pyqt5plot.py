from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
import plotly.graph_objs as go
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
ladd1 = "Bangkok","mossZmossZ"
ladd2 = "China"
#print("Location address:",ladd1)
location = geolocator.geocode("bangkok")
location2 = geolocator.geocode(ladd2)
#print("Latitude and Longitude of the said address:")

data = [go.Scattergeo(
            #locationmode = 'ISO-3',
            lon = [location.longitude,location2.longitude],
            lat = [location.latitude,location2.latitude],
            mode = 'markers',
            marker = dict(
                size = 5,
                opacity = 0.8,
                symbol = 'circle',
                line = dict(width=1, color='rgba(102, 102, 102)')
            ),
            text = [str(ladd1),ladd2],
            name = 'Cities'
        )]
layout = dict(
            title = 'Geo Scatter plot',
            geo = dict(
                scope='world',
                projection=dict(type='equirectangular'),
                showland = True,
                landcolor = "rgb(250, 250, 250)",
                subunitcolor = "rgb(217, 217, 217)",
                countrycolor = "rgb(217, 217, 217)",
                countrywidth = 0.5,
                subunitwidth = 0.5
            )
        )
fig = go.Figure(data=data, layout=layout)
fig.to_html(include_plotlyjs = 'cdn')
#fig.show()
#view.setHtml(fig.to_html(include_plotlyjs = 'cdn'))

# Create the PyQt5 application and main window
app = QApplication([])
window = QMainWindow()
widget = QWidget()
layout = QVBoxLayout(widget)

# Create the QWebEngineView widget and load the HTML plot
view = QWebEngineView()
#view.load(QUrl("https://www.google.com"))
view.setHtml(fig.to_html(include_plotlyjs = 'cdn'))
layout.addWidget(view)

# Set the widget as the central widget of the main window and show it
window.setCentralWidget(widget)
window.show()
app.exec_()

This is a dash app utilizing Plot.ly's open source module to build an analytical app. 

It is currently hosted in Azure at https://kong-dash-app.azurewebsites.net/

Link to Plot.ly's Dash documentation - https://dash.plot.ly/  
Link to some examples from Plot.ly - https://dash-gallery.plotly.host/Portal/

How to clone onto your machine

git clone -b master https://github.com/kongmyang/DashAppDemo.git

required libraries are in the requirements.txt file, would recommend launching this application in venv.

How to launch the app locally on your machine

"source" / python app.py

Gunicorn command on Azure web app settings
gunicorn --bind=0.0.0.0 --timeout 600 app:server

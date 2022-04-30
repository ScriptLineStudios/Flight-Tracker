<h1 align="center">Flight Tracker ✈︎</h1>

<h4 align="center">Get the current location of any plane located on a map</h4>
  <p align="center">
  </p>

# 💬 About:

Every 10 seconds a call is made to the <a href="https://">OpenSky Network API</a> to retrive to longitude and latitude of the plane you are tracking. It then uses folium to plot those points on a map. 

# 🔧 Setup:
Install the dependencies:

`python -m pip install -r requirements.txt`

# 🖥️ Usage:
Simply add the ICAO of the flight yout would like to track to the `config.py` file then run the file `run.py` and the website and traker will start.

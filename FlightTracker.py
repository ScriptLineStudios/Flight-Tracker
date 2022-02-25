import requests
import time
import folium
import pickle
import os

class FlightTracker:
    def __init__(self, icao):
        self.icao = icao
        self.jet_image = folium.features.CustomIcon('./images/jet_image.png', icon_size=(30,30))
        self.status = "Status: None"
        self.title_html = '''
                    <h3 align="center" style="font-size:16px"><b>{}</b></h3>
                    '''.format(self.status)  
        self.map = folium.Map(location=[0,0], zoom_start=2)
        self.base_url = f"https://opensky-network.org/api/states/all?time=0&icao24={self.icao}"
        self.points = []
        if os.path.exists("point_data/points.pickle"):
            with open("point_data/points.pickle", "rb") as point_file:
                self.points = pickle.load(point_file)
        else:
            with open("point_data/points.pickle", "wb") as point_file:
                pickle.dump(self.points, point_file)

    def generate_map(self, points) -> None:
        folium.PolyLine(points, color='black').add_to(self.map)
        folium.Marker(points[-1], tooltip="Jet", icon=self.jet_image).add_to(self.map)
        self.map.get_root().html.add_child(folium.Element(self.title_html))
        self.map.save("templates/map.html")

    def update_title(self, status) -> None:
        self.title_html = '''
                    <h3 align="center" style="font-size:16px"><b>{}</b></h3>
                    '''.format(status)  

    def locate(self) -> None: 
        while True:
            data = requests.get(self.base_url).json()

            if data["states"] != None:
                self.update_title("Status: Flying")

                self.points.append((data['states'][0][6], data['states'][0][5]))
                with open("point_data/points.pickle", "wb") as point_file:
                    pickle.dump(self.points, point_file)
                self.generate_map(self.points)
            else:
                self.update_title("Status: Grounded")

            time.sleep(10)

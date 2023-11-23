import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.mapview import MapView
from kivy.uix.label import Label
from mapbox import Geocoder

class ParkApp(App):
    def build(self):
        # Generate random latitude and longitude values
        latitude = random.uniform(-90, 90)
        longitude = random.uniform(-180, 180)

        # Initialize the Mapbox geocoder
        geocoder = Geocoder(access_token='sk.eyJ1IjoidGFuYXkyMiIsImEiOiJjbHBiMjM3MmgwZzNtMmpua3VxdzB6MnYwIn0.y9XcBNPoA6TuMMp5VuEEQw')

        # Reverse geocode the location to get the address
        response = geocoder.reverse(lon=longitude, lat=latitude)

        # Print the response for debugging
        print(response.json())

        # Get the formatted address from the response
        try:
            address = response.json()['features'][0]['place_name']
        except IndexError:
            address = "Address not found"

        # Create a label to display the address
        label = Label(text=address)

        # Create a map view
        mapview = MapView(zoom=15, lat=latitude, lon=longitude)

        # Create a layout to hold the label and map view
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(label)
        layout.add_widget(mapview)

        return layout

# Run the app
if __name__ == '__main__':
    ParkApp().run()

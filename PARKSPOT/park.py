from kivy.app import App
from kivy.uix.label import Label
from mapbox import Geocoder

class ParkApp(App):
    def build(self):
        # Get the user's location using the GPS (Note: This won't work on a non-Android device)
        latitude = 0.0
        longitude = 0.0

        # Initialize the Mapbox geocoder
        geocoder = Geocoder(access_token='sk.eyJ1IjoidGFuYXkyMiIsImEiOiJjbHBiMjM3MmgwZzNtMmpua3VxdzB6MnYwIn0.y9XcBNPoA6TuMMp5VuEEQw')

        # Reverse geocode the user's location to get the address
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

        return label

# Run the app
if __name__ == '__main__':
    ParkApp().run()
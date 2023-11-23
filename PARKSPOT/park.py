import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy_garden.mapview import MapView, MapMarker
from kivy.uix.label import Label
from mapbox import Geocoder
from kivy.uix.anchorlayout import AnchorLayout

class ParkApp(App):
    def build(self):
        # Initialize the Mapbox geocoder
        self.geocoder = Geocoder(access_token='sk.eyJ1IjoidGFuYXkyMiIsImEiOiJjbHBiMjM3MmgwZzNtMmpua3VxdzB6MnYwIn0.y9XcBNPoA6TuMMp5VuEEQw')

        # Create a label with the address
        self.label = Label()

        # Create a MapView
        self.mapview = MapView(zoom=15)

        # Create a MapMarker
        self.marker = MapMarker()
        self.mapview.add_widget(self.marker)

        # Create a vertical BoxLayout
        layout = BoxLayout(orientation='vertical')

        # Create a horizontal BoxLayout for the search box and button
        search_layout = BoxLayout(orientation='horizontal', size_hint=(0.8, None))

        # Create a search box and add it to the search layout
        self.search_box = TextInput(hint_text='Enter address', size_hint=(0.8, 1))
        search_layout.add_widget(self.search_box)

        # Create a search button and add it to the search layout
        search_button = Button(text='Search', size_hint=(0.2, 1))
        search_button.bind(on_press=self.search_address)
        search_layout.add_widget(search_button)

        # Create an AnchorLayout and add the search layout to it
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center')
        anchor_layout.add_widget(search_layout)

        # Add the AnchorLayout to the main layout
        layout.add_widget(anchor_layout)

        # Add the label and MapView to the layout
        layout.add_widget(self.label)
        layout.add_widget(self.mapview)

        return layout

    def search_address(self, instance):
        address = self.search_box.text
        response = self.geocoder.forward(address)
        try:
            feature = response.json()['features'][0]
            self.mapview.lat = feature['center'][1]
            self.mapview.lon = feature['center'][0]
            self.marker.lat = feature['center'][1]
            self.marker.lon = feature['center'][0]
            self.label.text = feature['place_name']
        except IndexError:
            self.label.text = "Address not found"

if __name__ == '__main__':
    ParkApp().run()

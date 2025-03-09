import folium
from folium import plugins
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView

def create_map(latitude, longitude, zoom_start=12):
    """
    Create an interactive map with a custom marker at specified coordinates.
    
    Parameters:
    latitude (float): Latitude of the location
    longitude (float): Longitude of the location
    zoom_start (int): Initial zoom level of the map (default: 12)
    
    Returns:
    folium.Map: Interactive map object
    """
    # Create a map centered at the specified location
    m = folium.Map(location=[latitude, longitude], 
                   zoom_start=zoom_start,
                   tiles='OpenStreetMap')
    
    # Add a marker with a popup
    folium.Marker(
        [latitude, longitude],
        popup='Selected Location',
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(m)
    
    # Add a circle around the marker
    folium.Circle(
        radius=1000,  # 1000 meters radius
        location=[latitude, longitude],
        color='crimson',
        fill=True,
    ).add_to(m)
    
    # Add fullscreen button
    plugins.Fullscreen().add_to(m)
    
    # Add location finder
    plugins.LocateControl().add_to(m)
    
    return m


class MapWindow(QMainWindow):
    def __init__(self, latitude, longitude, zoom_start=12):
        super().__init__()
        
        # Create the map
        self.map = create_map(latitude, longitude, zoom_start)
        
        # Save the map to an HTML file
        self.map.save('map.html')
        
        # Create a QWebEngineView widget
        self.browser = QWebEngineView()
        
        # Load the HTML content into the QWebEngineView
        self.browser.setHtml(self.map.get_root().render())
        
        # Set the central widget of the MainWindow to the QWebEngineView
        self.setCentralWidget(self.browser)
        
        # Set the window title
        self.setWindowTitle('Folium Map with PyQt5')
        
        # Set the window size
        self.resize(800, 600)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Example coordinates (New York City)
    latitude = 40.7128
    longitude = -74.0060
    
    # Create the main window
    window = MapWindow(latitude, longitude)
    window.show()
    
    # Run the application
    sys.exit(app.exec())
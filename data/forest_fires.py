import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Load file in and read contents
filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    file_content = csv.reader(f)
    headings = next(file_content)

    # Display index and headings
    # for idx, heading in enumerate(headings):
    #     print(idx, heading)
    # Retrieve data
    lats, lons, brightness = [], [], []
    for data in file_content:
        lats.append(float(data[0]))
        lons.append(float(data[1]))
        brightness.append(float(data[2]))
my_layout = Layout(title='Fires')
print(brightness)
data = [{
    'type': 'scattergeo',
    'lat': lats,
    'lon': lons,
    'marker': {
        'size': [br/300 for br in brightness],
        'color': brightness,
        'colorscale': "Viridis",
        'colorbar': {'title': 'Magnitude'}


    }
}]
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='n.html')
import folium
import sqlite3
import branca.colormap as cm
from covid19_data import JHU
from flask import Flask, render_template


# DATA BASE STUFF
conn = sqlite3.connect('countries.db', check_same_thread=False)
c = conn.cursor()
# List of tuples of the country alongside with the coordinates
# [('Austria', 13.199959, 47.2000338)......]
coordinates = c.execute('SELECT * FROM countries')


# Global variables
countries = [x for x in JHU.countries]
cases = {}
for country in countries:
    confirmed = JHU.dataByName(country).confirmed
    cases[country] = confirmed

# Flask Settings
app = Flask(__name__)

def total_confirmed():
    '''Return the number of the confirmed COVID-19 cases in total.'''
    return JHU.Total.confirmed


def total_recovered():
    '''Return the number of the recovered COVID-19 cases in total.'''
    return JHU.Total.recovered


def total_deaths():
    '''Return the number of the death cases in total.'''
    return JHU.Total.deaths


def death_rate():
    '''Calculate the death rate due to COVID-19.'''
    deaths = total_deaths()
    confirmed = total_confirmed()
    return round((deaths / confirmed) * 100, 2)


def create_map(coords, cases):
    '''Create world map and add markers'''
    rad = 0
    color = ''
    
    world_map= folium.Map(location=[30.48693541064179, -31.689018918623677],
                          tiles='cartodbpositron',
                          zoom_start=2.6,
                          height='70%')

    colormap = cm.LinearColormap(colors=['#19fc00' ,'#a84a32'],
                                 vmin=1000,
                                 vmax=1000000)
    for elem in coords:
        # e.g ('Austria', 13.199959, 47.2000338)...
        country = elem[0]
        longitude = elem[1]
        latitude = elem[2]

        if cases[country] > 1000000:
            rad = 200000
            color = '#a84a32'  # Red
        elif cases[country] > 100000:
            rad = 100000
            color = '#ff9100'  # Orange
        elif cases[country] > 10000:
            rad = 70000
            color = '#f7e300'  # Yellow
        elif cases[country] > 1000:
            rad = 60000
            color = '#a2d631'  # Green-ish
        elif cases[country] < 1000:
            rad = 50000
            color = '#19fc00'  # Green
        folium.Circle(location=[latitude, longitude],
                      radius=rad,
                      color=color,
                      fill=True,
                      tooltip=country,
                      popup=f"Confirmed cases: {cases[country]: ,}"
                    ).add_to(world_map)
    colormap.add_to(world_map)
    return world_map


world_map = create_map(coordinates, cases)
world_map.save('templates/map.html')


@app.route("/")
def home():
    confirmed = format(total_confirmed(), ',d')
    recovered = format(total_recovered(), ',d')
    deaths = format(total_deaths(), ',d')
    return render_template(
        "home.html",
        total_confirmed=confirmed,
        total_recovered=recovered,
        total_deaths=deaths,
        death_rate=death_rate()
    )

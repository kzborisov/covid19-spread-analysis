# Covid 19 Spread Dashboard

## About

> Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus.
> At this time, there are no specific vaccines or treatments for COVID-19. The best way to prevent and slow down transmission is be **well informed** about the COVID-19 virus.

The goal of this project is to build a COVID-19 Spread dashboard, showing the confirmed cases of the virus in an interactive map by country. It also shows the total confirmed. recovered, deaths count of the virusi and a death rate in percents.

The project is created using Flask, sqlite3, folium, covid19_data, JavaScript, HTML5 and CSS3.

## Getting Started

### Prerequisites

* Python; [pyenv](https://github.com/pyenv/pyenv) recommended
* Pip

### Installing

Get the project up and running locally in just 5 easy steps.

1. Create a personal [Fork](https://github.com/login?return_to=%2FBrianRuizy%2Fcovid19-dashboard) of this repository.

2. **Clone** the fork with HTTPS, using your local terminal to a preferred location, and **cd** into the project.

```bash
git clone https://github.com/<username>/covid19-spread-analysis.git 
cd covid19-spread-analysis/
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run local server, and **DONE**!

```bash
export FLASK_APP=application.py
export FLASK_ENV=development
flask run

 * Serving Flask app "application.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

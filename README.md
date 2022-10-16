# SBSPS-Challenge-9552-Real-Time-Air-Quality-Monitoring-Weather-Forecasting-System
<h3>Real-Time Air Quality Monitoring &amp; Weather Forecasting System.</h3>


# <img width="100" height="50" src="Project Files/IBM-HackChallenge-Frontend/images/Logo.PNG" alt="Airmoqual icon" align="top" /> Airmoqual

Air pollution is one of the serious environmental problems that is leading to millions of
premature deaths each year. Air quality monitoring systems will be one of the proactive
solutions for reducing deaths.
Our project provides air quality measurement and pollutant values(PM2.5, PM10, NO2,
NH3, CO, etc) of each city in India.
We have built our model using the Xgboost(Extreme Gradient Boosting) algorithm with high
accuracy of 99%. After that, we used an API to collect real-world pollutant values. With this
data we predicted air quality and with the help of tableau software, we have represented air
quality in India Map. Eventually, we integrated this map with a web application which is
developed using front-end technologies(HTML, CSS, and JS).
<p align="center">
  <img width="492" align="center" alt="Airqmon window with measurement details" src="https://media.istockphoto.com/vectors/air-quality-index-numerical-scale-concept-vector-illustration-vector-id1201722905?k=20&m=1201722905&s=612x612&w=0&h=rt0Xo1NZ5M4jPoq_nLaE6qL0UeZ31I6vItHe5WsMVHw=" />
</p>

<!-- <p align="center">
  <img src="https://user-images.githubusercontent.com/1029142/36537429-674931ba-17d0-11e8-88ee-c246226c1053.png" width="378px" align="center" alt="Airqmon notification about air quality" />
</p> -->

<!-- ## Supported data providers

- [Airly][airly] - over 20k sensor stations in many cities around the world in addition to data provided from third-party services like PurpleAir. Check the [Airly map][airly-map] for full coverage.

## Source code-only

Due to the reasons described in [this comment](https://github.com/jsynowiec/airqmon/issues/50#issuecomment-1008751034), I am no longer willing to cover the monthly costs associated with the Airqmon API and Google Geolocation.

I have removed all binaries from the current and previous releases as they will no longer work. You can host the Airqmon API on your own and clone the latest release to build your version of the app. -->


## Requirements

1. Google colab(latest version).
2.  python 3.8.0.
3. front_end tools HTML, CSS, JavaScript.
4. Tableau 2022.2.2.0.

## Tasks

1. Machine Learning Model.
2. Generation of map view of Tableau.
3. Website Devolopment.
4. Integration of map with website.


## Build & installation

1. Clone the [latest release][Airmoqual-latest-release].
2. Install the dependancies given in Readme.md file.
3. Build the Project and run it on your system.

## Preferences

There are a few options available to customize on the preferences window that you can access by clicking on the button with a cog or by pressing the `⌘ + ,` shortcut.

## Airmoqual API

From version 2, Airqmon uses the [Airmon API][airqmon-api], a supplementary service, to find the nearest station and fetch measurements.


## Privacy

Airmoqual application does not track any personally identifiable information or usage analytics.


## License

This app is an open-source software licensed under the [Tableau License, Version 2022.2.2.0][license]

[license]: https://raw.githubusercontent.com/jsynowiec/airmoqual/main/LICENSE
[airmoqual-latest-release]: https://github.com/jsynowiec/airmoqual/releases/latest
[airmoqual-api]: https://github.com/jsynowiec/airqmon-api
[gh-actions]: https://actions-badge.atrox.dev/jsynowiec/airmoqual/goto?ref=main


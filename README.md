# Light-AirQ

Simple and fast API for the CitiAir project

## Installing

You can install the latest version using `pipenv`:

    $ git clone "https://github.com/KnightParzivalll/Light-AirQ"
    $ cd Light-AirQ
    $ pipenv install
    $ pipenv shell
    ...

## Example

First you need to get a TOKEN from your personal page in [CitiAir](https://cityair.ru) or you can request access to the data for research groups

### Initial setup

There is an `example.py` in the repository, where it is necessary to replace two lines:

    ref_point = ("lat", "lon")
    TOKEN = "token"

Where `lat` is the latitude and `lon` is the longitude of the place where you want to get air quality data.
`token` - token for API access.

The script itself finds the station closest to the point with these coordinates.

### Result

    $ python example.py 

    postId - ...
    date - ...
    version - .....
    temperature - 6.638 °C
    pressure - 753.1735 mm Hg
    humidity - 68.304 %
    pm2 - 0.0032000002 mg/m³
    pm10 - 0.0036 mg/m³
    co - 0.19982488 mg/m³
    no2 - 0.027084269 mg/m³
    so2 - 0 mg/m³
    o3 - 0.020531181 mg/m³
    h2s - 0 mg/m³
    cityairAqi - 3

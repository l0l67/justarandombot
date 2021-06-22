import requests


def get_weather(city):
    API_key = "API-KEY from openweathermap.org"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    weimar_id = "2812482"
    berlin_id = "2950159"
    graz_id = "2778067"

    global we_hum, be_hum, we_temp_c, we_feels_c, be_temp_c, be_feels_c, ga_temp_c, ga_feels_c, ga_hum


    weimar_url = base_url + "appid=" + API_key + "&id=" + weimar_id
    berlin_url = base_url + "appid=" + API_key + "&id=" + berlin_id
    graz_url = base_url + "appid=" + API_key + "&id=" + graz_id

    weimar_data = requests.get(weimar_url).json()
    berlin_data = requests.get(berlin_url).json()
    graz_data = requests.get(graz_url).json()

    we_temp = weimar_data['main']['temp']
    we_temp_c = we_temp - 273.15
    we_temp_c = format(we_temp_c, '.2f')

    be_temp = berlin_data['main']['temp']
    be_temp_c = be_temp - 273.15
    be_temp_c = format(be_temp_c, '.2f')

    ga_temp = graz_data['main']['temp']
    ga_temp_c = ga_temp - 273.15
    ga_temp_c = format(ga_temp_c, '.2f')



    we_feels = weimar_data['main']['feels_like']
    we_feels_c = we_feels - 273.15
    we_feels_c = format(we_feels_c, '.2f')

    be_feels = berlin_data['main']['feels_like']
    be_feels_c = be_feels - 273.15
    be_feels_c = format(be_feels_c, '.2f')

    ga_feels = graz_data['main']['feels_like']
    ga_feels_c = ga_feels - 273.15
    ga_feels_c = format(ga_feels_c, '.2f')

    we_hum = weimar_data['main']['humidity']
    be_hum = berlin_data['main']['humidity']
    ga_hum = graz_data['main']['humidity']

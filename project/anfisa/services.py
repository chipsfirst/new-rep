import requests


def what_weather(city):
    url = f'http://wttr.in/{city}'
    weather_parameters = {
        'format': 2,
        'M': ''
    }
    try:
        response = requests.get(url, params=weather_parameters)
    except requests.ConnectionError:
        return '<сетевая ошибка>'
    if response.status_code == 200:
        return response.text.strip()
    else:
        return '<ошибка на сервере погоды. попробуйте позже>'

    
def what_temperature(weather):     
    if (weather == '<сетевая ошибка>' or
        weather == '<ошибка на сервере погоды. попробуйте позже>'):
        return weather
    # Получите часть строки с температурой из weather и сохраните в temperature
    temperature = weather.split()[1]
    parsed_temperature = ''
    for char in temperature:
        if char == '-':
            char += parsed_temperature
        # Температура может быть и отрицательной, предусмотрите это:
        # если встретился символ "минус" — добавьте его в переменную parsed_temperature        
        try:
            num = int(char)
            
            # Попробуйте привести символ char к целому числу. 
            
            # Если символ приводится к числу — добавьте его в переменную parsed_temperature
            parsed_temperature += char
        except ValueError:
            continue
    return parsed_temperature

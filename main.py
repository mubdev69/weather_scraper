import requests
import os
from time import strftime
from datetime import datetime


try:
    import colorama
except:
    if ImportError:
        os.system("pip install colorama")



class WeatherScraper:
    def __init__(self, api_key):
        self.api_key = 'f2856ff1953b5e7cd88d92321e5810d2'
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
   

    def get_weather(self, city):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'  # or 'imperial' for Fahrenheit
        }
        try:
            response = requests.get(self.base_url, params=params)
            data = response.json()
            if data.get('cod') != 200:
                 print(colorama.Fore.RED+"Place not found :(")
                
            city = data['name']
            temp = data['main']['temp']
            feels = data['main']['feels_like']
            hum = data['main']['humidity']
            cn = data['sys']['country']
            clds = data['clouds']['all']
            vis = data['visibility']
            weather = data['weather'][0]['description']
            time = strftime("%H:%M")
            sunrise = data['sys']['sunrise']
            sunset = data['sys']['sunset']
            wind = data['wind']['speed']
            dir = data['wind']['deg']
            sunrise = datetime.fromtimestamp(sunrise)
            sunset = datetime.fromtimestamp(sunset)
            def angle_to_direction(angle):
             
                directions = {
         "N": (337.5, 22.5),
         "NE": (22.5, 67.5),
         "E": (67.5, 112.5),
         "SE": (112.5, 157.5),
         "S": (157.5, 202.5),
         "SW": (202.5, 247.5),
         "W": (247.5, 292.5),
         "NW": (292.5, 337.5)
    }
    
        
                angle = angle % 360

     
                for direction, (low, high) in directions.items():
                  if low <= angle < high or (low > high and (angle >= low or angle < high)):
                     return direction
        
            directions = angle_to_direction(dir)
            print(colorama.Fore.YELLOW + f"temperature : 🌡 {temp}°C")
            print(colorama.Fore.YELLOW + f"feels like : 🌡 {feels}°C")
            print(colorama.Fore.YELLOW + f"weather : {weather} ")
            print(colorama.Fore.YELLOW + f"clouds : ☁️ {clds}% ")
            print(colorama.Fore.YELLOW + f"wind : 💨 {wind}km/h ")
            print(colorama.Fore.YELLOW + f"wind direction: {directions} 🧭")
            print(colorama.Fore.YELLOW + f"humidity : 💧{hum}% ")
            print(colorama.Fore.YELLOW + f"visibility : 👁 {vis/1000}km ")
            print(colorama.Fore.YELLOW + f"sunrise : 🌅 {sunrise.time()}")
            print(colorama.Fore.YELLOW + f"sunset :  🌇 {sunset.time()}")
            print(colorama.Fore.YELLOW + f"city : 📌 {city},{cn} ")
            print(colorama.Fore.YELLOW + f"updated : 🕐 {time}")

        except:
            if ConnectionError:
                print(colorama.Fore.RED+"Connection Failed :(")
        
    


if __name__ == "__main__":
    api_key = 'f2856ff1953b5e7cd88d92321e5810d2'
    while 1:
        weather_scraper = WeatherScraper(api_key)
        print(colorama.Fore.GREEN+"\t ****** Made by Mubashir with ❤  ****** ")
        city = input(colorama.Fore.CYAN+"Enter city name: ")
        weather = weather_scraper.get_weather(city)
        if city == " ":
            continue
        else:
            continue
    
    

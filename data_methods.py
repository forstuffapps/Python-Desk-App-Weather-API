import requests
from os.path import *
import yaml
from yaml.loader import SafeLoader
from urllib.request import urlopen




class Weather():

    
    def __init__(self):
        

        self.abs_path_of_the_file = abspath(__file__)
        self.parent_path_file = dirname(self.abs_path_of_the_file)

        with open(self.parent_path_file+'/config.yaml', 'r') as f:
            data = list(yaml.load_all(f, Loader=SafeLoader))[0]
        
        

        self.__City_Name = data['City']
        self.__API_KEY = data['API_KEY']
        self.__Time_Interval = data['Interval']
        self.__URL = data['URL']
        self.__Image_URL = data['Image_URL']



    def get_api_data(self, city="q"):
        if city=="q":
            city = self.__City_Name
        url = self.__URL
        url = url.format(city, self.__API_KEY)
        response = requests.get(url)

        JSON_DATA = response.json()
        api_data= {}
        api_data['City'] = JSON_DATA['name']
        api_data['Country'] = JSON_DATA['sys']
        api_data['Temperature'] = JSON_DATA['main']['temp']
        api_data['Temperature'] -= 273.15
        api_data['Weather'] = JSON_DATA['weather'][0]['main']
        api_data['Image_ID'] = JSON_DATA['weather'][0]['icon']
        api_data['Info'] = [JSON_DATA['visibility'], JSON_DATA['wind']['speed'], 
        JSON_DATA['main']['humidity'], JSON_DATA['main']['pressure']]
        
        return api_data
    

    def get_image_raw_data(self, image_id):
        image_url = self.__Image_URL.format(image_id)
        image_instance = urlopen(image_url)
        Raw_Data = image_instance.read()
        image_instance.close()
        return Raw_Data
    

    def interval(self):
        return self.__Time_Interval
    


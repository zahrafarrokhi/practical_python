import discord
import os
import random
import requests
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


cities = {
  'tehran':{
      'lat':35.790240,
      'lon':51.425365
  },
  'esfahan':{
      'lat':32.647715,
      'lon':51.665297
  },
  'shiraz':{
      'lat':29.618418 ,
      'lon':52.507003
  },
  'ramsar':{
      'lat':36.919756,
      'lon':50.657446
  },
}

@bot.command(name='get_weather_loc', help='Get weather data with lat/lon')
async def get_weather_loc(ctx, lat: float, lon: float):
    response = requests.get('https://api.openweathermap.org/data/2.5/weather', {
        'lat' : lat,
        'lon': lon,
        'appid': os.getenv('API_KEY'),
        'units': 'metric',
    })
    data = response.json()
    
    
    await ctx.send(data['main']['temp'])

@bot.command(name='get_weather', help='Get weather data by city(tehran, shiraz, esfahan, ramsar)')
async def get_weather(ctx, city: str):
    response = requests.get('https://api.openweathermap.org/data/2.5/weather', {
        'lat': cities[city]['lat'],
        'lon': cities[city]['lon'],
        'appid': os.getenv('API_KEY'),
        'units': 'metric',
    })
    data = response.json()
    
    
    await ctx.send(data['main']['temp'])

bot.run(TOKEN)



    
  
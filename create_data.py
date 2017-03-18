import pandas as pd
import numpy as np
import billboard
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import requests

dates = [year for year in range(2008, 2017)]
danceability = []
energy = []
speechiness = []
successes = []
for year in dates:
	_id_ = []
	chart = billboard.ChartData('hot-100', date=str(year) + '-12-31')
	for song in chart:
		_id_.append(str(song.spotifyID))
	client_credentials_manager = SpotifyClientCredentials('Client ID', 'Client Secret')
	sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
	for i in _id_: 
		try:
			tid = 'spotify:track:' + i
			analysis = sp.audio_features(tid)
			results = json.dumps(analysis, indent=4)
			results = json.loads(results)
			danceability.append(results[0]['danceability'])
			energy.append(results[0]['energy'])
			speechiness.append(results[0]['speechiness'])
		except requests.exceptions.HTTPError:
			pass
		except TypeError:
			pass
	for song in chart:
		successes.append(song.weeks)

data = {'danceability': [d for d in danceability if d > 0.5], 'energy':[e for e in energy if e > 0.5], 'speechiness':[s for s in speechiness if s < 0.5], 'successes':successes}
# data['successes'] = data['succcesses'].replace([[s for s in successes if successes<1], [s for s in successes if successes>1]], [0,1])

dataframe = pd.DataFrame.from_dict(data, orient='index')
dataframe = dataframe.transpose()
dataframe.to_csv('prediction_data.csv')



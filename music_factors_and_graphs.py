import spotipy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import billboard
from spotipy.oauth2 import SpotifyClientCredentials
import json
import sys

chart = billboard.ChartData('hot-100', date='2016-12-31')

_id_ = []
for song in chart:
	_id_.append(str(song.spotifyID))

# successes = [song for song in chart if song.weeks > 1]
# print(successes)

client_credentials_manager = SpotifyClientCredentials('2b211ac7629d41699c48e4c5a9098ee3', '1373301210f141a1a9b7a60c684c5e05')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
# sp.trace=True

danceability = []
energy = []
tempo = []
speechiness = []
for i in _id_: 
	tid = 'spotify:track:' + i
	analysis = sp.audio_features(tid)
	results = json.dumps(analysis, indent=4)
	results = json.loads(results)
	try:
		danceability.append(results[0]['danceability'])
		energy.append(results[0]['energy'])
		tempo.append(results[0]['tempo'])
		speechiness.append(results[0]['speechiness'])
	except TypeError:
		pass

plt.figure()
plt.subplot(211)
plt.plot(danceability[int(len(danceability)/2):])
plt.title('Danceability in Top 100 hits - Lower 50')
plt.ylabel('Danceability')
plt.xlabel('Spot in Lower 50')
print('Danceability Mean (Lower 50): ' + str(np.mean(danceability[int(len(danceability)/2):])))
plt.subplot(212)
plt.plot(danceability[:int(len(danceability)/2)])
plt.title('Danceability in Top 100 hits - Top 50')
plt.ylabel('Danceability')
plt.xlabel('Spot in Top 50')
print('Danceability Mean (Top 50): ' + str(np.mean(danceability[:int(len(danceability)/2)])))
plt.tight_layout()
plt.savefig('danceability.png')


# plt.figure()
# plt.subplot(211)
# plt.plot(energy[int(len(energy)/2):])
# plt.title('Energy in Top 100 hits - Lower 50')
# plt.ylabel('Energy')
# plt.xlabel('Spot in Lower 50')
print('Energy Mean (Lower 50): ' + str(np.mean(energy[int(len(energy)/2):])))
# plt.subplot(212)
# plt.plot(energy[:int(len(energy)/2)])
# plt.title('Energy in Top 100 hits - Top 50')
# plt.ylabel('Energy')
# plt.xlabel('Spot in Top 50')
print('Energy Mean (Top 50): ' + str(np.mean(energy[:int(len(energy)/2)])))
# plt.tight_layout()
# plt.savefig('Energy.png')

# plt.figure()
# plt.subplot(211)
# plt.plot(tempo[int(len(tempo)/2):])
# plt.title('Tempo in Top 100 hits - Lower 50')
# plt.ylabel('Tempo')
# plt.xlabel('Spot in Lower 50')
print('Tempo Mean (Lower 50): ' + str(np.mean(tempo[int(len(tempo)/2):])))
# plt.subplot(212)
# plt.plot(tempo[:int(len(tempo)/2)])
# plt.title('Tempo in Top 100 hits - Top 50')
# plt.ylabel('Tempo')
# plt.xlabel('Spot in Top 50')
print('Tempo Mean (Top 50): ' + str(np.mean(tempo[:int(len(tempo)/2)])))
# plt.tight_layout()
# plt.savefig('Tempo.png')

# plt.figure()
# plt.subplot(211)
# plt.plot(speechiness[int(len(speechiness)/2):])
# plt.title('Speechiness in Top 100 hits - Lower 50')
# plt.ylabel('Speechiness')
# plt.xlabel('Spot in Lower 50')
print('Speechiness Mean (Lower 50): ' + str(np.mean(speechiness[int(len(speechiness)/2):])))
# plt.subplot(212)
# plt.plot(speechiness[:int(len(speechiness)/2)])
# plt.title('Speechiness in Top 100 hits - Top 50')
# plt.ylabel('Speechiness')
# plt.xlabel('Spot in Top 50')
print('Speechiness Mean (Top 50): ' + str(np.mean(speechiness[:int(len(speechiness)/2)])))
# plt.tight_layout()
# plt.savefig('Speechiness.png')


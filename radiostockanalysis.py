import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import billboard

data_pre = pd.read_csv('raio_pre.csv')
mean1 = np.mean(data_pre['Close'].get_values())

data_post = pd.read_csv('raio_post.csv')
mean2 = np.mean(data_post['Close'].get_values())

chart = billboard.ChartData('hot-100', date='2016-12-31')
successes = [song for song in chart if song.weeks > 1]
print(len(successes))

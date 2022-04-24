import NeuralNetwork as nn
import Data as dt
import json

MIN_NOISE = 10;
MAX_NOISE = 90;


def store_stats(stats):
	with open('statistics.txt', 'w') as f:
		json.dump(stats, f);


def load_stats():
	with open('statistics.txt', 'r') as f:
		stats = json.load(f);
	return stats;


def get_stats():
	computed_stats = [];
	for i in range(MIN_NOISE, MAX_NOISE+1, 10):
		model1 = nn.Model1(128);
		model2 = nn.Model2(128, 512, 256);
		data = dt.load_data(i);
		mse1, mae1, amse1 = nn.eval_model(model1, data);
		mse2, mae2, amse2 = nn.eval_model(model2, data);
		computed_stats.append({"noise"+str(i):{"model1": [mse1, mae1, amse1], "model2": [mse2, mae2, amse2]}});
	return computed_stats;
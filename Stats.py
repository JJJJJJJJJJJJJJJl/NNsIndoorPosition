import NeuralNetwork as nn
import Data as dt
import json


def convert_metric(metric):
	if metric == "mse":
		return 0;
	elif metric == "amae":
		return 1;
	elif metric == "mae":
		return 2;
	return -1;

def get_noise_values():
	noise_values = [];
	for i in range(dt.MIN_NOISE, dt.MAX_NOISE+1, 10):
		noise_values.append(i);
	return noise_values;


def store_stats(stats):
	with open('statistics.txt', 'w') as f:
		json.dump(stats, f);


def load_stats():
	with open('statistics.txt', 'r') as f:
		stats = json.load(f);
	return stats;


def get_stats(model_num, model, data):
	model_stats = nn.test_model(model_num, model, data);
	return model_stats;
	
import NeuralNetwork as nn
import Data as dt
import random

# raw model predictions
def model_predictions(model, data):
	predictions = model.predict(data.test_phases)
	mean_abs_error = 0;
	for i in range(0, predictions.shape[0]):
		mean_abs_error = mean_abs_error + abs((data.test_labels[i]*360) - (predictions[i][0]*360));
		#print("label: (", data.test_labels[i],",", data.test_labels[i]*360, ") - guess: (", predictions[i][0], ",", predictions[i][0]*360, ")");
	mean_abs_error = mean_abs_error/36000;
	print("mean_abs_error: ", mean_abs_error);

def compile_model(model):
	# compiling the model
	model.compile(optimizer='adam',
					#tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
				#loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
				loss = "mse",
				metrics=['mean_squared_error', 'mean_absolute_error']); #rootmeansqaurederror
	return model;

def eval_model1():
	data = dt.Dataset(30);
	data.normalize_data();
	print('train_phases:', data.train_phases.shape, data.train_phases.min(), data.train_phases.max(), data.train_phases.dtype);
	print('test_phases:', data.test_phases.shape, data.test_phases.min(), data.test_phases.max(), data.test_phases.dtype);
	print('train_labels:', data.train_labels.shape, data.train_labels.min(), data.train_labels.max(), data.train_labels.dtype);
	print('test_labels:', data.test_labels.shape, data.test_labels.min(), data.test_labels.max(), data.test_labels.dtype);

	model = nn.Model1(128);
	model = compile_model(model);
	model.fit(data.train_phases, data.train_labels, epochs=15);
	test_loss, test_mse, test_mae = model.evaluate(data.test_phases,  data.test_labels, verbose=2);

	print('\n(TEST) Mean Squared Error:', test_mse);
	print('(TEST) Mean Absolute Error:', test_mae);

	model_predictions(model, data);

def eval_model2():
	data = dt.Dataset(30);
	data.normalize_data();
	print('train_phases:', data.train_phases.shape, data.train_phases.min(), data.train_phases.max(), data.train_phases.dtype);
	print('test_phases:', data.test_phases.shape, data.test_phases.min(), data.test_phases.max(), data.test_phases.dtype);
	print('train_labels:', data.train_labels.shape, data.train_labels.min(), data.train_labels.max(), data.train_labels.dtype);
	print('test_labels:', data.test_labels.shape, data.test_labels.min(), data.test_labels.max(), data.test_labels.dtype);

	model = nn.Model2(128, 512, 256);
	model = compile_model(model);
	model.fit(data.train_phases, data.train_labels, epochs=15);
	test_loss, test_mse, test_mae = model.evaluate(data.test_phases,  data.test_labels, verbose=2);

	print('\n(TEST) Mean Squared Error:', test_mse);
	print('(TEST) Mean Absolute Error:', test_mae);

	model_predictions(model, data);

def main():
	eval_model1();
	eval_model2();

main();
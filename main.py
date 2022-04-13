import NeuralNetwork as nn
import Data as dt

def main():
	data = dt.LoadDataset(10);
	print('train_phases:', data.train_phases.shape, data.train_phases.min(), data.train_phases.max(), data.train_phases.dtype);
	print('test_phases:', data.test_phases.shape, data.test_phases.min(), data.test_phases.max(), data.test_phases.dtype);
	data.normalize_data();
	print('train_phases:', data.train_phases.shape, data.train_phases.min(), data.train_phases.max(), data.train_phases.dtype);
	print('test_phases:', data.test_phases.shape, data.test_phases.min(), data.test_phases.max(), data.test_phases.dtype);

	model = nn.Model1(128);
	#model = nn.Model2(128, 512, 256);

	# compiling the model
	model.compile(optimizer='adam',
					#tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
				#loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
				loss = "mse",
				metrics=['mean_squared_error', 'mean_absolute_error']); #rootmeansqaurederror
	# training the model
	model.fit(data.train_phases, data.train_labels, epochs=10);

	# testing the model
	test_loss, test_mse, test_mae = model.evaluate(data.test_phases,  data.test_labels, verbose=2);

	print('\nMean Squared Error:', test_mse);
	print('Mean Absolute Error:', test_mae);

	"""
	predictions = model.predict(test_phases)
	print("predictions_shape: ", predictions.shape);
	for i in range(0, predictions.shape[0]):
	if random.random() >= 0.5:
		print("label: ", test_labels[i], " - guess: ", predictions[i][0]);
	"""

main();
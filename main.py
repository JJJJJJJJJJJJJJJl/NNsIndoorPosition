import NeuralNetwork as nn
import Data as dt

def load_data():
	data = dt.Dataset(10);
	data.normalize_data();
	print('train_phases:', data.train_phases.shape, data.train_phases.min(), data.train_phases.max(), data.train_phases.dtype);
	print('test_phases:', data.test_phases.shape, data.test_phases.min(), data.test_phases.max(), data.test_phases.dtype);
	print('train_labels:', data.train_labels.shape, data.train_labels.min(), data.train_labels.max(), data.train_labels.dtype);
	print('test_labels:', data.test_labels.shape, data.test_labels.min(), data.test_labels.max(), data.test_labels.dtype);
	return data;

# raw model predictions
def model_predictions(model, data):
	predictions = model.predict(data.test_phases)
	mean_abs_error = 0;
	for i in range(0, predictions.shape[0]):
		mean_abs_error = mean_abs_error + abs((data.test_labels[i]*360) - (predictions[i][0]*360));
	mean_abs_error = mean_abs_error/36000;
	return mean_abs_error;

def compile_model(model):
	# compiling the model
	model.compile(optimizer='adam',
					#tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
				#loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
				loss = "mse",
				metrics=['mean_squared_error', 'mean_absolute_error']); #rootmeansqaurederror
	return model;

def eval_model1(data):
	model = nn.Model1(128);
	model = compile_model(model);
	model.fit(data.train_phases, data.train_labels, epochs=1);
	test_loss, test_mse, test_mae = model.evaluate(data.test_phases,  data.test_labels, verbose=2);
	angle_mean_abs_error = model_predictions(model, data);
	return test_mse, test_mae, angle_mean_abs_error;

def eval_model2(data):
	model = nn.Model2(128, 512, 256);
	model = compile_model(model);
	model.fit(data.train_phases, data.train_labels, epochs=1);
	test_loss, test_mse, test_mae = model.evaluate(data.test_phases,  data.test_labels, verbose=2);
	angle_mean_abs_error =  model_predictions(model, data);
	return test_mse, test_mae, angle_mean_abs_error;

def main():
	data = load_data();
	mse1, mae1, amse1 = eval_model1(data);
	mse2, mae2, amse2 = eval_model2(data);
	print("mse1: ", mse1, "mae1: ", mae1, "amse1: ", amse1);
	print("mse2: ", mse2, "mae2: ", mae2, "amse2: ", amse2);

main();
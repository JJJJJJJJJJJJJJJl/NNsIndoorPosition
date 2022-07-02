import NeuralNetwork as nn
import Data as dt
import Stats as st
import VisualStats as vs

def main():
	#loading data
	""" data = dt.load_data(); """

	# Models creation 
	""" model1 = nn.Model1(128);
	model2 = nn.Model2(128, 512, 256);
	model3 = nn.Model3(128, 512, 256); """

	# Models training
	""" nn.train_model(model1, data);
	nn.train_model(model2, data);
	nn.train_model(model3, data); """

	# Models storing
	""" nn.save_models(1, model1);
	nn.save_models(2, model2);
	nn.save_models(3, model3); """

	# Models loading (if they exist)
	""" model1 = load_model(1);
	model2 = load_model(2);
	model3 = load_model(3); """

	# Models testing + Statistics collection
	""" model1_stats = st.get_stats(1, model1, data)
	model2_stats = st.get_stats(2, model2, data)
	model3_stats = st.get_stats(3, model3, data) """
	
	# Statistics storing
	""" all_stats = {"stats":[model1_stats, model2_stats, model3_stats]};
	print(all_stats);
	st.store_stats(all_stats); """

	#load statistics + show graphs
	loaded_stats = st.load_stats();
	vs.show_graph("Mean Squared Error", 
		vs.get_metric_values(st.convert_metric("mse"), loaded_stats, 1),
		vs.get_metric_values(st.convert_metric("mse"), loaded_stats, 2),
		vs.get_metric_values(st.convert_metric("mse"), loaded_stats, 3),
		st.get_noise_values());
	vs.show_graph("Mean Absolute Error", 
		vs.get_metric_values(st.convert_metric("mae"), loaded_stats, 1),
		vs.get_metric_values(st.convert_metric("mae"), loaded_stats, 2),
		vs.get_metric_values(st.convert_metric("mae"), loaded_stats, 3),
		st.get_noise_values());
	vs.show_graph("Angle Mean Absolute Error", 
		vs.get_metric_values(st.convert_metric("amae"), loaded_stats, 1),
		vs.get_metric_values(st.convert_metric("amae"), loaded_stats, 2),
		vs.get_metric_values(st.convert_metric("amae"), loaded_stats, 3),
		st.get_noise_values());

	# ploting models
	""" data = dt.load_data(10);
	model1 = nn.Model1(128);
	model1 = nn.compile_model(model1);
	model1.fit(data.train_phases, data.train_labels, epochs=1);
	nn.plot_model(model1, "model1.png");
	model2 = nn.Model2(128, 512, 256);
	model2 = nn.compile_model(model2);
	model2.fit(data.train_phases, data.train_labels, epochs=1);
	nn.plot_model(model2, "model2.png");
	data = dt.load_data(10);
	model3 = nn.Model3(128, 512, 256);
	model3 = nn.compile_model(model3);
	model3.fit(data.train_phases, data.train_labels, epochs=1);
	nn.plot_model(model3, "model3.png"); """

main();
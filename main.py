import NeuralNetwork as nn
import Data as dt
import Stats as st
import VisualStats as vs

def main():
	#train/test models + get/save statistics
	""" stats = st.get_stats();
	st.store_stats(stats); """

	#load statistics + show graphs
	""" loaded_stats = st.load_stats();
	vs.show_graph("Mean Squared Error", 
		vs.get_metric_values(st.convert_metric("mse"),loaded_stats, "model1"),
		vs.get_metric_values(st.convert_metric("mse"),loaded_stats, "model2"),
		st.get_noise_values());
	vs.show_graph("Mean Absolute Error", 
		vs.get_metric_values(st.convert_metric("mae"),loaded_stats, "model1"),
		vs.get_metric_values(st.convert_metric("mae"),loaded_stats, "model2"),
		st.get_noise_values());
	vs.show_graph("Angle Mean Absolute Error", 
		vs.get_metric_values(st.convert_metric("amae"),loaded_stats, "model1"),
		vs.get_metric_values(st.convert_metric("amae"),loaded_stats, "model2"),
		st.get_noise_values()); """

	# ploting models
	""" data = dt.load_data(10);
	model1 = nn.Model1(128);
	model1 = nn.compile_model(model1);
	model1.fit(data.train_phases, data.train_labels, epochs=1);
	nn.plot_model(model1, "model1.png");
	model2 = nn.Model2(128, 512, 256);
	model2 = nn.compile_model(model2);
	model2.fit(data.train_phases, data.train_labels, epochs=1);
	nn.plot_model(model2, "model2.png"); """

main();
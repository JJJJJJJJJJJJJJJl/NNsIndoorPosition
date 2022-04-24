import NeuralNetwork as nn
import Stats as st

def main():
	stats = st.get_stats();
	for i in range (st.MIN_NOISE, st.MAX_NOISE+1, 10):
		i = (int)((i-1)/10);
		noise = (i+1)*10;
		print("Noise", noise);
		noise_stats = stats[i]["noise"+str(noise)];
		print(noise_stats["model1"][0], noise_stats["model1"][1], noise_stats["model1"][2]);
		print(noise_stats["model2"][0], noise_stats["model2"][1], noise_stats["model2"][2]);
	st.store_stats(stats);

	loaded_stats = st.load_stats();
	print(loaded_stats);
	""" data = dt.load_data(30);
	mse1, mae1, amse1 = nn.eval_model(nn.Model1(128), data);
	mse2, mae2, amse2 = nn.eval_model(nn.Model2(128, 512, 256), data);
	print("mse1: ", mse1, "mae1: ", mae1, "amse1: ", amse1);
	print("mse2: ", mse2, "mae2: ", mae2, "amse2: ", amse2); """

main();
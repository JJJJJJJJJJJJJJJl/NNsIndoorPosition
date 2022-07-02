import matplotlib.pyplot as plt

"""
metric (mapped number):
    - mse: 0
    - amae: 1
    - mae: 2
model: model1 or model2
"""
def get_metric_values(metric, data, model):
    metric_values = [];
    model_stats = data['stats'][model-1][str(model)];
    for i in range(1,10):
        noise = "noise" + str(i*10);
        metric_values.append(model_stats[i-1][noise][metric]);
    return metric_values;

"""
metric (string): 
    - mean squared error
    - mean absolute error
    - angle mean absolute error
model1_stats: array containing model1 stat values
model2_stats: array containing model2 stat values
noise_values: array containing all noise values [10..90]
"""
def show_graph(metric, model1_stats, model2_stats, model3_stats, noise_values):
    plt.plot(noise_values, model1_stats, label="Model1");
    plt.plot(noise_values, model2_stats, label="Model2");
    plt.plot(noise_values, model3_stats, label="Model3");
    plt.xlabel("Noise");
    plt.ylabel(metric);
    plt.legend();
    plt.show();

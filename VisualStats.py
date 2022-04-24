import matplotlib.pyplot as plt

"""
metric (mapped number):
    - mse: 0
    - mae: 1
    - amae: 2
model: model1 or model2
"""
def get_metric_values(metric, data, model):
    metric_values = [];
    for i in range(0,9):
        noise = "noise" + str((i+1)*10)
        metric_values.append(data[i][noise][model][metric]);
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
def show_graph(metric, model1_stats, model2_stats, noise_values):
    plt.plot(noise_values, model1_stats, label="Model1");
    plt.plot(noise_values, model2_stats, label="Model2");
    plt.xlabel("Noise");
    plt.ylabel(metric);
    #plt.legend();
    plt.show();

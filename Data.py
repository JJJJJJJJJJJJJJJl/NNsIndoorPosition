import numpy as np

class Dataset:
    def __init__(self, noise):
        #load train data
        train_dataset_path = "./dataset_generator/generation/train_data_" + str(noise) + "noise.csv";
        print("Loading.: ", train_dataset_path);
        train_data = np.genfromtxt(train_dataset_path, delimiter=',');
        #assigning train data
        self.train_labels = train_data[:,8];
        self.train_phases = train_data = np.delete(train_data,8,1);

        #load test data
        test_dataset_path = "./dataset_generator/generation/test_data_"+ str(noise) + "noise.csv";
        print("Loading.: ", test_dataset_path);
        test_data = np.genfromtxt(test_dataset_path, delimiter=',');
        #assigning test data
        self.test_labels = test_data[:,8];
        self.test_phases = test_data = np.delete(test_data,8,1);

    def normalize_data(self):
        self.train_phases = (self.train_phases + 180) / 360;  #X_train
        self.test_phases = (self.test_phases + 180) / 360;  #X_test
        self.train_labels = self.train_labels / 360;  #Y_train
        self.test_labels = self.test_labels / 360;   #Y_test

def load_data(noise):
	data = Dataset(noise);
	data.normalize_data();
	print('train_phases:', data.train_phases.shape, data.train_phases.min(), data.train_phases.max(), data.train_phases.dtype);
	print('test_phases:', data.test_phases.shape, data.test_phases.min(), data.test_phases.max(), data.test_phases.dtype);
	print('train_labels:', data.train_labels.shape, data.train_labels.min(), data.train_labels.max(), data.train_labels.dtype);
	print('test_labels:', data.test_labels.shape, data.test_labels.min(), data.test_labels.max(), data.test_labels.dtype);
	return data;
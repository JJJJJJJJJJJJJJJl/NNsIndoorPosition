import numpy as np

class LoadDataset:
    def __init__(self, noise):
        #load train data
        train_data = np.genfromtxt("./dataset_generator/generation/train_data_" + str(30) + "noise.csv", delimiter=',');
        #assigning train data
        self.train_labels = train_data[:,8];
        self.train_phases = train_data = np.delete(train_data,8,1);

        #load test data
        test_data = np.genfromtxt("./dataset_generator/generation/test_data_"+ str(30) + "noise.csv", delimiter=',');
        #assigning test data
        self.test_labels = test_data[:,8];
        self.test_phases = test_data = np.delete(test_data,8,1);

    def normalize_data(self):
        self.train_phases = (self.train_phases + 180) / 360;  #X_train
        self.test_phases = (self.test_phases + 180) / 360;  #X_test
        self.train_labels = self.train_labels / 360;  #Y_train
        self.test_labels = self.test_labels / 360;   #Y_test
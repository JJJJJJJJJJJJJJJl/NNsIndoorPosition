import tensorflow as tf

class NeuralNetwork(tf.keras.Model):
    #create layers
    def __init__(self, hidden_nodes):
        super().__init__()
        self.hidden = tf.keras.layers.Dense(hidden_nodes, input_shape=(8,), activation='relu');
        self.mouth = tf.keras.layers.Dense(1);
    
    #link layers
    def call(self, input):
        forward = self.hidden(input);
        return self.mouth(forward);
        
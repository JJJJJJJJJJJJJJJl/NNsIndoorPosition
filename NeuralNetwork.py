import tensorflow as tf

class Model1(tf.keras.Model):
    #create layers
    def __init__(self, hidden_nodes):
        super().__init__();
        self.hidden = tf.keras.layers.Dense(hidden_nodes, input_shape=(8,), activation='relu');
        self.mouth = tf.keras.layers.Dense(1, activation='linear');
    
    #link layers
    def call(self, input):
        forward = self.hidden(input);
        return self.mouth(forward);

class Model2(tf.keras.Model):
    def __init__(self, hidden_nodes1, hidden_nodes2, hidden_nodes3):
        super().__init__();
        self.dense1 = tf.keras.layers.Dense(hidden_nodes1, input_shape=(8,), kernel_initializer='normal', activation='relu');
        self.dense2 = tf.keras.layers.Dense(hidden_nodes2, kernel_initializer='normal', activation='relu');
        self.dense3 = tf.keras.layers.Dense(hidden_nodes3, kernel_initializer='normal', activation='relu');
        self.mouth = tf.keras.layers.Dense(1, kernel_initializer='normal', activation='linear');

    def call(self, input):
        layer = self.dense1(input);
        layer = self.dense2(layer);
        layer = self.dense3(layer);
        return self.mouth(layer); 
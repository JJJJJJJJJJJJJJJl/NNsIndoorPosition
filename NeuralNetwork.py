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

    def build_graph(self):
        x = tf.keras.layers.Input(shape=((8,)));
        return tf.keras.Model(inputs=[x], outputs=self.call(x));

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
    
    def build_graph(self):
        x = tf.keras.layers.Input(shape=((8,)));
        return tf.keras.Model(inputs=[x], outputs=self.call(x));

class Model3(tf.keras.Model):
    def __init__(self, hidden_nodes1, hidden_nodes2, hidden_nodes3):
        super().__init__();
        self.entry_reshape = tf.keras.layers.Reshape((8,1), input_shape=(8,));
        self.conv1 = tf.keras.layers.Conv1D(filters=32, kernel_size=3, padding="same", activation='relu', input_shape=(8,1));
        self.max_pool1 = tf.keras.layers.MaxPooling1D(2);
        self.conv2 = tf.keras.layers.Conv1D(filters=64, kernel_size=3, padding="same", activation='relu');
        self.max_pool2 = tf.keras.layers.MaxPooling1D(2);
        self.conv3 = tf.keras.layers.Conv1D(filters=64, kernel_size=3, padding="same", activation='relu');
        self.flat = tf.keras.layers.Flatten();
        self.dense1 = tf.keras.layers.Dense(hidden_nodes1, input_shape=(8,), kernel_initializer='normal', activation='relu');
        self.dense2 = tf.keras.layers.Dense(hidden_nodes2, kernel_initializer='normal', activation='relu');
        self.dense3 = tf.keras.layers.Dense(hidden_nodes3, kernel_initializer='normal', activation='relu');
        self.mouth = tf.keras.layers.Dense(1, kernel_initializer='normal', activation='linear');

    def call(self, input):
        layer = self.entry_reshape(input);
        layer = self.conv1(layer);
        layer = self.max_pool1(layer);
        layer = self.conv2(layer);
        layer = self.max_pool2(layer);
        layer = self.conv3(layer);
        layer = self.flat(layer);
        layer = self.dense1(layer);
        layer = self.dense2(layer);
        layer = self.dense3(layer);
        return self.mouth(layer);
    
    def build_graph(self):
        x = tf.keras.layers.Input(shape=((8,)));
        return tf.keras.Model(inputs=[x], outputs=self.call(x));

def plot_model(model, file):
    tf.keras.utils.plot_model(
        model.build_graph(),
        to_file=file,
        show_shapes=True,
        show_layer_names=True,
        dpi=96,
        show_layer_activations=True
    )

# raw model predictions
def angle_mean_absolute_error(model, data):
	predictions = model.predict(data.test_phases)
	mean_abs_error = 0;
	for i in range(0, predictions.shape[0]):
		mean_abs_error = mean_abs_error + abs((data.test_labels[i]*360) - (predictions[i][0]*360));
	mean_abs_error = mean_abs_error/72000;
	return mean_abs_error;

def compile_model(model):
	model.compile(optimizer='adam',
				loss = "mse",
				metrics=['mean_squared_error', 'mean_absolute_error']);
	return model;

def eval_model(model, data):
	print("Evaluating model", model);
	model = compile_model(model);
	model.fit(data.train_phases, data.train_labels, epochs=15);
	test_loss, test_mse, test_mae = model.evaluate(data.test_phases,  data.test_labels, verbose=2);
	angle_mean_abs_error = angle_mean_absolute_error(model, data);
	return test_mse, test_mae, angle_mean_abs_error;
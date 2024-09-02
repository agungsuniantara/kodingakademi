import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import json
import pickle

# Load and preprocess data
intents_file = open('dataset.json').read()
intents = json.loads(intents_file)

X = []  # Patterns
y = []  # Intent tags

for intent in intents['intents']:
    for pattern in intent['patterns']:
        X.append(pattern)
        y.append(intent['tag'])

# Tokenize and create bag-of-words representation
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X).toarray()

# Convert intent tags to numerical labels
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Split the dataset into training and testing sets
train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the model
model = Sequential()
model.add(Dense(128, input_shape=(X.shape[1],), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(len(set(y)), activation='softmax'))

# Compile the model
sgd = SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
model.compile(loss='sparse_categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Train the model
model.fit(train_x, train_y, epochs=100, batch_size=5, verbose=1)

# Evaluate the model
loss, accuracy = model.evaluate(test_x, test_y, verbose=0)
print("Loss:", loss)
print("Accuracy:", accuracy)

# Save the model and label encoder
model.save('chatbot_model.h5')

# Save the vectorizer and label encoder for future use
with open('vectorizer.pkl', 'wb') as file:
    pickle.dump(vectorizer, file)

with open('label_encoder.pkl', 'wb') as file:
    pickle.dump(label_encoder, file)

print("Model, vectorizer, and label encoder created and saved.")
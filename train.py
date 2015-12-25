import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM

model = Sequential()
model.add(Embedding(4, 16, input_length=4))
model.add(LSTM(output_dim=128, activation='sigmoid', inner_activation='hard_sigmoid'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='rmsprop')

X = [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [1, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 0], [1, 1, 1, 1], [1, 0, 1, 1], [2, 1, 1, 1], [1, 1, 0, 1], [0, 0, 0, 0], [1, 2, 1, 2], [0, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 2], [0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 2, 1], [1, 0, 0, 1], [1, 2, 2, 1], [1, 0, 1, 1], [0, 0, 0, 0], [1, 1, 2, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 2], [1, 1, 1, 0], [1, 1, 1, 2], [0, 0, 0, 0], [0, 1, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [1, 2, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 1, 1], [0, 1, 1, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [1, 1, 1, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 2, 1], [1, 2, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0], [1, 2, 2, 1], [1, 0, 0, 1], [1, 1, 1, 1], [0, 1, 0, 1], [1, 1, 1, 1], [0, 0, 0, 0], [1, 0, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0], [1, 1, 1, 2], [1, 1, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1], [0, 0, 0, 0], [1, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [1, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 2, 2, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 2, 1], [1, 1, 1, 1], [1, 1, 0, 1], [1, 2, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 2, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2, 1, 1, 1], [1, 1, 2, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 2, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 1, 2], [1, 2, 2, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 1], [2, 1, 1, 1], [1, 1, 1, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 2, 1, 1], [0, 0, 0, 0], [1, 1, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2, 1, 1, 1], [0, 0, 0, 0], [1, 0, 1, 1], [1, 1, 1, 2], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 2], [0, 0, 0, 0], [1, 2, 1, 1], [1, 2, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 0, 1], [1, 1, 0, 1], [0, 0, 0, 0], [1, 1, 2, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0], [1, 2, 2, 2], [0, 0, 0, 0], [1, 1, 0, 1], [0, 0, 0, 1], [1, 1, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 1], [1, 0, 0, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 2, 1], [1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 1], [0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0], [1, 1, 1, 1], [1, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 1, 1], [0, 0, 0, 0], [1, 1, 2, 1], [1, 1, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 2, 1], [1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 2], [2, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0], [1, 1, 2, 1], [1, 1, 1, 1], [1, 1, 1, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [1, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 2, 1, 2], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0], [0, 1, 0, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 1], [1, 0, 1, 0], [1, 1, 1, 1], [2, 1, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1], [1, 1, 1, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [0, 0, 0, 0], [1, 0, 0, 0], [1, 1, 1, 2], [0, 0, 0, 0], [0, 1, 1, 0], [1, 1, 1, 1], [1, 2, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [2, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 1], [1, 1, 1, 2], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [1, 0, 0, 1], [1, 1, 2, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2, 2, 2, 2], [0, 1, 1, 1], [0, 0, 0, 0], [1, 1, 2, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [1, 2, 1, 1], [1, 1, 0, 1], [1, 2, 1, 1], [1, 2, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [2, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 2, 2, 2], [0, 1, 0, 0], [1, 2, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0], [2, 1, 1, 1], [1, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 1], [1, 2, 1, 1], [0, 1, 1, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 2], [0, 0, 0, 0], [1, 1, 0, 1], [0, 0, 0, 0], [2, 1, 2, 1], [0, 0, 0, 1], [1, 1, 1, 2], [1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 2, 1], [1, 2, 1, 2], [1, 1, 1, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 2, 1], [0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 2, 1], [0, 0, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 1], [0, 1, 0, 1], [1, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 2], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [2, 1, 1, 1], [0, 1, 1, 1], [0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 2, 1], [0, 0, 0, 0], [1, 0, 1, 0], [0, 0, 0, 0], [1, 0, 0, 1], [0, 0, 0, 0], [0, 1, 1, 1], [2, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [2, 2, 1, 1], [2, 2, 1, 1], [0, 0, 0, 0], [2, 1, 1, 1], [1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 2], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [1, 0, 1, 0], [0, 1, 1, 0], [2, 2, 1, 2], [0, 0, 0, 0], [0, 0, 0, 1], [2, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 2], [1, 0, 0, 1], [1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 0], [1, 0, 1, 0], [1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 2], [1, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 2, 1, 2], [1, 2, 1, 2], [0, 0, 0, 0], [2, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [2, 1, 1, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 0], [1, 1, 2, 2], [1, 2, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 2, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 1], [1, 0, 1, 1], [0, 0, 0, 0], [0, 1, 1, 1], [1, 1, 1, 0], [0, 0, 0, 0], [1, 1, 1, 0], [1, 1, 1, 1], [0, 0, 0, 0], [1, 2, 2, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 1, 1], [1, 1, 1, 1], [1, 1, 1, 2], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 2, 1, 1], [0, 0, 0, 0], [1, 0, 1, 0], [1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [1, 2, 1, 1], [0, 0, 0, 0], [0, 1, 1, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 1, 1], [0, 0, 0, 0], [1, 2, 2, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 0, 1], [1, 0, 1, 0], [0, 1, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0], [1, 1, 2, 1], [0, 1, 0, 0], [0, 1, 1, 0], [2, 2, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 2, 2, 1], [1, 1, 1, 1], [0, 0, 0, 0], [2, 1, 2, 1], [1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 1, 0, 1], [0, 0, 0, 0], [1, 1, 1, 2], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0], [1, 1, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 2], [1, 0, 1, 0], [1, 0, 1, 0], [2, 1, 1, 2], [0, 0, 0, 0], [0, 1, 1, 0], [1, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2, 1, 2, 1], [0, 0, 0, 0], [1, 1, 2, 1], [1, 0, 1, 1], [1, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 1, 1, 2], [1, 2, 1, 1], [0, 0, 0, 0], [2, 1, 1, 1], [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 2, 1, 1], [1, 0, 0, 1], [0, 0, 0, 0], [1, 1, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 2, 1], [1, 0, 1, 1], [1, 1, 1, 0], [1, 1, 1, 0], [0, 1, 1, 1], [0, 1, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 1, 0, 1], [0, 0, 0, 0], [1, 0, 0, 0], [1, 1, 2, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 2, 1, 1], [2, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0], [1, 1, 0, 1], [0, 0, 0, 0], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 2, 1], [0, 1, 0, 1], [1, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 1], [1, 1, 1, 1], [0, 1, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2, 1, 1, 1], [1, 1, 1, 2], [1, 1, 1, 2], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 0], [2, 1, 1, 1], [0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [2, 1, 1, 2], [1, 0, 1, 0], [0, 0, 0, 0], [1, 0, 1, 1], [1, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 1, 1], [2, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [1, 1, 1, 1], [1, 1, 2, 1], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [1, 0, 0, 1], [0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1], [0, 0, 0, 0], [0, 0, 1, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 1, 1], [1, 2, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0], [0, 0, 0, 0], [1, 1, 1, 0], [0, 0, 0, 1], [1, 2, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 1], [0, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 1], [2, 1, 1, 1], [0, 1, 1, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1], [0, 0, 0, 0], [1, 2, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 0], [0, 0, 0, 0], [1, 2, 1, 1], [1, 1, 1, 2], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 0], [1, 1, 1, 1], [2, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 1, 1], [1, 0, 0, 1], [1, 0, 1, 1]]
Y = [0.0, 0.5, 0.0, 0.5, 1.0, 0.0, 0.0, 1.0, 0.5, 1.0, 0.5, 0.0, 1.0, 0.0, 1.0, 0.5, 0.0, 0.0, 0.5, 0.5, 0.5, 1.0, 0.5, 1.0, 0.0, 0.0, 1.0, 0.0, 0.5, 0.0, 0.5, 0.5, 0.5, 0.0, 1.0, 0.5, 0.0, 1.0, 0.5, 0.0, 0.5, 0.5, 1.0, 1.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.5, 1.0, 0.0, 0.5, 1.0, 0.5, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.5, 0.0, 1.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.5, 1.0, 0.5, 0.5, 0.0, 1.0, 0.5, 0.0, 0.5, 0.5, 0.0, 0.0, 1.0, 0.5, 0.5, 1.0, 0.0, 1.0, 1.0, 0.0, 0.5, 1.0, 0.0, 0.5, 0.5, 0.0, 0.5, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.5, 1.0, 0.5, 1.0, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.5, 1.0, 0.5, 0.0, 0.0, 0.5, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.5, 1.0, 1.0, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.5, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.5, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.5, 0.0, 0.5, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, 1.0, 0.5, 0.5, 0.0, 0.5, 1.0, 1.0, 1.0, 0.5, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, 0.0, 0.0, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0, 0.5, 0.5, 0.5, 0.0, 1.0, 1.0, 0.5, 1.0, 0.0, 0.5, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.5, 0.0, 1.0, 0.5, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0, 0.0, 0.0, 0.5, 0.0, 0.5, 0.0, 1.0, 0.5, 0.0, 0.0, 0.5, 0.5, 0.0, 0.5, 0.5, 1.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, 1.0, 0.5, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0, 0.0, 1.0, 1.0, 0.5, 0.0, 0.0, 0.5, 0.0, 1.0, 0.5, 0.0, 1.0, 0.5, 0.0, 1.0, 0.0, 0.0, 0.0, 0.5, 0.0, 1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.5, 1.0, 0.5, 0.0, 0.0, 0.0, 0.5, 0.0, 0.5, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.5, 1.0, 0.0, 0.0, 0.5, 1.0, 0.5, 1.0, 1.0, 0.0, 0.0, 0.5, 0.5, 1.0, 0.0, 0.5, 0.0, 1.0, 0.0, 0.5, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.5, 0.0, 0.5, 0.0, 0.5, 0.0, 0.5, 0.0, 0.0, 0.0, 0.5, 0.0, 1.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.5, 1.0, 0.5, 1.0, 0.5, 1.0, 0.0, 0.5, 0.0, 0.5, 0.0, 0.5, 0.0, 0.0, 1.0, 0.0, 0.5, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0, 0.5, 1.0, 0.0, 0.5, 0.0, 0.5, 0.5, 0.5, 0.0, 1.0, 1.0, 1.0, 0.5, 1.0, 0.0, 0.0, 0.0, 1.0, 0.5, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 1.0, 0.5, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.5, 0.5, 0.0, 1.0, 0.5, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.5, 1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.5, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.5, 0.5, 0.0, 1.0, 0.5, 0.0, 1.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.5, 0.0, 0.0, 0.0, 0.5, 0.5, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0, 1.0, 0.0, 0.0, 0.5, 0.0, 0.5, 1.0, 0.0, 0.5, 0.5, 0.5, 0.0, 0.5, 1.0, 1.0, 0.0, 0.0, 0.5, 0.0, 0.0, 0.5, 0.0, 0.5, 1.0, 0.0, 0.5, 0.0, 0.5, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.5, 0.0, 0.0, 0.5, 0.5, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.5, 0.5, 0.0, 0.5, 0.0, 0.5, 0.5, 1.0, 0.0, 0.5, 0.5, 1.0, 0.5, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.5, 1.0, 0.5, 1.0, 0.5, 1.0, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0, 0.5, 1.0, 0.0, 0.5, 0.5, 0.0, 1.0, 0.5, 1.0, 0.0, 0.0, 1.0, 1.0, 0.5, 1.0, 0.5, 0.0, 1.0, 0.0, 1.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 1.0, 1.0, 1.0, 0.5, 0.5, 0.5, 0.0, 0.5, 0.0, 0.5, 0.0, 0.5, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.5, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.5, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.5, 0.0, 1.0, 0.5, 1.0, 0.5, 1.0, 0.0, 0.0, 0.5, 0.0, 0.5, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.5, 0.5, 0.0, 1.0, 0.5, 0.0, 0.5, 0.0, 0.5, 0.5, 1.0, 0.0, 1.0, 0.0, 1.0, 0.5, 0.0, 1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 1.0, 0.0, 0.5, 0.0, 0.5, 0.0, 1.0, 0.5, 0.0, 0.0, 0.0, 0.5, 0.5, 1.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.5, 0.0, 0.5, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.5, 0.0, 0.0, 0.5, 0.0, 0.0, 0.5, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.5, 1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 1.0, 0.0, 0.5, 1.0, 0.5, 0.0, 1.0, 0.0, 0.0, 1.0, 0.5, 0.5, 1.0, 0.5, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 1.0, 0.5, 0.0, 1.0, 0.5, 0.5, 1.0, 0.5, 0.5, 0.5, 1.0, 0.5, 0.5, 0.0, 0.5, 0.0, 0.5, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.5, 0.0, 0.5, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 1.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.5, 0.0, 1.0, 0.5, 0.0, 0.0, 1.0, 0.0, 1.0, 0.5, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0]

model.fit(np.array(X[:900]), np.array(Y[:900]), batch_size=16, nb_epoch=10)
print model.predict(np.array(X[900:]))
print Y[900:]

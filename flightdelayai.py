import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
def probability(schedtime, carrier, distance, flightnum, weather, dayweek, daymonth):
  dataset = pd.read_csv("data.csv")
  dataset.describe()
  x = dataset.drop(columns=['delay'])
  y = dataset['delay']
  x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
  model = tf.keras.models.Sequential()

  model.add(tf.keras.layers.Dense(256, input_shape=x_train.shape[1:], activation='sigmoid'))
  model.add(tf.keras.layers.Dense(256, activation='sigmoid'))
  model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

  model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

  model.fit(x_train, y_train, epochs=50)

  """**schedtime**: scheduled time of flight

  ---


  **carriernum**: number assigned to each carrier
    1 - North-Western Cargo International Airlines Co., Ltd. (CO)
    2 - Norwegian Air Norway AS (DH)
    3 - Delta Air Lines, Inc.(DL)
    4 - Envoy Air Inc. (MQ)
    5 - PSA Airlines, Inc. (OH)
    6 - AirBridgeCargo Airlines LLC (RU)
    7 - United Airlines, Inc. (UA)
    8 - US Airways (US)

  ---


  **distance**: distance of flight

  ---


  **flightnum**: flight number

  ---


  **weather**:
    0 - no rain
    1 - rain

  ---


  **dayweek**: day of the week from 1 to 7, 1 being Monday

  ---


  **daymonth**: day of the month from 1 to 31
  """

  predictions = model.predict([[int(schedtime),
                              int(carrier),
                              int(distance),
                              int(flightnum),
                              int(weather),
                              int(dayweek),
                              int(daymonth)]])
  pred=predictions[0][0]
  return pred
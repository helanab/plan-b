import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array

import 'extract-clips-and-create-spectrograms' as create_spects

create_spects.extract_clips_and_create_spectrograms()

model = tf.keras.models.load_model('./BirdMLModel.h5')

#not gonna work
for file in spect_folder:
    spectrogram = np.reshape(img_to_array(load_img('./spect/${file}')), (-1, 256, 256, 3)) / 255.
    model.predict(spectrogram)[0]

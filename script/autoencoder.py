import sys
sys.path.append('/home/nbuser/library/')
import pandas as pd



class Autoencoder():


	#Function that get the file with all the classes sorted using the main age ((StartYear,EndYear)\2)
	def encoder_decoder_model():
  #Encoder 
  		model = Sequential(name='Convolutional_AutoEncoder_Model')
  		model.add(Conv2D(64, kernel_size=(3, 3),activation='relu',input_shape=(224, 224, 3),padding='same', name='Encoding_Conv2D_1'))
  		model.add(MaxPooling2D(pool_size=(2, 2), strides=2, padding='same', name='Encoding_MaxPooling2D_1'))
  		model.add(Conv2D(128, kernel_size=(3, 3),strides=1,kernel_regularizer = tf.keras.regularizers.L2(0.001),activation='relu',padding='same', name='Encoding_Conv2D_2'))
  		model.add(MaxPooling2D(pool_size=(2, 2), strides=2, padding='same', name='Encoding_MaxPooling2D_2'))
  		model.add(Conv2D(256, kernel_size=(3, 3), activation='relu',kernel_regularizer= tf.keras.regularizers.L2(0.001), padding='same', name='Encoding_Conv2D_3'))
  		model.add(MaxPooling2D(pool_size=(2, 2), strides=2, padding='same', name='Encoding_MaxPooling2D_3'))
  		model.add(Conv2D(512, kernel_size=(3, 3), activation='relu',kernel_regularizer= tf.keras.regularizers.L2(0.001), padding='same', name='Encoding_Conv2D_4'))
  		model.add(MaxPooling2D(pool_size=(2, 2), strides=2,padding='valid', name='Encoding_MaxPooling2D_4'))
  		model.add(Conv2D(512, kernel_size=(3, 3), activation='relu', padding='same', name='Encoding_Conv2D_5'))
  		model.add(MaxPooling2D(pool_size=(2,2), strides=2, padding='valid'))
    
  #Decoder
  		model.add(Conv2D(512, kernel_size=(3, 3), kernel_regularizer = tf.keras.regularizers.L2(0.001),activation='relu', padding='same', name='Decoding_Conv2D_1'))
  		model.add(UpSampling2D((2, 2), name='Decoding_Upsamping2D_1'))
  		model.add(Conv2D(512, kernel_size=(3, 3), kernel_regularizer = tf.keras.regularizers.L2(0.001), activation='relu', padding='same', name='Decoding_Conv2D_2'))
  		model.add(UpSampling2D((2, 2), name='Decoding_Upsamping2D_2'))
  		model.add(Conv2D(256, kernel_size=(3, 3), kernel_regularizer = tf.keras.regularizers.L2(0.001), activation='relu', padding='same',name='Decoding_Conv2D_3'))
  		model.add(UpSampling2D((2, 2),name='Decoding_Upsamping2D_3'))
  		model.add(Conv2D(128, kernel_size=(3, 3), activation='relu', kernel_regularizer = tf.keras.regularizers.L2(0.001), padding='same',name='Decoding_Conv2D_4'))
  		model.add(UpSampling2D((2, 2),name='Decoding_Upsamping2D_4'))
  		model.add(Conv2D(64, kernel_size=(3, 3), activation='relu', kernel_regularizer = tf.keras.regularizers.L2(0.001), padding='same',name='Decoding_Conv2D_5'))
  		model.add(UpSampling2D((2, 2),name='Decoding_Upsamping2D_5'))
  		model.add(Conv2D(3, kernel_size=(3, 3), padding='same',activation='sigmoid',name='Decoding_Output'))

  		return model
    




	def spatial_pyramid_matching(image, descriptor, codebook, level):
	    pyramid = []
	    if level == 0:
	        pyramid += build_spatial_pyramid(image, descriptor, level=0)
	        code = [input_vector_encoder(crop, codebook) for crop in pyramid]
	        return np.asarray(code).flatten()
	    if level == 1:
	        pyramid += build_spatial_pyramid(image, descriptor, level=0)
	        pyramid += build_spatial_pyramid(image, descriptor, level=1)
	        code = [input_vector_encoder(crop, codebook) for crop in pyramid]
	        code_level_0 = 0.5 * np.asarray(code[0]).flatten()
	        code_level_1 = 0.5 * np.asarray(code[1:]).flatten()
	        return np.concatenate((code_level_0, code_level_1))
	    if level == 2:
	        pyramid += build_spatial_pyramid(image, descriptor, level=0)
	        pyramid += build_spatial_pyramid(image, descriptor, level=1)
	        pyramid += build_spatial_pyramid(image, descriptor, level=2)
	        code = [input_vector_encoder(crop, codebook) for crop in pyramid]
	        code_level_0 = 0.25 * np.asarray(code[0]).flatten()
	        code_level_1 = 0.25 * np.asarray(code[1:5]).flatten()
	        code_level_2 = 0.5 * np.asarray(code[5:]).flatten()
	        return np.concatenate((code_level_0, code_level_1, code_level_2))
		

	




	 
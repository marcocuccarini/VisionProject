import sys
sys.path.append('/home/nbuser/library/')
import pandas as pd



class Pyramid():


	#Function that get the file with all the classes sorted using the main age ((StartYear,EndYear)\2)
	def build_spatial_pyramid(image, descriptor, level):
	    """
	    Rebuild the descriptors according to the level of pyramid
	    """
	    assert 0 <= level <= 2, "Level Error"
	    step_size = DSIFT_STEP_SIZE
	    #from utils import DSIFT_STEP_SIZE as s
	    s = 4
	    assert s == step_size, "step_size must equal to DSIFT_STEP_SIZE in utils.extract_DenseSift_descriptors()"
	    h = image.shape[0] // step_size
	    w = image.shape[1] // step_size
	    idx_crop = np.array(range(len(descriptor))).reshape(h,w)
	    size = idx_crop.itemsize
	    height, width = idx_crop.shape
	    bh, bw = 2**(3-level), 2**(3-level)
	    shape = (height//bh, width//bw, bh, bw)
	    strides = size * np.array([width*bh, bw, width, 1])
	    crops = np.lib.stride_tricks.as_strided(
	            idx_crop, shape=shape, strides=strides)
	    des_idxs = [col_block.flatten().tolist() for row_block in crops
	                for col_block in row_block]
	    pyramid = []
	    for idxs in des_idxs:
	        pyramid.append(np.asarray([descriptor[idx] for idx in idxs]))
	    return pyramid



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
		

	




	 
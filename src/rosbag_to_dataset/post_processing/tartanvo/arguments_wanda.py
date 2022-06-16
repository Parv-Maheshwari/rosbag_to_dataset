# arguments for tartandrive
common_args = {}
common_args['image_width']      = 1440 # the width of the image from the sensor
common_args['image_height']     = 1080 # the height of the image from the sensor
common_args['focal_x']          = 1103.34 # The focal length of the camera
common_args['focal_y']          = 1103.34 # The focal length of the camera
common_args['center_x']         = 648.283 # The optical center of the camera
common_args['center_y']         = 581.72 # The optical center of the camera
common_args['focal_x_baseline'] = 579.8 # focal lengh multiplied by baseline
common_args['batch_size']       = 8 # The batch size
common_args['worker_num']       = 4 # The number of workers in the dataloader
common_args['image_compressed'] = True 
common_args['stereo_maps']      = 'wanda_mono_prior.npy' 

vo_args = {}
vo_args['model_name']           = '43_6_2_vonet_30000_wo_pwc.pkl' # 'The name of the pretrained model, located in the model folder. 
vo_args['network_type']         = 2 # Load different architecture of vonet
vo_args['image_crop_w']         = 0 # crop out the image because of vignette effect
vo_args['image_crop_h']         = 16 # crop out the image because of vignette effect
vo_args['image_resize_w']       = 640 # the width of the input image into the model
vo_args['image_resize_h']       = 480 # the height of the input image into the model
vo_args['image_input_w']        = 640 # the width of the input image into the model
vo_args['image_input_h']        = 448 # the height of the input image into the model
vo_args['visualize']            = False # help='visualize the depth estimation (default: False)

stereo_args = {}
stereo_args['model_name']       = '6_3_2_stereo_60000.pkl' # The name of the pretrained model, located in the model folder. 
stereo_args['image_crop_w']     = 0 # crop out the image because of vignette effect
stereo_args['image_crop_h_low'] = 360 
stereo_args['image_crop_h_high']= 0 
stereo_args['image_input_w']    = 512 # the width of the input image into the model
stereo_args['image_input_h']    = 256 # the height of the input image into the model
stereo_args['visualize_depth']  = False # visualize the depth estimation (default: False)
stereo_args['pc_min_dist']      = 1.0 # Minimum distance of the points, filter out close points on the vehicle
stereo_args['pc_max_dist']      = 15.0 # Maximum distance of the points
stereo_args['pc_max_height']    = 2.0 # Maximum height of the points
stereo_args['uncertainty_thresh']    = -2.5 
stereo_args['mask_file']        = '' 
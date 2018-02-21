
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# for model uncertainty estimates

# inputs
type_in = 'x_cubed_gap' 	# data type to use - drunk_bow_tie x_cubed_gap ~boston
loss_type = 'qd_soft' 		# loss type to train on - qd_soft mve mse (mse=simple point prediction)
n_samples = 100		# if generating data, how many points to generate
h_size = [100]	# number of hidden units in network: [50]=layer_1 of 50, [8,4]=layer_1 of 8, layer_2 of 4
alpha = 0.05		# data points captured = (1 - alpha)
n_epoch = 150		# number epochs to train for
optim = 'adam' 		# opitimiser - SGD adam
l_rate = 0.02		# learning rate of optimiser
decay_rate=0.92		# learning rate decay
soften = 160. 		# hyper param for QD_soft
lambda_in = 15. 	# hyper param for QD_soft
sigma_in=0.3 		# initialise std dev of NN weights
is_run_test=False	# if averaging over lots of runs - turns off some prints and graphs
n_ensemble=5		# number of individual NNs in ensemble
n_bootstraps=1 		# how many boostrap resamples to perform
n_runs=20 if is_run_test else 1
is_batch=True 		# train in batches?
n_batch=100 		# batch size
lube_perc=90. 		# if model uncertainty method = perc - 50 to 100
perc_or_norm='norm' # model uncertainty method - perc norm (paper uses norm)
is_early_stop=False # stop training early (didn't use in paper)
is_bootstrap=False if n_bootstraps == 1 else True
train_prop=0.9 		# % of data to use as training

out_biases=[3.,-3.] # chose biases for output layer (for mve is overwritten to 0,1)
activation='relu' 	# NN activation fns - tanh relu

# plotting options
is_use_val=True
save_graphs=False
show_graphs=False if is_run_test else True
show_train=False if is_run_test else True
is_y_rescale=False
is_y_sort=False
is_print_info=True
var_plot=0 # lets us plot against different variables, use 0 for univariate
is_err_bars=True
is_norm_plot=False
is_boundary=True # boundary stuff ONLY works for univariate - turn off for larger
is_bound_val=False # plot validation points for boundary
is_bound_train=True # plot training points for boundary
is_bound_indiv=True # plot individual boundary estimates
is_bound_ideal=True # plot ideal boundary
is_title=True # show title w metrics on graph
bound_limit=6. # how far to plot boundary

# resampling
bootstrap_method='replace_resample' # whether to boostrap or jacknife - prop_of_data replace_resample
prop_select=0.8 # if jacknife (=prop_of_data), how much data to use each time

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# for boston housing data


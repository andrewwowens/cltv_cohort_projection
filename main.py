def cltv_cohort_projection(data):
	from shifted_beta_geometric import derl, fit, predicted_survival
	alpha, beta = fit(example_data)
	future = predicted_survival(alpha, beta, len(example_data) + l)[-l:]
	data = example_data.extend(future)
	#print example_data 
	return data

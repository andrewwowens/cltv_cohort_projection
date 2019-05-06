def cltv_cohort_projection(example_data):
    from shifted_beta_geometric import derl, fit, predicted_survival
    alpha, beta = fit(example_data)
    future = predicted_survival(alpha, beta, len(example_data) + l)[-l:]
    example_data.extend(future)
    return example_data

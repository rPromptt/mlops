def normalize_data(data):
    return (data - data.mean()) / data.std()

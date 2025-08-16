import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

def generate_dataset():
    datasets = {}
    datasets["normal"] =[np.random.normal(loc=0, scale=1, size=500) for _ in range(5)]
    datasets["binomial"] = [np.random.binomial(n=20, p=0.5, size=500) for _ in range(5)]
    datasets["poisson"] = [np.random.poisson(lam=5, size=500) for _ in range(5)]
    datasets["uniform"] = [np.random.uniform(low=-3, high=3, size=500) for _ in range(5)]
    datasets["exponetial"] = [np.random.exponential(scale=1, size=1) for _ in range(5)]
    datasets["gamma"] = [np.random.gamma(shape=2, scale=2, size=500) for _ in range(5)]
    datasets["lognormal"] = [np.random.lognormal(mean=0, sigma=1, size=500) for _ in range(5)]
    return datasets

all_datasets = generate_dataset()

def find_outlier(data):
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    higher = Q3 + 1.5 * IQR
    outliers = (data<lower)|(data>higher)
    return outliers

def plot_graph(data: dict):
    for name, arr in data.items():
        for dat in arr:
            outlier = find_outlier(dat)
            plt.figure(figsize=(8,4))
            plt.scatter(dat, range(len(dat)), c=np.where(outlier, "red","blue"), alpha=0.6)
            plt.title(name)
            plt.show()

plot_graph(all_datasets)
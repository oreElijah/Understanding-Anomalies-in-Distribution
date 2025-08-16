from flask import Flask, request, render_template
import numpy as np
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)
normal_datasets = [np.random.normal(loc=0, scale=1, size=500) for _ in range(5)]
binomial_datasets = [np.random.binomial(n=20, p=0.5, size=500) for _ in range(5)]
poisson_datasets = [np.random.poisson(lam=5, size=500) for _ in range(5)]
uniform_datasets = [np.random.uniform(low=-3, high=3, size=500) for _ in range(5)]
exponetial_datasets = [np.random.exponential(scale=1, size=1) for _ in range(5)]
gamma_datasets = [np.random.gamma(shape=2, scale=2, size=500) for _ in range(5)]
lognormal_datasets = [np.random.lognormal(mean=0, sigma=1, size=500) for _ in range(5)]

def find_outlier(data):
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    higher = Q3 + 1.5 * IQR
    outliers = (data<lower)|(data>higher)
    return outliers

@app.route("/binomial", methods=["GET", "POST"])
def binomial():
    name = "Binomial"
    chart_html = ""
    if request.method == "POST":
        dataset_no = int(request.form.get("datasetNo")) - 1
        data = binomial_datasets[dataset_no]
        outliers = find_outlier(data)
        fig = px.scatter(
        x=data,
        y=range(len(data)),
        color=np.where(outliers, "Outlier", "Normal"),
        title="Binomial Distribution with Outliers"
         )
        chart_html = pio.to_html(fig, full_html=False)
    return render_template("index.html", chart_html=chart_html, name=name)


@app.route("/normal", methods=["GET", "POST"])
def normal():
    name = "Normal"
    chart_html = ""
    if request.method == "POST":
        dataset_no = int(request.form.get("datasetNo")) - 1
        data = normal_datasets[dataset_no]
        outliers = find_outlier(data)
        fig = px.scatter(
        x=data,
        y=range(len(data)),
        color=np.where(outliers, "Outlier", "Normal"),
        title="Distribution with Outliers"
         )
        chart_html = pio.to_html(fig, full_html=False)
    return render_template("index.html", chart_html=chart_html, name=name)


@app.route("/poisson", methods=["GET", "POST"])
def poisson():
    name = "Poisson"
    chart_html = ""
    if request.method == "POST":
        dataset_no = int(request.form.get("datasetNo")) - 1
        data = poisson_datasets[dataset_no]
        outliers = find_outlier(data)
        fig = px.scatter(
        x=data,
        y=range(len(data)),
        color=np.where(outliers, "Outlier", "Normal"),
        title="Poisson distribution with Outliers"
         )
        chart_html = pio.to_html(fig, full_html=False)
    return render_template("index.html", chart_html=chart_html, name=name)


@app.route("/exponetial", methods=["GET", "POST"])
def exponetial():
    name = "Exponetial"
    chart_html = ""
    if request.method == "POST":
        dataset_no = int(request.form.get("datasetNo")) - 1
        data = exponetial_datasets[dataset_no]
        outliers = find_outlier(data)
        fig = px.scatter(
        x=data,
        y=range(len(data)),
        color=np.where(outliers, "Outlier", "Normal"),
        title="Distribution with Outliers"
         )
        chart_html = pio.to_html(fig, full_html=False)
    return render_template("index.html", chart_html=chart_html, name=name)


@app.route("/uniform", methods=["GET", "POST"])
def uniform():
    name = "Uniform"
    chart_html = ""
    if request.method == "POST":
        dataset_no = int(request.form.get("datasetNo")) - 1
        data = uniform_datasets[dataset_no]
        outliers = find_outlier(data)
        fig = px.scatter(
        x=data,
        y=range(len(data)),
        color=np.where(outliers, "Outlier", "Normal"),
        title="Uniform distribution with Outliers"
         )
        chart_html = pio.to_html(fig, full_html=False)
    return render_template("index.html", chart_html=chart_html, name=name)

@app.route("/lognormal", methods=["GET", "POST"])
def lognormal():
    name = "Lognormal"
    chart_html = ""
    if request.method == "POST":
        dataset_no = int(request.form.get("datasetNo")) - 1
        data = lognormal_datasets[dataset_no]
        outliers = find_outlier(data)
        fig = px.scatter(
        x=data,
        y=range(len(data)),
        color=np.where(outliers, "Outlier", "Normal"),
        title="Lognormal distribution with Outliers"
         )
        chart_html = pio.to_html(fig, full_html=False)
    return render_template("index.html", chart_html=chart_html, name=name)


@app.route("/gamma", methods=["GET", "POST"])
def gamma():
    name = "Gamma"
    chart_html = ""
    if request.method == "POST":
        dataset_no = int(request.form.get("datasetNo")) - 1
        data = gamma_datasets[dataset_no]
        outliers = find_outlier(data)
        fig = px.scatter(
        x=data,
        y=range(len(data)),
        color=np.where(outliers, "Outlier", "Normal"),
        title="Gamma distribution with Outliers"
         )
        chart_html = pio.to_html(fig, full_html=False)
    return render_template("index.html", chart_html=chart_html, name=name)

@app.route("/")
def home():
    return render_template("home.html")

if __name__=="__main__":
    app.run(debug=True)
# Understanding Anomaly in Distributions

A **Flask** web app to explore how outliers (anomalies) appear in seven common probability distributions.  
The app generates multiple datasets for each distribution, applies **IQR (Interquartile Range) outlier detection**, and visualizes normal vs. anomalous values. It also includes a python script that performs a similar function and makes use of the module matplotlib.

---

## Features

- 7 probability distributions:
  - Normal  
  - Uniform  
  - Exponential  
  - Poisson  
  - Binomial  
  - Gamma  
  - Lognormal  

- 5 datasets per distribution, each with ≥500 samples.  
- Interactive visualization powered by **Plotly**.  
- Outlier detection using **IQR Rule**:  
  - 🔵 Normal points → Blue  
  - 🔴 Outliers → Red  
- Simple **Flask backend** with Jinja templates.  
- Clean separation of pages per distribution.  

---

##  Outlier Detection Method (IQR Rule)

For each dataset:

1. Compute Q1 (25th percentile) and Q3 (75th percentile).  
2. Find the IQR = Q3 − Q1.  
3. A value is flagged as an outlier if:  

   ```
   value < Q1 − 1.5 × IQR
   OR
   value > Q3 + 1.5 × IQR
   ```

This method works well across both symmetric and skewed distributions.

---

## 🗂️ Project Structure

```
├── app.py              
├── templates/
│   ├── home.html       
│   └── index.html      
├── static/             
│   └── style.css
├── distribution.py
│       
└── README.md           
```

---

## 🚀 Installation & Usage

Clone the repo and install dependencies:

```bash
git clone {{url}}
cd anomaly-distributions

# create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# install required packages
pip install flask numpy plotly
```

Run the app:

```bash
python app.py
```

Then open your browser at:  
👉 http://127.0.0.1:5000/

---

## 📸 Demo Screenshots

(Add screenshots of your plots here!)

---

## 🛠️ Tech Stack

- Python (**Flask, NumPy**)  
- **Plotly** for interactive charts  
- **Jinja2** templates  
- HTML/CSS for frontend  

---

## 🌟 Future Improvements

- Add histogram view alongside scatter plots.  
- Allow users to upload their own dataset.  
- Save charts as downloadable PNG/HTML.  
- Add more anomaly detection methods (Z-score, Isolation Forest, etc.).  

---

## 📜 License

**MIT License**  
Free to use, modify, and share.  

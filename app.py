from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Intentamos cargar el dataset
try:
    df = pd.read_csv('data/WA_Fn-UseC_-Telco-Customer-Churn.csv')
except FileNotFoundError:
    df = pd.DataFrame()

@app.route('/')
def home():
    # Enviamos los datos a la única página que tenemos (index.html)
    if not df.empty:
        columnas = df.columns.tolist()
        filas = df.head(15).values.tolist()
        total_filas = len(df)
        total_columnas = len(columnas)
    else:
        columnas, filas, total_filas, total_columnas = [], [], 0, 0

    return render_template('index.html', columnas=columnas, filas=filas, total_filas=total_filas, total_columnas=total_columnas)

if __name__ == '__main__':
    app.run(debug=True)
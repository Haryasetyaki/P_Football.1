import streamlit as st import pandas as pd import numpy as np import joblib from keras.models import load_model

Load model dan scaler

model = load_model('models/lstm_model.h5') scaler = joblib.load('models/scaler.save')

st.title("Prediksi Skor Pertandingan Sepak Bola")

Upload CSV

uploaded_file = st.file_uploader("Upload dataset pertandingan (CSV)", type=['csv'])

if uploaded_file: df = pd.read_csv(uploaded_file) st.write("Contoh data:") st.dataframe(df.head())

# Pilih dua tim
tim_home = st.selectbox("Pilih Tim Home", df['home_team'].unique())
tim_away = st.selectbox("Pilih Tim Away", df['away_team'].unique())

if st.button("Prediksi Skor"):
    latest = df[(df['home_team'] == tim_home) & (df['away_team'] == tim_away)].tail(1)

    if latest.empty:
        st.warning("Pertandingan tidak ditemukan dalam dataset.")
    else:
        fitur = [
            'home_xg', 'away_xg', 'home_xga', 'away_xga',
            'home_possession', 'away_possession',
            'home_shots', 'away_shots',
            'home_rank', 'away_rank',
            'home_form', 'away_form',
            'home_lineup_strength', 'away_lineup_strength',
            'home_formation', 'away_formation'
        ]

        X = latest[fitur]
        X_scaled = scaler.transform(X)
        X_input = X_scaled.reshape((X_scaled.shape[0], 1, X_scaled.shape[1]))

        pred = model.predict(X_input)
        pred = np.round(pred, 2)

        st.success(f"Prediksi skor: {tim_home} {pred[0][0]} : {pred[0][1]} {tim_away}")

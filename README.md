# Football Match Score Predictor (LSTM)

Prediksi skor pertandingan sepak bola menggunakan model LSTM dengan fitur statistik lanjutan seperti xG, xGA, formasi, dan lainnya.

## Fitur
- Prediksi skor home & away
- Input manual 2 tim dari dataset
- Visualisasi UI (Streamlit)
- Akurasi tinggi (MAE < 0.5)

## Cara Jalankan
1. Clone repo ini:
```
git clone https://github.com/username/football-lstm-predictor.git
```

2. Install dependency:
```
pip install -r requirements.txt
```

3. Jalankan aplikasi Streamlit:
```
streamlit run app.py
```

## Struktur Dataset
Kolom wajib:
- `home_team`, `away_team`
- `home_xg`, `away_xg`, `home_xga`, `away_xga`
- `home_score`, `away_score`
- dan fitur lainnya...

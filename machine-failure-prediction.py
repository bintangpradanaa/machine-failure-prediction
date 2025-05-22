import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model dan scaler
final_best_model = joblib.load("best_machine_failure_model.pkl")
scaler = joblib.load("scaler_machine_failure_model.pkl")

st.title("Prediksi Kerusakan Mesin")
st.markdown("Masukkan nilai parameter sensor mesin di bawah ini:")

col1, col2, col3 = st.columns(3)

with col1:
    footfall = st.number_input("Footfall", min_value=0, step=1, format="%d",  help="Jumlah orang atau objek yang melewati mesin")
    AQ = st.number_input("Air Quality (AQ)", min_value=0.0, step=1.0, format="%.2f",  help="Indeks kualitas udara di sekitar mesin")
    RP = st.number_input("Rotational Position / RPM (RP)", min_value=0.0, step=1.0, format="%.2f", help="Kecepatan putaran komponen mesin")

with col2:
    tempMode = st.number_input("Temp Mode", min_value=0, step=1, format="%d",  help="Mode suhu pada mesin")
    USS = st.number_input("Ultrasonic Sensor (USS)", min_value=0.0, step=1.0, format="%.2f", help="Jarak objek dari mesin via sensor ultrasonik")
    IP = st.number_input("Input Pressure (IP)", min_value=0.0, step=1.0, format="%.2f",  help="Tekanan masuk ke dalam mesin")

with col3:
    CS = st.number_input("Current Sensor (CS)", min_value=0.0, step=1.0, format="%.2f",  help="Arus listrik yang digunakan mesin")
    VOC = st.number_input("Volatile Organic Compounds (VOC)", min_value=0.0, step=1.0, format="%.2f", help=" Kandungan senyawa organik volatil di sekitar mesin")
    Temperature = st.number_input("Operating Temperature", min_value=0.0, step=1.0, format="%.2f", help="Suhu operasional mesin saat berjalan")

st.markdown("<br>", unsafe_allow_html=True)  # Spacer

if st.button("Prediksi", use_container_width=True):
    input_data = pd.DataFrame([[footfall, tempMode, AQ, USS, CS, VOC, RP, IP, Temperature]],
                              columns=['footfall', 'tempMode', 'AQ', 'USS', 'CS', 'VOC', 'RP', 'IP', 'Temperature'])
    input_scaled = scaler.transform(input_data)
    failure_probability = final_best_model.predict_proba(input_scaled)[0][1]

    st.subheader("Hasil Prediksi")
    st.write(f"**Probabilitas Kerusakan:** {failure_probability * 100:.2f}%")


    if failure_probability < 0.25:
        st.success("✅ Mesin Sangat Bagus (Tingkat Kerusakan Rendah)")
    elif failure_probability < 0.5:
        st.info("🟦 Mesin Cukup Bagus (Tingkat Kerusakan Cukup Rendah)")
    elif failure_probability < 0.75:
        st.warning("⚠️ Mesin Kurang Bagus (Tingkat Kerusakan Cukup Tinggi)")
    else:
        st.error("❌ Mesin Tidak Bagus (Tingkat Kerusakan Tinggi)")

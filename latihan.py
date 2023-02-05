import streamlit as st

# st.write("Hello World")
st.title("CONTOH PROGRAM PENJUMLAHAN SEDERHANA")

bil1 = st.number_input("Silahkan masukkan angka pertama")

bil2 = st.number_input("Silahkan masukkan angka kedua")

hitung = st.button("Hitung !")

if hitung:
    total = bil1 + bil2
    st.success(f"hasilnya adalah {total}")
    st.balloons()

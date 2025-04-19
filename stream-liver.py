import pickle
import streamlit as st

#membaca model
liver_model = pickle.load(open('liver_model.sav'))

#judul web
st.title('Data Mining Diagnosa Penyakit Liver')

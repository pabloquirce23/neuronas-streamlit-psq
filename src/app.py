import streamlit as st
import pandas as pd
import joblib

st.image("https://images.theconversation.com/files/339172/original/file-20200602-133875-1u1teus.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=754&fit=clip", width=500)

st.title("¡Hola neurona!")

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

with tab1:
   st.header("Una neurona con una entrada y un peso")
   weight = st.slider('Peso', 0.0, 5.0)
   input = st.number_input("Introduzca el valor de entrada")

   if st.button("Calcular la salida", key="button1"):
      y = weight * input
      print("La salida de la neurona es ", y)
      st.text(f"La salida de la neurona es {y}")

with tab2:
   col1, col2 = st.columns(2)
   with col1:
      weight_w0 = st.slider('Peso w0', 0.0, 5.0, key="weightw01")
   with col2:
      weight_w1 = st.slider('Peso w1', 0.0, 5.0, key="weightw11")

   col1, col2 = st.columns(2)
   with col1:
      input_x0 = st.number_input("Entrada x0", key="input01")
   with col2:
      input_x1 = st.number_input("Entrada x1", key="input11")

   if st.button("Calcular la salida", key="button2"):
      y = weight_w0 * input_x0 + weight_w1 * input_x1
      st.text(f"La salida de la neurona es {y}")

with tab3:
   col1, col2, col3 = st.columns(3)
   with col1:
      weight_w0 = st.slider('Peso w0', 0.0, 5.0, key="weight02")
   with col2:
      weight_w1 = st.slider('Peso w1', 0.0, 5.0, key="weight12")
   with col3:
      weight_w2 = st.slider('Peso w2', 0.0, 5.0)

   col1, col2, col3 = st.columns(3)
   with col1:
      input_x0 = st.number_input("Entrada x0", key="input02")
   with col2:
      input_x1 = st.number_input("Entrada x1", key="input12")
   with col3:
      input_x2 = st.number_input("Entrada x2")
   input_sesgo = st.number_input("Introduzca el valor del sesgo")

   if st.button("Calcular la salida", key="button3"):
      y = weight_w0 * input_x0 + weight_w1 * input_x1 + weight_w2 * input_x2 + input_sesgo
      st.text(f"La salida de la neurona es {y}")
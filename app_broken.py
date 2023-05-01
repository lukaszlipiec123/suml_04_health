# źródło danych [https://www.kaggle.com/c/titanic/](https://www.kaggle.com/c/titanic)

import pathlib
import pickle
from datetime import datetime
from pathlib import Path

import streamlit as st

startTime = datetime.now()

temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

filename = "model.sv"
model = pickle.load(open(filename, "rb"))
# otwieramy wcześniej wytrenowany model

symptomps_d = {1: "1", 2: "2", 3: "3", 4: "4", "5": 5}
comorbidity_d = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", "5": 5}
drugs_d = {1: "1", 2: "2", 3: "3", 4: "4"}
# o ile wcześniej kodowaliśmy nasze zmienne, to teraz wprowadzamy etykiety z ich nazewnictwem

title = "App Titanic"


def main():
    st.set_page_config(page_title=title)
    overview = st.container()
    left, right = st.columns(2)
    prediction = st.container()

    st.image("https://strongerhabits.com/wp-content/uploads/2015/02/shutterstock_214341322-450x391.jpg")

    with overview:
        st.title(title)

    with left:
        symptomps_radio = st.radio(
            "Choroby", list(symptomps_d.keys()), format_func=lambda x: symptomps_d[x]
        )
        comorbidity_radio = st.radio(
            "Choroby współistniejące",
            list(comorbidity_d.keys()),
            format_func=lambda x: comorbidity_d[x],
        )
        drugs_radio = st.radio(
            "Leki",
            list(drugs_d.keys()),
            index=2,
            format_func=lambda x: drugs_d[x],
        )

    with right:
        age_slider = st.slider("Wiek", value=1, min_value=11, max_value=77)
        height_slider = st.slider("Wzrost", value=1, min_value=164, max_value=200)

    data = [
        [
            symptomps_radio,
            comorbidity_radio,
            drugs_radio,
            age_slider,
            height_slider,
        ]
    ]
    survival = model.predict(data)
    s_confidence = model.predict_proba(data)

    with prediction:
        st.subheader("Czy osoba jest zdrowa")
        st.subheader(("Tak" if survival[0] == 1 else "Nie"))
        st.write(
            "Pewność predykcji {0:.2f} %".format(s_confidence[0][survival][0] * 100)
        )


if __name__ == "__main__":
    main()

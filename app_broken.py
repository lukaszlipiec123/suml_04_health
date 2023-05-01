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
# embarked_d = {0: "Cherbourg", 1: "Queenstown", 2: "Southampton"}
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
        # embarked_radio = st.radio(
        #     "Port zaokrętowania",
        #     list(embarked_d.keys()),
        #     index=2,
        #     format_func=lambda x: embarked_d[x],
        # )
        # pclass_radio = st.radio(
        #     "Klasa", list(pclass_d.keys()), format_func=lambda x: pclass_d[x]
        # )

    with right:
        age_slider = st.slider("Wiek", value=1, min_value=11, max_value=77)
    #     sibsp_slider = st.slider(
    #         "Liczba rodzeństwa i/lub partnera", min_value=0, max_value=10
    #     )
    #     parch_slider = st.slider(
    #         "Liczba rodziców i/lub dzieci", min_value=0, max_value=10
    #     )
    #     fare_slider = st.slider("Cena biletu", min_value=0, max_value=480, step=1)

    data = [
        [
            symptomps_radio,
            comorbidity_radio,
            # sex_radio,
            # age_slider,
            # sibsp_slider,
            # parch_slider,
            age_slider,
            # embarked_radio,
        ]
    ]
    # survival = model.predict(data)
    # s_confidence = model.predict_proba(data)

    with prediction:
        st.subheader("Czy osoba jest zdrowa")
        # st.subheader(("Tak" if survival[0] == 1 else "Nie"))
        # st.write(
        #     "Pewność predykcji {0:.2f} %".format(s_confidence[0][survival][0] * 100)
        # )


if __name__ == "__main__":
    main()

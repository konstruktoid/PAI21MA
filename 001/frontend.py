#!/usr/bin/env python
"""PAI21MA/001: Python API and Class test. Streamlit frontend."""

import datetime
import re
import requests
import streamlit as st

try:
    import json
except ImportError:
    import simplejson as json

HOST = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="PAI21MA/001",
    page_icon="",
    layout="centered",
)

st.title("Stock information")
user_input = st.text_input("", "")

if len(user_input) == 0:
    response = requests.get(HOST + "/generation_date")
    epoch_date = json.loads(response.content)
    converted_epoch = datetime.datetime.fromtimestamp(epoch_date["generation_date"])
    st.write(
        "Enter stock ID or shortname. "
        "Info updated at " + str(converted_epoch) + ". "
        "Use '*' to show all stocks."
    )
elif user_input == "*":
    dump_response = requests.get(HOST + "/dump")
    stock_dump = json.loads(dump_response.content)
    try:
        col1, col2, col3 = st.columns([2, 1, 1])
        for stock in stock_dump["stockData"]:
            with col1:
                st.write(stock["name"])
            with col2:
                st.write(stock["listing"]["tickerSymbol"])
            with col3:
                st.write(stock["orderbookId"])
    except KeyError:
        pass
else:
    user_input = re.sub(r"[^a-zA-Z0-9. ]", "", user_input)
    response = requests.get(HOST + "/stock/" + user_input)
    st.write(json.loads(response.content))

    try:
        api_country_code = json.loads(response.content)
        country_response = requests.get(
            HOST + "/country/" + api_country_code["country_code"]
        )
        st.write(json.loads(country_response.content))
    except KeyError:
        pass

    try:
        api_marketplace_code = json.loads(response.content)
        exchange_respose = requests.get(
            HOST + "/exchange/" + api_marketplace_code["marketplace_code"]
        )
        st.write(json.loads(exchange_respose.content))
    except KeyError:
        pass

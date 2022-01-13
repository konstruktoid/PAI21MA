#!/usr/bin/env python
"""PAI21MA/001: Find and fetch stock data from json file."""

import csv
import os
import re

try:
    import json
except ImportError:
    import simplejson as json


def dump():
    """The stock_information.json file dump."""
    with open(
        os.getcwd() + "/stock_information.json", "r", encoding="UTF-8"
    ) as stock_json:
        stock_data = json.load(stock_json)
        return stock_data


def generation_date():
    """The stock_information.json file generation date."""
    with open(
        os.getcwd() + "/stock_information.json", "r", encoding="UTF-8"
    ) as stock_json:
        stock_data = json.load(stock_json)

        for stock in stock_data["stockData"]:
            try:
                if stock["generationDate"]:
                    return {"generation_date": stock["generationDate"]}
            except KeyError:
                pass

    return {"generation_date": "unknown"}


def get_stock_data(stock_id):
    """Get misc stock data."""
    with open(
        os.getcwd() + "/stock_information.json", "r", encoding="UTF-8"
    ) as stock_json:
        stock_data = json.load(stock_json)
        for stock in stock_data["stockData"]:
            try:
                stock_id = re.sub(r"[^a-zA-Z0-9. ]", "", stock_id)
                if stock_id in (
                    stock["name"],
                    stock["orderbookId"],
                    stock["listing"]["tickerSymbol"],
                ):
                    return {
                        "company_name": stock["name"],
                        "short_name": stock["listing"]["shortName"],
                        "stock_id": stock["orderbookId"],
                        "ticker_symbol": stock["listing"]["tickerSymbol"],
                        "country_code": stock["listing"]["countryCode"],
                        "currency": stock["listing"]["currency"],
                        "marketplace_code": stock["listing"]["marketPlaceCode"],
                        "website": stock["company"]["homepage"],
                    }
            except KeyError:
                pass

    return {"stock_name": "unknown"}


def get_market_place(marketplace_code):
    """Get market place."""
    with open(os.getcwd() + "/ISO10383_MIC.csv", "r", encoding="UTF-8") as mic_csv:
        csv_reader = csv.DictReader(mic_csv)
        for row in csv_reader:
            if marketplace_code in (
                row["MIC"],
                row["OPERATING MIC"],
            ):
                return {
                    "marketplace_code": marketplace_code,
                    "market_identifier_code": row["MIC"],
                    "name": row["NAME-INSTITUTION DESCRIPTION"],
                    "website": row["WEBSITE"],
                }

    return {"market_place": "unknown"}


def get_country(country_code):
    """Get country."""
    if country_code == "CA":
        return {"country": "Canada"}
    if country_code == "DE":
        return {"country": "Germany"}
    if country_code == "DK":
        return {"country": "Denmark"}
    if country_code == "FI":
        return {"country": "Finland"}
    if country_code == "FR":
        return {"country": "France"}
    if country_code == "IT":
        return {"country": "Italy"}
    if country_code == "NL":
        return {"country": "Netherlands (the)"}
    if country_code == "NO":
        return {"country": "Norway"}
    if country_code == "PT":
        return {"country": "Portugal"}
    if country_code == "SE":
        return {"country": "Sweden"}
    if country_code == "US":
        return {"country": "United States"}

    return {"country": "unknown"}

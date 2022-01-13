#!/usr/bin/env python
"""PAI21MA/001: Python API and Class test."""

from fastapi import FastAPI
import stockdata

app = FastAPI()


@app.get("/dump")
async def dump():
    return stockdata.dump()


@app.get("/generation_date")
async def generation_date():
    return stockdata.generation_date()


@app.get("/stock/{stock_id}")
async def read_stock_id(stock_id):
    return stockdata.get_stock_data(stock_id)


@app.get("/country/{country_code}")
async def read_country(country_code: str):
    return stockdata.get_country(country_code)


@app.get("/exchange/{exchange_code}")
async def read_exchange(exchange_code: str):
    return stockdata.get_market_place(exchange_code)

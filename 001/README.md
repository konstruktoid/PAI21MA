# PAI21MA/001

## Installation

```sh
"$(which python3)" -m pip install -r requirements.txt
```

## Workflow

```console
streamlit (frontend.py) -> FastAPI (main.py) -> functions (stockdata.py)
functions (stockdata.py) -> stock information (stock_information.json)
functions (stockdata.py) -> exchange information (ISO10383_MIC.csv)
```

## Usage

Start `uvicorn` and `streamlit`.

`streamlit` is only needed if you want a frontend.

```sh
uvicorn main:app --reload
streamlit run frontend.py
```

If you're using `streamlit`, browse to the app and as the first query enter a '\*'.
This will present a list with all available stocks.\
Then enter e.g. "DANT" to see basic information regarding the "Dantax" stock and
the stock exchange it's traded on.

### API shell example

```sh
#!/bin/bash

set -eu -o pipefail

echo 52413 | while read -r stock_id; do
  country_code=$(curl -s -X 'GET' "http://127.0.0.1:8000/stock/${stock_id}" -H 'accept: application/json' | jq -r '.["country_code"]')
  country=$(curl -s -X 'GET' "http://127.0.0.1:8000/country/${country_code}" -H 'accept: application/json' | jq -r '.["country"]')
  ticker_symbol=$(curl -s -X 'GET' "http://127.0.0.1:8000/stock/${stock_id}" -H 'accept: application/json' | jq -r '.["ticker_symbol"]')
  company_name=$(curl -s -X 'GET' "http://127.0.0.1:8000/stock/${stock_id}" -H 'accept: application/json' | jq -r '.["company_name"]')

  echo "${company_name} (ID ${stock_id} and ticker symbol \"${ticker_symbol}\") got country code ${country_code} (${country})"
done
```

## Documentation

This file and the API is documented at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

### Improvements

- Fetch stock information directly from trader website, instead of `stock_information.json`.
  Alternatively fetch stock information from trader website and store in MongoDB, then fetch information from database.

- Draw stock price trends, price information is included in `stock_information.json` but not used.

### Links

Stock data from [Avanza](https://www.avanza.se/)

API: [FastAPI](https://fastapi.tiangolo.com/)

Frontend: [streamlit](http://streamlit.io/)

[Market identifier codes](https://www.iso20022.org/market-identifier-codes)

## Testing

```sh
black
pylint
python3 -m flake8 --ignore=E501,W503,S101
codespell
```

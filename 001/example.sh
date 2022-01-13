#!/bin/bash

set -eu -o pipefail

echo 4482 | while read -r stock_id; do
  country_code=$(curl -s -X 'GET' "http://127.0.0.1:8000/stock/${stock_id}" -H 'accept: application/json' | jq -r '.["country_code"]')
  country=$(curl -s -X 'GET' "http://127.0.0.1:8000/country/${country_code}" -H 'accept: application/json' | jq -r '.["country"]')
  ticker_symbol=$(curl -s -X 'GET' "http://127.0.0.1:8000/stock/${stock_id}" -H 'accept: application/json' | jq -r '.["ticker_symbol"]')
  company_name=$(curl -s -X 'GET' "http://127.0.0.1:8000/stock/${stock_id}" -H 'accept: application/json' | jq -r '.["company_name"]')

  echo "${company_name} (ID ${stock_id} and ticker symbol \"${ticker_symbol}\") got country code ${country_code} (${country})"
done

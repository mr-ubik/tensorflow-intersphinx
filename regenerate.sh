#!/bin/sh
pip install -r requirements.in \
&& (
  cd tf_docs_scraper \
  && rm -f core_symbols.json core_symbols_tfp.json \
  && scrapy crawl tf_docs -o core_symbols.json \
  && scrapy crawl tfp_docs -o core_symbols_tfp.json \
) \
&& python inventipy.py

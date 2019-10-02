TensorFlow Intersphinx
======================

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

----

This repository contains the Sphinx Inventory of the TensorFlow 2.0 API together
with the scraper and conversion script used to generate it.

Intersphinx Usage
-----------------

Add the following line inside your Sphinx Intersphinx configuration:
``"tensorflow": ("https://www.tensorflow.org/api_docs/python", "https://github.com/mr-ubik/tensorflow-intersphinx/raw/master/tf2_py_objects.inv")``

**Example**

.. code:: python

    # Example configuration for intersphinx: refer to the Python standard library.
    intersphinx_mapping = {
        "flask": ("http://flask.pocoo.org/docs/1.0/", None),
        "numpy": ("https://docs.scipy.org/doc/numpy/", None),
        "python": ("https://docs.python.org/", None),
        "tensorflow": (
            "https://www.tensorflow.org/api_docs/python",
            "https://github.com/mr-ubik/tensorflow-intersphinx/raw/master/tf2_py_objects.inv",
        ),
    }

Installation
------------

Inside a virtual environment run ``pip install scrapy sphobjinv``

DIY
---

* After installation:

``cd tf_docs_scraper && scrapy crawl tf_docs -o core_symbols.json``

* After the scraping process finish:

``cd .. && python inventipy.py``

Contributing
------------

* Install the development dependencies via ``pip install -r requirements.txt``
* Format everything with ``black``
* Use **reStructuredText** for Sphinx Documentation

TensorFlow Intersphinx
======================

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

----

This repository contains the Sphinx Inventory of the TensorFlow 2.4 API and the TensorFlow Probability 0.12 API together
with the scraper and conversion script used to generate it.

Intersphinx Usage
-----------------

Add the following line inside the ``intersphinx_mapping`` setting in your Sphinx configuration (``conf.py``) if you want to use this repository's GitHub-hosted Inventory:
``"tensorflow": ("https://www.tensorflow.org/api_docs/python", "https://github.com/GPflow/tensorflow-intersphinx/raw/master/tf2_py_objects.inv")``
Or use the following line for having your own copy locally relative to your Sphinx ``conf.py``:
``"tensorflow": ("https://www.tensorflow.org/api_docs/python", "tf2_py_objects.inv")``
For TensorFlow Probability, use (GitHub-hosted)
``"tensorflow_probability": ("https://www.tensorflow.org/probability/api_docs/python", "https://github.com/GPflow/tensorflow-intersphinx/raw/master/tfp_py_objects.inv")``
or (locally)
``"tensorflow_probability": ("https://www.tensorflow.org/probability/api_docs/python", "tfp_py_objects.inv")``

**Example**

.. code:: python

    # Example configuration for intersphinx: refer to the Python standard library.
    intersphinx_mapping = {
        "numpy": ("https://numpy.org/doc/stable/", None),
        "python": ("https://docs.python.org/3/", None),
        "tensorflow": (
            "https://www.tensorflow.org/api_docs/python",
            "https://github.com/GPflow/tensorflow-intersphinx/raw/master/tf2_py_objects.inv"
        ),
        "tensorflow_probability": (
            "https://www.tensorflow.org/probability/api_docs/python",
            "https://github.com/GPflow/tensorflow-intersphinx/raw/master/tfp_py_objects.inv"
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

TensorFlow Intersphinx
======================

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

----

This repository contains the Sphinx Inventory of the TensorFlow 2.4 API and the TensorFlow Probability 0.12 API together
with the scraper and conversion script used to generate it.

Intersphinx Usage
-----------------

To enable these intersphinx inventories in your Sphinx documentation, add the following items inside the ``intersphinx_mapping`` dictionary in your Sphinx configuration (*conf.py*).

For TensorFlow,

* GitHub-hosted:

  .. code:: python

      "tensorflow": ("https://www.tensorflow.org/api_docs/python", "https://github.com/GPflow/tensorflow-intersphinx/raw/master/tf2_py_objects.inv")

* local copy (relative to *conf.py*):

  .. code:: python

      "tensorflow": ("https://www.tensorflow.org/api_docs/python", "tf2_py_objects.inv")

For TensorFlow Probability,

* GitHub-hosted:
  
  .. code:: python
      
      "tensorflow_probability": ("https://www.tensorflow.org/probability/api_docs/python", "https://github.com/GPflow/tensorflow-intersphinx/raw/master/tfp_py_objects.inv")

* local copy (relative to *conf.py*):

  .. code:: python

      "tensorflow_probability": ("https://www.tensorflow.org/probability/api_docs/python", "tfp_py_objects.inv")

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


Find the correct reference
--------------------------

You can view the contents of the inventories by running
``python -msphinx.ext.intersphinx tf2_py_objects.inv``
or
``python -msphinx.ext.intersphinx tfp_py_objects.inv``
The output is separated into classes, functions, and modules.

Regenerate the Sphinx Inventories
---------------------------------

* Install dependencies:
  ``pip install -r requirements.in``
* After installation, run the scraper (make sure to delete old versions of the json files first, ``rm -f tf_docs_scraper/core_symbols.json tf_docs_scraper/core_symbols_tfp.json``):
  ``cd tf_docs_scraper && scrapy crawl tf_docs -o core_symbols.json && cd ..`` (TensorFlow)
  ``cd tf_docs_scraper && scrapy crawl tfp_docs -o core_symbols_tfp.json && cd ..`` (TensorFlow Probability)
* After the scraping process finishes:
  ``python inventipy.py``

These steps can be run all-in-one using the ``regenerate.sh`` shell script.

Note that the TensorFlow and TensorFlow Probability versions (displayed as part
of the intersphinx links in your docs) are hard-coded in ``inventipy.py``, and
have to be updated in there as required.

Contributing
------------

* Install the development dependencies via ``pip install -r requirements.txt``
* Format everything with ``black``
* Use **reStructuredText** for Sphinx Documentation

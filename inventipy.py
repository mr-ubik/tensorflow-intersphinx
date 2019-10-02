"""Generate an objects.inv for TensorFlow."""

import json

import sphobjinv as soi


def main():
    inv = soi.Inventory()
    inv.project = "TensorFlow"
    inv.version = "2.0"

    with open("./tf_docs_scraper/core_symbols.json") as fp:
        symbols = json.load(fp)

    for symbol in symbols:
        add_to_inventory(inv, symbol)

    text = inv.data_file(contract=True)
    ztext = soi.compress(text)
    soi.writebytes("tf2_py_objects.inv", ztext)
    print("All done!")


def add_to_inventory(inv, symbol):
    common_url = "https://www.tensorflow.org/api_docs/python/"

    name = symbol["name"]
    uri = symbol["url"].replace(common_url, "")
    role = symbol["role"]

    # Intersphinx has no "package" role, we convert it to "module" -> :py:module:`tf.keras`
    if role == "pacakage":
        role = "module"

    print(name, uri, role)

    inv.objects.append(
        soi.DataObjStr(
            uri=uri, name=name, domain="py", role=role, priority="1", dispname="-"
        )
    )


if __name__ == "__main__":
    main()

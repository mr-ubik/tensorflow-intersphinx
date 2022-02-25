"""Generate an objects.inv for TensorFlow."""

import json

import sphobjinv as soi


def main(
    project="TensorFlow",
    version="2.0",
    symbols_file="./tf_docs_scraper/core_symbols.json",
    common_url="https://www.tensorflow.org/api_docs/python/",
    inv_file="tf2_py_objects.inv",
):
    inv = soi.Inventory()
    inv.project = project
    inv.version = version

    with open(symbols_file) as fp:
        symbols = json.load(fp)

    for symbol in symbols:
        add_to_inventory(inv, symbol, common_url)

    text = inv.data_file(contract=True)
    ztext = soi.compress(text)
    soi.writebytes(inv_file, ztext)
    print("All done!")


def add_to_inventory(inv, symbol, common_url):

    name = symbol["name"]
    uri = symbol["url"].replace(common_url, "")
    role = symbol["role"]

    # Intersphinx has no "package" role, we convert it to "module" -> :py:module:`tf.keras`
    if role == "package":
        role = "module"

    print(name, uri, role)

    inv.objects.append(
        soi.DataObjStr(
            uri=uri, name=name, domain="py", role=role, priority="1", dispname=name
        )
    )
    if name.startswith("tf."):
        other_name = "tensorflow." + name[3:]
        inv.objects.append(
            soi.DataObjStr(
                uri=uri,
                name=other_name,
                domain="py",
                role=role,
                priority="1",
                dispname=name,
            )
        )
    elif name.startswith("tfp."):
        other_name = "tensorflow_probability." + name[4:]
        inv.objects.append(
            soi.DataObjStr(
                uri=uri,
                name=other_name,
                domain="py",
                role=role,
                priority="1",
                dispname=name,
            )
        )


if __name__ == "__main__":
    main(
        project="TensorFlow",
        version="2.8",  # UPDATE as required
        symbols_file="./tf_docs_scraper/core_symbols.json",
        common_url="https://www.tensorflow.org/api_docs/python/",
        inv_file="tf2_py_objects.inv",
    )
    main(
        project="TensorFlow Probability",
        version="0.16",  # UPDATE as required
        symbols_file="./tf_docs_scraper/core_symbols_tfp.json",
        common_url="https://www.tensorflow.org/probability/api_docs/python/",
        inv_file="tfp_py_objects.inv",
    )

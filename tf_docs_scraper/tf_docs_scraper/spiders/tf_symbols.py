"""Simple Spider for scraping the TensorFlow Documentation."""

from typing import Dict, Iterable

import scrapy


class TensorFlowDocSpider(scrapy.Spider):
    no_compat = True
    name = "tf_docs"
    start_urls = ["https://www.tensorflow.org/api_docs/python"]

    def parse(self, response):
        for uri in self._parse_symbols_index(response):
            if (self.no_compat) & ("compat" not in uri.split("/")):
                yield response.follow(uri, callback=self._parse_role)
            else:
                self.log("Skipping compat symbol.")

    @staticmethod
    def _parse_symbols_index(response) -> Iterable[str]:
        """
        Extract URI of each TensorFlow symbols.

        Args:
            response: PLACEHOLDER.

        Returns:
            Parsed URIs.

        """
        uri_query = "//code/parent::a/@href"
        symbols_uri = response.xpath(uri_query).getall()
        for uri in symbols_uri:
            yield uri

    @staticmethod
    def _parse_role(response: scrapy.http.response.Response) -> Dict[str, str]:
        """
        Extract Sphinx role from a crawled page.

        Valid roles:
            - function
            - class
            - module

        Args:
            response: PLACEHOLDER.

        Returns:
            String containing the role.

        """
        url = response.url

        name_query = "//h1/text()"
        name = response.xpath(name_query).get()

        if url == "https://www.tensorflow.org/api_docs/python/tf":
            return {"name": name, "url": url, "role": "package"}

        section_query = "//h2/text()"
        sections = response.xpath(section_query).getall()

        if "Module" in name.split(": "):
            role = "module"
            name = name.split(": ")[-1]
        elif "Attributes" in sections or "Methods" in sections:
            role = "class"
        else:
            # If the object is not a Module or a Class then it is a function.
            role = "function"

        return {"name": name, "url": url, "role": role}

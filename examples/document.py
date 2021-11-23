from modelspec.BaseTypes import *
from modelspec.utils import *

# Example showing how to create a model of a document and use it to create/serialise instances


class Document(BaseWithId):

    _definition = "A model for documents"

    def __init__(self, **kwargs):

        self.allowed_children = collections.OrderedDict(
            [
                ("pages", ("The pages", Page)),
            ]
        )

        self.allowed_fields = collections.OrderedDict(
            [
                ("title", ("Document title", str)),
                (
                    "ISBN",
                    (
                        "International Standard Book Number",
                        int,
                    ),
                ),
            ]
        )

        super(Document, self).__init__(**kwargs)


class Page(BaseWithId):

    _definition = "A model of a page"

    def __init__(self, **kwargs):

        self.allowed_children = collections.OrderedDict(
            [
                ("lines", ("The pages", Line)),
            ]
        )

        super(Page, self).__init__(**kwargs)


class Line(Base):

    _definition = "A model of a line"

    def __init__(self, **kwargs):

        self.allowed_fields = collections.OrderedDict(
            [
                ("title", ("Document title", str)),
            ]
        )


doc = Document(id="MyBook")
doc.title = "My life in Python"

doc.pages.append(Page(id=1))
doc.pages.append(Page(id=2))

print(doc)

doc.to_json_file("document.json")
doc.to_yaml_file("document.yaml")

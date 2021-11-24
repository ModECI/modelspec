from modelspec.BaseTypes import *
from modelspec.utils import *

# Example showing how to create a model of a document and use it to create/serialise instances


class Document(BaseWithId):

    _definition = "A model for documents"

    def __init__(self, **kwargs):

        self.allowed_children = collections.OrderedDict(
            [
                ("sections", ("The Sections", Section)),
            ]
        )

        #self.add_allowed_child("sections", "The sections of the document", Section)


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


class Section(BaseWithId):

    _definition = "A model of a section of the document"

    def __init__(self, **kwargs):

        self.allowed_children = collections.OrderedDict(
            [
                ("paragraphs", ("The paragraphs", Paragraph)),
            ]
        )

        super(Section, self).__init__(**kwargs)


class Paragraph(Base):

    _definition = "A model of a paragraph"

    def __init__(self, **kwargs):

        self.allowed_fields = collections.OrderedDict(
            [
                ("contents", ("Paragraph contents", str)),
            ]
        )

        super(Paragraph, self).__init__(**kwargs)

doc = Document(id="MyBook")
doc.title = "My life in Python"

a = Section(id="Abstract")
p = Paragraph(contents='Blah blah blah')
a.paragraphs.append(p)
doc.sections.append(a)
doc.sections.append(Section(id="Chapter 1"))

print(doc)

doc.to_json_file("document.json")
doc.to_yaml_file("document.yaml")

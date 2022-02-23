from modelspec.BaseTypes import *
from modelspec.utils import *

# Example showing how to create a model of a document and use it to create/serialise instances


class Document(BaseWithId):

    _definition = "A model for documents"

    def __init__(self, **kwargs):

        self.add_allowed_child("sections", "The sections of the document", Section)

        self.add_allowed_field("title", "Document title", str)
        self.add_allowed_field("ISBN", "International Standard Book Number", int)

        super(Document, self).__init__(**kwargs)

        print("Created:: %s" % (self))


class Section(BaseWithId):

    _definition = "A model of a section of the document. Will contain a _Paragraph_ or two"

    def __init__(self, **kwargs):

        self.add_allowed_child("paragraphs", "The paragraphs", Paragraph)

        super(Section, self).__init__(**kwargs)


class Paragraph(Base):

    _definition = "A model of a paragraph"

    def __init__(self, **kwargs):

        self.add_allowed_field("contents", "Paragraph contents, which make up the _Section_s.", str)

        super(Paragraph, self).__init__(**kwargs)


doc = Document(id="MyBook")
doc.title = "My life in Python"

a = Section(id="Abstract")
p = Paragraph(contents="Blah blah blah")
a.paragraphs.append(p)
doc.sections.append(a)
doc.sections.append(Section(id="Chapter 1"))

print(doc)

doc.to_json_file("document.json")
doc.to_yaml_file("document.yaml")

doc_md = doc.generate_documentation(format="markdown")

with open("document.md", "w") as d:
    d.write(doc_md)

doc_rst = doc.generate_documentation(format="rst")

with open("document.rst", "w") as d:
    d.write(doc_rst)

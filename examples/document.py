
import modelspec
from modelspec import field, instance_of, optional
from modelspec.base_types import Base
from typing import List, Optional, Union

# Example showing how to create a model of a document and use it to create/serialize instances


@modelspec.define
class Paragraph(Base):
    """
    A model of a paragraph

    Args:
        contents: Paragraph contents, which make up the _Section_s.
    """
    contents: str = field(validator=instance_of(str))


@modelspec.define
class Section(Base):
    """
    A model of a section of the document. Will contain a _Paragraph_ or two

    Args:
        id: The id of the section
        paragraphs: The paragraphs
    """
    id: str = field(validator=instance_of(str))
    paragraphs: List[Paragraph] = field(factory=list)


@modelspec.define
class Document(Base):
    """
    A model for documents

    Args:
        id: The unique id of the document
        title: Document title
        ISBN: International Standard Book Number
        sections: The sections of the document
    """
    id: str = field(validator=instance_of(str))
    title: str = field(default=None, validator=optional(instance_of(str)))
    ISBN: int = field(default=None, validator=optional(instance_of(int)))
    sections: List[Section] = field(factory=list)


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

import modelspec
from modelspec import field, instance_of, optional
from modelspec.base_types import Base
from typing import List

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
    A model of a section of the :class:`Document`. Will contain one :class:`Paragraph` or more

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
a.paragraphs.append(Paragraph(contents="Blah blah blah"))
a.paragraphs.append(Paragraph(contents="Blah2"))
doc.sections.append(a)

c1 = Section(id="Chapter 1")
doc.sections.append(c1)
c1.paragraphs.append(Paragraph(contents="More..."))

print(doc)

doc.to_json_file("document.json")
doc.to_yaml_file("document.yaml")

doc_md = doc.generate_documentation(format="markdown")

with open("document.md", "w") as d:
    d.write(doc_md)

doc_rst = doc.generate_documentation(format="rst")

with open("document.rst", "w") as d:
    d.write(doc_rst)


print("\nGenerating specification in dict form")
doc_dict = doc.generate_documentation(format="dict")

import json
import yaml

with open("document.specification.json", "w") as d:
    d.write(json.dumps(doc_dict, indent=4))

print("Generating specification in YAML")
with open("document.specification.yaml", "w") as d:
    d.write(yaml.dump(doc_dict, indent=4, sort_keys=False))

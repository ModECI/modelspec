# Simple example on the use of Modelspec

See also packages [NeuroMLlite](https://github.com/NeuroML/NeuroMLlite) & [MDF](https://github.com/ModECI/MDF) for usage of Modelspec.

## A simple definition of the structure of a Document in modelspec

### 1) Define the structure of a "Document"

A Python file defining the structure of the Document, as well as saving an instance (see below) can be found here: [document.py](https://github.com/ModECI/modelspec/blob/main/examples/document.py).


### 2) Generate human and machine readable specifications of what can be in a Document

A generated Markdown file where the structure of a Document is defined is here: [document.md](https://github.com/ModECI/modelspec/blob/main/examples/document.md). To generate this:
```
    doc_md = doc.generate_documentation(format="markdown")
```

A similar file can be done in reStructuredText (RST) format ([document.rst](https://github.com/ModECI/modelspec/blob/main/examples/document.rst))
```
    doc_rst = doc.generate_documentation(format="rst")
```

For a machine readable version of this, generate in dict format and save to [YAML](https://github.com/ModECI/modelspec/blob/main/examples/document.specification.yaml) or [JSON](https://github.com/ModECI/modelspec/blob/main/examples/document.specification.json).
```
doc_dict = doc.generate_documentation(format="dict")

with open("document.specification.json", "w") as d:
    d.write(json.dumps(doc_dict, indent=4))

with open("document.specification.yaml", "w") as d:
    d.write(yaml.dump(doc_dict, indent=4, sort_keys=False))
```

### 3) Create an instance of a Document

The actual instance of a document which is built (in [document.py](https://github.com/ModECI/modelspec/blob/main/examples/document.py)) can be saved in [YAML](https://github.com/ModECI/modelspec/blob/main/examples/document.yaml) or [JSON](https://github.com/ModECI/modelspec/blob/main/examples/document.json) format or [BSON](https://github.com/ModECI/modelspec/blob/main/examples/document.bson) format:
```
doc = Document(id="MyBook")
doc.title = "My life in Python"

a = Section(id="Abstract")
doc.sections.append(a)

...

doc.to_json_file("document.json")
doc.to_yaml_file("document.yaml")
doc.to_bson_file("document.bson")
```

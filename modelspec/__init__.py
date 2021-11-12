import collections

__version__ = "0.1.1"


from modelspec.BaseTypes import Base
from modelspec.BaseTypes import BaseWithId
from modelspec.BaseTypes import NetworkReader


class EvaluableExpression(str):
    def __init__(self, expr):
        self.expr = expr



if __name__ == "__main__":

    net = Network(id="net")
    doc = net.generate_documentation(format="markdown")
    print(doc)
    with open("../docs/README.md", "w") as d:
        d.write(doc)

    import json
    import yaml

    doc = net.generate_documentation(format="dict")
    doc = {"version": "NeuroMLlite v%s" % __version__, "specification": doc}
    with open("../docs/NeuroMLlite_specification.json", "w") as d:
        d.write(json.dumps(doc, indent=4))
    with open("../docs/NeuroMLlite_specification.yaml", "w") as d:
        d.write(yaml.dump(doc, indent=4, sort_keys=False))

#!/usr/bin/env python3

"""
derived from https://github.com/combine-org/draft-modelspec-sbml-api/blob/main/test_sbml32.py
a minimalish sbml to xml example
"""

import json
import yaml
import os

from sbml32spec import *


def test_example_sbml_minimal():
    "aiming to match the xml file example_sbml_minimal.xml"

    name = "test_minimal_example"

    sbml_doc = sbml(id=name, version="2", level="3")
    # open(f"{path}.docs.json", "w").write(json.dumps(sbml_doc.generate_documentation(format="dict"), indent=4))

    model = Model(substanceUnits="mole", timeUnits="second", extentUnits="mole")
    sbml_doc.model = model

    unit_def = unitDefinition(id="per_second")

    model.listOfUnitDefinitions = ListOfUnitDefinitions()

    model.listOfUnitDefinitions.listOfUnitDefinitions.append(unit_def)

    unit_s = unit(kind="second", exponent=-1.0)
    unit_def.listOfUnits = ListOfUnits()
    unit_def.listOfUnits.listOfUnits.append(unit_s)

    print("------------------------------------------------")
    print(sbml_doc)
    print("------------------------------------------------")

    sbml_doc.to_json_file(f"{name}.json")
    sbml_doc.to_yaml_file(f"{name}.yaml")
    sbml_doc.to_xml_file(f"{name}.xml")


if __name__ == "__main__":
    test_example_sbml_minimal()

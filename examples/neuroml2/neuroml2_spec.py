import modelspec
from modelspec import field, instance_of, optional
from modelspec.base_types import Base
from typing import List
import sys

# Example showing ...


@modelspec.define
class population(Base):
    """
    Some description...

    Args:
        id: The id of the population
        component: the component to use in the population
        size: the size of the population
    """

    id: str = field(validator=instance_of(str))
    component: str = field(default=None, validator=optional(instance_of(str)))
    size: int = field(default=None, validator=optional(instance_of(int)))


@modelspec.define
class explicitInput(Base):
    """
    Some description...

    Args:
        target: the target of the input
        input: the input, e.g. pulseGenerator
    """

    target: str = field(default=None, validator=optional(instance_of(str)))
    input: str = field(default=None, validator=optional(instance_of(str)))


@modelspec.define
class network(Base):
    """
    Some description...

    Args:
        id: The id of the network
        populations: the pops in the net
    """

    id: str = field(validator=instance_of(str))

    populations: List[population] = field(factory=list)
    explicitInputs: List[explicitInput] = field(factory=list)


@modelspec.define
class pulseGenerator(Base):
    """
    Some description...

    Args:
        id: The id of the pulseGenerator
        delay: the delay
        duration: the duration
        amplitude: the amplitude
    """

    id: str = field(validator=instance_of(str))
    delay: str = field(validator=instance_of(str))
    duration: str = field(validator=instance_of(str))
    amplitude: str = field(validator=instance_of(str))


@modelspec.define
class izhikevich2007Cell(Base):
    """
    Some description...

    Args:
        id: The id of the cell...
    """

    id: str = field(validator=instance_of(str))

    C: str = field(validator=instance_of(str))
    v0: str = field(validator=instance_of(str))
    k: str = field(validator=instance_of(str))
    vr: str = field(validator=instance_of(str))
    vt: str = field(validator=instance_of(str))
    vpeak: str = field(validator=instance_of(str))
    a: str = field(validator=instance_of(str))
    b: str = field(validator=instance_of(str))
    c: str = field(validator=instance_of(str))
    d: str = field(validator=instance_of(str))


@modelspec.define
class neuroml(Base):
    """
    Some description...

    Args:
        id: The id of the NeuroML 2 document
        xmlns: Default namespace for the NeuroML file, usually http://www.neuroml.org/schema/neuroml2
        xmlns_xsi: Namespace for XMLSchema-instance
        xmlns_loc: Specifies location of the main namespace
        izhikevich2007Cells: The izhikevich2007Cells
        pulseGenerators: The pulse current generators
        networks: The networks present
    """

    id: str = field(validator=instance_of(str))

    xmlns: str = field(
        validator=instance_of(str), default="http://www.neuroml.org/schema/neuroml2"
    )
    xmlns_xsi: str = field(
        validator=instance_of(str), default="http://www.w3.org/2001/XMLSchema-instance"
    )
    xmlns_loc: str = field(
        validator=instance_of(str),
        default="http://www.neuroml.org/schema/neuroml2 https://raw.github.com/NeuroML/NeuroML2/development/Schemas/NeuroML2/NeuroML_v2.3.xsd",
    )

    izhikevich2007Cells: List[izhikevich2007Cell] = field(factory=list)
    pulseGenerators: List[pulseGenerator] = field(factory=list)
    networks: List[network] = field(factory=list)


if __name__ == "__main__":

    nml_doc = neuroml(id="TestNeuroML")

    izh = izhikevich2007Cell(
        id="izh2007RS0",
        C="100pF",
        v0="-60mV",
        k="0.7nS_per_mV",
        vr="-60mV",
        vt="-40mV",
        vpeak="35mV",
        a="0.03per_ms",
        b="-2nS",
        c="-50.0mV",
        d="100pA",
    )
    nml_doc.izhikevich2007Cells.append(izh)

    pg = pulseGenerator(
        id="pulseGen_0", delay="100ms", duration="800ms", amplitude="0.07 nA"
    )
    nml_doc.pulseGenerators.append(pg)

    net = network(id="IzNet")
    nml_doc.networks.append(net)

    net.populations.append(population("IzhPop0", component="izh2007RS0", size=1))
    net.explicitInputs.append(explicitInput(target="IzhPop0[0]", input="pulseGen_0"))

    print(nml_doc)
    print(nml_doc.id)

    nml_doc.to_json_file("%s.json" % nml_doc.id)
    nml_doc.to_yaml_file("%s.yaml" % nml_doc.id)
    print(" >> Full document details in YAML format:\n")
    print(nml_doc.to_yaml())

    nml_doc.to_bson_file("%s.bson" % nml_doc.id)

    if sys.version_info >= (3, 8):
        nml_doc.to_xml_file("%s.xml" % nml_doc.id)
        print(" >> Full document details in XML format:\n")
        print(nml_doc.to_xml())

    print("Generating documentation...")

    doc_md = nml_doc.generate_documentation(format="markdown")

    with open("NeuroML2.md", "w") as d:
        d.write(doc_md)

    doc_rst = nml_doc.generate_documentation(format="rst")

    with open("NeuroML2.rst", "w") as d:
        d.write(doc_rst)

    print("\n  >> Generating specification in dict form...")
    doc_dict = nml_doc.generate_documentation(format="dict")

    import json
    import yaml

    with open("NeuroML2.specification.json", "w") as d:
        d.write(json.dumps(doc_dict, indent=4))

    print("  >> Generating specification in YAML...\n")

    with open("NeuroML2.specification.yaml", "w") as d:
        yy = yaml.dump(doc_dict, indent=4, sort_keys=False)
        print(yy)
        d.write(yy)

    from modelspec.utils import load_xml

    new_neuroml = load_xml("hello_world_neuroml.net.nml")
    print(new_neuroml)

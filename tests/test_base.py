import modelspec


from modelspec import field, instance_of, optional, Base
from modelspec.base_types import value_expr_types, ValueExprType, print_v

from typing import List, Dict, Any, Optional

import sys

# Some test modelspec classes to use in the tests


@modelspec.define
class NewCell(Base):
    """
    A new cell definition

    Args:
        id: the cell id
        neuroml2_source_file: The path to the source file
    """

    id: str = field(validator=instance_of(str))
    neuroml2_source_file: str = field(
        default=None, validator=optional(instance_of(str))
    )


@modelspec.define
class NewSynapse(Base):
    """
    A new synapse definition

    Args:
        id: the synapse id
        neuroml2_source_file: The path to the source file
        tested: A boolean attribute
    """

    id: str = field(validator=instance_of(str))
    neuroml2_source_file: str = field(
        default=None, validator=optional(instance_of(str))
    )
    tested: bool = field(default=None, validator=optional(instance_of(bool)))


@modelspec.define
class NewRandomConnectivity(Base):
    """
    A new random connectivity definition

    Args:
        probability: Random probability of connection

    """

    probability: ValueExprType = field(
        default=None, validator=optional(instance_of(value_expr_types))
    )


@modelspec.define
class NewNetwork(Base):
    """
    A new network definition

    Args:
        id: a unique identifier for the network
        cells: a list of cells
        synapses: a list of synapses
        version: Information on verson of NeuroMLlite
        seed: Seed for random number generator used when building network
        stable: Testing...
        parameters: Dictionary of global parameters for the network
        random_connectivity: Use random connectivity
    """

    id: str = field(validator=instance_of(str))
    cells: List[NewCell] = field(factory=list)
    synapses: List[NewSynapse] = field(factory=list)
    version: str = field(default="NeuroMLlite 0.0", validator=instance_of(str))
    seed: int = field(default=None, validator=optional(instance_of(int)))
    stable: bool = field(default=None, validator=optional(instance_of(bool)))
    parameters: Dict[str, Any] = field(
        default=None, validator=optional(instance_of(dict))
    )
    random_connectivity: NewRandomConnectivity = field(
        default=None, validator=optional(instance_of(NewRandomConnectivity))
    )
    ee0: ValueExprType = field(
        default=None, validator=optional(instance_of(value_expr_types))
    )
    ee1: ValueExprType = field(
        default=None, validator=optional(instance_of(value_expr_types))
    )
    ee2: ValueExprType = field(
        default=None, validator=optional(instance_of(value_expr_types))
    )
    ee3: ValueExprType = field(
        default=None, validator=optional(instance_of(value_expr_types))
    )
    ee4: ValueExprType = field(
        default=None, validator=optional(instance_of(value_expr_types))
    )
    ee5: ValueExprType = field(
        default=None, validator=optional(instance_of(value_expr_types))
    )
    ee6: ValueExprType = field(
        default=None, validator=optional(instance_of(value_expr_types))
    )


def test_save_load_json(tmp_path):
    net = NewNetwork(id="netid", parameters={"size": 3, "name": None})

    # Some tests on what's allowed
    net.ee0 = "str"
    net.ee1 = {"a": 2}
    net.ee2 = 1
    net.ee3 = 1.1
    net.ee4 = True
    net.ee5 = [1, 2]
    net.ee6 = None

    cell = NewCell(id="cellid1")
    cell.neuroml2_source_file = "nnn"
    cell2 = NewCell(id="cellid2")
    cell2.neuroml2_source_file = "nnn2"
    # net.cells.append(cell)

    print(net)
    print(net.cells)
    print(net)
    """  """
    net.cells.append(cell)
    net.cells.append(cell2)

    syn0 = NewSynapse(id="syn0", neuroml2_source_file=None, tested=True)
    net.synapses.append(syn0)
    syn1 = NewSynapse(id="syn1", neuroml2_source_file="xx", tested=None)
    net.synapses.append(syn1)

    rc = NewRandomConnectivity(probability=0.01)
    net.random_connectivity = rc
    net.stable = False
    print(rc)
    print(net)

    try:
        print(net.notcells)
    except Exception as e:
        print("  As expected, an exception: [%s]..." % e)

    str_orig = str(net)

    filenamej = str(tmp_path / f"{net.id}.json")
    net.to_json_file(filenamej)

    filenamey = str(tmp_path / f"{net.id}.yaml")
    # net.id = net.id+'_yaml'
    net.to_yaml_file(filenamey)
    from modelspec.utils import load_json, load_yaml

    dataj = load_json(filenamej)
    print_v("Loaded network specification from %s" % filenamej)
    netj = NewNetwork.from_dict(dataj)

    str_netj = str(netj)

    datay = load_yaml(filenamey)
    print_v("Loaded network specification from %s" % filenamey)

    nety = NewNetwork.from_dict(datay)
    str_nety = str(nety)

    print("----- Before -----")
    print(str_orig)
    print("----- After via %s -----" % filenamej)
    print(str_netj)
    print("----- After via %s -----" % filenamey)
    print(str_nety)

    print("Test JSON..")
    if sys.version_info[0] == 2:
        assert len(str_orig) == len(
            str_netj
        )  # Order not preserved in py2, just test len
    else:
        assert str_orig == str_netj

    print("Test YAML..")
    if sys.version_info[0] == 2:
        assert len(str_orig) == len(
            str_nety
        )  # Order not preserved in py2, just test len
    else:
        assert str_orig == str_nety

    print("Test EvaluableExpressions")
    for i in range(7):
        assert eval("net.ee%i" % i) == eval("netj.ee%i" % i)
        assert eval("net.ee%i" % i) == eval("nety.ee%i" % i)


def test_generate_documentation():
    net = NewNetwork(id="netid", parameters={"size": 3, "name": None})

    # Some tests on what's allowed
    net.ee0 = "str"
    net.ee1 = {"a": 2}
    net.ee2 = 1
    net.ee3 = 1.1
    net.ee4 = True
    net.ee5 = [1, 2]
    net.ee6 = None

    cell = NewCell(id="cellid1")
    cell.neuroml2_source_file = "nnn"
    cell2 = NewCell(id="cellid2")
    cell2.neuroml2_source_file = "nnn2"
    # net.cells.append(cell)

    print(net)
    print(net.cells)
    print(net)
    """  """
    net.cells.append(cell)
    net.cells.append(cell2)

    syn0 = NewSynapse(id="syn0", neuroml2_source_file=None, tested=True)
    net.synapses.append(syn0)
    syn1 = NewSynapse(id="syn1", neuroml2_source_file="xx", tested=None)
    net.synapses.append(syn1)

    rc = NewRandomConnectivity(probability=0.01)
    net.random_connectivity = rc
    net.stable = False

    md_str = net.generate_documentation()
    print(md_str)


def test_generate_documentation_example():
    """Test the documentation generation in examples/"""

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

    doc.to_json()
    doc.to_yaml()
    doc.generate_documentation(format="markdown")
    doc.generate_documentation(format="rst")


def test_ndarray_json_metadata():
    import numpy as np

    @modelspec.define(eq=False)
    class Node(Base):
        id: str = field(validator=instance_of(str))
        metadata: Optional[Dict[str, Any]] = field(
            kw_only=True, default=None, validator=optional(instance_of(dict))
        )

    model = Node(id="a", metadata={"b": np.array([0])})
    model.to_json()


def test_bson_array(tmp_path):
    import numpy as np

    test_filename = str(tmp_path / "test_array.bson")

    @modelspec.define(eq=False)
    class ArrayTestModel(Base):
        array: Optional[ValueExprType] = field()
        list_of_lists: List[List[int]] = field(default=None)
        ragged_list: List[List[int]] = field(default=None)

    model = ArrayTestModel(
        array=np.arange(27).reshape((3, 3, 3)),
        list_of_lists=[[1, 2], [3, 4]],
        ragged_list=[[1, 2], [1]],
    )

    model.to_bson_file(test_filename)

    # Load it back in
    m2 = model.from_bson_file(test_filename)
    # Check we get the same values back
    np.testing.assert_array_equal(model.array, m2.array)
    assert model.list_of_lists == m2.list_of_lists
    assert model.ragged_list == m2.ragged_list

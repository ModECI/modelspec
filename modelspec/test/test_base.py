from modelspec import *
from modelspec.utils import *

import pickle

try:
    import unittest2 as unittest
except ImportError:
    import unittest


class TestCustomSaveLoad(unittest.TestCase):
    def test_save_load_json(self):
        class NewNetwork(BaseWithId):

            _definition = "..."

            def __init__(self, **kwargs):

                self.allowed_children = collections.OrderedDict(
                    [
                        ("cells", ("The cell definitions...", NewCell)),
                        ("synapses", ("The synapse definitions...", NewSynapse)),
                    ]
                )

                self.allowed_fields = collections.OrderedDict(
                    [
                        ("version", ("Information on verson of NeuroMLlite", str)),
                        (
                            "seed",
                            (
                                "Seed for random number generator used when building network",
                                int,
                            ),
                        ),
                        ("stable", ("Testing...", bool)),
                        (
                            "parameters",
                            ("Dictionary of global parameters for the network", dict),
                        ),
                        (
                            "random_connectivity",
                            ("Use random connectivity", NewRandomConnectivity),
                        ),
                        ("ee0", ("TestEE", EvaluableExpression)),
                        ("ee1", ("TestEE", EvaluableExpression)),
                        ("ee2", ("TestEE", EvaluableExpression)),
                        ("ee3", ("TestEE", EvaluableExpression)),
                        ("ee4", ("TestEE", EvaluableExpression)),
                        ("ee5", ("TestEE", EvaluableExpression)),
                        ("ee6", ("TestEE", EvaluableExpression)),
                    ]
                )

                super(NewNetwork, self).__init__(**kwargs)

                self.version = "NeuroMLlite 0.0"

        class NewCell(BaseWithId):
            def __init__(self, **kwargs):

                self.allowed_fields = collections.OrderedDict(
                    [("neuroml2_source_file", ("File name of NeuroML2 file", str))]
                )

                super(NewCell, self).__init__(**kwargs)

        class NewSynapse(BaseWithId):
            def __init__(self, **kwargs):

                self.allowed_fields = collections.OrderedDict(
                    [
                        ("neuroml2_source_file", ("File name of NeuroML2 file", str)),
                        ("tested", ("Is it tested?", bool)),
                    ]
                )

                super(NewSynapse, self).__init__(**kwargs)

        class NewRandomConnectivity(Base):
            def __init__(self, **kwargs):

                self.allowed_fields = collections.OrderedDict(
                    [
                        (
                            "probability",
                            ("Random probability of connection", EvaluableExpression),
                        )
                    ]
                )

                super(NewRandomConnectivity, self).__init__(**kwargs)

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

        filenamej = "%s.json" % net.id
        net.to_json_file(filenamej)

        filenamey = "%s.yaml" % net.id
        # net.id = net.id+'_yaml'
        net.to_yaml_file(filenamey)
        from modelspec.utils import load_json, load_yaml, _parse_element

        dataj = load_json(filenamej)
        print_v("Loaded network specification from %s" % filenamej)
        netj = NewNetwork()
        _parse_element(dataj, netj)
        str_netj = str(netj)

        datay = load_yaml(filenamey)
        print_v("Loaded network specification from %s" % filenamey)

        nety = NewNetwork()
        _parse_element(datay, nety)
        str_nety = str(nety)

        verbose = False
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


if __name__ == "__main__":

    # Some tests
    tc = TestCustomSaveLoad()
    tc.test_save_load_json()

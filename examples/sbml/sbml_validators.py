"""
functions used to validate the user assigned values of items
these functions will generally be called by passing to the validator option of attrs.field
"""

import re
from lxml import etree
from io import StringIO
import sys

# sbml.level-3.version-2.core.release-2.pdf Table 2
sbml_si_units = """
ampere coulomb gray joule litre mole radian steradian weber avogadro dimensionless henry katal lumen newton
second tesla becquerel farad hertz kelvin lux ohm siemens volt candela gram item kilogram metre pascal sievert watt
""".split()

SBML_VERSION = "2"
SBML_LEVEL = "3"


def valid_kind(instance, attribute, value):
    if value not in sbml_si_units:
        raise ValueError(
            f"kind {value} must be one of the standard SI units: {sbml_si_units}"
        )


def valid_mathml(instance, attribute, value):
    "http://www.w3.org/1998/Math/MathML"


def xmlns_sbml(instance, attribute, value):
    if value != "http://www.sbml.org/sbml/level3/version2/core":
        raise ValueError(
            "xmlns must be 'http://www.sbml.org/sbml/level3/version2/core'"
        )


def xmlns_notes(instance, attribute, value):
    if value != "http://www.w3.org/1999/xhtml":
        raise ValueError("xmlns must be 'http://www.w3.org/1999/xhtml'")


def xmlns_math(instance, attribute, value):
    if value != "http://www.w3.org/1998/Math/MathML":
        raise ValueError("xmlns must be 'http://www.w3.org/1998/Math/MathML'")


def fixed_level(instance, attribute, value):
    if value != SBML_LEVEL:
        raise ValueError("this implementation only supports level %s" % SBML_LEVEL)


def fixed_version(instance, attribute, value):
    if value != SBML_VERSION:
        raise ValueError("this implementation only supports version %s" % SBML_VERSION)


def valid_sid(instance, attribute, value):
    if value is not None:
        if not re.fullmatch("[_A-Za-z][_A-Za-z0-9]*", value):
            raise ValueError(
                "an SId must match the regular expression: [_A-Za-z][_A-Za-z0-9]*"
            )


def valid_unitsid(instance, attribute, value):
    "same as sid except has a separate namespace"
    if not re.fullmatch("[_A-Za-z][_A-Za-z0-9]*", value):
        raise ValueError(
            "a UnitSId must match the regular expression: [_A-Za-z][_A-Za-z0-9]*"
        )


def valid_unitsid(instance, attribute, value):
    if not re.fullmatch("[_A-Za-z][_A-Za-z0-9]*", value):
        raise ValueError(
            "a UnitSId must match the regular expression: [_A-Za-z][_A-Za-z0-9]*"
        )


def valid_sbo(instance, attribute, value):
    if not re.fullmatch("SBO:[0-9]{7}", value):
        raise ValueError("an SBOTerm must match the regular expression: SBO:[0-9]{7}")


def valid_xml_id(instance, attribute, value):
    "a valid XML 1.0 ID"
    # not implemented yet: CombiningChar , Extender
    # NameChar ::= letter | digit | '.' | '-' | '_' | ':' | CombiningChar | Extender
    # ID ::= ( letter | '_' | ':' ) NameChar*

    if not re.fullmatch("[A-Za-z_:][A-Za-z0-9._:-]*", value):
        raise ValueError("an SBOTerm must match the regular expression: SBO:[0-9]{7}")


def valid_xhtml(instance, attribute, value):
    "use etree to validate XHTML, throw exception on error"
    etree.parse(StringIO(value), etree.HTMLParser(recover=False))


def valid_xml_content(instance, attribute, value):
    "stub"

    if not re.search("<.*>", value):
        raise ValueError(
            f"{value} doesn't look like XML (this validator is only a stub)"
        )


def valid_mathml(instance, attribute, value):
    """
    stubvalidator for MathML
    note: see pdf section 4.3.2 for special rules for FunctionDefinition MathML
    versus all other MathML uses in SBML
    """

    if not re.search("<math.*</math>", value):
        raise ValueError(
            f"{value} doesn't look like MathML (this validator is only a stub)"
        )


# from: https://github.com/combine-org/combine-notebooks


def validate_sbml(doc, units_consistency: bool = False) -> None:
    """Validate sbml."""
    import libsbml

    # set the unit checking, similar for the other settings
    doc.setConsistencyChecks(libsbml.LIBSBML_CAT_UNITS_CONSISTENCY, units_consistency)
    doc.checkConsistency()
    # get errors/warnings
    n_errors: int = doc.getNumErrors()
    errors: List[libsbml.SBMLError] = list()
    warnings: List[libsbml.SBMLError] = list()
    for k in range(n_errors):
        error: libsbml.SBMLError = doc.getError(k)
        severity = error.getSeverity()
        if (severity == libsbml.LIBSBML_SEV_ERROR) or (
            severity == libsbml.LIBSBML_SEV_FATAL
        ):
            errors.append(error)
        else:
            warnings.append(error)
    # print results
    print("-" * 80)
    print(f"{'validation error(s)':<25}: {len(errors)}")
    print(f"{'validation warning(s)':<25}: {len(warnings)}")
    if len(errors) > 0:
        print("--- errors ---")
        for kerr in enumerate(errors):
            print(f"E{kerr}: {error.getCategoryAsString()} L{error.getLine()}")
            print(
                f"[{error.getSeverityAsString()}] {error.getShortMessage()} | {error.getMessage()}"
            )
    if len(warnings) > 0:
        print("--- warnings ---")
        for kwarn in enumerate(warnings):
            print(f"E{kwarn}: {error.getCategoryAsString()} L{error.getLine()}")
            print(
                f"[{error.getSeverityAsString()}] {error.getShortMessage()} | {error.getMessage()}"
            )
    print("-" * 80)

    return len(warnings) + len(errors)


if __name__ == "__main__":
    import libsbml

    sbml_file = sys.argv[1]

    print("Going to validate SBML file: %s" % sbml_file)
    reader = libsbml.SBMLReader()
    document = reader.readSBML(sbml_file)

    issues = validate_sbml(document, units_consistency=False)

    exit(issues)

#!/usr/bin/env python3

"""
initial attempt at creating an SBML API using modelspec
https://github.com/combine-org/compbiolibs/issues/28

based on sbml.level-3.version-2.core.release-2.pdf
"""

import modelspec
from modelspec import field, instance_of, optional
from modelspec.base_types import Base
from typing import List

from sbml_validators import *


@modelspec.define
class Notes(Base):
    """
    XHTML field of SBase

    Args:
        xmlns: str fixed "http://www.w3.org/1999/xhtml"
        content: str valid XHTML
    """

    xmlns: str = field(
        default="http://www.w3.org/1999/xhtml",
        validator=[instance_of(str), xmlns_notes],
    )
    content: str = field(
        default=None, validator=optional([instance_of(str), valid_xhtml])
    )


@modelspec.define
class Math(Base):
    """
    Subset of MathML 2.0 used to define all formulae in SBML
    """

    xmlns: str = field(
        default="http://www.w3.org/1998/Math/MathML",
        validator=[instance_of(str), xmlns_math],
    )
    content: str = field(
        default=None, validator=optional([instance_of(str), valid_mathml])
    )


@modelspec.define
class SBase(Base):
    """
    Abstract base class for all SBML objects

    Args:
        sid:     SId optional
        name:    string optional
        metaid:  XML ID optional
        sboTerm: SBOTerm optional

        notes:      XHTML 1.0 optional
        annotation: XML content optional
    """

    sid: str = field(default=None, validator=optional([instance_of(str), valid_sid]))
    name: str = field(default=None, validator=optional(instance_of(str)))

    metaid: str = field(
        default=None, validator=optional([instance_of(str), valid_xml_id])
    )
    sboTerm: str = field(
        default=None, validator=optional([instance_of(str), valid_sbo])
    )

    notes: Notes = field(default=None, validator=optional(instance_of(Notes)))
    annotation: str = field(
        default=None, validator=optional([instance_of(str), valid_xml_content])
    )


@modelspec.define
class SBaseWithId(SBase):
    id: str = field(default=None, validator=optional([instance_of(str), valid_sid]))


@modelspec.define
class Trigger(SBase):
    initialValue: bool = field(default=None, validator=instance_of(bool))
    persistent: bool = field(default=None, validator=instance_of(bool))
    math: str = field(default=None, validator=optional(instance_of(str)))


@modelspec.define
class Priority(SBase):
    math: str = field(default=None, validator=optional(instance_of(str)))


@modelspec.define
class Delay(SBase):
    math: str = field(default=None, validator=optional(instance_of(str)))


@modelspec.define
class EventAssignment(SBase):
    """
    Args:
        variable: SIdRef
    """

    math: str = field(default=None, validator=optional(instance_of(str)))
    variable: str = field(default=None, validator=optional(instance_of(str)))


@modelspec.define
class Event(SBase):
    useValuesFromTriggerTime: bool = field(default=None, validator=instance_of(bool))
    trigger: Trigger = field(default=None, validator=optional(instance_of(Trigger)))
    priority: Priority = field(default=None, validator=optional(instance_of(Priority)))
    delay: Delay = field(default=None, validator=optional(instance_of(Delay)))
    listOfEventAssignments: List[EventAssignment] = field(factory=list)


@modelspec.define
class SimpleSpeciesReference(SBase):
    """
    Base class used by SpeciesReference and ModifierSpeciesReference

    Args:
        species: SIdRef
    """

    species: str = field(default=None, validator=instance_of(str))


@modelspec.define
class ModifierSpeciesReference(SimpleSpeciesReference):
    """"""


@modelspec.define
class SpeciesReference(SimpleSpeciesReference):
    """
    Args:
        stoichiometry: double optional
        constant: boolean
    """

    stoichiometry: float = field(default=None, validator=optional(instance_of(float)))
    constant: bool = field(default=None, validator=instance_of(bool))


@modelspec.define
class LocalParameter(SBase):
    """
    Args:
        units: UnitSIdRef optional
    """

    value: float = field(default=None, validator=optional(instance_of(float)))
    units: str = field(default=None, validator=optional(instance_of(str)))


@modelspec.define
class KineticLaw(SBase):
    """ """

    math: str = field(default=None, validator=optional(instance_of(str)))

    listOfLocalParameters: List[LocalParameter] = field(factory=list)


@modelspec.define
class Reaction(SBase):
    """
    A model reaction

    Args:
        reversible: boolean
        compartment: SIdRef optional
    """

    reversible: bool = field(default=None, validator=instance_of(bool))
    compartment: str = field(default=None, validator=optional(instance_of(str)))

    listOfReactants: List[SpeciesReference] = field(factory=list)
    listOfProducts: List[SpeciesReference] = field(factory=list)
    listOfModifiers: List[ModifierSpeciesReference] = field(factory=list)

    kineticLaw: KineticLaw = field(
        default=None, validator=optional(instance_of(KineticLaw))
    )


@modelspec.define
class Constraint(SBase):
    """
    A model constraint

    Args:
        math:    MathML optional
        message: XHTML 1.0 optional
    """

    math: str = field(default=None, validator=optional(instance_of(str)))
    message: str = field(default=None, validator=optional(instance_of(str)))


@modelspec.define
class Rule(SBase):
    """
    A rule, either algebraic, assignment or rate

    Args:
        math: MathML optional
    """

    math: str = field(default=None, validator=optional(instance_of(str)))


@modelspec.define
class AlgebraicRule(Rule):
    """
    An algebraic rule
    """


@modelspec.define
class AssignmentRule(Rule):
    """
    An assignment rule

    Args:
        variable: SIdRef required
    """

    variable: str = field(default=None, validator=instance_of(str))


@modelspec.define
class RateRule(Rule):
    """
    A rate rule

    Args:
        variable: SIdRef required
    """

    variable: str = field(default=None, validator=instance_of(str))


@modelspec.define
class InitialAssignment(SBase):
    """
    An initial assignment

    Args:
        symbol: SIdRef required
        math: MathML optional
    """

    symbol: str = field(default=None, validator=instance_of(str))
    math: str = field(default=None, validator=optional(instance_of(str)))


@modelspec.define
class Parameter(SBase):
    """
    A parameter

    Args:
        value: double optional
        units: UnitSIdRef optional
        constant: boolean
    """

    constant: bool = field(default=None, validator=instance_of(bool))

    value: float = field(default=None, validator=optional(instance_of(float)))
    units: str = field(default=None, validator=optional(instance_of(str)))


@modelspec.define
class Species(SBase):
    """
    A species: entities of the same kind participating in reactions within a specific compartment

    Args:
        compartment: SIdRef
        initialAmount: double optional
        initialConcentration: double optional
        substanceUnits: UnitSIdRef optional
        hasOnlySubstanceUnits: boolean
        boundaryCondition: boolean
        constant: boolean
        conversionFactor: SIdRef optional
    """

    compartment: str = field(default=None, validator=instance_of(str))
    hasOnlySubstanceUnits: bool = field(default=None, validator=instance_of(bool))
    boundaryCondition: bool = field(default=None, validator=instance_of(bool))
    constant: bool = field(default=None, validator=instance_of(bool))

    initialAmount: float = field(default=None, validator=optional(instance_of(float)))
    initialConcentration: float = field(
        default=None, validator=optional(instance_of(float))
    )
    substanceUnits: str = field(default=None, validator=optional(instance_of(str)))
    conversionFactor: str = field(default=None, validator=optional(instance_of(str)))


@modelspec.define
class Compartment(SBase):
    """
    A compartment

    Args:
        spatialDimensions: eg 3 for three dimensional space etc
        size: initial size of compartment
        units: units being used to define the compartment's size
        constant: whether size is fixed
    """

    constant: bool = field(default=None, validator=instance_of(bool))

    spatialDimensions: float = field(
        default=None, validator=optional(instance_of(float))
    )
    size: float = field(default=None, validator=optional(instance_of(float)))
    units: str = field(default=None, validator=optional(instance_of(str)))


@modelspec.define
class unit(SBase):
    """
    A unit used to compose a unit definition.
    unit = (multiplier x 10^scale x kind)^exponent

    Args:
        kind: base unit (base or derived SI units only, see Table 2 of the SBML spec)
        exponent: double
        scale: integer
        multiplier: double
    """

    kind: str = field(default=None, validator=[instance_of(str), valid_kind])
    exponent: str = field(default=1.0, validator=instance_of(float))
    scale: str = field(default=0, validator=instance_of(int))
    multiplier: str = field(default=1.0, validator=instance_of(float))


@modelspec.define
class ListOfUnits(SBase):
    """
    A listOfUnits

    Args:
        listOfUnits: the actual list Of Units
    """

    listOfUnits: List[unit] = field(factory=list)


@modelspec.define
class unitDefinition(SBaseWithId):
    """
    A unit definition

    Args:
        listOfUnits: List of units used to compose the definition
    """

    listOfUnits: ListOfUnits = field(
        default=None, validator=optional(instance_of(ListOfUnits))
    )


@modelspec.define
class ListOfUnitDefinitions(SBase):
    """
    A listOfUnitDefinitions

    Args:
        listOfUnitDefinitions: the actual list Of Unit Definitions
    """

    listOfUnitDefinitions: List[unitDefinition] = field(factory=list)


@modelspec.define
class FunctionDefinition(SBase):
    """
    A function definition using MathML

    Args:
        sid:  SId required

        math: MathML function definition optional
    """

    sid: str = field(default=None, validator=[instance_of(str), valid_sid])

    math: Math = field(default=None, validator=optional(instance_of(Math)))


@modelspec.define
class Model(SBase):
    """
    The model

    Args:
        substanceUnits:   UnitSIdRef optional
        timeUnits:        UnitSIdRef optional
        volumeUnits:      UnitSIdRef optional
        areaUnits:        UnitSIdRef optional
        lengthUnits:      UnitSIdRef optional
        extentUnits:      UnitSIdRef optional
        conversionFactor: SIdRef optional
    """

    substanceUnits: str = field(
        default=None, validator=optional([instance_of(str), valid_unitsid])
    )
    timeUnits: str = field(
        default=None, validator=optional([instance_of(str), valid_unitsid])
    )
    volumeUnits: str = field(
        default=None, validator=optional([instance_of(str), valid_unitsid])
    )
    areaUnits: str = field(
        default=None, validator=optional([instance_of(str), valid_unitsid])
    )
    lengthUnits: str = field(
        default=None, validator=optional([instance_of(str), valid_unitsid])
    )
    extentUnits: str = field(
        default=None, validator=optional([instance_of(str), valid_unitsid])
    )
    conversionFactor: str = field(
        default=None, validator=optional([instance_of(str), valid_unitsid])
    )

    listOfFunctionDefinitions: List[FunctionDefinition] = field(factory=list)

    listOfUnitDefinitions: ListOfUnitDefinitions = field(
        default=None, validator=optional(instance_of(ListOfUnitDefinitions))
    )

    listOfCompartments: List[Compartment] = field(factory=list)
    listOfSpecies: List[Species] = field(factory=list)
    listOfParameters: List[Parameter] = field(factory=list)
    listOfInitialAssignments: List[InitialAssignment] = field(factory=list)
    listOfRules: List[Rule] = field(factory=list)
    listOfConstraints: List[Constraint] = field(factory=list)
    listOfReactions: List[Reaction] = field(factory=list)
    listOfEvents: List[Event] = field(factory=list)


@modelspec.define
class sbml(SBaseWithId):
    """
    The top-level SBML container implementing SBML 3.2.
    See sbml.level-3.version-2.core.release-2.pdf section 4.
    http://www.sbml.org/sbml/level3/version2/

    Args:
        xmlns:   string, fixed to "http://www.sbml.org/sbml/level3/version2/core"
        level:   SBML level, fixed to 3
        version: SBML version, fixed to 2

        model:   Optional model
    """

    xmlns: str = field(
        default="http://www.sbml.org/sbml/level3/version%s/core" % SBML_VERSION,
        validator=[instance_of(str), xmlns_sbml],
    )
    level: str = field(default=None, validator=[instance_of(str), fixed_level])
    version: str = field(default=None, validator=[instance_of(str), fixed_version])

    model: Model = field(default=None, validator=optional(instance_of(Model)))
    # models: List[Model] = field(factory=list)

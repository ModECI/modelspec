====
sbml
====
The top-level SBML container implementing SBML 3.2. See sbml.level-3.version-2.core.release-2.pdf section 4.
http://www.sbml.org/sbml/level3/version2/

**Allowed parameters**

===============  =======================================  ================================================================
Allowed field    Data Type                                Description
===============  =======================================  ================================================================
**sid**          str                                      SId optional
**name**         str                                      string optional
**metaid**       str                                      XML ID optional
**sboTerm**      str                                      SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**   str                                      XML content optional
**id**           str
**xmlns**        str                                      string, fixed to "http://www.sbml.org/sbml/level3/version2/core"
**level**        str                                      SBML level, fixed to 3
**version**      str                                      SBML version, fixed to 2
**model**        `<class 'sbml32spec.Model'> <#model>`__  Optional model
===============  =======================================  ================================================================

=====
Notes
=====
XHTML field of SBase

**Allowed parameters**

===============  ===========  ========================================
Allowed field    Data Type    Description
===============  ===========  ========================================
**xmlns**        str          str fixed "http://www.w3.org/1999/xhtml"
**content**      str          str valid XHTML
===============  ===========  ========================================

=====
Model
=====
The model

**Allowed parameters**

=========================  =======================================================================  ====================
Allowed field              Data Type                                                                Description
=========================  =======================================================================  ====================
**sid**                    str                                                                      SId optional
**name**                   str                                                                      string optional
**metaid**                 str                                                                      XML ID optional
**sboTerm**                str                                                                      SBOTerm optional
**notes**                  `<class 'sbml32spec.Notes'> <#notes>`__                                  XHTML 1.0 optional
**annotation**             str                                                                      XML content optional
**substanceUnits**         str                                                                      UnitSIdRef optional
**timeUnits**              str                                                                      UnitSIdRef optional
**volumeUnits**            str                                                                      UnitSIdRef optional
**areaUnits**              str                                                                      UnitSIdRef optional
**lengthUnits**            str                                                                      UnitSIdRef optional
**extentUnits**            str                                                                      UnitSIdRef optional
**conversionFactor**       str                                                                      SIdRef optional
**listOfUnitDefinitions**  `<class 'sbml32spec.ListOfUnitDefinitions'> <#listofunitdefinitions>`__
=========================  =======================================================================  ====================

**Allowed children**

=============================  ============================================  =============
Allowed child                  Data Type                                     Description
=============================  ============================================  =============
**listOfFunctionDefinitions**  `FunctionDefinition <#functiondefinition>`__
**listOfCompartments**         `Compartment <#compartment>`__
**listOfSpecies**              `Species <#species>`__
**listOfParameters**           `Parameter <#parameter>`__
**listOfInitialAssignments**   `InitialAssignment <#initialassignment>`__
**listOfRules**                `Rule <#rule>`__
**listOfConstraints**          `Constraint <#constraint>`__
**listOfReactions**            `Reaction <#reaction>`__
**listOfEvents**               `Event <#event>`__
=============================  ============================================  =============

=====
Notes
=====
XHTML field of SBase

**Allowed parameters**

===============  ===========  ========================================
Allowed field    Data Type    Description
===============  ===========  ========================================
**xmlns**        str          str fixed "http://www.w3.org/1999/xhtml"
**content**      str          str valid XHTML
===============  ===========  ========================================

=====================
ListOfUnitDefinitions
=====================
A listOfUnitDefinitions

**Allowed parameters**

===============  =======================================  ====================
Allowed field    Data Type                                Description
===============  =======================================  ====================
**sid**          str                                      SId optional
**name**         str                                      string optional
**metaid**       str                                      XML ID optional
**sboTerm**      str                                      SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**   str                                      XML content optional
===============  =======================================  ====================

**Allowed children**

=========================  ====================================  ===================================
Allowed child              Data Type                             Description
=========================  ====================================  ===================================
**listOfUnitDefinitions**  `unitDefinition <#unitdefinition>`__  the actual list Of Unit Definitions
=========================  ====================================  ===================================

=====
Notes
=====
XHTML field of SBase

**Allowed parameters**

===============  ===========  ========================================
Allowed field    Data Type    Description
===============  ===========  ========================================
**xmlns**        str          str fixed "http://www.w3.org/1999/xhtml"
**content**      str          str valid XHTML
===============  ===========  ========================================

==============
unitDefinition
==============
A unit definition

**Allowed parameters**

===============  ===================================================  ============================================
Allowed field    Data Type                                            Description
===============  ===================================================  ============================================
**sid**          str                                                  SId optional
**name**         str                                                  string optional
**metaid**       str                                                  XML ID optional
**sboTerm**      str                                                  SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__              XHTML 1.0 optional
**annotation**   str                                                  XML content optional
**id**           str
**listOfUnits**  `<class 'sbml32spec.ListOfUnits'> <#listofunits>`__  List of units used to compose the definition
===============  ===================================================  ============================================

=====
Notes
=====
XHTML field of SBase

**Allowed parameters**

===============  ===========  ========================================
Allowed field    Data Type    Description
===============  ===========  ========================================
**xmlns**        str          str fixed "http://www.w3.org/1999/xhtml"
**content**      str          str valid XHTML
===============  ===========  ========================================

===========
ListOfUnits
===========
A listOfUnits

**Allowed parameters**

===============  =======================================  ====================
Allowed field    Data Type                                Description
===============  =======================================  ====================
**sid**          str                                      SId optional
**name**         str                                      string optional
**metaid**       str                                      XML ID optional
**sboTerm**      str                                      SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**   str                                      XML content optional
===============  =======================================  ====================

**Allowed children**

===============  ================  ========================
Allowed child    Data Type         Description
===============  ================  ========================
**listOfUnits**  `unit <#unit>`__  the actual list Of Units
===============  ================  ========================

=====
Notes
=====
XHTML field of SBase

**Allowed parameters**

===============  ===========  ========================================
Allowed field    Data Type    Description
===============  ===========  ========================================
**xmlns**        str          str fixed "http://www.w3.org/1999/xhtml"
**content**      str          str valid XHTML
===============  ===========  ========================================

====
unit
====
A unit used to compose a unit definition. unit = (multiplier x 10^scale x kind)^exponent

**Allowed parameters**

===============  =======================================  =======================================================================
Allowed field    Data Type                                Description
===============  =======================================  =======================================================================
**sid**          str                                      SId optional
**name**         str                                      string optional
**metaid**       str                                      XML ID optional
**sboTerm**      str                                      SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**   str                                      XML content optional
**kind**         str                                      base unit (base or derived SI units only, see Table 2 of the SBML spec)
**exponent**     str                                      double
**scale**        str                                      integer
**multiplier**   str                                      double
===============  =======================================  =======================================================================

=====
Notes
=====
XHTML field of SBase

**Allowed parameters**

===============  ===========  ========================================
Allowed field    Data Type    Description
===============  ===========  ========================================
**xmlns**        str          str fixed "http://www.w3.org/1999/xhtml"
**content**      str          str valid XHTML
===============  ===========  ========================================

==================
FunctionDefinition
==================
A function definition using MathML

**Allowed parameters**

===============  =======================================  ===================================
Allowed field    Data Type                                Description
===============  =======================================  ===================================
**name**         str                                      string optional
**metaid**       str                                      XML ID optional
**sboTerm**      str                                      SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**   str                                      XML content optional
**sid**          str                                      SId optional
**math**         `<class 'sbml32spec.Math'> <#math>`__    MathML function definition optional
===============  =======================================  ===================================

=====
Notes
=====
XHTML field of SBase

**Allowed parameters**

===============  ===========  ========================================
Allowed field    Data Type    Description
===============  ===========  ========================================
**xmlns**        str          str fixed "http://www.w3.org/1999/xhtml"
**content**      str          str valid XHTML
===============  ===========  ========================================

====
Math
====
Subset of MathML 2.0 used to define all formulae in SBML

**Allowed parameters**

===============  ===========  =============
Allowed field    Data Type    Description
===============  ===========  =============
**xmlns**        str
**content**      str
===============  ===========  =============

===========
Compartment
===========
A compartment

**Allowed parameters**

=====================  =======================================  =================================================
Allowed field          Data Type                                Description
=====================  =======================================  =================================================
**sid**                str                                      SId optional
**name**               str                                      string optional
**metaid**             str                                      XML ID optional
**sboTerm**            str                                      SBOTerm optional
**notes**              `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**         str                                      XML content optional
**constant**           bool                                     whether size is fixed
**spatialDimensions**  float                                    eg 3 for three dimensional space etc
**size**               float                                    initial size of compartment
**units**              str                                      units being used to define the compartment's size
=====================  =======================================  =================================================

=====
Notes
=====
XHTML field of SBase

**Allowed parameters**

===============  ===========  ========================================
Allowed field    Data Type    Description
===============  ===========  ========================================
**xmlns**        str          str fixed "http://www.w3.org/1999/xhtml"
**content**      str          str valid XHTML
===============  ===========  ========================================

=======
Species
=======
A species: entities of the same kind participating in reactions within a specific compartment

**Allowed parameters**

=========================  =======================================  ====================
Allowed field              Data Type                                Description
=========================  =======================================  ====================
**sid**                    str                                      SId optional
**name**                   str                                      string optional
**metaid**                 str                                      XML ID optional
**sboTerm**                str                                      SBOTerm optional
**notes**                  `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**             str                                      XML content optional
**compartment**            str                                      SIdRef
**hasOnlySubstanceUnits**  bool                                     boolean
**boundaryCondition**      bool                                     boolean
**constant**               bool                                     boolean
**initialAmount**          float                                    double optional
**initialConcentration**   float                                    double optional
**substanceUnits**         str                                      UnitSIdRef optional
**conversionFactor**       str                                      SIdRef optional
=========================  =======================================  ====================

=====
Notes
=====
XHTML field of SBase

**Allowed parameters**

===============  ===========  ========================================
Allowed field    Data Type    Description
===============  ===========  ========================================
**xmlns**        str          str fixed "http://www.w3.org/1999/xhtml"
**content**      str          str valid XHTML
===============  ===========  ========================================

=========
Parameter
=========
A parameter

**Allowed parameters**

===============  =======================================  ====================
Allowed field    Data Type                                Description
===============  =======================================  ====================
**sid**          str                                      SId optional
**name**         str                                      string optional
**metaid**       str                                      XML ID optional
**sboTerm**      str                                      SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**   str                                      XML content optional
**constant**     bool                                     boolean
**value**        float                                    double optional
**units**        str                                      UnitSIdRef optional
===============  =======================================  ====================

=====
Notes
=====
XHTML field of SBase

**Allowed parameters**

===============  ===========  ========================================
Allowed field    Data Type    Description
===============  ===========  ========================================
**xmlns**        str          str fixed "http://www.w3.org/1999/xhtml"
**content**      str          str valid XHTML
===============  ===========  ========================================

=================
InitialAssignment
=================
An initial assignment

**Allowed parameters**

===============  =======================================  ====================
Allowed field    Data Type                                Description
===============  =======================================  ====================
**sid**          str                                      SId optional
**name**         str                                      string optional
**metaid**       str                                      XML ID optional
**sboTerm**      str                                      SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**   str                                      XML content optional
**symbol**       str                                      SIdRef required
**math**         str                                      MathML optional
===============  =======================================  ====================

=====
Notes
=====
XHTML field of SBase

**Allowed parameters**

===============  ===========  ========================================
Allowed field    Data Type    Description
===============  ===========  ========================================
**xmlns**        str          str fixed "http://www.w3.org/1999/xhtml"
**content**      str          str valid XHTML
===============  ===========  ========================================

====
Rule
====
A rule, either algebraic, assignment or rate

**Allowed parameters**

===============  =======================================  ====================
Allowed field    Data Type                                Description
===============  =======================================  ====================
**sid**          str                                      SId optional
**name**         str                                      string optional
**metaid**       str                                      XML ID optional
**sboTerm**      str                                      SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**   str                                      XML content optional
**math**         str                                      MathML optional
===============  =======================================  ====================

=====
Notes
=====
XHTML field of SBase

**Allowed parameters**

===============  ===========  ========================================
Allowed field    Data Type    Description
===============  ===========  ========================================
**xmlns**        str          str fixed "http://www.w3.org/1999/xhtml"
**content**      str          str valid XHTML
===============  ===========  ========================================

==========
Constraint
==========
A model constraint

**Allowed parameters**

===============  =======================================  ====================
Allowed field    Data Type                                Description
===============  =======================================  ====================
**sid**          str                                      SId optional
**name**         str                                      string optional
**metaid**       str                                      XML ID optional
**sboTerm**      str                                      SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**   str                                      XML content optional
**math**         str                                      MathML optional
**message**      str                                      XHTML 1.0 optional
===============  =======================================  ====================

=====
Notes
=====
XHTML field of SBase

**Allowed parameters**

===============  ===========  ========================================
Allowed field    Data Type    Description
===============  ===========  ========================================
**xmlns**        str          str fixed "http://www.w3.org/1999/xhtml"
**content**      str          str valid XHTML
===============  ===========  ========================================

========
Reaction
========
A model reaction

**Allowed parameters**

===============  =================================================  ====================
Allowed field    Data Type                                          Description
===============  =================================================  ====================
**sid**          str                                                SId optional
**name**         str                                                string optional
**metaid**       str                                                XML ID optional
**sboTerm**      str                                                SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__            XHTML 1.0 optional
**annotation**   str                                                XML content optional
**reversible**   bool                                               boolean
**compartment**  str                                                SIdRef optional
**kineticLaw**   `<class 'sbml32spec.KineticLaw'> <#kineticlaw>`__
===============  =================================================  ====================

**Allowed children**

===================  ========================================================  =============
Allowed child        Data Type                                                 Description
===================  ========================================================  =============
**listOfReactants**  `SpeciesReference <#speciesreference>`__
**listOfProducts**   `SpeciesReference <#speciesreference>`__
**listOfModifiers**  `ModifierSpeciesReference <#modifierspeciesreference>`__
===================  ========================================================  =============

=====
Notes
=====
XHTML field of SBase

**Allowed parameters**

===============  ===========  ========================================
Allowed field    Data Type    Description
===============  ===========  ========================================
**xmlns**        str          str fixed "http://www.w3.org/1999/xhtml"
**content**      str          str valid XHTML
===============  ===========  ========================================

==========
KineticLaw
==========
**Allowed parameters**

===============  =======================================  ====================
Allowed field    Data Type                                Description
===============  =======================================  ====================
**sid**          str                                      SId optional
**name**         str                                      string optional
**metaid**       str                                      XML ID optional
**sboTerm**      str                                      SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**   str                                      XML content optional
**math**         str
===============  =======================================  ====================

**Allowed children**

=========================  ====================================  =============
Allowed child              Data Type                             Description
=========================  ====================================  =============
**listOfLocalParameters**  `LocalParameter <#localparameter>`__
=========================  ====================================  =============

=====
Notes
=====
XHTML field of SBase

**Allowed parameters**

===============  ===========  ========================================
Allowed field    Data Type    Description
===============  ===========  ========================================
**xmlns**        str          str fixed "http://www.w3.org/1999/xhtml"
**content**      str          str valid XHTML
===============  ===========  ========================================

==============
LocalParameter
==============
**Allowed parameters**

===============  =======================================  ====================
Allowed field    Data Type                                Description
===============  =======================================  ====================
**sid**          str                                      SId optional
**name**         str                                      string optional
**metaid**       str                                      XML ID optional
**sboTerm**      str                                      SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**   str                                      XML content optional
**value**        float
**units**        str                                      UnitSIdRef optional
===============  =======================================  ====================

=====
Notes
=====
XHTML field of SBase

**Allowed parameters**

===============  ===========  ========================================
Allowed field    Data Type    Description
===============  ===========  ========================================
**xmlns**        str          str fixed "http://www.w3.org/1999/xhtml"
**content**      str          str valid XHTML
===============  ===========  ========================================

================
SpeciesReference
================
**Allowed parameters**

=================  =======================================  ====================
Allowed field      Data Type                                Description
=================  =======================================  ====================
**sid**            str                                      SId optional
**name**           str                                      string optional
**metaid**         str                                      XML ID optional
**sboTerm**        str                                      SBOTerm optional
**notes**          `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**     str                                      XML content optional
**species**        str                                      SIdRef
**stoichiometry**  float                                    double optional
**constant**       bool                                     boolean
=================  =======================================  ====================

=====
Notes
=====
XHTML field of SBase

**Allowed parameters**

===============  ===========  ========================================
Allowed field    Data Type    Description
===============  ===========  ========================================
**xmlns**        str          str fixed "http://www.w3.org/1999/xhtml"
**content**      str          str valid XHTML
===============  ===========  ========================================

================
SpeciesReference
================
**Allowed parameters**

=================  =======================================  ====================
Allowed field      Data Type                                Description
=================  =======================================  ====================
**sid**            str                                      SId optional
**name**           str                                      string optional
**metaid**         str                                      XML ID optional
**sboTerm**        str                                      SBOTerm optional
**notes**          `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**     str                                      XML content optional
**species**        str                                      SIdRef
**stoichiometry**  float                                    double optional
**constant**       bool                                     boolean
=================  =======================================  ====================

=====
Notes
=====
XHTML field of SBase

**Allowed parameters**

===============  ===========  ========================================
Allowed field    Data Type    Description
===============  ===========  ========================================
**xmlns**        str          str fixed "http://www.w3.org/1999/xhtml"
**content**      str          str valid XHTML
===============  ===========  ========================================

========================
ModifierSpeciesReference
========================
**Allowed parameters**

===============  =======================================  ====================
Allowed field    Data Type                                Description
===============  =======================================  ====================
**sid**          str                                      SId optional
**name**         str                                      string optional
**metaid**       str                                      XML ID optional
**sboTerm**      str                                      SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**   str                                      XML content optional
**species**      str                                      SIdRef
===============  =======================================  ====================

=====
Notes
=====
XHTML field of SBase

**Allowed parameters**

===============  ===========  ========================================
Allowed field    Data Type    Description
===============  ===========  ========================================
**xmlns**        str          str fixed "http://www.w3.org/1999/xhtml"
**content**      str          str valid XHTML
===============  ===========  ========================================

=====
Event
=====
**Allowed parameters**

============================  =============================================  ====================
Allowed field                 Data Type                                      Description
============================  =============================================  ====================
**sid**                       str                                            SId optional
**name**                      str                                            string optional
**metaid**                    str                                            XML ID optional
**sboTerm**                   str                                            SBOTerm optional
**notes**                     `<class 'sbml32spec.Notes'> <#notes>`__        XHTML 1.0 optional
**annotation**                str                                            XML content optional
**useValuesFromTriggerTime**  bool
**trigger**                   `<class 'sbml32spec.Trigger'> <#trigger>`__
**priority**                  `<class 'sbml32spec.Priority'> <#priority>`__
**delay**                     `<class 'sbml32spec.Delay'> <#delay>`__
============================  =============================================  ====================

**Allowed children**

==========================  ======================================  =============
Allowed child               Data Type                               Description
==========================  ======================================  =============
**listOfEventAssignments**  `EventAssignment <#eventassignment>`__
==========================  ======================================  =============

=====
Notes
=====
XHTML field of SBase

**Allowed parameters**

===============  ===========  ========================================
Allowed field    Data Type    Description
===============  ===========  ========================================
**xmlns**        str          str fixed "http://www.w3.org/1999/xhtml"
**content**      str          str valid XHTML
===============  ===========  ========================================

=======
Trigger
=======
**Allowed parameters**

================  =======================================  ====================
Allowed field     Data Type                                Description
================  =======================================  ====================
**sid**           str                                      SId optional
**name**          str                                      string optional
**metaid**        str                                      XML ID optional
**sboTerm**       str                                      SBOTerm optional
**notes**         `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**    str                                      XML content optional
**initialValue**  bool
**persistent**    bool
**math**          str
================  =======================================  ====================

=====
Notes
=====
XHTML field of SBase

**Allowed parameters**

===============  ===========  ========================================
Allowed field    Data Type    Description
===============  ===========  ========================================
**xmlns**        str          str fixed "http://www.w3.org/1999/xhtml"
**content**      str          str valid XHTML
===============  ===========  ========================================

========
Priority
========
**Allowed parameters**

===============  =======================================  ====================
Allowed field    Data Type                                Description
===============  =======================================  ====================
**sid**          str                                      SId optional
**name**         str                                      string optional
**metaid**       str                                      XML ID optional
**sboTerm**      str                                      SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**   str                                      XML content optional
**math**         str
===============  =======================================  ====================

=====
Notes
=====
XHTML field of SBase

**Allowed parameters**

===============  ===========  ========================================
Allowed field    Data Type    Description
===============  ===========  ========================================
**xmlns**        str          str fixed "http://www.w3.org/1999/xhtml"
**content**      str          str valid XHTML
===============  ===========  ========================================

=====
Delay
=====
**Allowed parameters**

===============  =======================================  ====================
Allowed field    Data Type                                Description
===============  =======================================  ====================
**sid**          str                                      SId optional
**name**         str                                      string optional
**metaid**       str                                      XML ID optional
**sboTerm**      str                                      SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**   str                                      XML content optional
**math**         str
===============  =======================================  ====================

=====
Notes
=====
XHTML field of SBase

**Allowed parameters**

===============  ===========  ========================================
Allowed field    Data Type    Description
===============  ===========  ========================================
**xmlns**        str          str fixed "http://www.w3.org/1999/xhtml"
**content**      str          str valid XHTML
===============  ===========  ========================================

===============
EventAssignment
===============
**Allowed parameters**

===============  =======================================  ====================
Allowed field    Data Type                                Description
===============  =======================================  ====================
**sid**          str                                      SId optional
**name**         str                                      string optional
**metaid**       str                                      XML ID optional
**sboTerm**      str                                      SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**   str                                      XML content optional
**math**         str
**variable**     str                                      SIdRef
===============  =======================================  ====================

=====
Notes
=====
XHTML field of SBase

**Allowed parameters**

===============  ===========  ========================================
Allowed field    Data Type    Description
===============  ===========  ========================================
**xmlns**        str          str fixed "http://www.w3.org/1999/xhtml"
**content**      str          str valid XHTML
===============  ===========  ========================================

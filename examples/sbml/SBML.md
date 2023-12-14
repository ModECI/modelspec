## sbml
The top-level SBML container implementing SBML 3.2. See sbml.level-3.version-2.core.release-2.pdf section 4.
http://www.sbml.org/sbml/level3/version2/

### Allowed parameters
<table>
  <tr>
    <td><b>sid</b></td>
    <td>str</td>
    <td><i>    SId optional</i></td>
 </tr>


  <tr>
    <td><b>name</b></td>
    <td>str</td>
    <td><i>   string optional</i></td>
 </tr>


  <tr>
    <td><b>metaid</b></td>
    <td>str</td>
    <td><i> XML ID optional</i></td>
 </tr>


  <tr>
    <td><b>sboTerm</b></td>
    <td>str</td>
    <td><i>SBOTerm optional</i></td>
 </tr>


  <tr>
    <td><b>notes</b></td>
    <td><a href="#notes">Notes</a></td>
    <td><i>     XHTML 1.0 optional</i></td>
 </tr>


  <tr>
    <td><b>annotation</b></td>
    <td>str</td>
    <td><i>XML content optional</i></td>
 </tr>


  <tr>
    <td><b>id</b></td>
    <td>str</td>
    <td><i></i></td>
 </tr>


  <tr>
    <td><b>xmlns</b></td>
    <td>str</td>
    <td><i>  string, fixed to "http://www.sbml.org/sbml/level3/version2/core"</i></td>
 </tr>


  <tr>
    <td><b>level</b></td>
    <td>str</td>
    <td><i>  SBML level, fixed to 3</i></td>
 </tr>


  <tr>
    <td><b>version</b></td>
    <td>str</td>
    <td><i>SBML version, fixed to 2</i></td>
 </tr>


  <tr>
    <td><b>model</b></td>
    <td><a href="#model">Model</a></td>
    <td><i>  Optional model</i></td>
 </tr>


</table>

## Notes
XHTML field of SBase

### Allowed parameters
<table>
  <tr>
    <td><b>xmlns</b></td>
    <td>str</td>
    <td><i>str fixed "http://www.w3.org/1999/xhtml"</i></td>
 </tr>


  <tr>
    <td><b>content</b></td>
    <td>str</td>
    <td><i>str valid XHTML</i></td>
 </tr>


</table>

## Model
The model

### Allowed parameters
<table>
  <tr>
    <td><b>sid</b></td>
    <td>str</td>
    <td><i>    SId optional</i></td>
 </tr>


  <tr>
    <td><b>name</b></td>
    <td>str</td>
    <td><i>   string optional</i></td>
 </tr>


  <tr>
    <td><b>metaid</b></td>
    <td>str</td>
    <td><i> XML ID optional</i></td>
 </tr>


  <tr>
    <td><b>sboTerm</b></td>
    <td>str</td>
    <td><i>SBOTerm optional</i></td>
 </tr>


  <tr>
    <td><b>notes</b></td>
    <td><a href="#notes">Notes</a></td>
    <td><i>     XHTML 1.0 optional</i></td>
 </tr>


  <tr>
    <td><b>annotation</b></td>
    <td>str</td>
    <td><i>XML content optional</i></td>
 </tr>


  <tr>
    <td><b>substanceUnits</b></td>
    <td>str</td>
    <td><i>  UnitSIdRef optional</i></td>
 </tr>


  <tr>
    <td><b>timeUnits</b></td>
    <td>str</td>
    <td><i>       UnitSIdRef optional</i></td>
 </tr>


  <tr>
    <td><b>volumeUnits</b></td>
    <td>str</td>
    <td><i>     UnitSIdRef optional</i></td>
 </tr>


  <tr>
    <td><b>areaUnits</b></td>
    <td>str</td>
    <td><i>       UnitSIdRef optional</i></td>
 </tr>


  <tr>
    <td><b>lengthUnits</b></td>
    <td>str</td>
    <td><i>     UnitSIdRef optional</i></td>
 </tr>


  <tr>
    <td><b>extentUnits</b></td>
    <td>str</td>
    <td><i>     UnitSIdRef optional</i></td>
 </tr>


  <tr>
    <td><b>conversionFactor</b></td>
    <td>str</td>
    <td><i>SIdRef optional</i></td>
 </tr>


  <tr>
    <td><b>listOfUnitDefinitions</b></td>
    <td><a href="#listofunitdefinitions">ListOfUnitDefinitions</a></td>
    <td><i></i></td>
 </tr>


</table>

### Allowed children
<table>
  <tr>
    <td><b>listOfFunctionDefinitions</b></td>
    <td><a href="#functiondefinition">FunctionDefinition</a></td>
    <td><i></i></td>
  </tr>


  <tr>
    <td><b>listOfCompartments</b></td>
    <td><a href="#compartment">Compartment</a></td>
    <td><i></i></td>
  </tr>


  <tr>
    <td><b>listOfSpecies</b></td>
    <td><a href="#species">Species</a></td>
    <td><i></i></td>
  </tr>


  <tr>
    <td><b>listOfParameters</b></td>
    <td><a href="#parameter">Parameter</a></td>
    <td><i></i></td>
  </tr>


  <tr>
    <td><b>listOfInitialAssignments</b></td>
    <td><a href="#initialassignment">InitialAssignment</a></td>
    <td><i></i></td>
  </tr>


  <tr>
    <td><b>listOfRules</b></td>
    <td><a href="#rule">Rule</a></td>
    <td><i></i></td>
  </tr>


  <tr>
    <td><b>listOfConstraints</b></td>
    <td><a href="#constraint">Constraint</a></td>
    <td><i></i></td>
  </tr>


  <tr>
    <td><b>listOfReactions</b></td>
    <td><a href="#reaction">Reaction</a></td>
    <td><i></i></td>
  </tr>


  <tr>
    <td><b>listOfEvents</b></td>
    <td><a href="#event">Event</a></td>
    <td><i></i></td>
  </tr>


</table>

## Notes
XHTML field of SBase

### Allowed parameters
<table>
  <tr>
    <td><b>xmlns</b></td>
    <td>str</td>
    <td><i>str fixed "http://www.w3.org/1999/xhtml"</i></td>
 </tr>


  <tr>
    <td><b>content</b></td>
    <td>str</td>
    <td><i>str valid XHTML</i></td>
 </tr>


</table>

## ListOfUnitDefinitions
A listOfUnitDefinitions

### Allowed parameters
<table>
  <tr>
    <td><b>sid</b></td>
    <td>str</td>
    <td><i>    SId optional</i></td>
 </tr>


  <tr>
    <td><b>name</b></td>
    <td>str</td>
    <td><i>   string optional</i></td>
 </tr>


  <tr>
    <td><b>metaid</b></td>
    <td>str</td>
    <td><i> XML ID optional</i></td>
 </tr>


  <tr>
    <td><b>sboTerm</b></td>
    <td>str</td>
    <td><i>SBOTerm optional</i></td>
 </tr>


  <tr>
    <td><b>notes</b></td>
    <td><a href="#notes">Notes</a></td>
    <td><i>     XHTML 1.0 optional</i></td>
 </tr>


  <tr>
    <td><b>annotation</b></td>
    <td>str</td>
    <td><i>XML content optional</i></td>
 </tr>


</table>

### Allowed children
<table>
  <tr>
    <td><b>listOfUnitDefinitions</b></td>
    <td><a href="#unitdefinition">unitDefinition</a></td>
    <td><i>the actual list Of Unit Definitions</i></td>
  </tr>


</table>

## Notes
XHTML field of SBase

### Allowed parameters
<table>
  <tr>
    <td><b>xmlns</b></td>
    <td>str</td>
    <td><i>str fixed "http://www.w3.org/1999/xhtml"</i></td>
 </tr>


  <tr>
    <td><b>content</b></td>
    <td>str</td>
    <td><i>str valid XHTML</i></td>
 </tr>


</table>

## unitDefinition
A unit definition

### Allowed parameters
<table>
  <tr>
    <td><b>sid</b></td>
    <td>str</td>
    <td><i>    SId optional</i></td>
 </tr>


  <tr>
    <td><b>name</b></td>
    <td>str</td>
    <td><i>   string optional</i></td>
 </tr>


  <tr>
    <td><b>metaid</b></td>
    <td>str</td>
    <td><i> XML ID optional</i></td>
 </tr>


  <tr>
    <td><b>sboTerm</b></td>
    <td>str</td>
    <td><i>SBOTerm optional</i></td>
 </tr>


  <tr>
    <td><b>notes</b></td>
    <td><a href="#notes">Notes</a></td>
    <td><i>     XHTML 1.0 optional</i></td>
 </tr>


  <tr>
    <td><b>annotation</b></td>
    <td>str</td>
    <td><i>XML content optional</i></td>
 </tr>


  <tr>
    <td><b>id</b></td>
    <td>str</td>
    <td><i></i></td>
 </tr>


  <tr>
    <td><b>listOfUnits</b></td>
    <td><a href="#listofunits">ListOfUnits</a></td>
    <td><i>List of units used to compose the definition</i></td>
 </tr>


</table>

## Notes
XHTML field of SBase

### Allowed parameters
<table>
  <tr>
    <td><b>xmlns</b></td>
    <td>str</td>
    <td><i>str fixed "http://www.w3.org/1999/xhtml"</i></td>
 </tr>


  <tr>
    <td><b>content</b></td>
    <td>str</td>
    <td><i>str valid XHTML</i></td>
 </tr>


</table>

## ListOfUnits
A listOfUnits

### Allowed parameters
<table>
  <tr>
    <td><b>sid</b></td>
    <td>str</td>
    <td><i>    SId optional</i></td>
 </tr>


  <tr>
    <td><b>name</b></td>
    <td>str</td>
    <td><i>   string optional</i></td>
 </tr>


  <tr>
    <td><b>metaid</b></td>
    <td>str</td>
    <td><i> XML ID optional</i></td>
 </tr>


  <tr>
    <td><b>sboTerm</b></td>
    <td>str</td>
    <td><i>SBOTerm optional</i></td>
 </tr>


  <tr>
    <td><b>notes</b></td>
    <td><a href="#notes">Notes</a></td>
    <td><i>     XHTML 1.0 optional</i></td>
 </tr>


  <tr>
    <td><b>annotation</b></td>
    <td>str</td>
    <td><i>XML content optional</i></td>
 </tr>


</table>

### Allowed children
<table>
  <tr>
    <td><b>listOfUnits</b></td>
    <td><a href="#unit">unit</a></td>
    <td><i>the actual list Of Units</i></td>
  </tr>


</table>

## Notes
XHTML field of SBase

### Allowed parameters
<table>
  <tr>
    <td><b>xmlns</b></td>
    <td>str</td>
    <td><i>str fixed "http://www.w3.org/1999/xhtml"</i></td>
 </tr>


  <tr>
    <td><b>content</b></td>
    <td>str</td>
    <td><i>str valid XHTML</i></td>
 </tr>


</table>

## unit
A unit used to compose a unit definition. unit = (multiplier x 10^scale x kind)^exponent

### Allowed parameters
<table>
  <tr>
    <td><b>sid</b></td>
    <td>str</td>
    <td><i>    SId optional</i></td>
 </tr>


  <tr>
    <td><b>name</b></td>
    <td>str</td>
    <td><i>   string optional</i></td>
 </tr>


  <tr>
    <td><b>metaid</b></td>
    <td>str</td>
    <td><i> XML ID optional</i></td>
 </tr>


  <tr>
    <td><b>sboTerm</b></td>
    <td>str</td>
    <td><i>SBOTerm optional</i></td>
 </tr>


  <tr>
    <td><b>notes</b></td>
    <td><a href="#notes">Notes</a></td>
    <td><i>     XHTML 1.0 optional</i></td>
 </tr>


  <tr>
    <td><b>annotation</b></td>
    <td>str</td>
    <td><i>XML content optional</i></td>
 </tr>


  <tr>
    <td><b>kind</b></td>
    <td>str</td>
    <td><i>base unit (base or derived SI units only, see Table 2 of the SBML spec)</i></td>
 </tr>


  <tr>
    <td><b>exponent</b></td>
    <td>str</td>
    <td><i>double</i></td>
 </tr>


  <tr>
    <td><b>scale</b></td>
    <td>str</td>
    <td><i>integer</i></td>
 </tr>


  <tr>
    <td><b>multiplier</b></td>
    <td>str</td>
    <td><i>double</i></td>
 </tr>


</table>

## Notes
XHTML field of SBase

### Allowed parameters
<table>
  <tr>
    <td><b>xmlns</b></td>
    <td>str</td>
    <td><i>str fixed "http://www.w3.org/1999/xhtml"</i></td>
 </tr>


  <tr>
    <td><b>content</b></td>
    <td>str</td>
    <td><i>str valid XHTML</i></td>
 </tr>


</table>

## FunctionDefinition
A function definition using MathML

### Allowed parameters
<table>
  <tr>
    <td><b>name</b></td>
    <td>str</td>
    <td><i>   string optional</i></td>
 </tr>


  <tr>
    <td><b>metaid</b></td>
    <td>str</td>
    <td><i> XML ID optional</i></td>
 </tr>


  <tr>
    <td><b>sboTerm</b></td>
    <td>str</td>
    <td><i>SBOTerm optional</i></td>
 </tr>


  <tr>
    <td><b>notes</b></td>
    <td><a href="#notes">Notes</a></td>
    <td><i>     XHTML 1.0 optional</i></td>
 </tr>


  <tr>
    <td><b>annotation</b></td>
    <td>str</td>
    <td><i>XML content optional</i></td>
 </tr>


  <tr>
    <td><b>sid</b></td>
    <td>str</td>
    <td><i>    SId optional</i></td>
 </tr>


  <tr>
    <td><b>math</b></td>
    <td><a href="#math">Math</a></td>
    <td><i>MathML function definition optional</i></td>
 </tr>


</table>

## Notes
XHTML field of SBase

### Allowed parameters
<table>
  <tr>
    <td><b>xmlns</b></td>
    <td>str</td>
    <td><i>str fixed "http://www.w3.org/1999/xhtml"</i></td>
 </tr>


  <tr>
    <td><b>content</b></td>
    <td>str</td>
    <td><i>str valid XHTML</i></td>
 </tr>


</table>

## Math
Subset of MathML 2.0 used to define all formulae in SBML

### Allowed parameters
<table>
  <tr>
    <td><b>xmlns</b></td>
    <td>str</td>
    <td><i></i></td>
 </tr>


  <tr>
    <td><b>content</b></td>
    <td>str</td>
    <td><i></i></td>
 </tr>


</table>

## Compartment
A compartment

### Allowed parameters
<table>
  <tr>
    <td><b>sid</b></td>
    <td>str</td>
    <td><i>    SId optional</i></td>
 </tr>


  <tr>
    <td><b>name</b></td>
    <td>str</td>
    <td><i>   string optional</i></td>
 </tr>


  <tr>
    <td><b>metaid</b></td>
    <td>str</td>
    <td><i> XML ID optional</i></td>
 </tr>


  <tr>
    <td><b>sboTerm</b></td>
    <td>str</td>
    <td><i>SBOTerm optional</i></td>
 </tr>


  <tr>
    <td><b>notes</b></td>
    <td><a href="#notes">Notes</a></td>
    <td><i>     XHTML 1.0 optional</i></td>
 </tr>


  <tr>
    <td><b>annotation</b></td>
    <td>str</td>
    <td><i>XML content optional</i></td>
 </tr>


  <tr>
    <td><b>constant</b></td>
    <td>bool</td>
    <td><i>whether size is fixed</i></td>
 </tr>


  <tr>
    <td><b>spatialDimensions</b></td>
    <td>float</td>
    <td><i>eg 3 for three dimensional space etc</i></td>
 </tr>


  <tr>
    <td><b>size</b></td>
    <td>float</td>
    <td><i>initial size of compartment</i></td>
 </tr>


  <tr>
    <td><b>units</b></td>
    <td>str</td>
    <td><i>units being used to define the compartment's size</i></td>
 </tr>


</table>

## Notes
XHTML field of SBase

### Allowed parameters
<table>
  <tr>
    <td><b>xmlns</b></td>
    <td>str</td>
    <td><i>str fixed "http://www.w3.org/1999/xhtml"</i></td>
 </tr>


  <tr>
    <td><b>content</b></td>
    <td>str</td>
    <td><i>str valid XHTML</i></td>
 </tr>


</table>

## Species
A species: entities of the same kind participating in reactions within a specific compartment

### Allowed parameters
<table>
  <tr>
    <td><b>sid</b></td>
    <td>str</td>
    <td><i>    SId optional</i></td>
 </tr>


  <tr>
    <td><b>name</b></td>
    <td>str</td>
    <td><i>   string optional</i></td>
 </tr>


  <tr>
    <td><b>metaid</b></td>
    <td>str</td>
    <td><i> XML ID optional</i></td>
 </tr>


  <tr>
    <td><b>sboTerm</b></td>
    <td>str</td>
    <td><i>SBOTerm optional</i></td>
 </tr>


  <tr>
    <td><b>notes</b></td>
    <td><a href="#notes">Notes</a></td>
    <td><i>     XHTML 1.0 optional</i></td>
 </tr>


  <tr>
    <td><b>annotation</b></td>
    <td>str</td>
    <td><i>XML content optional</i></td>
 </tr>


  <tr>
    <td><b>compartment</b></td>
    <td>str</td>
    <td><i>SIdRef</i></td>
 </tr>


  <tr>
    <td><b>hasOnlySubstanceUnits</b></td>
    <td>bool</td>
    <td><i>boolean</i></td>
 </tr>


  <tr>
    <td><b>boundaryCondition</b></td>
    <td>bool</td>
    <td><i>boolean</i></td>
 </tr>


  <tr>
    <td><b>constant</b></td>
    <td>bool</td>
    <td><i>boolean</i></td>
 </tr>


  <tr>
    <td><b>initialAmount</b></td>
    <td>float</td>
    <td><i>double optional</i></td>
 </tr>


  <tr>
    <td><b>initialConcentration</b></td>
    <td>float</td>
    <td><i>double optional</i></td>
 </tr>


  <tr>
    <td><b>substanceUnits</b></td>
    <td>str</td>
    <td><i>UnitSIdRef optional</i></td>
 </tr>


  <tr>
    <td><b>conversionFactor</b></td>
    <td>str</td>
    <td><i>SIdRef optional</i></td>
 </tr>


</table>

## Notes
XHTML field of SBase

### Allowed parameters
<table>
  <tr>
    <td><b>xmlns</b></td>
    <td>str</td>
    <td><i>str fixed "http://www.w3.org/1999/xhtml"</i></td>
 </tr>


  <tr>
    <td><b>content</b></td>
    <td>str</td>
    <td><i>str valid XHTML</i></td>
 </tr>


</table>

## Parameter
A parameter

### Allowed parameters
<table>
  <tr>
    <td><b>sid</b></td>
    <td>str</td>
    <td><i>    SId optional</i></td>
 </tr>


  <tr>
    <td><b>name</b></td>
    <td>str</td>
    <td><i>   string optional</i></td>
 </tr>


  <tr>
    <td><b>metaid</b></td>
    <td>str</td>
    <td><i> XML ID optional</i></td>
 </tr>


  <tr>
    <td><b>sboTerm</b></td>
    <td>str</td>
    <td><i>SBOTerm optional</i></td>
 </tr>


  <tr>
    <td><b>notes</b></td>
    <td><a href="#notes">Notes</a></td>
    <td><i>     XHTML 1.0 optional</i></td>
 </tr>


  <tr>
    <td><b>annotation</b></td>
    <td>str</td>
    <td><i>XML content optional</i></td>
 </tr>


  <tr>
    <td><b>constant</b></td>
    <td>bool</td>
    <td><i>boolean</i></td>
 </tr>


  <tr>
    <td><b>value</b></td>
    <td>float</td>
    <td><i>double optional</i></td>
 </tr>


  <tr>
    <td><b>units</b></td>
    <td>str</td>
    <td><i>UnitSIdRef optional</i></td>
 </tr>


</table>

## Notes
XHTML field of SBase

### Allowed parameters
<table>
  <tr>
    <td><b>xmlns</b></td>
    <td>str</td>
    <td><i>str fixed "http://www.w3.org/1999/xhtml"</i></td>
 </tr>


  <tr>
    <td><b>content</b></td>
    <td>str</td>
    <td><i>str valid XHTML</i></td>
 </tr>


</table>

## InitialAssignment
An initial assignment

### Allowed parameters
<table>
  <tr>
    <td><b>sid</b></td>
    <td>str</td>
    <td><i>    SId optional</i></td>
 </tr>


  <tr>
    <td><b>name</b></td>
    <td>str</td>
    <td><i>   string optional</i></td>
 </tr>


  <tr>
    <td><b>metaid</b></td>
    <td>str</td>
    <td><i> XML ID optional</i></td>
 </tr>


  <tr>
    <td><b>sboTerm</b></td>
    <td>str</td>
    <td><i>SBOTerm optional</i></td>
 </tr>


  <tr>
    <td><b>notes</b></td>
    <td><a href="#notes">Notes</a></td>
    <td><i>     XHTML 1.0 optional</i></td>
 </tr>


  <tr>
    <td><b>annotation</b></td>
    <td>str</td>
    <td><i>XML content optional</i></td>
 </tr>


  <tr>
    <td><b>symbol</b></td>
    <td>str</td>
    <td><i>SIdRef required</i></td>
 </tr>


  <tr>
    <td><b>math</b></td>
    <td>str</td>
    <td><i>MathML optional</i></td>
 </tr>


</table>

## Notes
XHTML field of SBase

### Allowed parameters
<table>
  <tr>
    <td><b>xmlns</b></td>
    <td>str</td>
    <td><i>str fixed "http://www.w3.org/1999/xhtml"</i></td>
 </tr>


  <tr>
    <td><b>content</b></td>
    <td>str</td>
    <td><i>str valid XHTML</i></td>
 </tr>


</table>

## Rule
A rule, either algebraic, assignment or rate

### Allowed parameters
<table>
  <tr>
    <td><b>sid</b></td>
    <td>str</td>
    <td><i>    SId optional</i></td>
 </tr>


  <tr>
    <td><b>name</b></td>
    <td>str</td>
    <td><i>   string optional</i></td>
 </tr>


  <tr>
    <td><b>metaid</b></td>
    <td>str</td>
    <td><i> XML ID optional</i></td>
 </tr>


  <tr>
    <td><b>sboTerm</b></td>
    <td>str</td>
    <td><i>SBOTerm optional</i></td>
 </tr>


  <tr>
    <td><b>notes</b></td>
    <td><a href="#notes">Notes</a></td>
    <td><i>     XHTML 1.0 optional</i></td>
 </tr>


  <tr>
    <td><b>annotation</b></td>
    <td>str</td>
    <td><i>XML content optional</i></td>
 </tr>


  <tr>
    <td><b>math</b></td>
    <td>str</td>
    <td><i>MathML optional</i></td>
 </tr>


</table>

## Notes
XHTML field of SBase

### Allowed parameters
<table>
  <tr>
    <td><b>xmlns</b></td>
    <td>str</td>
    <td><i>str fixed "http://www.w3.org/1999/xhtml"</i></td>
 </tr>


  <tr>
    <td><b>content</b></td>
    <td>str</td>
    <td><i>str valid XHTML</i></td>
 </tr>


</table>

## Constraint
A model constraint

### Allowed parameters
<table>
  <tr>
    <td><b>sid</b></td>
    <td>str</td>
    <td><i>    SId optional</i></td>
 </tr>


  <tr>
    <td><b>name</b></td>
    <td>str</td>
    <td><i>   string optional</i></td>
 </tr>


  <tr>
    <td><b>metaid</b></td>
    <td>str</td>
    <td><i> XML ID optional</i></td>
 </tr>


  <tr>
    <td><b>sboTerm</b></td>
    <td>str</td>
    <td><i>SBOTerm optional</i></td>
 </tr>


  <tr>
    <td><b>notes</b></td>
    <td><a href="#notes">Notes</a></td>
    <td><i>     XHTML 1.0 optional</i></td>
 </tr>


  <tr>
    <td><b>annotation</b></td>
    <td>str</td>
    <td><i>XML content optional</i></td>
 </tr>


  <tr>
    <td><b>math</b></td>
    <td>str</td>
    <td><i>   MathML optional</i></td>
 </tr>


  <tr>
    <td><b>message</b></td>
    <td>str</td>
    <td><i>XHTML 1.0 optional</i></td>
 </tr>


</table>

## Notes
XHTML field of SBase

### Allowed parameters
<table>
  <tr>
    <td><b>xmlns</b></td>
    <td>str</td>
    <td><i>str fixed "http://www.w3.org/1999/xhtml"</i></td>
 </tr>


  <tr>
    <td><b>content</b></td>
    <td>str</td>
    <td><i>str valid XHTML</i></td>
 </tr>


</table>

## Reaction
A model reaction

### Allowed parameters
<table>
  <tr>
    <td><b>sid</b></td>
    <td>str</td>
    <td><i>    SId optional</i></td>
 </tr>


  <tr>
    <td><b>name</b></td>
    <td>str</td>
    <td><i>   string optional</i></td>
 </tr>


  <tr>
    <td><b>metaid</b></td>
    <td>str</td>
    <td><i> XML ID optional</i></td>
 </tr>


  <tr>
    <td><b>sboTerm</b></td>
    <td>str</td>
    <td><i>SBOTerm optional</i></td>
 </tr>


  <tr>
    <td><b>notes</b></td>
    <td><a href="#notes">Notes</a></td>
    <td><i>     XHTML 1.0 optional</i></td>
 </tr>


  <tr>
    <td><b>annotation</b></td>
    <td>str</td>
    <td><i>XML content optional</i></td>
 </tr>


  <tr>
    <td><b>reversible</b></td>
    <td>bool</td>
    <td><i>boolean</i></td>
 </tr>


  <tr>
    <td><b>compartment</b></td>
    <td>str</td>
    <td><i>SIdRef optional</i></td>
 </tr>


  <tr>
    <td><b>kineticLaw</b></td>
    <td><a href="#kineticlaw">KineticLaw</a></td>
    <td><i></i></td>
 </tr>


</table>

### Allowed children
<table>
  <tr>
    <td><b>listOfReactants</b></td>
    <td><a href="#speciesreference">SpeciesReference</a></td>
    <td><i></i></td>
  </tr>


  <tr>
    <td><b>listOfProducts</b></td>
    <td><a href="#speciesreference">SpeciesReference</a></td>
    <td><i></i></td>
  </tr>


  <tr>
    <td><b>listOfModifiers</b></td>
    <td><a href="#modifierspeciesreference">ModifierSpeciesReference</a></td>
    <td><i></i></td>
  </tr>


</table>

## Notes
XHTML field of SBase

### Allowed parameters
<table>
  <tr>
    <td><b>xmlns</b></td>
    <td>str</td>
    <td><i>str fixed "http://www.w3.org/1999/xhtml"</i></td>
 </tr>


  <tr>
    <td><b>content</b></td>
    <td>str</td>
    <td><i>str valid XHTML</i></td>
 </tr>


</table>

## KineticLaw
### Allowed parameters
<table>
  <tr>
    <td><b>sid</b></td>
    <td>str</td>
    <td><i>    SId optional</i></td>
 </tr>


  <tr>
    <td><b>name</b></td>
    <td>str</td>
    <td><i>   string optional</i></td>
 </tr>


  <tr>
    <td><b>metaid</b></td>
    <td>str</td>
    <td><i> XML ID optional</i></td>
 </tr>


  <tr>
    <td><b>sboTerm</b></td>
    <td>str</td>
    <td><i>SBOTerm optional</i></td>
 </tr>


  <tr>
    <td><b>notes</b></td>
    <td><a href="#notes">Notes</a></td>
    <td><i>     XHTML 1.0 optional</i></td>
 </tr>


  <tr>
    <td><b>annotation</b></td>
    <td>str</td>
    <td><i>XML content optional</i></td>
 </tr>


  <tr>
    <td><b>math</b></td>
    <td>str</td>
    <td><i></i></td>
 </tr>


</table>

### Allowed children
<table>
  <tr>
    <td><b>listOfLocalParameters</b></td>
    <td><a href="#localparameter">LocalParameter</a></td>
    <td><i></i></td>
  </tr>


</table>

## Notes
XHTML field of SBase

### Allowed parameters
<table>
  <tr>
    <td><b>xmlns</b></td>
    <td>str</td>
    <td><i>str fixed "http://www.w3.org/1999/xhtml"</i></td>
 </tr>


  <tr>
    <td><b>content</b></td>
    <td>str</td>
    <td><i>str valid XHTML</i></td>
 </tr>


</table>

## LocalParameter
### Allowed parameters
<table>
  <tr>
    <td><b>sid</b></td>
    <td>str</td>
    <td><i>    SId optional</i></td>
 </tr>


  <tr>
    <td><b>name</b></td>
    <td>str</td>
    <td><i>   string optional</i></td>
 </tr>


  <tr>
    <td><b>metaid</b></td>
    <td>str</td>
    <td><i> XML ID optional</i></td>
 </tr>


  <tr>
    <td><b>sboTerm</b></td>
    <td>str</td>
    <td><i>SBOTerm optional</i></td>
 </tr>


  <tr>
    <td><b>notes</b></td>
    <td><a href="#notes">Notes</a></td>
    <td><i>     XHTML 1.0 optional</i></td>
 </tr>


  <tr>
    <td><b>annotation</b></td>
    <td>str</td>
    <td><i>XML content optional</i></td>
 </tr>


  <tr>
    <td><b>value</b></td>
    <td>float</td>
    <td><i></i></td>
 </tr>


  <tr>
    <td><b>units</b></td>
    <td>str</td>
    <td><i>UnitSIdRef optional</i></td>
 </tr>


</table>

## Notes
XHTML field of SBase

### Allowed parameters
<table>
  <tr>
    <td><b>xmlns</b></td>
    <td>str</td>
    <td><i>str fixed "http://www.w3.org/1999/xhtml"</i></td>
 </tr>


  <tr>
    <td><b>content</b></td>
    <td>str</td>
    <td><i>str valid XHTML</i></td>
 </tr>


</table>

## SpeciesReference
### Allowed parameters
<table>
  <tr>
    <td><b>sid</b></td>
    <td>str</td>
    <td><i>    SId optional</i></td>
 </tr>


  <tr>
    <td><b>name</b></td>
    <td>str</td>
    <td><i>   string optional</i></td>
 </tr>


  <tr>
    <td><b>metaid</b></td>
    <td>str</td>
    <td><i> XML ID optional</i></td>
 </tr>


  <tr>
    <td><b>sboTerm</b></td>
    <td>str</td>
    <td><i>SBOTerm optional</i></td>
 </tr>


  <tr>
    <td><b>notes</b></td>
    <td><a href="#notes">Notes</a></td>
    <td><i>     XHTML 1.0 optional</i></td>
 </tr>


  <tr>
    <td><b>annotation</b></td>
    <td>str</td>
    <td><i>XML content optional</i></td>
 </tr>


  <tr>
    <td><b>species</b></td>
    <td>str</td>
    <td><i>SIdRef</i></td>
 </tr>


  <tr>
    <td><b>stoichiometry</b></td>
    <td>float</td>
    <td><i>double optional</i></td>
 </tr>


  <tr>
    <td><b>constant</b></td>
    <td>bool</td>
    <td><i>boolean</i></td>
 </tr>


</table>

## Notes
XHTML field of SBase

### Allowed parameters
<table>
  <tr>
    <td><b>xmlns</b></td>
    <td>str</td>
    <td><i>str fixed "http://www.w3.org/1999/xhtml"</i></td>
 </tr>


  <tr>
    <td><b>content</b></td>
    <td>str</td>
    <td><i>str valid XHTML</i></td>
 </tr>


</table>

## SpeciesReference
### Allowed parameters
<table>
  <tr>
    <td><b>sid</b></td>
    <td>str</td>
    <td><i>    SId optional</i></td>
 </tr>


  <tr>
    <td><b>name</b></td>
    <td>str</td>
    <td><i>   string optional</i></td>
 </tr>


  <tr>
    <td><b>metaid</b></td>
    <td>str</td>
    <td><i> XML ID optional</i></td>
 </tr>


  <tr>
    <td><b>sboTerm</b></td>
    <td>str</td>
    <td><i>SBOTerm optional</i></td>
 </tr>


  <tr>
    <td><b>notes</b></td>
    <td><a href="#notes">Notes</a></td>
    <td><i>     XHTML 1.0 optional</i></td>
 </tr>


  <tr>
    <td><b>annotation</b></td>
    <td>str</td>
    <td><i>XML content optional</i></td>
 </tr>


  <tr>
    <td><b>species</b></td>
    <td>str</td>
    <td><i>SIdRef</i></td>
 </tr>


  <tr>
    <td><b>stoichiometry</b></td>
    <td>float</td>
    <td><i>double optional</i></td>
 </tr>


  <tr>
    <td><b>constant</b></td>
    <td>bool</td>
    <td><i>boolean</i></td>
 </tr>


</table>

## Notes
XHTML field of SBase

### Allowed parameters
<table>
  <tr>
    <td><b>xmlns</b></td>
    <td>str</td>
    <td><i>str fixed "http://www.w3.org/1999/xhtml"</i></td>
 </tr>


  <tr>
    <td><b>content</b></td>
    <td>str</td>
    <td><i>str valid XHTML</i></td>
 </tr>


</table>

## ModifierSpeciesReference
### Allowed parameters
<table>
  <tr>
    <td><b>sid</b></td>
    <td>str</td>
    <td><i>    SId optional</i></td>
 </tr>


  <tr>
    <td><b>name</b></td>
    <td>str</td>
    <td><i>   string optional</i></td>
 </tr>


  <tr>
    <td><b>metaid</b></td>
    <td>str</td>
    <td><i> XML ID optional</i></td>
 </tr>


  <tr>
    <td><b>sboTerm</b></td>
    <td>str</td>
    <td><i>SBOTerm optional</i></td>
 </tr>


  <tr>
    <td><b>notes</b></td>
    <td><a href="#notes">Notes</a></td>
    <td><i>     XHTML 1.0 optional</i></td>
 </tr>


  <tr>
    <td><b>annotation</b></td>
    <td>str</td>
    <td><i>XML content optional</i></td>
 </tr>


  <tr>
    <td><b>species</b></td>
    <td>str</td>
    <td><i>SIdRef</i></td>
 </tr>


</table>

## Notes
XHTML field of SBase

### Allowed parameters
<table>
  <tr>
    <td><b>xmlns</b></td>
    <td>str</td>
    <td><i>str fixed "http://www.w3.org/1999/xhtml"</i></td>
 </tr>


  <tr>
    <td><b>content</b></td>
    <td>str</td>
    <td><i>str valid XHTML</i></td>
 </tr>


</table>

## Event
### Allowed parameters
<table>
  <tr>
    <td><b>sid</b></td>
    <td>str</td>
    <td><i>    SId optional</i></td>
 </tr>


  <tr>
    <td><b>name</b></td>
    <td>str</td>
    <td><i>   string optional</i></td>
 </tr>


  <tr>
    <td><b>metaid</b></td>
    <td>str</td>
    <td><i> XML ID optional</i></td>
 </tr>


  <tr>
    <td><b>sboTerm</b></td>
    <td>str</td>
    <td><i>SBOTerm optional</i></td>
 </tr>


  <tr>
    <td><b>notes</b></td>
    <td><a href="#notes">Notes</a></td>
    <td><i>     XHTML 1.0 optional</i></td>
 </tr>


  <tr>
    <td><b>annotation</b></td>
    <td>str</td>
    <td><i>XML content optional</i></td>
 </tr>


  <tr>
    <td><b>useValuesFromTriggerTime</b></td>
    <td>bool</td>
    <td><i></i></td>
 </tr>


  <tr>
    <td><b>trigger</b></td>
    <td><a href="#trigger">Trigger</a></td>
    <td><i></i></td>
 </tr>


  <tr>
    <td><b>priority</b></td>
    <td><a href="#priority">Priority</a></td>
    <td><i></i></td>
 </tr>


  <tr>
    <td><b>delay</b></td>
    <td><a href="#delay">Delay</a></td>
    <td><i></i></td>
 </tr>


</table>

### Allowed children
<table>
  <tr>
    <td><b>listOfEventAssignments</b></td>
    <td><a href="#eventassignment">EventAssignment</a></td>
    <td><i></i></td>
  </tr>


</table>

## Notes
XHTML field of SBase

### Allowed parameters
<table>
  <tr>
    <td><b>xmlns</b></td>
    <td>str</td>
    <td><i>str fixed "http://www.w3.org/1999/xhtml"</i></td>
 </tr>


  <tr>
    <td><b>content</b></td>
    <td>str</td>
    <td><i>str valid XHTML</i></td>
 </tr>


</table>

## Trigger
### Allowed parameters
<table>
  <tr>
    <td><b>sid</b></td>
    <td>str</td>
    <td><i>    SId optional</i></td>
 </tr>


  <tr>
    <td><b>name</b></td>
    <td>str</td>
    <td><i>   string optional</i></td>
 </tr>


  <tr>
    <td><b>metaid</b></td>
    <td>str</td>
    <td><i> XML ID optional</i></td>
 </tr>


  <tr>
    <td><b>sboTerm</b></td>
    <td>str</td>
    <td><i>SBOTerm optional</i></td>
 </tr>


  <tr>
    <td><b>notes</b></td>
    <td><a href="#notes">Notes</a></td>
    <td><i>     XHTML 1.0 optional</i></td>
 </tr>


  <tr>
    <td><b>annotation</b></td>
    <td>str</td>
    <td><i>XML content optional</i></td>
 </tr>


  <tr>
    <td><b>initialValue</b></td>
    <td>bool</td>
    <td><i></i></td>
 </tr>


  <tr>
    <td><b>persistent</b></td>
    <td>bool</td>
    <td><i></i></td>
 </tr>


  <tr>
    <td><b>math</b></td>
    <td>str</td>
    <td><i></i></td>
 </tr>


</table>

## Notes
XHTML field of SBase

### Allowed parameters
<table>
  <tr>
    <td><b>xmlns</b></td>
    <td>str</td>
    <td><i>str fixed "http://www.w3.org/1999/xhtml"</i></td>
 </tr>


  <tr>
    <td><b>content</b></td>
    <td>str</td>
    <td><i>str valid XHTML</i></td>
 </tr>


</table>

## Priority
### Allowed parameters
<table>
  <tr>
    <td><b>sid</b></td>
    <td>str</td>
    <td><i>    SId optional</i></td>
 </tr>


  <tr>
    <td><b>name</b></td>
    <td>str</td>
    <td><i>   string optional</i></td>
 </tr>


  <tr>
    <td><b>metaid</b></td>
    <td>str</td>
    <td><i> XML ID optional</i></td>
 </tr>


  <tr>
    <td><b>sboTerm</b></td>
    <td>str</td>
    <td><i>SBOTerm optional</i></td>
 </tr>


  <tr>
    <td><b>notes</b></td>
    <td><a href="#notes">Notes</a></td>
    <td><i>     XHTML 1.0 optional</i></td>
 </tr>


  <tr>
    <td><b>annotation</b></td>
    <td>str</td>
    <td><i>XML content optional</i></td>
 </tr>


  <tr>
    <td><b>math</b></td>
    <td>str</td>
    <td><i></i></td>
 </tr>


</table>

## Notes
XHTML field of SBase

### Allowed parameters
<table>
  <tr>
    <td><b>xmlns</b></td>
    <td>str</td>
    <td><i>str fixed "http://www.w3.org/1999/xhtml"</i></td>
 </tr>


  <tr>
    <td><b>content</b></td>
    <td>str</td>
    <td><i>str valid XHTML</i></td>
 </tr>


</table>

## Delay
### Allowed parameters
<table>
  <tr>
    <td><b>sid</b></td>
    <td>str</td>
    <td><i>    SId optional</i></td>
 </tr>


  <tr>
    <td><b>name</b></td>
    <td>str</td>
    <td><i>   string optional</i></td>
 </tr>


  <tr>
    <td><b>metaid</b></td>
    <td>str</td>
    <td><i> XML ID optional</i></td>
 </tr>


  <tr>
    <td><b>sboTerm</b></td>
    <td>str</td>
    <td><i>SBOTerm optional</i></td>
 </tr>


  <tr>
    <td><b>notes</b></td>
    <td><a href="#notes">Notes</a></td>
    <td><i>     XHTML 1.0 optional</i></td>
 </tr>


  <tr>
    <td><b>annotation</b></td>
    <td>str</td>
    <td><i>XML content optional</i></td>
 </tr>


  <tr>
    <td><b>math</b></td>
    <td>str</td>
    <td><i></i></td>
 </tr>


</table>

## Notes
XHTML field of SBase

### Allowed parameters
<table>
  <tr>
    <td><b>xmlns</b></td>
    <td>str</td>
    <td><i>str fixed "http://www.w3.org/1999/xhtml"</i></td>
 </tr>


  <tr>
    <td><b>content</b></td>
    <td>str</td>
    <td><i>str valid XHTML</i></td>
 </tr>


</table>

## EventAssignment
### Allowed parameters
<table>
  <tr>
    <td><b>sid</b></td>
    <td>str</td>
    <td><i>    SId optional</i></td>
 </tr>


  <tr>
    <td><b>name</b></td>
    <td>str</td>
    <td><i>   string optional</i></td>
 </tr>


  <tr>
    <td><b>metaid</b></td>
    <td>str</td>
    <td><i> XML ID optional</i></td>
 </tr>


  <tr>
    <td><b>sboTerm</b></td>
    <td>str</td>
    <td><i>SBOTerm optional</i></td>
 </tr>


  <tr>
    <td><b>notes</b></td>
    <td><a href="#notes">Notes</a></td>
    <td><i>     XHTML 1.0 optional</i></td>
 </tr>


  <tr>
    <td><b>annotation</b></td>
    <td>str</td>
    <td><i>XML content optional</i></td>
 </tr>


  <tr>
    <td><b>math</b></td>
    <td>str</td>
    <td><i></i></td>
 </tr>


  <tr>
    <td><b>variable</b></td>
    <td>str</td>
    <td><i>SIdRef</i></td>
 </tr>


</table>

## Notes
XHTML field of SBase

### Allowed parameters
<table>
  <tr>
    <td><b>xmlns</b></td>
    <td>str</td>
    <td><i>str fixed "http://www.w3.org/1999/xhtml"</i></td>
 </tr>


  <tr>
    <td><b>content</b></td>
    <td>str</td>
    <td><i>str valid XHTML</i></td>
 </tr>


</table>

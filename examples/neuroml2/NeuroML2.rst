=======
NeuroML
=======
Some description...

**Allowed parameters**

===============  ===========  ================================
Allowed field    Data Type    Description
===============  ===========  ================================
**id**           str          The id of the NeuroML 2 document
**version**      str          NeuroML version used
===============  ===========  ================================

**Allowed children**

=======================  ================  ====================
Allowed child            Data Type         Description
=======================  ================  ====================
**izhikevich2007Cells**  `List <#list>`__
**pulseGenerators**      `List <#list>`__
**networks**             `List <#list>`__  The networks present
=======================  ================  ====================

==================
Izhikevich2007Cell
==================
Some description...

**Allowed parameters**

===============  ===========  =====================
Allowed field    Data Type    Description
===============  ===========  =====================
**id**           str          The id of the cell...
**C**            str
**v0**           str
**k**            str
**vr**           str
**vt**           str
**vpeak**        str
**a**            str
**b**            str
**c**            str
**d**            str
===============  ===========  =====================

==============
PulseGenerator
==============
Some description...

**Allowed parameters**

===============  ===========  ============================
Allowed field    Data Type    Description
===============  ===========  ============================
**id**           str          The id of the pulseGenerator
**delay**        str          the delay
**duration**     str          the duration
**amplitude**    str          the amplitude
===============  ===========  ============================

=======
Network
=======
Some description...

**Allowed parameters**

===============  ===========  =====================
Allowed field    Data Type    Description
===============  ===========  =====================
**id**           str          The id of the network
===============  ===========  =====================

**Allowed children**

==================  ================  ===================
Allowed child       Data Type         Description
==================  ================  ===================
**populations**     `List <#list>`__  the pops in the net
**explicitInputs**  `List <#list>`__
==================  ================  ===================

==========
Population
==========
Some description...

**Allowed parameters**

===============  ===========  ======================================
Allowed field    Data Type    Description
===============  ===========  ======================================
**id**           str          The id of the population
**component**    str          the component to use in the population
**size**         int          the size of the population
===============  ===========  ======================================

=============
ExplicitInput
=============
Some description...

**Allowed parameters**

===============  ===========  ==============================
Allowed field    Data Type    Description
===============  ===========  ==============================
**target**       str          the target of the input
**input**        str          the input, e.g. pulseGenerator
===============  ===========  ==============================

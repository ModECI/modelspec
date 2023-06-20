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

=======================  ============================================  ====================
Allowed child            Data Type                                     Description
=======================  ============================================  ====================
**izhikevich2007Cells**  `Izhikevich2007Cell <#izhikevich2007cell>`__
**pulseGenerators**      `PulseGenerator <#pulsegenerator>`__
**networks**             `Network <#network>`__                        The networks present
=======================  ============================================  ====================

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

==================  ==================================  ===================
Allowed child       Data Type                           Description
==================  ==================================  ===================
**populations**     `Population <#population>`__        the pops in the net
**explicitInputs**  `ExplicitInput <#explicitinput>`__
==================  ==================================  ===================

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

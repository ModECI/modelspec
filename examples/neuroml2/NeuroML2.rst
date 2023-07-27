=======
neuroml
=======
Some description...

**Allowed parameters**

===============  ===========  ====================================================================
Allowed field    Data Type    Description
===============  ===========  ====================================================================
**id**           str          The id of the NeuroML 2 document
**xmlns**        str          Schema for NeuroML 2, usually http://www.neuroml.org/schema/neuroml2
===============  ===========  ====================================================================

**Allowed children**

=======================  ============================================  ====================
Allowed child            Data Type                                     Description
=======================  ============================================  ====================
**izhikevich2007Cells**  `izhikevich2007Cell <#izhikevich2007cell>`__
**pulseGenerators**      `pulseGenerator <#pulsegenerator>`__
**networks**             `network <#network>`__                        The networks present
=======================  ============================================  ====================

==================
izhikevich2007Cell
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
pulseGenerator
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
network
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
**populations**     `population <#population>`__        the pops in the net
**explicitInputs**  `explicitInput <#explicitinput>`__
==================  ==================================  ===================

==========
population
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
explicitInput
=============
Some description...

**Allowed parameters**

===============  ===========  ==============================
Allowed field    Data Type    Description
===============  ===========  ==============================
**target**       str          the target of the input
**input**        str          the input, e.g. pulseGenerator
===============  ===========  ==============================

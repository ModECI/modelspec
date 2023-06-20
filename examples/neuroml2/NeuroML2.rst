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

===============  ================  ====================
Allowed child    Data Type         Description
===============  ================  ====================
**networks**     `List <#list>`__  The networks present
===============  ================  ====================

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

===============  ================  ===================
Allowed child    Data Type         Description
===============  ================  ===================
**populations**  `List <#list>`__  the pops in the net
===============  ================  ===================

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

========
Document
========
A model for documents.

**Allowed parameters**

===============  ===========  ====================================
Allowed field    Data Type    Description
===============  ===========  ====================================
**id**           str          *The unique id of the document*
**title**        str          *Document title*
**ISBN**         int          *International Standard Book Number*
===============  ===========  ====================================

**Allowed children**

===============  =====================  ==============================
Allowed child    Data Type              Description
===============  =====================  ==============================
**sections**     `Section <#section>`_  *The sections of the document*
===============  =====================  ==============================

=======
Section
=======
A model of a section of the `Document <#document>`_ . Will contain one `Paragraph <#paragraph>`_  or more


**Allowed parameters**

===============  ===========  =======================
Allowed field    Data Type    Description
===============  ===========  =======================
**id**           str          *The id of the section*
===============  ===========  =======================

**Allowed children**

===============  =========================  ================
Allowed child    Data Type                  Description
===============  =========================  ================
**paragraphs**   `Paragraph <#paragraph>`_  *The paragraphs*
===============  =========================  ================

=========
Paragraph
=========
A model of a paragraph.

**Allowed parameters**

===============  ===========  ===================================================
Allowed field    Data Type    Description
===============  ===========  ===================================================
**contents**     str          *Paragraph contents, which make up the _Section_s.*
===============  ===========  ===================================================

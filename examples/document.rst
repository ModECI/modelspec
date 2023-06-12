========
Document
========
A model for documents.

**Allowed parameters**

===============  ===========  ==================================
Allowed field    Data Type    Description
===============  ===========  ==================================
**id**           str          The unique id of the document
**title**        str          The document title
**ISBN**         int          International Standard Book Number
===============  ===========  ==================================

**Allowed children**

===============  ======================  ============================
Allowed child    Data Type               Description
===============  ======================  ============================
**sections**     `Section <#section>`__  The sections of the document
===============  ======================  ============================

=======
Section
=======
A model of a section of the `Document <#document>`__. Will contain one `Paragraph <#paragraph>`__ or more, i.e the `Paragraph(s) <#paragraph>`__ in the section, probably related to the **title** of the `Document <#document>`_.

**Allowed parameters**

===============  ===========  =====================
Allowed field    Data Type    Description
===============  ===========  =====================
**id**           str          The id of the section
===============  ===========  =====================

**Allowed children**

===============  ==========================  ==============
Allowed child    Data Type                   Description
===============  ==========================  ==============
**paragraphs**   `Paragraph <#paragraph>`__  The paragraphs
===============  ==========================  ==============

=========
Paragraph
=========
A model of a paragraph.

**Allowed parameters**

===============  ===========  ==============================================================
Allowed field    Data Type    Description
===============  ===========  ==============================================================
**contents**     str          Paragraph contents, which make up the `Sections <#section>`__.
===============  ===========  ==============================================================

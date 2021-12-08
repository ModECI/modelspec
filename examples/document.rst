========
Document
========
A model for documents

Allowed parameters
==================

===============  ===========  ====================================
Allowed field    Data Type    Description
===============  ===========  ====================================
**title**        str          *Document title*
**ISBN**         int          *International Standard Book Number*
**id**           str          *Unique ID of element*
**notes**        str          *Human readable notes*
===============  ===========  ====================================

Allowed children
================

===============  ====================  ==============================
Allowed child    Data Type             Description
===============  ====================  ==============================
**sections**     `section <Section>`_  *The sections of the document*
===============  ====================  ==============================

=======
Section
=======
A model of a section of the document

Allowed parameters
==================

===============  ===========  ======================
Allowed field    Data Type    Description
===============  ===========  ======================
**id**           str          *Unique ID of element*
**notes**        str          *Human readable notes*
===============  ===========  ======================

Allowed children
================

===============  ========================  ================
Allowed child    Data Type                 Description
===============  ========================  ================
**paragraphs**   `paragraph <Paragraph>`_  *The paragraphs*
===============  ========================  ================

=========
Paragraph
=========
A model of a paragraph

Allowed parameters
==================

===============  ===========  ====================
Allowed field    Data Type    Description
===============  ===========  ====================
**contents**     str          *Paragraph contents*
===============  ===========  ====================


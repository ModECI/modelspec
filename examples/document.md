## Document
A model for documents
#### Allowed parameters
<table><tr><td><b>title</b></td><td>str</td><td><i>Document title</i></td></tr>

<tr><td><b>ISBN</b></td><td>int</td><td><i>International Standard Book Number</i></td></tr>

<tr><td><b>id</b></td><td>str</td><td><i>Unique ID of element</i></td></tr>

<tr><td><b>notes</b></td><td>str</td><td><i>Human readable notes</i></td></tr>


</table>

#### Allowed children
<table><tr><td><b>sections</b></td><td><a href="#section">Section</a></td><td><i>The sections of the document</i></td></tr>


</table>

## Section
A model of a section of the document
#### Allowed parameters
<table><tr><td><b>id</b></td><td>str</td><td><i>Unique ID of element</i></td></tr>

<tr><td><b>notes</b></td><td>str</td><td><i>Human readable notes</i></td></tr>


</table>

#### Allowed children
<table><tr><td><b>paragraphs</b></td><td><a href="#paragraph">Paragraph</a></td><td><i>The paragraphs</i></td></tr>


</table>

## Paragraph
A model of a paragraph
#### Allowed parameters
<table><tr><td><b>contents</b></td><td>str</td><td><i>Paragraph contents</i></td></tr>


</table>


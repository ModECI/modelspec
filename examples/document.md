## Document
A model for documents.

### Allowed parameters
<table>
  <tr>
    <td><b>id</b></td>
    <td>str</td>
    <td><i>The unique id of the document</i></td>
 </tr>


  <tr>
    <td><b>title</b></td>
    <td>str</td>
    <td><i>The document title</i></td>
 </tr>


  <tr>
    <td><b>ISBN</b></td>
    <td>int</td>
    <td><i>International Standard Book Number</i></td>
 </tr>


</table>

### Allowed children
<table>
  <tr>
    <td><b>sections</b></td>
    <td><a href="#section">Section</a></td>
    <td><i>The sections of the document</i></td>
  </tr>


</table>

## Section
A model of a section of the <a href="#document">Document</a>. Will contain one <a href="#paragraph">Paragraph</a> or more, i.e the <a href="#paragraph">Paragraph</a>(s) in the section, probably related to the <b>title</b> of the `Document <#document>`_.

### Allowed parameters
<table>
  <tr>
    <td><b>id</b></td>
    <td>str</td>
    <td><i>The id of the section</i></td>
 </tr>


</table>

### Allowed children
<table>
  <tr>
    <td><b>paragraphs</b></td>
    <td><a href="#paragraph">Paragraph</a></td>
    <td><i>The paragraphs</i></td>
  </tr>


</table>

## Paragraph
A model of a paragraph.

### Allowed parameters
<table>
  <tr>
    <td><b>contents</b></td>
    <td>str</td>
    <td><i>Paragraph contents, which make up the <a href="#section">Section</a>s.</i></td>
 </tr>


</table>

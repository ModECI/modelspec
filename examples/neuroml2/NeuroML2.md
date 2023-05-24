## NeuroML
Some description...

### Allowed parameters
<table>
  <tr>
    <td><b>id</b></td>
    <td>str</td>
    <td><i>The id of the NeuroML 2 document</i></td>
 </tr>


  <tr>
    <td><b>version</b></td>
    <td>str</td>
    <td><i>NeuroML version used</i></td>
 </tr>


</table>

### Allowed children
<table>
  <tr>
    <td><b>networks</b></td>
    <td><a href="#network">Network</a></td>
    <td><i>The networks present</i></td>
  </tr>


</table>

## Network
Some description...

### Allowed parameters
<table>
  <tr>
    <td><b>id</b></td>
    <td>str</td>
    <td><i>The id of the network</i></td>
 </tr>


</table>

### Allowed children
<table>
  <tr>
    <td><b>populations</b></td>
    <td><a href="#population">Population</a></td>
    <td><i>the pops in the net</i></td>
  </tr>


</table>

## Population
Some description...

### Allowed parameters
<table>
  <tr>
    <td><b>id</b></td>
    <td>str</td>
    <td><i>The id of the population</i></td>
 </tr>


  <tr>
    <td><b>component</b></td>
    <td>str</td>
    <td><i>the component to use in the population</i></td>
 </tr>


  <tr>
    <td><b>size</b></td>
    <td>int</td>
    <td><i>the size of the population</i></td>
 </tr>


</table>

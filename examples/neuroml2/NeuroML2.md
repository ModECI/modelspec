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
    <td><b>izhikevich2007Cells</b></td>
    <td><a href="#izhikevich2007cell">Izhikevich2007Cell</a></td>
    <td><i></i></td>
  </tr>


  <tr>
    <td><b>pulseGenerators</b></td>
    <td><a href="#pulsegenerator">PulseGenerator</a></td>
    <td><i></i></td>
  </tr>


  <tr>
    <td><b>networks</b></td>
    <td><a href="#network">Network</a></td>
    <td><i>The networks present</i></td>
  </tr>


</table>

## Izhikevich2007Cell
Some description...

### Allowed parameters
<table>
  <tr>
    <td><b>id</b></td>
    <td>str</td>
    <td><i>The id of the cell...</i></td>
 </tr>


  <tr>
    <td><b>C</b></td>
    <td>str</td>
    <td><i></i></td>
 </tr>


  <tr>
    <td><b>v0</b></td>
    <td>str</td>
    <td><i></i></td>
 </tr>


  <tr>
    <td><b>k</b></td>
    <td>str</td>
    <td><i></i></td>
 </tr>


  <tr>
    <td><b>vr</b></td>
    <td>str</td>
    <td><i></i></td>
 </tr>


  <tr>
    <td><b>vt</b></td>
    <td>str</td>
    <td><i></i></td>
 </tr>


  <tr>
    <td><b>vpeak</b></td>
    <td>str</td>
    <td><i></i></td>
 </tr>


  <tr>
    <td><b>a</b></td>
    <td>str</td>
    <td><i></i></td>
 </tr>


  <tr>
    <td><b>b</b></td>
    <td>str</td>
    <td><i></i></td>
 </tr>


  <tr>
    <td><b>c</b></td>
    <td>str</td>
    <td><i></i></td>
 </tr>


  <tr>
    <td><b>d</b></td>
    <td>str</td>
    <td><i></i></td>
 </tr>


</table>

## PulseGenerator
Some description...

### Allowed parameters
<table>
  <tr>
    <td><b>id</b></td>
    <td>str</td>
    <td><i>The id of the pulseGenerator</i></td>
 </tr>


  <tr>
    <td><b>delay</b></td>
    <td>str</td>
    <td><i>the delay</i></td>
 </tr>


  <tr>
    <td><b>duration</b></td>
    <td>str</td>
    <td><i>the duration</i></td>
 </tr>


  <tr>
    <td><b>amplitude</b></td>
    <td>str</td>
    <td><i>the amplitude</i></td>
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


  <tr>
    <td><b>explicitInputs</b></td>
    <td><a href="#explicitinput">ExplicitInput</a></td>
    <td><i></i></td>
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

## ExplicitInput
Some description...

### Allowed parameters
<table>
  <tr>
    <td><b>target</b></td>
    <td>str</td>
    <td><i>the target of the input</i></td>
 </tr>


  <tr>
    <td><b>input</b></td>
    <td>str</td>
    <td><i>the input, e.g. pulseGenerator</i></td>
 </tr>


</table>

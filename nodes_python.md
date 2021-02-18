# Data Structures for python interviews
## Nodes

### Node linking theory
~~~
Often, due to the data structure, nodes may only be linked to from a single other node. This makes it very important to consider how you implement modifying or removing nodes from a data structure.

If you inadvertently remove the single link to a node, that node’s data and any linked nodes could be “lost” to your application. When this happens to a node, it is called an orphaned node.

Examine the nodes in the diagram. node_c is only linked to by node_b. If you would like to remove node_b but not node_c, you can’t simply delete the link from node_a to node_b.

The most straightforward method to preserve node_c would be to change the link in node_a to point to node_c instead of node_b. However, some data structures may handle this in a different manner.
~~~
![Nodo](https://content.codecademy.com/courses/learn-nodes-general/NodeImplementations.svg)
### Node reviws

Nodes:

    Contain data, which can be a variety of data types
    Contain links to other nodes. If a node has no links, or they are all null, you have reached the end of the path you were following.
    Can be orphaned if there are no existing links to them

# Nodes Python
## Nodes Python introduction
~~~
We will use a basic node that contains data and one link to another node. The node’s data will be specified when creating the node and immutable (can’t be updated). The link will be optional at initialization and can be updated.

Remember that at the end of a node path, the link to the next node is null because there are no more nodes left. In Python, this means it will be set to 
~~~

### Node Python setters

~~~
The method should be called .set_link_node() and should take link_node as an argument. It should then update the self.link_node attribute as appropriate.
~~~
```python
class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
    
  def get_value(self):
    return self.value
  
  def get_link_node(self):
    return self.link_node
  
  # Define your set_link_node method below:
  def set_link_node(self,link_node):
    self.link_node = link_node

```
## Node python review
~~~
Outside of Node, instantiate three nodes. None have an argument for link_node:

    the first has a value of "likes to yak" and be assigned to a variable yacko
    the second has a value of "has a penchant for hoarding snacks" and be assigned to wacko
    the third has a value of "enjoys spending time in movie lots" and be assigned to dot

Now let’s give these nodes some responsibilities! yacko can keep track of dot and dot can keep up with wacko. wacko can’t keep track of anything though.

Below the newly created nodes, use your .set_link_node() method to give:

    yacko a link_node of dot
    dot a link_node of wacko



Create two new variables, dots_data, and wackos_data. Use both getter methods to get dot‘s value from yacko and get wacko‘s value from dot. Print dots_data and wackos_data to the console to see the results!

When your code is passing, take a moment to consider:

    How would you get yacko‘s value?
    How could you get from yacko to wacko‘s value?
    How do you think nodes could be helpful for keeping track of and storing information?

~~~
```python
class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
    
  def set_link_node(self, link_node):
    self.link_node = link_node
    
  def get_link_node(self):
    return self.link_node
  
  def get_value(self):
    return self.value

# Add your code below:
yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")

dot.set_link_node(wacko)
yacko.set_link_node(dot)

dots_data = yacko.get_link_node().get_value()
wackos_data = dot.get_link_node().get_value()

print(dots_data)
print(wackos_data)
```

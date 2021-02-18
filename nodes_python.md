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

# Data Structures for python interviews
## Linked List

### Linked List theory
~~~
Ahora que está familiarizado con los nodos, ¡el siguiente paso es usarlos para construir algo! La vinculación de nodos mediante su propiedad next_node crea una lista vinculada individualmente. Las listas con enlaces individuales son extremadamente versátiles y útiles, a la vez que hermosas por su simplicidad. Al igual que los nodos, estas listas se utilizan como base para futuras estructuras de datos y son una alternativa a las matrices cuando se intenta almacenar información de forma lineal.
~~~
### Double Linked List
~~~
Mientras que una lista unicamente enlazada consta de nodos con enlaces de un nodo al siguiente, una lista doblemente enlazada también tiene un enlace al nodo anterior. Estos enlaces prev_node, junto con la propiedad tail_node agregada, le permiten iterar hacia atrás a través de la lista tan fácilmente como podría iterar hacia adelante a través de la lista enlazada individualmente.
~~~

### Colas
~~~
Una cola es una colección lineal de nodos que exclusivamente agrega (pone en cola) nodos a la cola y elimina (retira de la cola) nodos del encabezado de la cola. Se pueden implementar usando diferentes estructuras de datos subyacentes, pero uno de los métodos más comunes es usar una lista enlazada individualmente, que es lo que usará para su clase de cola. Piense en la estructura de datos de la cola como una cola o línea real en una tienda de comestibles. La persona que está al frente debe dejar la línea primero, y cada persona que se une a la línea tiene que unirse al fondo.
~~~
### Pilas
~~~
Las pilas son otra estructura de datos con un nombre perfectamente descriptivo. Al igual que una cola, una pila es una colección lineal de nodos que agrega (empuja) datos a la cabeza o parte superior de la pila. Sin embargo, a diferencia de una cola, una pila elimina datos (pops) del encabezado de la pila. Piense en ello como una pila de libros, donde solo puede tomar el libro superior y agregar un libro nuevo al principio.
~~~
# Linked List Introduction

~~~
Linked lists are one of the basic data structures used in computer science. They have many direct applications and serve as the foundation for more complex data structures.

The list is comprised of a series of nodes as shown in the diagram. The head node is the node at the beginning of the list. Each node contains data and a link (or pointer) to the next node in the list. The list is terminated when a node’s link is null. This is called the tail node.

Consider a one-way air travel itinerary. The trip could involve traveling through several airports (nodes) connected by air travel segments (links). In this example, the initial departure city is the head node and the final arrival city is the tail node.

Since the nodes use links to denote the next node in the sequence, the nodes are not required to be sequentially located in memory. These links also allow for quick insertion and removal of nodes as you will see in future exercises.

Common operations on a linked list may include:

    adding nodes
    removing nodes
    finding a node
    traversing (or traveling through) the linked list

Linked lists typically contain unidirectional links (next node), but some implementations make use of bidirectional links (next and previous nodes).
~~~
![Listas](https://content.codecademy.com/courses/learn-linked-lists-general/LinkedListUpdated.svg)

### Linked List Example
~~~
As an example, we added values to the linked list diagram from the introduction.

This linked list contains three nodes (node_a, node_b, and node_c).

Each node in this particular list contains a string as its data. As the sequence is defined, the order is "cats", "dogs", and "birds".

The list ends at node_c, since the link within that node is set to null.

What links would need to be established to add a new head node to this list? What about the tail

~~~

![Nodo](https://content.codecademy.com/courses/learn-linked-lists-general/LinkedListExampleUpdated.svg)
## Linked Lists Adding and Removing Nodes
### Adding a new node
~~~
Adding a new node to the beginning of the list requires you to link your new node to the current head node. This way, you maintain your connection with the following nodes in the list.
~~~
### Removing a Node
~~~
If you accidentally remove the single link to a node, that node’s data and any following nodes could be lost to your application, leaving you with orphaned nodes. 
Depending on the language, nodes which are not referenced are removed automatically. “Removing” a node is equivalent to removing all references to the node.

In order to remove node_b, you must first link node_a to node_c (where node_b was linking).

Then you can remove node_b.
~~~
![Eliminarnodo](https://fotos-11.s3.amazonaws.com/metrocdmx/linked_list.PNG)


### Linked List reviews

Linked list:

  
  -  Are comprised of nodes
   - The nodes contain a link to the next node (and also the previous node for bidirectional linked lists)
   - Can be unidirectional or bidirectional
-    Are a basic data structure, and form the basis for many other data structures
 -   Have a single head node, which serves as the first node in the list
  -  Require some maintenance in order to add or remove nodes
   - The methods we used are an example and depend on the exact use case and/or programming language being used


# Linked list Python
## Linked list Python introduction
~~~
Within script.py in the pane to the right, create an empty Node class.

Inside, define an __init__() method for the Node. It should take a value and a next_node.

next_node should default to None if not provided. These variables should be saved to self with corresponding key names.
~~~
### Node implementation
```python
class Node():
  def __init__(self,value,next_node = None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self,next_node):
    self.next_node = next_node
  

my_node = Node(44)
print(my_node.get_value())
```

### Linked list implementation

~~~
With the Node in hand, we can start building the actual linked list. Depending on the end-use of the linked list, a variety of methods can be defined.

For our use, we want to be able to:

    get the head node of the list (it’s like peeking at the first item in line)
    add a new node to the beginning of the list
    print out the list values in order
    remove a node that has a particular value

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
~~~
First Task
Define an .__init__() method for the LinkedList. We want to be able to instantiate a LinkedList with a head node, so .__init__() should take value as an argument. Make sure value defaults to None if no value is provided.

Inside the .__init__() method, set self.head_node equal to a new Node with value as its value.
Second Task
Define a .get_head_node() method that helps us peek at the first node in the list.
Inside the method, return the head node of the linked list.
~~~
Code:
```python
# We'll be using our Node class
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

# Create your LinkedList class below:
class LinkedList():
  def __init__(self, value=None):
    self.head_node = Node(value)
  def get_head_node(self):
    return self.head_node

```

## Linked List implementation II
Next up, we’ll define methods for our LinkedList class that allow us to:

- Insert a new head node
- return all the nodes in the list as a string so we can print them out in the terminal!
~~~
Define an .insert_beginning() method which takes new_value as an argument.

Inside the method, instantiate a Node with new_value. Name this new_node.
Now, link new_node to the existing head_node.
Finally, replace the current head_node with new_node.
~~~
Task II 
~~~
Define a .stringify_list() method we can use to print out a string representation of a list’s nodes’ values.

The method should traverse the list, beginning at the head node, and collect each node’s value in a string. Once the end of the list has been reached, the method should return the string.

You can use str() to convert integers to strings!

Be sure to add "\n" between values so that each value prints on a new line.
~~~
```python
# We'll be using our Node class
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

# Our LinkedList class
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
# Add your insert_beginning and stringify_list methods below:

  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
    
  

# Test your code by uncommenting the statements below - did your list print to the terminal?
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())
```

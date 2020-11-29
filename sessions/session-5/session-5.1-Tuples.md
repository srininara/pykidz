## Tuples

### List with parens?

- List with parens - ordered like lists

```python
>>> my_friends = ('Amar', 'Akbar', 'Antony', 'Basheer', 'Bheem', 'Boris')
>>> type(my_friends)
<class 'tuple'>
```

### Tuples vs. Lists

- Check all the below for tuples are use that in slide

- Lists Are Ordered and so are Tuples

  ```python
  >>> my_friends_other = ('Amar', 'Antony', 'Basheer', 'Akbar','Bheem', 'Boris')
  >>> my_friends == my_friends
  True
  >>> my_friends == my_friends_other
  False
	```

- Lists can contain arbitrary objects (including nested items) and so can Tuples

  ```python
  >>> t_tup = (1, 'Kaali', True, ['Krishna',2,2.0, False, 'Aman'], ('as','the'),25.12)
  >>> t_tup
  (1, 'Kaali', True, ['Krishna', 2, 2.0, False, 'Aman'], ('as', 'the'), 25.12)
  >>> type(t_tup)
  <class 'tuple'>
	```

- List elements can be accessed by index and so can Tuples

  ```python
  >>> my_friends[0]
  'Amar'
  >>> t_tup[0]
  1
  >>> t_tup[1]
  'Kaali'
  >>> t_tup[2]
  True
  >>> t_tup[3]
  ['Krishna', 2, 2.0, False, 'Aman']
  >>> type(t_tup[3])
  <class 'list'>
  >>> type(t_tup[4])
  <class 'tuple'>
  >>> len(my_friends)
  6
	```

- Lists are dynamic & mutable but Tuples are not

  ```python
  >>> dir(my_friends.count)
  ['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__text_signature__']
  # Not seeing the append or remove function
  >>> help(my_friends.count)
  >>> t_tup[2]
  True
  >>> t_tup[2] = False
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: 'tuple' object does not support item assignment

  'tuple' object does not support item assignment
	```

### Tuples operations

- can do indexing and slicing to access (postive and negative)

```python
>>> my_friends[-1]
'Boris'
>>> my_friends[-1:-3]
()
>>> my_friends[-1:]
('Boris',)
>>> my_friends[-3:-1]
('Basheer', 'Bheem')
>>> my_friends[-4:-1]
('Antony', 'Basheer', 'Bheem')
```

- `in` and `not in` also works with Tuples

```python
>>> tups = ('a', 'an', 'the')
>>> tups
('a', 'an', 'the')
>>> 'a' in tups
True
```

- empty tuple - falsy?

  ```python
  >>> type(())
  <class 'tuple'>
  >>> bool(())
  False
  >>> bool((2,))
  True
  ```



### Tuples are immutable

- Reiterate

  - immutable - cannot change once created

  ```python
  >>> my_friends[0:2] + my_friends[3:]
  ('Amar', 'Akbar', 'Basheer', 'Bheem', 'Boris')
  >>> type(my_friends[0:2] + my_friends[3:])
  <class 'tuple'>
  >>> id(my_friends[0:2] + my_friends[3:])
  4564371232
  >>> type(my_friends)
  <class 'tuple'>
  >>> id(my_friends)
  4568016544
  >>> id(my_friends_other)
  4574411456
  # Compare it with lists
  >>> articles = ['a', 'an']
  >>> id(articles)
  4574181824
  >>> articles.append('the')
  >>> articles
  ['a', 'an', 'the']
  >>> id(articles)
  4574181824
  ```

  - Use this when you want to be sure it will never change - faster

### Tuple definition gotchas

- Tuple defining special cases

  - `(2,)` - need this for creating a tuple of one item

  ```python
  >>> a = ()
  >>> type(a)
  <class 'tuple'>
  >>> a = (2)
  >>> type(a)
  <class 'int'>
  >>> a = (2,)
  >>> type(a)
  <class 'tuple'>
  ```

### Assignment, packing & unpacking

- Tuple assignment, packing and unpacking

  - swapping without temp variable

  ```python
  >>> articles = ('a', 'an')
  >>> a, an = articles
  >>> a
  'a'
  >>> an
  'an'
  >>> a = 1
  >>> b = 3
  >>> a , b = b , a
  >>> a
  3
  >>> b
  1
  ```

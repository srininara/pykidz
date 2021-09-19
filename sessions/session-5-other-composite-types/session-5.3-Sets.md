## Sets

### Definition

- Set theory and venn diagrams (slide)

  - a set can be thought of simply as a well-defined collection of distinct objects, typically called **elements** or **members**
  - collection of distinct objects
  - unordered
  - They are interesting because of the kind of operations you can do with them.

  ```python
  >>> duri_friends = {'Karna', 'Ashwathama', 'Dushasana'}
  >>> type(duri_friends)
  <class 'set'>
  >>> duri_friends
  {'Dushasana', 'Ashwathama', 'Karna'}
  >>> duri2_friends = {'Karna', 'Ashwathama', 'Dushasana', 'Karna'}
  >>> duri2_friends
  {'Dushasana', 'Ashwathama', 'Karna'}
  ```

### Sets - Creation and change

- set can be modified, but elements inside the set must be immutable (so no list or dict or set)

```python
>>> duri_friends.add('Vikarna')
>>> duri_friends
{'Vikarna', 'Dushasana', 'Ashwathama', 'Karna'}
>>> duri_friends.add('Karna')
>>> duri_friends
{'Vikarna', 'Dushasana', 'Ashwathama', 'Karna'}
```

- Other ways to create sets - from other collections

```python
>>> x = set(['a','b','a'])
>>> x
{'b', 'a'}
>>> y = set(('a','b','d','a'))
>>> y
{'d', 'b', 'a'}
```

- a string to set `set(s)`

```python
>>> z = set('foolishness')
>>> z
{'s', 'l', 'o', 'e', 'f', 'i', 'n', 'h'}
```

- Empty set - `set()` only. The `{}` won't work - it will be taken as a dict

```python
>>> ab = {}
>>> type(ab)
<class 'dict'>
>>> abc = set()
>>> type(abc)
<class 'set'>
```

### Sets - some properties

- empty set - falsy?

```python
>>> bool(z)
True
>>> bool(abc)
False
```

- len

```python
>>> duri_friends
{'Vikarna', 'Dushasana', 'Ashwathama', 'Karna'}
>>> len(duri_friends)
4
```

- in and not in

```python
>>> z # This is foolishness added to a set.
{'s', 'l', 'o', 'e', 'f', 'i', 'n', 'h'}
>>> 'o' in z
True
>>> 'a' in z
False
>>> 'a' not in z
True
```

### Sets - The super operations

- set operations with ops and methods

  - `|` or `union()` - union - operator works with only sets, method can work with argument as any iterable (list, tuple, string etc.)

  ```python
  >>> ramayana = {'Ram','Sita','Lakshman','Hanuman','Raavan','Shiva'}
  >>> mahabharat = {'Yudhi','Bhim','Arjun','Saha','Nakul','Krishna','Hanuman','Shiva'}
  >>> len(ramayana)
  6
  >>> len(mahabharat)
  8
  >>> ramayana | mahabharat
  {'Nakul', 'Shiva', 'Saha', 'Lakshman', 'Yudhi', 'Bhim', 'Ram', 'Hanuman', 'Raavan', 'Krishna', 'Arjun', 'Sita'}
  >>> type(ramayana | mahabharat)
  <class 'set'>
  >>> len(ramayana | mahabharat)
  12
  >>> ramayana.union(mahabharat)
  {'Nakul', 'Shiva', 'Saha', 'Lakshman', 'Yudhi', 'Bhim', 'Ram', 'Hanuman', 'Raavan', 'Krishna', 'Arjun', 'Sita'}
  >>> ramayana
  {'Shiva', 'Lakshman', 'Raavan', 'Ram', 'Hanuman', 'Sita'}
  >>> mahabharat
  {'Nakul', 'Shiva', 'Saha', 'Yudhi', 'Bhim', 'Krishna', 'Arjun', 'Hanuman'}
  >>> mahabharat_list = list(mahabharat)
  >>> mahabharat_list
  ['Nakul', 'Shiva', 'Saha', 'Yudhi', 'Bhim', 'Krishna', 'Arjun', 'Hanuman']
  >>> ramayana | mahabharat_list
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: unsupported operand type(s) for |: 'set' and 'list'
  >>> ramayana.union(mahabharat_list)
  {'Nakul', 'Saha', 'Yudhi', 'Sita', 'Shiva', 'Lakshman', 'Bhim', 'Ram', 'Raavan', 'Krishna', 'Arjun', 'Hanuman'}
  ```

  - `&` or `intersection()`

  ```python
  >>> ramayana & mahabharat
  {'Hanuman', 'Shiva'}
  >>> ramayana.intersection(mahabharat)
  {'Hanuman', 'Shiva'}
  ```

  - `< =` or `issubset()`

  ```python
  >>> {'Shiva','Sita','Ram'} <= ramayana
  True
  >>> {'Shiva','Sita','Bhim'} <= ramayana
  False
  >>> {'Shiva','Sita','Bhim'} <= ramayana | mahabharat
  True
  >>> {'Shiva','Sita','Ram'}.issubset(ramayana)
  True
  ```

  - `> = ` or `.issuperset()`

  ```python
  >>> ramayana | mahabharat >= ramayana
  True
  >>> (ramayana | mahabharat).issuperset(ramayana)
  True
  >>> (ramayana | mahabharat).issuperset(mahabharat_list)
  True
  ```

  - `|=` or `update` - update a set with union -  augmented assigment

  ```python
  >>> all = ramayana
  >>> all
  {'Shiva', 'Lakshman', 'Raavan', 'Ram', 'Hanuman', 'Sita'}
  >>> all |= mahabharat #augmented assignment
  >>> all
  {'Nakul', 'Shiva', 'Saha', 'Lakshman', 'Yudhi', 'Bhim', 'Raavan', 'Ram', 'Hanuman', 'Krishna', 'Arjun', 'Sita'}
  >>> ramayana  #aliasing
  {'Nakul', 'Shiva', 'Saha', 'Lakshman', 'Yudhi', 'Bhim', 'Raavan', 'Ram', 'Hanuman', 'Krishna', 'Arjun', 'Sita'}
  ```

### Sets - element methods

- s.add(elemn) - adding one element to a set - already covered

```python
>>> mahabharat.add('Duri')
>>> mahabharat
{'Nakul', 'Shiva', 'Saha', 'Yudhi', 'Bhim', 'Krishna', 'Duri', 'Arjun', 'Hanuman'}
```

- s.remove(elem) - remove an element - exception if elem is not found

```python
>>> mahabharat.remove('Duri')

>>> mahabharat
{'Nakul', 'Shiva', 'Saha', 'Yudhi', 'Bhim', 'Krishna', 'Arjun', 'Hanuman'}
>>> mahabharat.remove('Duri')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Duri'
```

- s.discard(elem) - remove an element if present - no exception if not found

```python
>>> mahabharat.discard('Shiva')
>>> mahabharat
{'Nakul', 'Saha', 'Yudhi', 'Bhim', 'Krishna', 'Arjun', 'Hanuman'}
>>> mahabharat.discard('Shiva')
>>>
```

- x.clear - clears a set

```python
>>> all
{'Nakul', 'Shiva', 'Saha', 'Lakshman', 'Yudhi', 'Bhim', 'Raavan', 'Ram', 'Hanuman', 'Krishna', 'Arjun', 'Sita'}
>>> all.clear # Make this mistake
<built-in method clear of set object at 0x10d7f1900>
>>> all.clear()
>>> all
set()
```

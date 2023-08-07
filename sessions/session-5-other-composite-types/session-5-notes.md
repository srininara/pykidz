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

---

## Maps/Dicts

- collection but of key and value - no index.  - e.g. people to favorite food

```python
>>> bhimsen_friends = ['Yudhi','Arjun','Nakul','Saha','Krishna']
>>> fav_foods = {'Bhim':'laddoo', 'Yudhi': 'Icecream', 'Arjun':'Kulfi', 'Saha':'Apple', 'Krishna':'Butter'}
```

### Defining Dicts

- definition

  - normal : `{'key':'value'}`, `{} #empty`

  ```python
  >>> {'key': 'value'}
  {'key': 'value'}
  >>> {}
  {}
  >>> type({})
  <class 'dict'>
  >>> type(fav_foods)
  <class 'dict'>
  ```

  - keyword arguments: `dict(key1='value1', key2='value2')

  ```python
  >>> another_map = dict(key1='value1',key2='value2')
  >>> another_map
  {'key1': 'value1', 'key2': 'value2'}
  >>> another_map = dict('k1'='value1','k2'='value2')#Wont work
  >>> another_map = dict(k1='value1',k2='value2')
  ```

I prefer the literal notation in the beginning (`fav_foods`)

### Access

- access by key

  - d['key1']

  ```python
  >>> fav_foods['Yudhi']
  'Icecream'
  ```

  - `KeyError` - raises exception when key not found. or when accessed by index

  ```python
  >>> fav_foods['Duri']
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  KeyError: 'Duri'
  >>> fav_foods[0]
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  KeyError: 0
  ```

- key can be any immutable type

  - Immutable means something that does not change

  ```python
  >>> v = "ABC"
  >>> id(v)
  4540228720
  >>> a = "ABC"
  >>> id(a)
  4540228720
  >>> v = v + a
  >>> v
  'ABCABC'
  >>> id(v)
  4579574128
  >>> a
  'ABC'
  >>> id(a)
  4540228720
  ```

  - integers could be keys - which might look like indexes but it is not. no negative indexes etc.

  ```python
  >>> list_of_articles = ['a','an','the']
  >>> list_like_articles_dict = {0:'a', 1:'an',2: 'the'}
  >>> list_of_articles[0]
  'a'
  >>> list_like_articles_dict[0]
  'a'
  >>> list_of_articles[2]
  'the'
  >>> list_like_articles_dict[2]
  'the'
  # Similarity ends there
  >>> list_of_articles[3]
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  IndexError: list index out of range
  >>> list_like_articles_dict[3]
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  KeyError: 3
  >>> list_of_articles[-1]
  'the'
  >>> list_like_articles_dict[-1]
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  KeyError: -1
  ```

  - keys can be even types and functions and normal datatypes and even tuples
  - key cannot be another dict or list - ***unhashable***

  ```python
  >>> parts_of_speech = {list_of_articles:"articles"}
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: unhashable type: 'list'
  >>> tuple_of_articles = tuple(list_of_articles)
  >>> tuple_of_articles
  ('a', 'an', 'the')
  >>> parts_of_speech = {tuple_of_articles:"articles"}
  >>> parts_of_speech
  {('a', 'an', 'the'): 'articles'}
  ```



### Change a dict

- No duplicate keys are allowed - update happens

  ```python
  >>> fav_foods
  {'Bhim': 'laddoo', 'Yudhi': 'Icecream', 'Arjun': 'Kulfi', 'Saha': 'Apple', 'Krishna': 'Butter'}
  >>> fav_foods.update({'Saha': 'Apple pie'})
  >>> fav_foods
  {'Bhim': 'laddoo', 'Yudhi': 'Icecream', 'Arjun': 'Kulfi', 'Saha': 'Apple pie', 'Krishna': 'Butter'}
  ```

  - values can be anything - no restrictions at all. also can be duplcated

  ```python
  >>> parts_of_speech = {"articles":list_of_articles}
  >>> parts_of_speech
  {'articles': ['a', 'an', 'the']}
  ```

- assignment - `d['key3'] = 'value3'

```python
>>> fav_foods['Draupadi'] = 'Kheer'
>>> fav_foods
{'Bhim': 'laddoo', 'Yudhi': 'Icecream', 'Arjun': 'Kulfi', 'Saha': 'Apple pie', 'Krishna': 'Butter', 'Draupadi': 'Kheer'}
```

- `del map[key]`

```python
>>> del fav_foods['Krishna']
>>> fav_foods
{'Bhim': 'laddoo', 'Yudhi': 'Icecream', 'Arjun': 'Kulfi', 'Saha': 'Apple pie', 'Draupadi': 'Kheer'}
```

- Replace/update by key - `d['key2'] = 'new value2'

```python
>>> fav_foods['Yudhi'] = 'Rasagulla'
>>> fav_foods
{'Bhim': 'laddoo', 'Yudhi': 'Rasagulla', 'Arjun': 'Kulfi', 'Saha': 'Apple pie', 'Draupadi': 'Kheer'}
```

- No +

```python
>>> fav_foods + {'Krishna': 'Butter'}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
```

### Membership and methods

- `in` and `not in` work with dict keys

  ```python
  >>> 'Arjun' in fav_foods
  True
  >>> 'Krishna' in fav_foods
  False
  # in does not work with values
  >>> 'Kulfi' in fav_foods
  False
  ```

  - use in for short circuiting without KeyError

  ```python
  >>> food = fav_foods['Bhim']
  >>> food
  'laddoo'
  >>> food2 = fav_foods['Krishna']
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  KeyError: 'Krishna'
  >>> food2 = 'Krishna' in fav_foods and fav_foods['Krishna']
  >>> food2
  False
  ```

- d.get('key', None)

```python
>>> food2 = fav_foods['Krishna']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Krishna'
>>> food2 = fav_foods.get('Krishna','no idea')
>>> food2
'no idea'
```

- d.items() - list like data structure of tuples

```python
>>> fav_foods.items()
dict_items([('Bhim', 'laddoo'), ('Yudhi', 'Rasagulla'), ('Arjun', 'Kulfi'), ('Saha', 'Apple pie'), ('Draupadi', 'Kheer')])
>>> type(fav_foods.items())
<class 'dict_items'>
>>> type(fav_foods.items()[0])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'dict_items' object is not subscriptable
>>> list(fav_foods.items())[0]
('Bhim', 'laddoo')
>>> type(list(fav_foods.items())[0])
<class 'tuple'>
```

- d.update(d2) - already covered
- d.clear()

```python
>>> fav_foods
{'Bhim': 'laddoo', 'Yudhi': 'Rasagulla', 'Arjun': 'Kulfi', 'Saha': 'Apple pie', 'Draupadi': 'Kheer'}
>>> fav_foods.clear()
>>> fav_foods
{}
```

- empty dict - falsy?

```python
>>> bool(fav_foods)
False
>>> fav_foods['Draupadi'] = 'Kheer'
>>> fav_foods
{'Draupadi': 'Kheer'}
>>> bool(fav_foods)
True
```

---

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

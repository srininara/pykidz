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

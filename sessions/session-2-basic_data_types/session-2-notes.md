# Pykidz Sessions - Video 2 - Notes

Welcome Developers, to Pykidz!, A kideveloper initiative.

Last session we covered the following

- Why programming is an essential skill.
- Python is your powerful friend.
- Python installation & python versions
- Python shell or the python REPL
- Operators & Variables

Hope you have completed the python setup and were able to follow those concepts. Today, we will be building on top of them. So, if you have not seen the previous session, please watch it before you see this.

---

Let us get started on today's session.

## Datatypes

<Presentation> We cover Data types today

We have seen variables and they store data. This data has a type. Let us open the python shell to see some examples.

<REPL>

```python
>>> x = 22
>>> s = 'Some text'
```

Now based on the type of data, we can do certain specific things on that type of data . Or it can do certain specific things.

One thing to remember - It is not really the variable that has the type. It is actually the value or literal that has the type. Variables get the type from the value they are labeling. So for all practical purposes, we can think that variables have a type even though it is not strictly correct.

How can we find the type of a variable?

```python
>>> type(x)
>>> type(s)
```

What is `type` ? It is one of the functions directly provided by python. Just like the `print` function we have seen earlier. These functions are called `built-in` functions.

### Basic Datatypes

<Presentation>  Let us look at the basic data types in Python.

* There are numeric datatypes of integer, float and complex. We will get into more details of integer and float types but I will not cover complex since in my opinion it is rarely used.
* There is a text related data type called Strings. We will cover this in detail
* And last but not the least Boolean which are about true and false. We will cover this in brief as well.

### Numeric Types

Let us first talk about Numeric types

The first one is integers.

<REPL>

We already saw `type(x)`. It shows that the class, which is another name for type is `int` - short for integer. So Python supports the integer or `int` data type. Let us see some examples

```python
>>> type(22)
>>> type(32424)
```

We can create very big integer values too. The python language does not put any restrictions on this. But the computer on which you are working might not be able to handle very very big numbers. For most of what we do this shouldn't be a problem. So let us just put a huge number and see

```python
>>> x = 100002121320123123131312312313123133434546456456745646532454435353534535345345
>>> type(x)
```

I think that is a pretty big number. But it is not readable is it. Even this is not easy to read

```python
>>> x = 10000000
```

Is that a crore or a million or ten crores? Difficult to tell is it not. But with your version of python you should be able to do this.

```python
>>> x = 10_000_000
>>> x
```

This makes it much more readable is it not. Here we are using an underscore to separate some of the digits. The value is still the same. But it just makes it easier to read and write big numbers. Support for this way of writing an numeric was added in one of the recent versions of python.

With this data type you already know that you can do calculations or arithmetic operations. We have seen this in the last session. Let us quickly look at a few of these operations

```python
>>> x = 10_000
>>> y = 22
>>> x + y
>>> x * y
>>> x - y
>>> x / y
```

​	Cool. That works. The last example leads us nicely into the second numeric data type which we will cover.

---

This is the `float` data type

This data type is about supporting numbers which have decimal values. Let us take some examples. We just did a division, so let us look at the type of the result:

```python
>>> type(x/y)
```

Now let us define our own number and check its type

```python
>>> x = 102.12
>>> type(x)
```

You can use the underscore style here too

```python
>>> x = 0.0_06
>>> x
```

Let us try a slightly longer number.

```python
>>> x = 0.000_000_008
>>> x
```

What happened here? What does this value mean? What does `8e-09` mean? It means

```python
>>> 8 * 10 ** -9
```

So what you saw was a short representation of this value. If you really want to see the full value printed we can use the `format` built-in function. I will use the `format` function here but I will not cover any details since it will take us away from the topic we are discussing.

```python
>>> format(x, '1.10f')
```

Just like integers we can do arithmetic operations with floats too.

```python
>>> x = 10.5
>>> y = 2.2
>>> x + y
>>> x * y
>>> x - y
>>> x / y
```

One thing to remember with doing arithmetic operations with floats. The resulting values of the operations cannot be relied to be accurate. It is rounded off to an approximately close number in many cases. This is not because of python, but because how floating point numbers work in our computers. Hence this applies to many languages.

For our sessions, we will use floats for working with decimal numbers. But when you grow to build a full fledged application which carry out business calculations, you should use a more advanced type called [decimal](https://docs.python.org/3/library/decimal.html#module-decimal). I will not discuss it here but we might cover it in future sessions.

I want to reiterate one concept again. The data type is for the value. And since a variable is assigned a value, the variable ends up having a type. If you change the value assigned to a variable then type of the variable also changes. Let us take a look at this:

```python
>>> s = 123123
>>> type(s)
>>> <class 'int'>
>>> s = 'sq323'
>>> type(s)
>>> <class 'str'>
```

------------

Time for a break now. And please do take a break. Pause the session, move away from your seat and come back after a 5 minute break and let us start the next topic.

### Strings

<Presentation> We are back and let us start with Strings

Strings represent the textual data type. It is represented as a class `str` in python. You have seen this type already.

A string is a sequence of characters, a "string" of characters and hence the name.

Just like integers, we can have very very big strings with python as long as your computer can manage them. Python does not have any problem. And you also won't have many problems with long strings during your course of learning.

<REPL> A string is created or *to use the developer language "defined"*  by writing a set of characters within a pair of quotes.

To be completely on developer lingo A string is defined by writing a sequence of characters *"delimited"* by quotes. Delimited by quotes means the boundaries (start and end) of the string value are marked by quotes

Let us try an example

> Aside for readers: "Before we look at this you should remember that `#` is the symbol in python to provide comments which are not executed by python. If you write anything after that symbol python will ignore it. Its use is for giving more information to us developers."

```python
>>> s = 'Tenali is a good person'  # single quote usage
>>> type(s)
>>> s
```

So that is a simple string. This is also called a string `literal`. Note how the shell or REPL shows this value. It is showing it with the quotes. If I print the same value, let us see what happens.

```python
>>> print(s)
```

Now you see there are no quotes shown. This is the true value of the string. When you type the variable directly in the shell or REPL it shows it with a quote to denote that it is a string.

For this session I will keep using the function `print` for strings so that I don't confuse you on what the real value of string that we are working with.

Let us define some more strings

```python
>>> s2 = "Tenali lives happily in his town"  # double quote usage
>>> type(s2)
>>> print(s2)
```

So that works too and you can see the printed value. Let us try writing another string.

```python
>>> print("Tenali likes to eat brinjals')  # error , mixed up quotes try again
>>> print('Tenali likes to eat brinjals")  # error, mixed it up again
```

Both these don't work because I got the wrong pair of quotes each time.

```python
>>> print('Tenali lives happily in his town')  # corrected
```

Let us see a few more example to look at different scenarios.

A case of apostrophe:

```python
>>> print('Tenali's life is good')  # error - example string with a quote inside
```

Why didn't that work? Since our written string or string definition starts with a single quote and there is an apostrophe, which is just another single quote, inside the string, the apostrophe signals to python that you have completed the string at that point. But you have not. So what do we do.

```python
>>> print("Tenali's life is good")  # corrected
```

Since my string has a single quote in it, I used the double quote mark the boundaries of my string. Now let us try writing a dialogue.

```python
>>> print(""Tenali's life is good", said the King")  # error - mixing both quotes
```

We see the `invalid syntax` error again. Again all sort of quotes present in the string confuses python. How do we get around it? We use the `\` - backslash.

Backslash can be used to tell python that "You should not think this quote as the end of string. You should move on." Or to quote the developer term - "You should escape it". So backslashes are used to escape quotes inside your string. Let us see an example.

```python
>>> print("\"Tenali\'s life is good\", said the King") # escaping using \
>>> print("\"Tenali's life is good\", said the King") # also works since " is the delimiter
```

This is a good. But there is another way I can achieve this and that way is more powerful. Let us look at it now. Instead of using backslash to escape quotes, we will use a totally different delimiter.

The triple quote -  `'''`

The speciality of this delimiter is that it is something which does not ordinarily appear in normal sentences. So when you use it, python does not get confused. Let us take an example.

```python
>>> print('''"Tenali's life is good", said the King''') # using '''
```

So that works! No need to look for all the quotes inside the string and escape them. Just use a the `'''` delimiter and you are done. The `'''` provides you with another powerful capability or feature.

Let us try to define a string which goes into multiple lines. We will use our normal quotes and see how that works.

```python
>>> print("Tenali is a good person. # multi line failure
```

Python does not like it. When using normal quotes (single or double), python expects the string to end in the same line. You cannot make the string flow into multiple lines. Let us now try to use our newly learned `'''` delimiter.

```python
>>> print('''Tenali is a good person.
... So are you''' # Using triple quote for multi line to work.
```

Wow! That worked. So with `'''` quotes, we can easily create strings with apostrophes and quotes within them. Even create multi-line strings. I think we are good here.

We have spent a lot of time trying to figure out different cases of creating or assigning string literals. I know it has been tedious and long but I wanted to look at these cases so that you have a sound grounding on string literals. It is something you will use very commonly in your life as a python developer.

Time for another break. Take the 5 minutes - step away, do a backflip (if you can do it without hurting yourselves) and come back. You have earned this break!

---

#### String Operations

<Presentation>

We have been doing a lot of string literal definitions. Let us do some operations on Strings. We will cover a few of them.

Let us look at at an example

```python
>>> print("Python can do " + "concatenation")
```

Concatentation is nothing but joining two strings together. Let us do that again with our favourite person.

```python
>>> print("Tenali goes to" + " the school") # concatenation
```

That works! Let us try something else now. The next one

```python
>>> print("Tenali" * 2 )
```

Here I have used the asterisk sign. And what is python doing. It is repeating the same string multiple times.

Remember, in all these cases I am using `print` function only to show you clearly what the string contains. I can do all these operation and definitions on strings without print too. Let us see one.

```python
>>> "Hip hip Hurray Tenali! " * 5
```

Repetition happened as expected. Only thing is that shell shows it with the quote delimiters. If you add a print then you can see it clearly without the delimiters.

```python
>>> print("Hip hip Hurray Tenali! " * 5)
```

Ok.

You just saw `+` and `*` operators used with strings. But they mean different things to strings when compared to numerics. So don't confuse them. `+` is concatentation in strings but addition in numerics. `*` is repetition is strings but for numerics it is multiplication. Also `/` and `-` are not applicable to strings. Only numerics support those operators.

Now let us try something else.

```python
>>> print("Here you go".upper())
```

That is cool. What happened here? This is called *"method calling"*. It is another way of manipulate or work with data types or just data. We will learn a lot more about this later.

Now we come to another interesting feature. Let's look at this string

```python
>>> print("You see, Tenali's house is faraway")
```

What I want to do is to use the name of the person as a variable. That way I can say the same sentence for different people. Let us try that:

```python
>>> name = "Tenali"
>>> print("You see, name's house is faraway")
```

Of course that did not work. Python just thinks that name is part of the string. We need to do something called Interpolation for this to work. Interpolation is about looking at a string literal, checking if it is got any variable place holders present in them and then replace them variable value in that place. Let us take an example.

```python
>>> print(f"You see, {name}'s house is faraway")
```

And lo behold! magic happened. In our example the `name` variable is placed in the middle of the sentence. When python sees the `f` in front of the string, it knows that there could be place holder variables inside this string. The placeholder variable is placed between `{}` (braces). Python identifies it and substitutes it with the value of the variable.

Let us change the variable value and try again.

```python
>>> name = "Kaali"
>>> print(f"You see, {name}'s house is faraway")
```

Works again. This is the `f string` method of interpolation in Python.  There are other method of interpolation supported by python but this is a good and clean one. So we will just stick with this.

### Booleans

<Presentation>

There is one more data type which is to be covered - `Boolean`. This is a separate datatype of python to express the concept of True and False. The only two values of the data type are as expected `True` and `False`.

```python
>>> s = True
>>> type(s)
>>> <class 'bool'>
>>> f = False
>>> type(s)
>>> <class 'bool'>
```

Though Boolean is a special data type present in python for expressing the concept of True and False, other types also exhibit the concept of true ness or `truthy` and false ness or `falsy`. The integer 0 is considered as false or `falsy` and all other integers are considered to be true or truthy. I will show you this a little later. We will see a lot more about booleans later when we come across conditionals and conditional operators. For now let us move on.

### Mixing it up

Let us try to mix these data types up.

```python
>>> name = "Tenali"
>>> age = 12
>>> name + age
```

Python complains. We know name is a string and age is an integer. Both support the operator `+` . A string says that you can use `+` to concatenate two strings. And integer says taht you can use `+` to add to integers. But we are doing something else. We are using this operator with a string and an integer. Python looks at the first value type then looks at the operator and think that you want to do concatenation. It then looks at the second value expecting it to be a string. But it finds a number. And of course you can't do that in Python... So the error. You try the other way and you will see an error but the other way.

```python
>>> age + name
```

You can't add a string to an integer. This happens because Python will strictly follow rules that are applicable to the data type. In developer language <Presentation> we say that Python is **strongly typed**. This means you cannot mix types of objects freely with different operations. That is what you see with the + operator here.

That said, sometimes you want to change them from one to the other. Let us look at a different example

```python
>>> age = "11"
>>> age + 10  # err

```

As expected that did not work. But we know that actual value inside age is an integer. We by mistake stored it as a string by putting those delimiters. In such case we can tell python to change it up.

```python
>>> int(age) + 10
```

Here, by using the `built-in` function `int` we are able to convert a value defined as string into a integer. This is called <Presentation> `Casting`. Let us see a few more examples

```python
>>> age = 20
>>> "My age is " + age # error. Does not work because python is strongly typed
>>> "My age is " + str(age)
```

Just like earlier, we are using a built-in function `str` to convert integer to string. Again this is called casting. Let us just do little more.

```python
>>> a = 23
>>> float(a) # That is integer to float using built-in function
>>> bool(a) # As mentioned earlier this is non zero and hence true or truthy
>>> a = 0
>>> bool(a) # falsy
```

We are using built-in function `float` and `bool` to convert data from other types to corresponding types of float and boolean.

One thing to remember is that casting is not magic. You cannot convert anything to anything. The underlying data must be compatible. Let me show you what I mean

```python
>>> a = "23"
>>> int(a) # This works because the underlying data is an actual number
>>> a = "twenty three"
>>> int(a)  # error. The underlying data is text. Python can't convert that.
```

So the underlying data must be such that python can understand it to be of the type you are casting into. Else python will spit back an error.

Before I close the part, I want to show you another good thing about `f String` based interpolation.

```python
>>> print (f"my age is {age}") # works
```

You can see that `f string` interpolation takes care of doing the casting for us.  I did say `f strings` are cool!

### Other Data Types

<Presentation>

There are other data types in python. One such kind are the composite data types - types which contain a collection of other data. There are also custom types - types which you create.

We will cover both these later. For now, we are done with data types in python.

Let us summarize!


---

## Summary

- We looked at data types - they define the type of data and what you can do with them.
- Within data types we first looked at numerics. - ints and floats. We did the same operations we did earlier.
- Then we looked at strings - defining literals, doing operations on them, interpolating them
- We also looked at booleans - the truthy and the falsy
- We then looked at how we cannot just mix thing up directly because python is strongly typed.
- But when you want to mix them up & you know what you are doing, then you can use casting.

Now, we close with a list of built-in functions we have seen till now in our sessions - just a way for to remember them.

We are done for today. Hope the concept of data types is clear to you. If you have any questions please ask them through comments. I will surely try & answer them. Bye for now. See you in the next session.

# Python: Exceptions & their handling

Whatever the programming language we work with, errors will always come. They are part of a developer's life. We need to understand them - why they occur, how they work and how we can handle them. This is a key learning to understand and work with any programming language.

Let us learn about these concepts in Python

## Errors in Python

Let us first discuss errors in python and how they are caused.

### Syntax Error vs Exceptions

In Python, an error can be a syntax error or an exception. Syntax errors are errors that happen when you code in Python and you make syntax mistakes (that is why the name). They are very simple in nature and are quickly caught be the Python interpreter (actually the python parser) and reported to us. Also some IDEs detect these syntax errors and make them visible even before you run the program. Let us checkout syntax errors in the REPL:

```python
# ptpython
>>> print("abc"))

# Syntax Error: unmatched ')' (<input>, line 1)
```

You see in *ptpython*, as soon as you hit enter, it showed an error. Same thing will happen on the normal python REPL too.

Now let us look at an exception. An exception is something which happens during the actual execution of the code.

The code no longer has syntax errors but when executing the program some error condition has occurred. That is an exception (something unexpected happened). Let us checkout an example.

```python
>>> print(0/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

If you look at this statement, syntactically it is correct. That is why you don't see a `Syntax Error` . So the parsing process completed succesfully and then the actual execution of the program started. But when you divide a number by 0 it is infinity and python cannot handle that. So it throws an exception - `ZeroDivisionError`.

An Exception is Python's way of telling something went wrong when it was running your code. In order to provide us the information of what went wrong, Python creates an object of type Exception.

Actually all data in Python is an object (even the ones which you learnt earlier like strings, sets etc.). So you can think of Exception as a special data type. Every exception has an associated value which indicates the detailed cause of the error. This is generally a string message but it could be other things as well. Another important thing which an exception object has, is the information of where it happened. This context is nothing but a collection of functions called before the problem happened. This is called a stack trace and it is contained in the exception object as a `__traceback__` . Let us use an example to understand this:

Let us take a case of 3 functions `a`, `b` and `c`. Let us say `a` calls `b` which in turn calls `c`. And let us say the exception occurs in `c`. I will define these function so that you get a better idea:

```python
>>> def c(): #Defining c first since b depends on it 
...     0/0 # this will cause the earlier error we saw
>>> def b(): #Now defining b since a depends on it. It just calls c
...     c()
>>> def a(): #Finally defining a
...     b()
>>> a() #Now we call a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in a
  File "<stdin>", line 2, in b
  File "<stdin>", line 2, in c
ZeroDivisionError: division by zero
```

Let us try to understand what is happening here. The function calling happens as `a -> b -> c`. Generally program execution control goes forward once in this direction and return back as `c --> b --> a` . It is as if a, b and c are added into a stack (one on top of the other) and then removed from top down. This is a stack right! Now keep this in mind.

Let us now talk about what is happening on the exception case. The exception actually happens in the function `c` but since `c` function is not doing anything about it, the exception moves down the stack and goes to `b` \- very similar to how the normal control goes back to the caller. Since nothing is done about the exception on `b` as well it moves down the stack to `a` . This is called **exception bubbling**.

![exception_bubbling.png](:/157fea29f2ec45619102eec89d3bfe3c)

I keep say nothing is done about the exception and you are probably thinking *"what should I do about an exception?"*. We will get to that soon but let me finish my story.

So `a` gets the exception and it also does nothing so the exception goes back to the REPL itself and the REPL shows it to us. If we were calling this function as part of file using the `python <file.py>` command then the exception information would have been shown outside and the program would have ended. Or the better term would be that the program **crashed**.

We talked about two key pieces of information which is contained in the exception object. The REPL is showing both these information. One is the message - `division by zero` \- this tells you the cause of the exception. This message is pretty clear to me. But there is another information needed - Where did it happen. It happened in c which is part of the stack and the *stack trace* is shown as the `traceback` here. You see the message and one line above it you know where it happened in the stack. This will help us understand and potentially correct the problem.

This is what an exception is. Actually we have seen exceptions happening before (like trying to find a non existent key in a dict - `KeyError`), but now we have a proper understanding of the same. In any python program there is a possibility of exception happening. These might be because of some code you write or because you use a library/module which throws that exception.

To improve our understanding of exceptions, I want to cover a few more topics. The first one is about raising an exception

### `raise` an Exception

We saw what an exception is, and I told you that the next step is to figure out how to cause an exception. You might be thinking why would I want to cause an exception myself. We will look at that right after we find out how to do it.

We can cause or create an Exception by **raising** it. An Exception as discussed earlier is an object and we can create and raise it anywhere in the code. Let me show you the mechanics of this process:

```python
>>> raise Exception("I have been raised") 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
Exception: I have been raised
```

The code `Exception("I have been raised")` is how we create an exception object. As we create this Exception object, we tell the object the message we want to convey to the receiver of the exception. The information of where it is happening is generally present implicitly in the object, although we have ways of overriding it (I don't think we will do that anytime soon).

But creating is not enough. We actually have to throw it and this is done by the keyword `raise`. As soon as an exception is raised, the control moves back to the caller. Now there is another aspect of how exception control works which I did not cover earlier. So let me do that now. Let me define two functions `x` and `y`

```python
>>> def y():
...     print("Before raising")
...     raise Exception("Exception raised")
...     print("After raising")

>>> def x():
...     print("Before calling y")
...     y()
...     print("After calling y")
```

The two functions are ready. If we call `x` that will in turn call `y` and `y` raises an exception. Before running this, I want you to try and guess the output of the program.

Let us now run it:

```python
>>> x()
Before calling y
Before raising
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in x
  File "<stdin>", line 3, in y
Exception: Exception raised
```

Did you guess that? In the output we see the exception message and stacktrace (traceback) just like we saw before. But there is something else to notice. You only see the printed messages of `Before...` in the output. What does this tell you? As soon as an exception happens in a function (because of some logic or calculation we did or because we raised it), the control immediately moves out of that function to the caller since we are not doing anything about it (more on this later). It seems to work like a return statement. But that is not all. In the function `x` which receives the exception, since we are not doing anything about it, the exception gets bubbled up (or down) the stack. Hence the `After...` statement inside `x` also does not get executed. This clearly tells you that when python encounters the exception, it will immediately pop the latest item on the stack (that is the latest called function) and give the control back to the caller (`x`) at the point where it called the callee `y`.

What I said might be confusing. So listen to it once more if you want to. Remember this behaviour and we will see how this can be modified down the line.

Right at the beginning of this topic, I had said that you might be wondering why you would want to raise an exception yourselves. I can give you a very common scenario for this:

Whenever you create a function which does something based on input parameters, we need to validate whether the input provided is something we can work with.

For showing you this in code, let us try to implement the division using a `divide` method

```python
>>> def divide(dividend, divisor):
...     return dividend/divisor

>>> a = 500

>>> b = 0

>>> divide(a,b)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in divide
ZeroDivisionError: division by zero
```

This works but the message is not very clear in the context of your function. So you can validate the input and raise an exception which provides a better message. Let me show you:

```python
>>> def divide(dividend, divisor):
...     if divisor == 0:
... 				# ValueError is one of the many built-in exceptions in Python  
...         raise ValueError("divisor cannot be 0")  
...     return dividend/divisor

>>> divide(a, b)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
ValueError: divisor cannot be 0
```

The new message is more clear with respect to your function. This is of course a trivial example. If you create a function for simple interest or compound interest, you might want to validate the input data before actually starting with the calculations (e.g. we can't allow negative time in years right.). You should actually try this out and see.

Another thing to note: Python has a ton of built-in exceptions. We just used one above (read more about it here - https://docs.python.org/3.8/library/exceptions.html#ValueError ) and if you want to know all about them you can visit this page - https://docs.python.org/3.8/library/exceptions.html. When you look at this documentation you will also find information which tells you in which scenario you should be using which exception to convey the right meaning to the caller. Pay attention to that.

For `ValueError` it says:

> Raised when an operation or function receives an argument that has the right type but an inappropriate value, and the situation is not described by a more precise exception such as [`IndexError`](https://docs.python.org/3.8/library/exceptions.html#IndexError)

In our case it fits since we were getting a number but the value was 0 which is not acceptable to us. Hope that makes sense. Spending more time on this will help you to understand which exception type to chose for which scenario in your development journey.

We will move on now to understand how we can handle an exception.

## Error Handling in Python

We have had a lot of fun creating and raising exceptions. We also saw that built-in functions and functions or methods provided by libraries can throw exceptions. And these nasty exceptions have the tendency to crash your program (remember exception bubbling) unless we figure out how to handle them. So let us do that.

### The `try` `except` block

Let us first create an example program to help us work with and understand the concepts of error handling. I am first creating an python module `util.py` which will contain our divide function (slightly changed from what we had earlier).

```python
# utils.py
def divide(dividend, divisor):
    dd = int(dividend)
    dr = int(divisor)
    if dr == 0:
    # This is one of the many built-in exceptions in Python  
        raise ValueError("divisor cannot be 0")  
    return dd/dr
```

This is the module I am going to use in my calculator program. This calculator will only support division as of now and it will use this utility function to get the work done. Let us create the calculator program:

```python
# calculator.py
import utils as u
print("Welcome to the calculator! I can do number divisions for you")
print("------------------------------------------------------------")
while(True):
    print("Let me have the numbers please.")
    dividend = input("Dividend please: ")
    divisor = input("Divisor please: ")
    quotient = u.divide(dividend, divisor)
    print("The quotient value is ", quotient)
    print("---------------------------------------")
    do_more = input("Do you want to do more? If so say y: ")
    print("---------------------------------------")
    if do_more != "y":
        break
print("Good bye!")
```

And let us take it for a run:

```sh
▶ python calculator.py
Welcome to the calculator! I can do number divisions for you
------------------------------------------------------------
Let me have the numbers please.
Dividend please: 200
Divisor please: 10
The quotient value is  20.0
---------------------------------------
Do you want to do more? If so say y: y
---------------------------------------
Let me have the numbers please.
Dividend please: 122
Divisor please: 2
The quotient value is  61.0
---------------------------------------
Do you want to do more? If so say y: n
---------------------------------------
Good bye!
```

That seems to work well. Now let us do something different:

```sh
▶ python calculator.py
Welcome to the calculator! I can do number divisions for you
------------------------------------------------------------
Let me have the numbers please.
Dividend please: 121
Divisor please: 11
The quotient value is  11.0
---------------------------------------
Do you want to do more? If so say y: y
---------------------------------------
Let me have the numbers please.
Dividend please: 200
Divisor please: 0
Traceback (most recent call last):
  File "calculator.py", line 8, in <module>
    quotient = u.divide(dividend, divisor)
  File "<<redacted>>cls-expns/utils.py", line 4, in divide
    raise ValueError("divisor cannot be 0")
ValueError: divisor cannot be 0
```

Ok. What you just witnessed is a *program* **crash**. We called the `util.divide` method every time and when we sent the `0` divisor, all hell broke loose. The util function raised an exception and our calculator program did not handle it and hence it bubbled up and crashed the program with the information provided by the raised exception. As a user of the program this output is confusing me and I don't know what to do. The user also got out of the calculator without wanting to. As the developer of the calculator program what are our options? If only we could handle the exception somehow.

Enter the `try except` block:

Whenever you are going to execute code which might cause exceptions you should enclose it in a `try except` block. A `try` block is executed up until the point where the first exception is encountered. As soon as the exception is encountered, the program control moves to the `except` clause and code inside it is executed. Rest of the statements in the `try` block are ignored. Once the statements in the `except` are completed, the program continues to next statement in the block. Let us change the code to see this in action:

```python
#calculator.py
import utils as u
print("Welcome to the calculator! I can do number divisions for you")
print("------------------------------------------------------------")
while(True):
    print("Let me have the numbers please.")
    dividend = input("Dividend please: ")
    divisor = input("Divisor please: ")
    try: # Below is the part of the code which can cause exceptions
        quotient = u.divide(dividend, divisor)
        print("The quotient value is ", quotient)
        print("---------------------------------------")
    except:
        pass #THIS IS NOT A GOOD IDEA
    do_more = input("Do you want to do more? If so say y: ")
    print("---------------------------------------")
    if do_more != "y":
        break
print("Good bye!")
```

Here we have enclosed the *"dangerous"* part of the code inside the `try except` block. The `except` block is not doing much at this point but as we said earlier this ensures that control continues to next line after the `try except` block which might be good enough to start with. Let us execute this to understand what happens.

```sh
▶ python calculator.py
Welcome to the calculator! I can do number divisions for you
------------------------------------------------------------
Let me have the numbers please.
Dividend please: 200
Divisor please: 10
The quotient value is  20.0
---------------------------------------
Do you want to do more? If so say y: y
---------------------------------------
Let me have the numbers please.
Dividend please: 21
Divisor please: 0
Do you want to do more? If so say y: y
---------------------------------------
Let me have the numbers please.
Dividend please: 32
Divisor please: 8
The quotient value is  4.0
---------------------------------------
Do you want to do more? If so say y: n
---------------------------------------
Good bye!
```

What happened this time? When we gave a divisor of `0` to the program this time, it did not crash. It just went forward to get the next input - which are the lines right after the `except` block. So as a programmer we have averted the crash and that is surely a good thing. But are we done yet? The user of the program still does not know what happened to the second divison she ordered. The program just acted as if it forgot about it. That is not very user friendly. So can we do something about it as a programmer? Of course yes. But before I do that, I want to share something else.

### The biggest crime of a python programmer

What I just did now is one of the biggest (if not the biggest) crime for a python programmer. Actually it is a crime in any programming language - it is developer crime. Let me show the structure of it again for you to follow along:

```python
# Show and tell (slide):
try:
    some_fantastic_work()
except:
    pass
```

There are subtle variations in defining the except block but they amount to the same thing — `except Exception:` or `except Exception as e:`. We will cover these styles soon. But the main point here is that is a crime. There are two points to consider:

- By using the `except :` or `except Exception:` or `except Exception as e:`, what we have effectively done is to catch any kind exception in the world that happens inside the try block. The called program might have failed for any reason - some reasons we expect and know how to handle and others we have no clue about. This kind of `except` clause will catch all of them and pass the control into the block.
- The next even bigger crime is that we are doing nothing in this block. That is not handling. That is eating up the exception. That is poisonous. Something has gone wrong and there is nobody who knows about it. The user, the called program, the developer, the support team (in big applications which are used by many users, there are people in teams who help the user to overcome problems they face) - nobody knows that something went wrong. By doing this we have ensured that the problem is never corrected.

Doing this in any project can lead to scenarios where the application does unpredictable things and nobody is wiser to correct it. It can lead to the user(s) losing faith on the application completely and the develeper(s) never knowing what went wrong. Never do this in any application or program you develop. If you see its presence anywhere change it immediately. Few things you could do:

- The minimum thing to do is to announce that something went wrong. This could be simple print or logging statement stating all the information you can provide about the exception scenario. This is the bare minimum. Of course the printing should be visible to people somehow- if it is not seen that the printing is useless.
- The next thing to d1o is to see if you can change the fact that we are catching all exceptions in the world (more on this soon). Try to figure out if you can pick an more specific exception and work with that. This ensures that only the relevant exceptions are caught and rest of the bubble up and are handled at the right places. The first step is still required to be done for this case.
- The third thing to do is to see if you can properly handle the relevant exception. If you don't have the context of the code then this is very difficult to do. In such a case the earlier steps would still add a lot of value.

To reiterate, never eat exceptions (if you are hungry reach for a piece of chocolate or ice cream or even salad). Eating exceptions is worse than crashing the program! This does not mean that you should let the program crash everytime. That is surely bad but eating the exception is worse.

### Return to the `try` `except` block

Let us continue where we left off. So the `try except` block is the way to handle unexpected situations in your application or program without allowing it to its crash.

Ideally inside the `except` clause which is also called the exception handler, we determine how we want our program to respond to the unexpected scenario - the exception. In our example earlier we pretty much ate up the exception so the user did not know what happened. As we learnt just now, let us at least follow the 1st requirement and tell the user what happened so that they are not in the dark. Let us change our **calculator.py** program:

```python
# calculatory.py
import utils as u
print("Welcome to the calculator! I can do number divisions for you")
print("------------------------------------------------------------")
while(True):
    print("Let me have the numbers please.")
    dividend = input("Dividend please: ")
    divisor = input("Divisor please: ")
    try: # Below is the part of the code which can cause exceptions
        quotient = u.divide(dividend, divisor)
        print("The quotient value is ", quotient)
        print("---------------------------------------")
    except Exception as error: #This is still not a good idea
        print("Skipping this one since the division cannot be done:", error) 
    do_more = input("Do you want to do more? If so say y: ")
    print("---------------------------------------")
    if do_more != "y":
        break
print("Good bye!")
```

Let us run this program to see how it works now:

```sh
▶ python calculator.py
Welcome to the calculator! I can do number divisions for you
------------------------------------------------------------
Let me have the numbers please.
Dividend please: 200
Divisor please: 0
Skipping this one since the division cannot be done: divisor cannot be 0
Do you want to do more? If so say y: y
---------------------------------------
Let me have the numbers please.
Dividend please: 200
Divisor please: 10
The quotient value is  20.0
---------------------------------------
Do you want to do more? If so say y: n
---------------------------------------
Good bye!
```

That is surely a much better experience for the user. They know what exactly went wrong and the program did not crash and they were allowed to continue.

This is good progress, but we are still not out of the woods. In our earlier section we talked about two issues or crimes. We have fixed one but there is still one more. We are still using the `Exception` class in the `except` clause. I did not cover this in detail earlier. So let me do it here. As I said earlier, in Python errors happen at runtime and the data around that error case is provided to us as an object.

> #### A brief interlude
> 
> Objects need to be defined in terms of the structure of data they contain and the kind of behavior they exhibit. In most languages and in Python as well (which is what we are mostly interested here), this is done using a class definition. So `Exception` is a class which defines some structure and behavior.
> 
> Objects & classes are concepts which are part of Object Oriented Programming and we are not planning to cover that in these sessions. But I am touching upon them here very lightly so that we can get a better understanding of exceptions.
> 
> Another related concept with respect to objects is inheritance. The idea is that the world is full of general kind of objects and specific kind of objects. Let me take an example. `Mammals` are a generic type of an object (which is alternatively called a class) and `Humans` , `Dogs` and `Cats` are specific type of objects which are all Mammals. So these specific objects all have the same characteristics of mammals. Mammals themselves are specific type of `Animals`.
> 
> ![object_hierarchy_real_world_example.png](:/c0f9770835784c3aa349c191de91064e)
> 
> So a Human is a Mammal which is an Animal. Inheritance means a `is a` relationship between types of objects or classes. When we work with objects in our code, Python will allow us to treat Humans as Mammals or Animals. As a parameter you might receive a Dog but you can treat it as a Mammal or Animal. That is because a Dog is a Mammal and an Animal. But if you receive a Dog and you want to treat it as a Human that won't be possible. In terms of OO, we call **Animal** the *"parent"* and **Mammal** the *"child"*. Similarly **Mammal** is considered the `parent class` and **Human**, **Dog** and **Cat** are called as `child classes`. I think that is a very short explanation of inheritance and that should be good enough for our needs

In the context of Python exceptions, there is similar setup of hierarchy of exceptions. I am going to show a partial hierarchy which is relevant to our discussion:

![python_exception_hierarchy_partial-min.png](:/69dcb4defde54ae3983e500f7397ee16)

So right in the center of the picture we see our `Exception` class. It inherits from `BaseException` but that is not very relevant here (we are interest in just mammals not all animals). Almost all classes or objects which represent error - we have recently seen `ZeroDivisionError` are *"child classes"* of the `Exception` class. This means that Python will be ok to treat any of these errors as `Exception`s.

Let us look at our code again:

```python
import utils as u
print("Welcome to the calculator! I can do number divisions for you")
print("------------------------------------------------------------")
while(True):
    print("Let me have the numbers please.")
    dividend = input("Dividend please: ")
    divisor = input("Divisor please: ")
    try: # Below is the part of the code which can cause exceptions
        quotient = u.divide(dividend, divisor)
        print("The quotient value is ", quotient)
        print("---------------------------------------")
    except Exception as error: #This is not a good idea
        print("Skipping this one since the division cannot be done:", error) 
    do_more = input("Do you want to do more? If so say y: ")
    print("---------------------------------------")
    if do_more != "y":
        break
print("Good bye!")
```

So when you say `except Exception as error` , what Python does is that any error coming from within the try block (here we called that util function and it is raising a `ValueError`) will be caught by this `except` block. This handler may not be good at handling all kinds of errors that can happen in the called program, so using this parent class to catch exceptions for handling can cause unexpected behavior. This is why we said earlier that doing this is a bad idea. Let us correct this.

We know that the `util.divide` function throws a `ValueError` exception. So we could just handle that and show a relevant message to the user. Let us do that now:

```python
import utils as u
print("Welcome to the calculator! I can do number divisions for you")
print("------------------------------------------------------------")
while(True):
    print("Let me have the numbers please.")
    dividend = input("Dividend please: ")
    divisor = input("Divisor please: ")
    try: # Below is the part of the code which can cause exceptions
        quotient = u.divide(dividend, divisor)
        print("The quotient value is ", quotient)
        print("---------------------------------------")
    except ValueError as error: # That is much better
        print("Skipping this division since the values provided are not divisible. Details:", error) 
    do_more = input("Do you want to do more? If so say y: ")
    print("---------------------------------------")
    if do_more != "y":
        break
print("Good bye!")
```

Let us run this.

```sh
▶ python calculator.py
Welcome to the calculator! I can do number divisions for you
------------------------------------------------------------
Let me have the numbers please.
Dividend please: 20
Divisor please: 0
Skipping this division since the values provided are not divisible. Details: divisor cannot be 0
Do you want to do more? If so say y: y
---------------------------------------
Let me have the numbers please.
Dividend please: 200
Divisor please: 10
The quotient value is  20.0
---------------------------------------
Do you want to do more? If so say y: n
---------------------------------------
Good bye!
```

That is a good error message and we have taken care of the second rule as well. The third rule I think was already taken care when we stopped the program from crashing. So we are good.

The story does not end here.

Now the library writer or the util function author sees that the function is not really handling the input properly. What happens if the caller calls the divide function sends two strings instead of numbers. Let us try it out

```python
# ptypthon
>>> import utils as u
>>> u.divide("ab", "c")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/apple/other/srini/my_projects/screencasts/code/trials/cls-expns/utils.py", line 2, in divide
    dd = int(dividend)
ValueError: invalid literal for int() with base 10: 'ab'
```

Ok we are getting some kind of an error but it is very difficult to figure out what is happening. This is where we should be doing validation of input and raising proper errors to the user of the function. Let us do that:

```python
def divide(dividend, divisor):
    # Validating if we are getting numbers only in the input.
    if not dividend.isnumeric() or not divisor.isnumeric():
        # If either of them are not numeric then we throw the
        # corresponding built-in exception in Python
        raise TypeError(f"Only numeric values are supported as input. {dividend} or {divisor} is not numeric.")
    dd = int(dividend)
    dr = int(divisor)
    if dr == 0:
    # This is one of the many built-in exceptions in Python  
        raise ValueError("divisor cannot be 0")  
    return dd/dr
```

Let us try out the improved version of the utils module in the REPL.

```python
>>> from importlib import reload
>>> reload(u)
<module 'utils' from '/Users/apple/other/srini/my_projects/screencasts/code/trials/cls-expns/utils.py'>

>>> u.divide("ab", 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/apple/other/srini/my_projects/screencasts/code/trials/cls-expns/utils.py", line 6, in divide
    raise TypeError(f"Only numeric values are supported as input. {dividend} or {divisor} is not numeric.")
TypeError: Only numeric values are supported as input. ab or 2 is not numeric.
```

That gives better information to the caller. And we are using the built-in `TypeError` because as per the documentation it is the error that is to be thrown when an operation is performed on the wrong type. In our case, division is not an operation to be performed on a string. So the exception type makes sense.

Now let us go back to our calculator program and run that:

```sh
▶ python calculator.py
Welcome to the calculator! I can do number divisions for you
------------------------------------------------------------
Let me have the numbers please.
Dividend please: abc
Divisor please: 23
Traceback (most recent call last):
  File "calculator.py", line 9, in <module>
    quotient = u.divide(dividend, divisor)
  File "/Users/apple/other/srini/my_projects/screencasts/code/trials/cls-expns/utils.py", line 6, in divide
    raise TypeError(f"Only numeric values are supported as input. {dividend} or {divisor} is not numeric.")
TypeError: Only numeric values are supported as input. abc or 23 is not numeric.
```

Oh oh! We see that new error but what we also see is that our calculator crashed. So much for library upgrades! Something you will keep having to deal with in your developer life! Now we have to fix our calculator program. Now the library function is throwing a different exception so we need to handle that separately. How? It is simple:

```python
# calculator.py
import utils as u
print("Welcome to the calculator! I can do number divisions for you")
print("------------------------------------------------------------")
while(True):
    print("Let me have the numbers please.")
    dividend = input("Dividend please: ")
    divisor = input("Divisor please: ")
    try: # Below is the part of the code which can cause exceptions
        quotient = u.divide(dividend, divisor)
        print("The quotient value is ", quotient)
        print("---------------------------------------")
    except ValueError as error:
        print("Skipping this division since the values provided are not divisible. Details:", error)
    except TypeError as type_err: # Now adding a different handler for a different exception
        print("Skipping this division since you are not passing numerals. Details:", type_err)
    do_more = input("Do you want to do more? If so say y: ")
    print("---------------------------------------")
    if do_more != "y":
        break
print("Good bye!")
```

We added a separate `except` block or exception handler. Now let us run the calculator again

```sh
▶ python calculator.py
Welcome to the calculator! I can do number divisions for you
------------------------------------------------------------
Let me have the numbers please.
Dividend please: zbc
Divisor please: 12
Skipping this division since you are not passing numerals. Details: Only numeric values are supported as input. zbc or 12 is not numeric.
Do you want to do more? If so say y: y
---------------------------------------
Let me have the numbers please.
Dividend please: 201
Divisor please: 12
The quotient value is  16.75
---------------------------------------
Do you want to do more? If so say y: n
---------------------------------------
Good bye!
```

That is surely better, right? So with `try except` block we can actually have more than one `except` blocks or exception handlers. This gives us better flexibility to handle different exceptions in a totally different manner. As you do more and more development you will find that this comes in very handy.

There is only more aspect which I want to cover on Exceptions before we close.

### The `finally` clause

We covered the `try catch` block in quite a lot of detail. There is one thing which I left out. It is called the `finally` clause.

> Generally we `try` to do something which works `except` when something goes wrong. But `finally` we do things that always need to get done.

This is exactly how the entire `try-except-finally` block works.

In the `try` clause, all statements are executed till an exception occurs. When that happens the `except` clause is used to catch and handle the exception. `finally` enables us to execute code that should always run, with or without any previously encountered exceptions.

Let me take a example. Let us say we use a program to read a file. The first time everything goes fine and we finish reading the file and *"finally we close the file"*. Second time, we read a file. Something goes wrong as we read the file. We handle that and *"finally we close the file"*. The *"closing of the file"* finally needs to happen whether all is well or if things go wrong. That is the concept of `finally`.

I am actually going to show you the code for the example. I am not going to explain the details of opening the file etc. because that is not the point of this example. Handling files is something you can learn later. I am using the file example because it is perfect for `finally`. The file which is opened needs to be closed no matter what happens. Similarly a connection to a database once open needs to be closed no matter what happens. Such examples are perfect to explain `finally`. Let us check out the code.

Let us first create the file which we want to read. Let us call it **file.txt** (*I know it is super creative! Right!*). I will put the contents here:

```txt
Hello
There
Super
Human!
How
are
you
doing
there?
```

Now we have the file ready for reading. Let us write the program for reading the file

```python
# filereader.py
try: # start off with the try block because we are going to open a file which can go wrong
    my_file = open('file.txt') # open a file - that is simple - that is Python
    print("Reading the file:") # Just some messages for warming up
    print("-----------------")
    while True: # Customary to start with endless loop and break out once done
        line = my_file.readline() # reading the file line by line
        if len(line) == 0: # once the last line is read, the line content will be empty
            break # If true breaking out of reading the file
        print(line, end='') # output what we have read
except KeyboardInterrupt: # exception handler when we interrupt it using Ctrl+C
    print('\nYou stopped the reading of the file.') # handling the interrupt
finally:
    my_file.close() # finally closing the file
    print('\nCleanup: Closed the file')
```

Let us run this normally

```sh
▶ python filereader.py
Reading the file:
-----------------
Hello
There
Super
Human!
How
are
you
doing
there?
Cleanup: Closed the file
```

As you see we read the entire file and once that is done we close the file by executing the finally clause.

Now let us try to create an exceptional scenario.

If we press `Ctrl + C` together when a program is running, we are sending a interruption or the right term is **interrupt** to the program. This is called a `KeyboardInterrupt`. And our code has a `except` block to handle this. So the idea is that when this interruption comes (a exceptional scenario) we handle it. And then we should finally close the file. Let try doing it.

*Trying execution with Ctrl + C*

Ok we have tried that 3 times but the program completes the work before I can hit the keys to stop it. There are two thing I can do.

1.  I can add a lot more text in the file which we read so that it takes more time to read the file. We will probably have put a lot of it and it will make the output more lengthy.
    
2.  Or we simulate some kind of delay in reading the file.
    

Second idea seems more fun. So we use the `sleep` function inside the `time` module to make the program sleep for couple of seconds in between doing the actual work. If we do that I will have the time to send the interrupt before the program finishes.

Remember in a real program you rarely want to add `sleep` because it is going slow down your program and not do any work (who wants a worker to sleep!). But for learning purposes it comes in handy. There could be other reasons too but they don't apply here. We are going to add sleep just so that we can learn.

So adding the sleep:

```python
#filereader.py
import time # We need to import the module before using the function.
try:
    my_file = open('file.txt')
    print("Reading the file:")
    print("-----------------")
    while True:
        line = my_file.readline()
        if len(line) == 0:
            break
        print(line, end='')
        time.sleep(2) # slow things down so that we can see how this works
except KeyboardInterrupt:
    print('\nYou stopped the reading of the file.')
finally:
    my_file.close()
    print('\nCleanup: Closed the file')
```

Now let us try the interrupt again. `Ctrl+C`

```sh
▶ python filereader.py
Reading the file:
-----------------
Hello
There
^C # That is the interrupt in play
You stopped the reading of the file. # This message is coming from the exception block

Cleanup: Closed the file # This comes from finally
```

So even when exception happened the `finally` block is executed. The `finally` block is always executed and therefore it comes in very handy.

When you start working with files in Python later, you will find that there are other mechanism which make it even more easy to work `with` files. They are called **"context managers"**. That is for some other time.

## Conclusion

We have come to the end of these sessions. We covered Errors and Error handling. There are more things to learn in Exceptions and error handling. One of them is about creating your own exception but I have not covered it as part of this basic course. At some point in your python journey you will surely learn and use that too.

For now whatever you have learned should stand you in good stead. Thanks. Until next time. Goodbye!
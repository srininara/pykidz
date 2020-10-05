<slide> Welcome back! In our path to build interactive programs that can be run later, we have covered how to get user input and also how to save code in files using a editor. Now let us look at using code from libraries created by others.

## Using/Reusing Code from Others

As you have been playing with python all this time, there is one thing you might have noticed. In order to do something we most times reach out and use the built-in functions of python.

Built-in functions are available for us to use in python without having to do anything. There are 69 of them available. But do you think these 69 cover everything you can do with python. Of course not. Python has a lot more to offer.

<slide> Python has a concept of modules and packages. A module of piece of code which has a specific purpose. Actually a python file is a module. Even the python file which you created is a sort of a module. To be precise a file with a `.py` extension is a module. 

<slide> Multiple modules can be included in a package. Packages are nothing but directories containing modules. Not all directories can be called a package. You need to do something more. But we will cover them later and at that time we might even create our own packages.

<slide> The more important thing to learn at this point is that there are already existing packages and modules which come with the python installation itself. This is called the `Python Standard Library` and is created by the python language and installation creators. This provides a bunch of modules which contain multiple functions and other useful things which you can make use of to do a lot of things. 

Other than the standard library, we can even use libraries created by other people. This is something we will look at later. Right now let us focus on how we can use the python standard library functions itself.

<slide> One of the basic modules in python standard library is the `math` module. The `math` module provides a lot of functions which are related to math operations. There are functions related to number theory, logarithms, trigonometry etc. Let us look at one function which we surely would understand and probably like to use from time to time. 

The `sqrt` function in math module allows us to find the square root of a number. Let us go to the REPL see how we can use this function.

```python
>>> sqrt(4096)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sqrt' is not defined
```

That of course did not work. Python does not know about the `sqrt` function. It is not a built-in function. 

<slide> The first step to make this function available for us is to `import` the function from its module - in this case the `math` module. To use a real world example, in order to use a watch which is made in different country's factory you need to import the watch to your country or house. Let us show you how to do that. 

Back to the REPL. But remember whatever we do in the REPL can be done in the python file as well.

```python
>>> from math import sqrt
>>> sqrt(4096)
64.0
```

Here I imported the `sqrt` function from the `math` module and then used it to calculate the square root of a number. <Exit the REPL>

Sometimes you are not content with one watch model. You want all the different watch models a factory produces. In order to achieve that you just import the entire factory itself. In the analogy, I am thinking of the module as a factory and the module's functions as the watch models. The way to import the entire factory or the module is as follows. In the REPL:

```python
>>> import math
>>> sqrt(4096)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sqrt' is not defined
```

What happened? Ok. Here I imported the entire math module. Earlier I had told python to import the `sqrt` from the math module. The function alone is imported and made available to python to use directly. But this time I have imported the module, python knows about the module only directly. It doesn't know the name of the functions inside it. So inorder to use the `sqrt` function I have to tell python to look for it inside the `math` module. Hence:

```python
>>> math.sqrt(4096)
64.0
```

That worked! Now that I have imported the entire module, I can use other things inside the module. I said earlier that modules can contain functions and other things. Among these other things, one is constants. Constants, as the word suggests are just things that don't change value. Similar to what you have heard in your math class. There is one famous constant within the math module. That is `pi`. Let me show you.

```python
>>> math.pi
3.141592653589793
# Let us calculate area of circle
>>> r = 20
>>> area = math.pi * r **2
>>> area
1256.6370614359173
```

So now I have used both a function and a constant from the math module. 

Ok I have said constant more than once. Let me tell you a secret. The truth is that python does not support true constants. This means that the value of `pi` present in `math` can be changed if you want to. But don't do it. It is not a good thing to do since it will defeat the purpose it being present in `math` module. Let us just keep it a secret between us. ;-).

I think we have covered enough ground to get us create the actual interactive programs. In the next part we will create our two programs.

If you have any questions, please ask in comments and I will answer them.

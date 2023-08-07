## Introduction
Welcome Developers, to Pykidz!, A kideveloper initiative. 

<slide> Last session 

- We covered datatypes and what they mean.
- We looked at numeric datatype - ints and floats - and did operations on them.
- We looked at strings. We defined them for multiple scenarios
- We did some operations on them. You might recall `f strings`.
- Then we covered booleans. Some basics.
- We then looked at python's strongly typed nature. We looked at how you can use casting to convert between types where it makes sense.

<slide> Please remember that these sessions will make a lot more sense if you actually work with them. If you just watch them as a video then they will not be much fun or much learning. You should open up the python shell and practice the things I am doing here so that you can learn with me. 

<slide> Now that we have gotten start with the python language, let us look at the things which will help you to build some programs with some interaction. In these set of sessions, we will learn the following things:

- Get input from the user as part of running the program - Session 3.1
- Move from REPL to storing your code in file - Session 3.2
- Import a module to use it in our program - Session 3.3

I will be covering each of these topics in separate video sessions so that it is easier for you to work with them. This is based on a feedback from my daughter!

Once we learn these things, we will build - that is another way of saying write code - couple of programs which can executed directly from the terminal. We won't need to get into the shell for this. We will discuss more on this later. The programs we will build are:

- A serious one - A simple interest calculator - Session 3.4 
- A silly one - A greeter - Session 3.4

Remember to watch the previous videos before you start with these ones. Also look at these series of videos one after the other. 

Without much ado, let us get started with the first topic.

## Getting User Input

<slide> To build an interactive program, we need to get input from the user. We can ask some relevant questions to the user and the user could respond to them. And based on these responses the program will do the promised work.

An interactive program allows a user to tell what she wants and change the way the program works according to her wishes. Of course you are the developer, so you are the final decision maker on what all ways, a user can control things or provide input. For now, let us stop worrying about what is the use of doing this. The examples provided in the later will illustrate the point. Let us get to some code.

<REPL>Open your REPL now by typing `python` on your terminal and you will see your prompt. 

Let us start with the customary greeting

```python
>>> name = "Tenali" # Add your name here
>>> print(f"Hello {name}")
```

We are done with greeting ourselves. 

> <slide> But before we move to the task at hand, I want to explain something quick.
>
> #### Function arguments
>
> In the above example `print` is a function, in this case a built-in function, a function directly provided by python. We pass a string to this function so that it can print it. This passed string is called an ***argument***.
>
> <REPL>
>
> ```python
> >>> argument = 'Hello World!'
> >>> print(argument)
> ```
>
> I have used the name argument but it could be any name or directly a literal
>
> ```python
> >>> print("Hello Tenali!")
> ```
>
> 
>
> Functions when called can take 0 or more arguments which they will use in doing their work. Here the `print` function is taking a string and printing it back on the screen. Other functions may do other things. 
>
> That is enough of a sidetrack. Only thing I want you to remember in this is the concept of passing ***arguments*** to a function.

<slide> Now let us get back. We want to get an input from the user. So what should we do? Simple, we use the built-in function `input`.  

```python
>>> s = input()

```

What is happening? Why are we not getting the REPL prompt back? It looks like something got stuck. Let me just hit `Ctrl + c` once. 

```python
>>> s = input()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyboardInterrupt
>>>
```

I get an error, but I got my prompt back. So let us forget the error and get back to what we want to do. Actually, the missing prompt is not an issue. When we asked python to get input by calling the built-in method `input`, it was waiting for taking that input. Let us try it again.

```python
>>> s = input()
Tenali # I type this in
```

Now I entered a string and hit enter and the prompt is back. Let us now look at the value of s

```python
>>> s
'Tenali'
>>> type(s)
```

So we see that the value we typed when python prompted us is stored in the variable `s`. And we also see the type is `str` - string.

The reason we became clueless earlier when the input prompt came, is that it was blank and did not give us any clue on what the program wanted us to do. We can remedy that:

```python
>>> s = input("Tell me your name")
Tell me your nameTenali
>>> s
'Tenali'
```

By giving some text to the built-in `input` function, we are able to provide some contextual information when we prompt the user to provide some input. Of course this prompt is not easy to read. Let us fix that.

```python
>>> s = input("Tell me your name: ")
Tell me your name: Tenali
>>> s
'Tenali'
```

By giving a colon and space at the end, our prompt for user input is that much more readable.

There is one more thing I want to cover with respect to getting user input.

```python
>>> n = input("Give me a number: ")
Give me a number: 22
```

Here we are asking the user to enter a number. The user does it too. Now let us look at its value and type.

```python
>>> n
'22'
>>> type(n)
<class 'str'>
```

So even though the user entered a number, python's `input` function will always take the input as a string. It is your job as a developer to handle this. Remember our trusty old casting functions.

```python
>>> int(n)
22
>>> type(int(n))
```

The casting function worked - now the type is int

> <slide> Let me cover another concept here:
>
> #### Function composition
>
> ```python
> >>> type(int(n))
> ```
>
> What I am doing here is first casting the value of `n` with the `int` built-in function. I am then passing the output of that function to the `type` function as an argument. This is called ***function composition***. 
>
> Let me explain that once more. In function composition, the output of one function is passed as an argument or input to the next function. And we can do this any number of times. That is, keep taking an output from one function and pass it as an argument to the next function which returns some output which can be become an argument for the next one and so on. Here is another example:
>
> ```python
> >>> print(int(input("Give me a number: ")))
> Give me a number: 23
> 23
> ```
>
> Here I get the input from the user using the `input` function. The input returns this as a string. That string is now passed as an argument to the `int` built-in function which casts its value to integer. The `int` function returns an integer which is given as a parameter to the print function which prints it on the screen. 

Ok. Now we have figured out how to collect input from the user of program. Let us move to the next step of building our executable programs in the next video.

If you have any questions or doubts, please use the comments and I will respond to them.

---

Ok. Welcome back. In the last video we finished learning how to get user input. This video we are going to focus on ability to create and save programs to run later. Let us get to it

## REPL vs Python File

<slide> Till this point we have been writing code in the REPL or the python shell. I keep using the word REPL for the python shell. This is actually an acronym. It stands for:

- ***Read*** - Reads the command you enter
- ***Evaluate*** - Evaluates (or understands) and executes the command
- ***Print*** - Prints the output (if any) to the console
- ***Loop*** - Loops back and repeats the process

Apart from Python many other languages like Ruby, Java also provide REPL based environments so that you can quickly try out things and learn stuff.

But there are problems with continuing our learning with the REPL. In the REPL, whatever you type in is present only in the REPL. Outside it, we cannot use or even see the code. Also, if you are trying to do something which needs multiple lines of code and want to use it again and again, it is not easy to do with the REPL. 

We want to create programs that we can store somewhere and run later when we want. So let us get to it.

<slide> Typically many python teachers use something called `IDLE` for writing, storing and executing python code as files. IDLE is short for **Integrated Development and Learning Environment** and comes with python installation . It is an ***IDE*** included with python. What is an IDE? IDE stands for Integrated Development Enviroment. It is a special program which allows us to enter program code, in our case python code, execute it and debug it. Some of the interesting features an IDE offers are:

- Syntax highlighting - diff. colours for diff. things
- Context sensitive help - show documentation
- Code completion - complete code for you
- Debugging - help you find mistakes

You may not understand them as of now. I will demonstrate these to you as we move forward.

As for me, I am going to take a different approach. I am going to download a good code editor which can be extended to provide python support. The reason is code editors are light weight i.e. another way of saying smaller and faster programs, and have general purpose. Today you might use the editor for learning python. Tomorrow you might want to do some javascript or html development for your site. A good editor will support all these usecases and more. I will use an editor to create the programs. For executing them I will use the terminal. 

There are multiple ways of creating programs. I tend to use this because it is simple to setup and keeps my system faster. You can start the same way as me. As you move forward in the journey of a developer, you might decide a different way  works better for you. If so, you should go ahead and do that.

<slide> Let us get back. We are going to use [VS Codium](https://vscodium.com/). VS Codium is the open source version of a the famous VS Code editor. It is a free code editor provided by Microsoft. 

You may not know what open source is. If so open your favorite browser and search for the term to understand it. May be I will talk about it at a different time but I think you should search and read about it. Part of being a developer is being inquistive and be resourceful to find answers.

Now VS Codium can be downloaded from the site. Let us do that.

<browser>

Once you download and install it, open up the editor. The first thing to do is to install an extension. You can go to the extensions section and search for `python`. The first extension you get is the `python` extension. Click on it and you will see what it provides. It mentions intellisense - which is another name for the features I mentioned like code completion, context sensitive help etc. Now install it. By doing this you have converted the simple code editor into a decent IDE.

Let us get started with VS Codium to figure out how we can create our first program.

<codium>

We use the open menu to pick the folder in which I am going to store my programs. You should pick a separate folder in a well known (to you) location, so that you can easily find your work later too.

Once I am in that folder, I can create a new file. I am going to name the file `hello.py`. Make a specific note about the file extension name - `.py`. The `py` file name extension is what tells the editor that you are writing python code in this file. Always double check that you got it right.

As tradition goes, the first line I am going to enter is:

```python
print("Hello World!")
```

I save this file (using the file menu or through the shortcut). I open my terminal and go to the directory where I saved the file. 

Now let us execute the program:

```shell
▶ python hello.py
Hello World!

```

Ok. We did it. We created a file which is a python progam and we executed it using the python command. This is a simple step but it is an important one. This is exact the thing you will do whether you are creating a one line program or 500 line program or 5000 line program - ok that might be different. So get very comfortable doing this.

Before I conclude I want to cover one more aspect.
<slide>
### Comments

In the file, on the first line I type this and hit enter

```python
# This is my first program
```

Save again and execute the program. You will see nothing new happens. And that is expected.

The line `# This is my first program` is called a comment. 

```python
# I am a comment
```

A comment is just a piece of text which is added inside a program file for developers to read. It is completely ignored by python. So when you execute the file, python just skips the first line and executes the second one. 

Comments is an important tool in a developer's toolkit. It allows the developer to provide information or context to other developers who might read this code. Actually it might provide context to you as a developer when you look at this code after sometime.

While comments can be useful, overusing them can create noise which might make it difficult to look at the code itself. 

One thing which is worse than lot of comments, is a comment which is out-dated i.e. the comment is wrong because the code has changed and the information provided in the comment is not correct. 

So use comments, but use it right.

That concludes this part of the session. Hope you are able to setup your editor and execute this simple hello world program. In the next part we will talk about  reusing code written by others.

As usual, if you have any questions or doubts, please use the comments and I will answer your questions.

---

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

---

<slide>
Welcome back! In this part we are going to actually apply the concepts we learnt in the previous parts and create programs that do something and can be run again and again.

## Example 1 - A simple interest calculator

First let us create a simple interest calculator.

```python
# principal = int(input("Please let me know your principal in Rs: "))
principal = float(input("Please let me know your principal in Rs: "))
rate = float(input("Please give me the rate of interest you are getting in %: "))
time = int(input("Please let me know the number of years you are investing: "))

# Formula for simple interest
si = principal * rate * time /100
print("***********************************************************")
print(f"Your investment: {principal}")
print(f"The rate applied: {rate}%")
print(f"The investment period: {term} years")
print(f"Simple interest you get the end of the period: Rs. {si}")
print(f"Total amount at the end of investment period: Rs. {si + principal}")
print("***********************************************************")

```
[Code reference](code/si_calculator.py)

The above example illustrates how by taking the input from the user we are able to provide them with useful information. If we did not get the input of the principal or rate or time from the user then the program would define these values inside the code which is not very useful to the end user.

## Example 2 - A greeter 

Let us now do our silly greeter. This time we will import some modules and use them here.

```python
from random import randint
from datetime import datetime
fname = input("Please tell me your first name: ")
lname = input("Please tell me your last name: ") 
print("***********************************")
# want to repeat greeting at random.
print(f"Hi! {fname} {lname}\n" * randint(1,10))
print("This is python greeter here!")
print("***********************************")
print(f'''How are you today, {fname}? 
Hope {datetime.today().strftime('%A, %B %d')} is a good day for you! 
Bye!''')
```
[Code reference](code/greeter.py)

## Conclusion

<slide>

We have developed and *saved two programs* that *interact with the user*, *import modules* from the python standard library to do different kinds of tricks and even *added some comments* to the code. 

You have practically used all the concepts you learn in this session. You also used some of the things which we learnt in earlier session. This concludes this session and all its parts. I will come back with a next topic in python. Please use the comments to ask your questions. Thanks and see you soon.

## References
- [Documentation for randint function inside random module](https://docs.python.org/3/library/random.html#random.randint)
- [Documentation for today function inside datetime class within datetime module](https://docs.python.org/3/library/datetime.html#datetime.datetime.today)
- [Documentation for strftime function inside datetime class within datetime module](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)
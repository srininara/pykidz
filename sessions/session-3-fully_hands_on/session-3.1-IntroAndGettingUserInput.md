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


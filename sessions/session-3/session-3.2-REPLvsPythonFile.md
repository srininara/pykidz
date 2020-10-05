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
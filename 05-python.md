# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

[![Think Python](img/think_python.png)](http://www.greenteapress.com/thinkpython/)

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

Complete the following exercises to check your ability with Python.

These exercises are implemented with doctests, which are runnable tests inside docstrings. Fill in the function definitions. Correct solutions will make it possible to run (for example) `python -m doctest strings.py` with no messages about failures.

 * [Strings](python/strings.py)
 * [Lists](python/lists.py)


---

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

> Both lists and tuples are a set of elements/values which can be referenced by numeric indices. Lists can be modified, add or remove elements while tuples are fixed. The values assigned to a tuple are permanent and there are no functions available to modify. Tuples can work as keys because of their immutable nature.

---


---

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

> Both lists and sets are series of values. A list is ordered, can contain duplicate values and can be referenced by index while a set is an unordered set of distinct elements. 
Example of list can be a queue at a ticketing counter with values corresponding to customer name and by order first in, first out. customers = ["Michelle", "Sam", "Nathan", "John", "Steve", "John"]
Example of a set can be for enrollment at a club where SSN is the unique value stored in a set. SSN should not have duplicates. id = set([123456, 345632, 334212])
In finding an element from a large set of data, sets are faster because they make use of hashtables.

---


---

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

> Lambdas are in-line, anonymous functions used when a particular piece of code will not be reused. It is helpful so as not to make the code cluttered with numerous regular functions that are used only once. Given a list of names = ["George Smith", "Anne Brown", "Mike James", "Katie Simpson"], we can sort by last name instead of the default first name sort using sorted(names, key=lambda name: name[name.index(" ")+1:]).

---


---

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

> List comprehensions are simple and compact python constructs that generate lists based on an expression to be executed for each variable in a list/collection with or without a condition. Map() takes 2 arguments, a function and a list of values to apply the function to. Filter() also takes 2 arguments, a function that returns only either True or False and filters the set of values retaining only those that return True. List comprehensions can combine the capabilities of both map() and filter() into one expression. Example of map: generate squares of a range of numbers = map(lambda x: x**2 , range(10)). Example of filter: only retain in list squares are greater than 50 = filter(lambda x: x**2 > 50 , range(10)). We can create a simple list comprehension of original list values with squares greater than 50 by  [x for x in range(10) if x**2 > 50], which sort of combines both map and filter functions.
Set comprehension: print all values divisible by 5 from 0 to 99 in sorted order = sorted({x for x in range(100) if x % 5 == 0})
Dictionary comprehension: return all letters in word with corresponding uppercase letters = {x: x.upper() for x in "traditional"}

---


Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

```bash
./markov.py chains.txt 40
```

A possible output would be:

> show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.

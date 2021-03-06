# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    #raise NotImplementedError
    
    if count < 10:
        return "Number of donuts: %s" % (count)
    else:
        return "Number of donuts: many"


def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    #raise NotImplementedError
    
    if len(s) < 2:
        return ""
    else:
        first_two = s[0:2]
        last_two = s[-2:len(s)]
        return "%s%s" % (first_two, last_two)


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    #raise NotImplementedError
    fix  = s[0]
    word = ""

    for index, char in enumerate(s):
        if char == fix:
            if index == 0:
                word = "%s%s" % (word, char)
            else:
                word = "%s%s" % (word, "*")
        else:
            word = "%s%s" % (word, char)

    print word


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    #raise NotImplementedError
    first_word = a[0:2]
    second_word = b[0:2]
    a_word = a[2:len(a)]
    b_word = b[2:len(b)]

    print "%s%s %s%s" % (second_word, a_word, first_word, b_word)

def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    #raise NotImplementedError
    if len(s) >= 3:
        if s[len(s)-3:len(s)] == "ing":
            return "%sly" % (s)
        else:
            return "%sing" % (s)
    else:
        return s

def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    #raise NotImplementedError
    if "not" in s and "bad" in s:
        if s.index("not") < s.index("bad"):
            first = s[:s.index("not")]
            last = s[s.index("bad")+3:]
            return "%sgood%s" % (first, last)
        else:
            return s
    else:
        return s

def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    #raise NotImplementedError
    a_split = len(a) / 2 + len(a) % 2
    b_split = len(b) / 2 + len(b) % 2

    a_front = a[:a_split]
    a_back = a[a_split:]
    b_front = b[:b_split]
    b_back = b[b_split:]

    return "%s%s%s%s" % (a_front, b_front, a_back, b_back) 

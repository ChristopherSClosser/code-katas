[![Build Status](https://travis-ci.org/ChristopherSClosser/code-katas.svg?branch=master)](https://travis-ci.org/ChristopherSClosser/code-katas)
[![Coverage Status](https://coveralls.io/repos/github/ChristopherSClosser/code-katas/badge.svg?branch=master)](https://coveralls.io/github/ChristopherSClosser/code-katas?branch=master)

# Code Katas

- **Chris Closser**
- **Version**: 1.0.8

### Overview
- This repo will continue to grow as I fight my way through code wars. Adding katas as I go.

### Getting Started
<!-- TODO: add stuff  -->
- You know the drill...fork or clone

### Architecture
<!-- Provide a detailed description of the application design. What technologies (languages, libraries, etc) you're using, and any other relevant design information. -->
- All Python -
  - Python libs
    * py-test
    * sys
----------------------------------------------------------------------------------------------------------------------------------    
### Katas:
#### - Tribonacci Sequence 6 kyu
- [Challenge url](https://www.codewars.com/kata/tribonacci-sequence)

  Summing the last 3 numbers of a sequence
to generate the next.

#### - HQ9+ 8 kyu
- [Challenge url](https://www.codewars.com/kata/8kyu-interpreters-hq9-plus)

  Implement a simple interpreter for the notorious esoteric language HQ9+

#### - Find The divisors 6 kyu
- [challenge url](https://www.codewars.com/kata/find-the-divisors)

  Takes an integer and returns an array with all of the integer's divisors (except for 1 and the number itself).

#### - Multiples of 3 and 5 6 kyu
- [challenge url](https://www.codewars.com/kata/multiples-of-3-and-5)

  List all the natural numbers that are multiples of 3 or 5.

#### - Friend or Foe 7 kyu
- [challenge url](https://www.codewars.com/kata/friend-or-foe)

  Make a program that filters a list of strings and returns a list with only your friends name in it.

#### - Jaden Casing Strings 7 kyu
- [challenge url](https://www.codewars.com/kata/jaden-casing-strings)

  Convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

#### - Disemvowel Trolls 7 kyu
- [challenge url](https://www.codewars.com/kata/disemvowel-trolls)

  A function that takes a string and return a new string with all vowels removed.

#### - Find the smallest integer in the array 7 kyu
- [challenge url](https://www.codewars.com/kata/find-the-smallest-integer-in-the-array)

  Given an array of integers your solution should find the smallest integer.

#### - Grasshopper - Terminal game move function 7 kyu
- [challenge url](https://www.codewars.com/kata/grasshopper-terminal-game-move-function)

  Create a function for the terminal game that takes the current position of the hero and the roll (1-6) and return the new position.


#### - Multiply 8 kyu
- [challenge url](https://www.codewars.com/kata/multiply)

  Multiply two numbers.


#### - Sort a Deck of cards 7 kyu
- [challenge url](https://www.codewars.com/kata/sort-deck-of-cards/train/python)

  Write a function sort_cards() that sorts a shuffled list of cards, so that any given list of cards is sorted by rank, no matter the starting collection.

  Using my PriorityQ


#### - Valid Parentheses 5 kyu
- [challenge url](https://www.codewars.com/kata/valid-parentheses/train/python)

  Write a function that takes a string of parentheses,
  and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.


#### - String Pyramid 6 kyu
- **URL**: [challenge url](https://www.codewars.com/kata/string-pyramid/train/python)

  You have to build a pyramid.

  This pyramid should be built from characters from a given string.

  You have to create the code for these four methods:

  The first method ("FromTheSide") shows the pyramid as you would see from the side.
  The second method ("FromAbove") shows the pyramid as you would see from above.
  The third method ("CountVisibleCharacters") should return the count of all characters, that are visible from outside the pyramid.
  The forth method ("CountAllCharacters") should count all characters of the pyramid. Consider that the pyramid is completely solid and has no holes or rooms in it.

  Every character will be used for building one layer of the pyramid. So the length of the given string will be the height of the pyramid. Every layer will be built with stones from the given character. There is no limit of stones.
  The pyramid should have perfect angles of 45 degrees.


#### - Rotate matrix in place 90 5 kyu
- **URL**: [challenge url](https://www.codewars.com/kata/rotate-a-square-matrix-in-place)

  Given a square matrix, rotate the original matrix 90 degrees clockwise... in place! This means that you are not allowed to build a rotated matrix and return it. Modify the original matrix using a temporary variable to swap elements and return it. You are allowed to use a couple scalar variables if needed.


#### - String incrementer 5 kyu
- **URL**: [challenge url](https://www.codewars.com/kata/string-incrementer)

  Your job is to write a function which increments a string, to create a new string. If the string already ends with a number, the number should be incremented by 1. If the string does not end with a number the number 1 should be appended to the new string. If the number has leading zeros the amount of digits should be considered.


#### - Bug Squish! 7 kyu
- **URL**: [challenge url](https://www.codewars.com/kata/bug-squish)

  Take debugging to a whole new level:
  Given a string, remove every single bug.
  This means you must remove all instances of the word 'bug' from within a given string, unless the word is plural ('bugs').
  For example, given 'obugobugobuoobugsoo', you should return 'ooobuoobugsoo'.
  Another example: given 'obbugugo', you should return 'obugo'.
  Note that all characters will be lowercase.

  Happy squishing!


#### - Typoglycemia Generator 5 kyu
- **URL**: [challenge url](https://www.codewars.com/kata/typoglycemia-generator)

  **Background**   
  There is a message that is circulating via public media that claims a reader can easily read a message where the inner letters of each words is scrambled, as long as the first and last letters remain the same and the word contains all the letters.

  Another example shows that it is quite difficult to read the text where all the letters are reversed rather than scrambled.

  In this kata we will make a generator that generates text in a similar pattern, but instead of scrambled or reversed, ours will be sorted alphabetically

  **Requirement**    
  return a string where:
  1. the first and last characters remain in original place for each word
  2. characters between the first and last characters must be sorted alphabetically
  3. punctuation should remain at the same place as it started, for example: shan't -> sahn't

  **Assumptions**   
  1. words are seperated by single spaces
  2. only spaces separate words, special characters do not, for example: tik-tak -> tai-ktk
  3. special characters do not take the position of the non special characters, for example: -dcba -> -dbca
  4. for this kata puctuation is limited to 4 characters: hyphen(-), apostrophe('), comma(,) and period(.)
  5. ignore capitalisation

for reference: http://en.wikipedia.org/wiki/Typoglycemia

----------------------------------------------------------------------------------------------------------------------------
### Change Log  
<!-- Use this are to document the iterative changes made to your application as each feature is successfully implemented. Use time stamps. Here's an example:

01-01-2001 4:59pm - Added functionality to add and delete some things.
-->
<pre>Oct 20 17 1300hrs&ensp;&ensp;-&ensp;&ensp;Init&ensp;&ensp;-  

Oct 21 17 0800hrs Kata: Tribonacci
                  Kata: HQ9+
                  README

Oct 21 17 0830hrs Kata: Find the divisors
                  Testing
                  README

Oct 21 17 0900hrs Kata: Multiples of 3 and 5 6
                  Testing
                  README

Oct 21 17 0930hrs Kata: Friend or Foe
                  Testing
                  README

Oct 21 17 1000hrs Kata: Jaden Casing Strings
                  Testing
                  README

Oct 21 17 1030hrs Kata: Disemvowel Trolls
                  Testing
                  README

Oct 21 17 1100hrs Kata: Find the smallest integer in the array
                  Testing
                  README

Oct 27 17 1030hrs continuous integration with travis-ci
                  test coverage with coveralls
                  .travis.yml                  
                  Testing
                  README
</pre>

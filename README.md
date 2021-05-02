## Maximal Palindrome

Threre is a method that returns the longest palindrome, that can be formed with the characters of a given string.

Give string `s`. Task is to find this longest possible [palindrome](https://en.wikipedia.org/wiki/Palindrome). I can use any number of the characters from `s` and
arrange them in ay order (so long as it results in a palindrome). If there are multiple longest palindromes that can be
formated, returned the one among that's [lexicographically smallest](https://en.wikipedia.org/wiki/Lexicographic_order).

### Example
* For `s = "aaabb"`, the output should be `maximalPalindrome(s) = "ababa"`.
There're two possible palindromes of length `s` that can be obtained (`"ababa"` and `"baaab"`), but `"ababa"` is lexicographically smaller, thus it is the answer.
* For `s = "aaabbbcc"`, the output should be `maximalPalindrome(s) = "abcacba"`.
It's not  possible to form a palindrome of length `s`, but  from several palindromes of length `7`. `"abcacba"` is the lexicographically smallest, thus it is the answer.

### Task input/output
* [execution time limit] **4 seconds** (py3)
* [input] **string `s`**.

The given string.
*Guaranteed constraints:*

`1 <= s.length <= 10^5`

* [output] **string**
The lexicographically smallest palindrome with maximal length that can be built from the given string `s`.


## Result
Method works good.

# Regular Expressions

## Character Sequences
Syntax | Description | Example
--- | --- | ---
[abcd] | Matches any of the characters in any sequence or count | 
[^abcd] | Matches any character not in the set
[a-d] | Matches any character in the range
[^a-d] | Matches any character not in the range
[a-d-] | Matches any character in the range and the '-' character

## Quantifiers
Syntax | Description | Example
--- | --- | ---
\* | Matches the preceding expression 0 or more times | /ab*c/ matches ac, abc, abbc, abbbc, and so on
\+ | Matches the preceding expression 1 or more times | /ab+c/ matches abc, abbc, abbbc, and so on
? | Matches the preceding expression 0 or 1 time | /ab?c/ matches ac or abc
{n} | Matches the preceding expression exactly n times | /ab{2}c/ matches abbc
{n,} | Matches the preceding expression at least n times | /ab{2,}c/ matches abbc, abbbc, and so on
{n,m} | Matches the preceding expression at least n times, but no more than m times | /ab{2,4}c/ matches abbc, abbbc, or abbbbc

## Character Classes
Syntax | Description | Example
--- | --- | ---
. | Matches any character except newline | /a.c/ matches abc, acc, a-c, a1c, and so on
\d | Matches any digit, equivalent to [0-9]
\D | Matches any non-digit, equivalent to [^0-9]
\w | Matches any alphanumeric (word) character, equivalent to [a-zA-Z0-9_]
\W | Matches any non-alphanumeric character, equivalent to [^a-zA-Z0-9_]
\t | Matches a tab character
\n | Matches a newline character
\r | Matches a carriage return character
\f | Matches a form feed character
\v | Matches a vertical tab character
\s | Matches any whitespace character, roughly equivalent to [\t\n\r\f\v]
\S | Matches any non-whitespace character, roughly equivalent to [^\t\n\r\f\v]

## Escaping
Syntax | Description | Example
--- | --- | ---
\ | Escape character, used to escape control characters | /\./ matches a period, not any character

## Combination of Expressions
Syntax | Description | Example
--- | --- | ---
\| | Alternation, matches either the expression before or after the | /a|b/ matches a or b

## Positions Constraints
Syntax | Description | Example
--- | --- | ---
| - | - | 
^ | Matches the start of a string | /^prefix_/
$ | Matches the end of a string | /_suffix$/
\b | Matches a word boundary, that is, the position between a word and a space | /\b

## Lookahead and -behind
Syntax | Description | Example
--- | --- | ---
x(?=y) | Positive lookahead, matches x only if it is followed by y | /Reg(?=Ex)/
x(?!y) | Negative lookahead, matches x only if it is not followed by y | /Reg(?!ression)/
(?<=y)x | Positive lookbehind, matches x only if it is preceded by y | /(?<=Reg)Ex/
(?<!y)x | Negative lookbehind, matches x only if it is not preceded by y | /(?<!Fed)Ex/

## Capturing Groups
Syntax | Description | Example
--- | --- | ---
(x) | Capturing group, matches x and remembers the match | /(foo)/
(?<Name>x) | Named capturing group, matches x and remembers the match | /(?<foo>bar)/
(?:x) | Non-capturing group, matches x but does not remember the match | /(?:foo)/
\n | Backreference, matches the results of the nth captured group | /\1(foo)/
|k<Name> | Named backreference, matches the results of the named captured group | /(?<foo>bar)\k<foo>/

## Flags
Syntax | Description | Example
--- | --- | ---
g | Global, match multiple times | /foo/g
i | Case-insensitive, ignore case | /foo/i
m | Multiline, ^ and $ match the start and end of a line, not the whole string
s | Single-line, . matches newline characters

## Assertions
Syntax | Description | Example
--- | --- | ---
x(?=y) | Positive lookahead, matches x only if it is followed by y | /Reg(?=Ex)/
x(?!y) | Negative lookahead, matches x only if it is not followed by y | /Reg(?!ression)/
(?<=y)x | Positive lookbehind, matches x only if it is preceded by y | /(?<=Reg)Ex/
(?<!y)x | Negative lookbehind, matches x only if it is not preceded by y | /(?<!Fed)Ex/

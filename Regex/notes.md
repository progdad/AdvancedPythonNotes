___
___
___

# 1. Literals and symbol classes

___

### `[abc]`
###### Matches any symbol: "a", "b" or "c".

__

### `[^abc]`
###### Any symbol but not "a", "b" or "c".

___

### `.`
###### Any symbol, but not *"\n"*. To include *"\n"*, use `re.DOTALL`.

___

### `\d`  
###### Any digit(in unicode). if `re.ASCII` is set then nothing but: `[0-9]`.

__expression is found

### `\D`
###### Any symbol, but a digit(in unicode). if `re.ASCII` is set, then anything but:`[^0-9]`.

___

### `\s`
###### Any space(in unicode). If `re.ASCII` is set, then only to `[ \t\n\r\f\v]`.

__

### `\S`
###### Any symbol, but a space(in unicode). If `re.ASCII` is set, then anything but: `[^ \t\n\r\f\v]`.

___

### `\w` 
###### Any word symbol: `[a-zA-Z0-9_а-явА-Я]`, etc. If `re.ASCII` is set, then only to `[a-zA-Z0-9_]`.

__

### `\W`
###### Any symbol, but a word symbol from: `[a-zA-Z0-9_а-явА-Я]`, etc. If `re.ASCII` is set, then anything, but: `[^a-zA-Z0-9_]`.

<br>

___
___
___

# 2. Quantifiers

___

### `x{n,m}`
###### `x{n,m}` - Letter *x* is repeated from *n* to *m* times in a row.

__

### `x{n}`
###### Letter *x* is repeated exactly *n* times in a row.

__

### `x{n,}`
###### Letter *x* is repeated not less than *n* times.

__

### `x{,m}`
###### Letter *x* is repeated not more than *m* times.
___

### There are two types of quantifiers: greedy and lazy.
- **Greedy ones are the quantifiers, that embrace everything till the end of a string.**
- **Lazy ones are opposite. These quantifiers embrace the least quantity of symbols. <br>
To make a quantifier lazy, use `?` in the end of a quantifier: <br>
`x{n,m}?`**

___

### *
###### The same as `{0,}`

___

### +
###### The same as `{1,}`

___

### ?
###### The same as `{0,1}`

<br>

___
___
___

# 3. Grouping

___

### Groups are defined by putting expressions in the round brackets

__


### There are two types of groups: capturing and non-capturing.
- **Capturing ones are the groups, that save a content of a group. <br> The syntax is: `(capturing|group)`**
- **Non-capturing are opposite, they simply don't save a content of a group. <br> The syntax is: `(?:non|capturing|group)`**

___

### Each group has its own identifier. 
#### By default, the ids are assigned one by one from "1" to the last group number.
#### That is made so we could use the same group as many times as we need, having the same value, that is inside a group we're reusing.
- For example `"(word1|word2)something\1"` is not the same as `"(word1|word2)something(word1|word2)"`. <br>
In the first case the value of the group is copied after "***something***", so if the value is equal to 
"***word1***" before "***something***", then it will be also "***word1***" after. In the second case, the values before and after "***something***" can be different.

___

### Set ID to a group
#### To define a custom id, write: `(?P<name>word1|word2)`
#### To reuse this group, write: `(?P=name)`

<br>

___
___
___

## 4.1. Flags

___

### `^`
###### The beginning of the whole text. If `re.MULTILINE` is set, then matches to the beginning of a new line.

___

### `$`
###### The end of the whole text. If `re.MULTILINE` is set, then matches to the position before `*\n*` symbol.

___

### `\A`
###### The beginning of the whole text.

___

### `\b`
###### The verge of a word.

___

### `\B`
###### The verge of NOT a word.

___

### `\Z`
###### The end of the whole text.

___

### `(?flags)`
###### `flags` - one ore more flags:
- `a` == `re.ASCII`
- `i` == `re.IGNORECASE`
- `m` == `re.MULTILINE`
- `s` == `re.DOTALL`
- `x` == `re.VERBOSE`

###

___
___

## 4.2 Checks

____

### Look ahead positive `X(?=Y)`
###### Match `X` if `Y` is after `X`.

__

### Look ahead negative  `X(?!Y)`
###### Match `X` if `Y` is NOT after `X`

___

### Look behind positive `(?<=Y)X`
###### Match `X` if `Y` is before `X`.

__

### Look behind negative `(?<!Y)X`
###### Match `X` if `Y` is NOT before `X`

<br>

___
___
___

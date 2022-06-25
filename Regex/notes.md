___
___
___
# Literals and symbol classes
___

### `[abc]`
###### Returns only one symbol: "a", "b" or "c".

__

### `[^abc]`
###### Matches any symbol but not "a", "b" or "c".

___

### `.`
###### Matches any symbol, but not *"\n"*. To include *"\n"*, use `re.DOTALL`.

___

### `\d`  
###### Matches any digit(in unicode). if `re.ASCII` is set then only to `[0-9]`.

__

### `\D`
###### Matches any symbol, but a digit(in unicode). if `re.ASCII` is set then only to `[^0-9]`.

___

### `\s`
###### Matches any space(in unicode). If `re.ASCII` is set, then only to `[ \t\n\r\f\v]`.

__

### `\S`
###### Matches any symbol, but a space(in unicode). If `re.ASCII` is set, then only to `[^ \t\n\r\f\v]`.

___

### `\w` 
###### Matches any word symbol: `[a-zA-Z0-9_а-явА-Я]`, etc. If `re.ASCII` is set, then only to `[a-zA-Z0-9_]`.

__

### `\W`
###### Matches any symbol, but a word symbol: `[a-zA-Z0-9_а-явА-Я]`, etc. If `re.ASCII` is set, then only to `[^a-zA-Z0-9_]`.

<br>

___
___
___

# Quantifiers

___

### `x{n, m}`
###### `x{n, m}` - Letter *x* is repeated from *n* to *m* times in a row.

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

###There are two types of quantifiers: greedy and lazy.
- **Greedy ones are the quantifiers, that embrace everything till the end of a string.**
- **Lazy ones are opposite. These quantifiers embrace the least quantity of symbols. <br>
To make a quantifier lazy, use `?` in the end of a quantifier: <br>
`x{n, m}?`**

___

### *
###### The same as `{0,}`

___

### +
###### The same as `{1,}`

___

### ?
###### The same as `{0,1}`

___
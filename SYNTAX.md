# z^2 syntax
> the syntax of the language

### Comments
`//`: Create a single line comment

`/* ... */`: Create a multi-line comment

### `print()`
`print("<string>/<boolean>/<integer>")`: Prints a String, Integer or Boolean.
* `*args`: String, Integer, Boolean
  * `print(^"{<variable_name>}")`: `^` string - print variable 

### `prompt()`
`prompt("<string>/<variable_name>/<integer>")`: Input a String, variable or integer.
* `*args`: String, variable, integer

### `cprompt()`
`cprompt("<string>/variable_name>/<integer>")`: Input a String, variable or integer without the cursor and text showing.
* `*args`: String, variable, integer

### `var`
`var <variable_name>`: Create a variable
* `= <variable_value>`: Add a value to a variable

### `whatif`
`whatif <variable_name> <operator> <value> {`: If statement
* `<variable_name>`: Variable name
* `<operator>`: An operator (`>`, `<`, `<=`, `>=`, `==`, `!=`, `isin`)
> The operators are pretty self-explanatory.

  * `>`: Greater than
  * `<`: Less than
  * `<=`: Less than or equal to
  * `>=`: Greater than or equal to
  * `==`: Equal to
  * `!=`: Not equal to
  * `isin`: Is inside of
* `<value>`: A value (integer, boolean, float, string)
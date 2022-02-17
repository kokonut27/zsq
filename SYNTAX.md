# z^2 syntax
> the syntax of the language

### Comments
`//`: Create a single line comment

`/* ... */`: Create a multi-line comment

### `print` func.
`print("<string>/<boolean>")`: Prints a String or Boolean.
* `*args`: String, Boolean
  * `print(^"{<variable_name>}")`: `^` string - print variable 

### `prompt` func.
`prompt("<string>/<variable_name>")`: Input a String, or variable.
* `*args`: String, variable

### `var` func.
`var <variable_name>`: Create a variable
* `= <variable_value>`: Add a value to a variable

### `whatif` statement
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
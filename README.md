> **\*\*Version 0.1.0.**

# z^2
> a complex language with high level programming and moderate syntax. 

## Get started
### Usage
1. Clone this repository: 
```
$ git clone https://github.com/JBYT27/zsq.git
```

2. Run z^2

Create a file named `index.zsq`, which will contain all of your code. Then enter the following in the shell:
```
$ cd zsq
$ python main.py
```
Enter the filepath, and now you're done!

### Special Ascii chars
* `\)`: `)`
* `\(`: `(`
* `\n`: `newline`
* `\t`: `tab`
* `\"`: `"`
* `\'`: `'`

### Simple example
> This is a current work in progress as of right now

```
// Defines the Fibonacci function
function Fibonacci(num) { // Creates an arg named num
  whatif num == 0 { // If num equals 0:
    return 0 // Return the value 0
  }
  elseif num == 1 { // Else if the num equals 1:
    return 1 // Return the value 1
  } 
  elseif num == 2 { // Else if the num equals 2:
    return 1 // Return the value 1
  }
  else {
    return Fibonacci(num-1) + Fibonacci(num-2)
  }
}

print(Fibonacci(7))
```

> **\*\*Note that `whatif` statements cannot be compound, if they can have more than one output, such as `if num == 1 or num == 2...`, it must be split in z^2** 

### Contributing
Feel free to contribute by [forking](https://github.com/JBYT27/zsq/network/members) the repo, and leaving a pull request!

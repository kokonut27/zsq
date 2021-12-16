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

### z^2 console
To get started with more features of z^2, enter the following command in the z^2 console:

```
>>> zsq --help
```

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
function Fibonacci(num) {
  whatif num == 0 {
    return 0
  }
	elseif num == 1 {
    return 1
  } 
  elseif num == 2 {
    return 1
  }
	else {
    return Fibonacci(num-1) + Fibonacci(num-2)
  }
}

print(Fibonacci(7))
```

### Contributing
Feel free to contribute by [forking](https://github.com/JBYT27/zsq/network/members) the repo, and leaving a pull request!
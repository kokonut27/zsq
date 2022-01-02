> **\*\*Version 0.1.0.**

# z^2
> a complex language with high level programming and moderate syntax.

## Get started
### Usage
1. Clone this repository: 
```
$ git clone https://github.com/JBYT27/zsq.git
```

2. Add an alias

#### macOS/Linux
Create a `.zshrc` or `.bashrc` files and add the following code:
```zsh
alias zsq="python $HOME/zsq/main.py"
```

#### Windows
Create a `.bashrc` files and add the following code:
```zsh
alias zsq="python $HOME/zsq/main.py"
```

#### Alternative console
An alternative to this is copying the following code, and pasting it into the console:
```
$ alias zsq="python $HOME/zsq/main.py"
```

--- 

3. Run z^2

Create a file named `index.zsq`, which will contain all of your code. Then enter the following in the shell:
```zsh
$ zsq index.zsq
```
Then you're all done!

### Example program
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

### Contributing
Feel free to contribute by [forking](https://github.com/JBYT27/zsq/network/members) the repo, and leaving a pull request!

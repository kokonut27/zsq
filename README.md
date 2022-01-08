> **\*\*Version 0.1.0.**

# z^2
> a complex language with high level programming and moderate syntax.

## Get started
### Usage
1. Clone this repository: 
```zsh
$ git clone https://github.com/JBYT27/zsq.git
```

2. Add an alias

#### macOS/Linux
If you use macOS Catalina or newer, you will use Z-Shell so you will have a `.zshrc` file in your home folder.

Most distributions of Linux use Bash by default, so you will have a `.bashrc` file in your home folder.

*Of course, it is possible to change your shell so you should check before running the command.*

Run the following command. If you use Bash replace `.zshrc` with `.bashrc`:
```zsh
echo "alias zsq='python $HOME/zsq/main.py'" >> .zshrc
```

#### Windows
*You may want to install [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install)*

```zsh
echo "alias zsq='python $HOME/zsq/main.py'" >> .bashrc
```

#### Alternative console
> I suggest this alternative for those who use Replit as their code editor

An alternative to this is copying the following code, and pasting it into the console:
```zsh
$ alias zsq="python $HOME/zsq/main.py"
```
However, whenever your repl is reloaded you will need to re-run the command.

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

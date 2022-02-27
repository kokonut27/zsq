> **\*\*Version 0.1.3.**

[<img src="https://github.com/kokonut27/zsq/blob/main/docs/media/temp_logo.jpeg"/>](https://github.com/kokonut27/zsq)
<br>
[![issues](https://img.shields.io/github/issues/kokonut27/zsq)](https://github.com/kokonut27/zsq/issues)
[![pull requests](https://img.shields.io/github/issues-pr/kokonut27/zsq)](https://github.com/kokonut27/zsq/pulls)
![code size](https://img.shields.io/github/languages/code-size/kokonut27/zsq)
![total lines](https://img.shields.io/tokei/lines/github.com/kokonut27/zsq?color=176606)

# z^2
> a complex language with high level programming and moderate syntax.

## Get started
### Usage
1. Clone this repository: 
```zsh
$ git clone https://github.com/kokonut27/zsq.git
```

2. Add an alias

#### macOS/Linux
If you use macOS Catalina or newer, you will use Z-Shell so you will have a `.zshrc` file in your home folder. Most distributions of Linux use Bash by default, so you will have a `.bashrc` file in your home folder. 
> *Of course, it is possible to change your shell so you should check before running the command.*

Run the following command. If you use Bash replace `.zshrc` with `.bashrc`:
```zsh
echo "alias zsq='python -B zsq'" >> .zshrc
```

#### Windows
*You may want to install [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install)*

```zsh
echo "alias zsq='python -B zsq'" >> .bashrc
```

#### Alternative shell
> I suggest this alternative for those who use Replit as their code editor

An alternative to this is copying the following code, and pasting it into the shell:
```zsh
$ alias zsq="python -B zsq"
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
function Fibonacci(num) { // Creates an arg 'num'
  whatif num <= 1 {
    return(num)
  }
  else {
    return(Fibonacci(num-1) + Fibonacci(num-2))
  }

var ask = prompt("amount of fibonacci sequence? ")

for fib_seq in span(ask) {
  print(Fibonacci(fib_seq))
}
```

Visit [EXAMPLES.md](https://github.com/kokonut27/zsq/tree/main/examples) for more examples.

### Contributing
Feel free to contribute by [forking](https://github.com/kokonut27/zsq/network/members) the repo, and leaving a pull request!

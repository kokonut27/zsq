[<img src="https://github.com/kokonut27/zsq/blob/main/docs/media/temp_logo.jpeg"/>](https://github.com/kokonut27/zsq)
<br>
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/kokonut27/zsq.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/kokonut27/zsq/context:python)
![build](https://github.com/kokonut27/zsq/actions/workflows/format.yml/badge.svg)
[![code size](https://img.shields.io/github/languages/code-size/kokonut27/zsq)](https://github.com/kokonut27/zsq)
[![version](https://img.shields.io/badge/version-0.1.4-orange)](https://github.com/kokonut27/zsq/releases)
 
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

#### Shell
```zsh
$ alias zsq="python -B zsq"
```

<br>

3. Run z^2

Create a file named `index.zsq`, which will contain all of your code. Then enter the following in the shell:
```zsh
$ zsq index.zsq
```
Then you're all done!

### Example program
> This is a current work in progress as of right now

```js
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

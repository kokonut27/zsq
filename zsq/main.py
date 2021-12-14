import time
import os
import sys
import getpass
import re
import string

def zsq_version():
  return "Z^2 v0.1.0"

def helpe(function):
  if function == "help":
    return "Prints helpful information"
  elif function == "run":
    return "Runs a program and/or project"
  elif function == "install":
    return "Installs a package or module"
  elif function == "clear":
    return "Clears the console"
  elif function == "version":
    return "Prints the current version of z^2"
  elif function == "quit":
    return "Quits the program"
  elif function == "credits":
    return "Prints credits"
  else:
    return (bold + red + "no such function exists!" + w)

def console():
  while True:
    cmd = input(">>> ")
    if f"zsq {fp}" in cmd:
        while " " in cmd:
            cmd = cmd.replace(" ", "")
        if cmd == f"zsq{fp}":
            break
    if "zsq run" in cmd:
        while " " in cmd:
            cmd = cmd.replace(" ", "")
        if cmd == "zsqrun":
            break
    if "zsq install popup" in cmd:
        print("installing popup")
        # Add loading and installing.
    elif "zsq help " in cmd:
      cmd = cmd[9:]
      try:
        print(f"{cmd}: "+helpe(cmd))
      except:
        print(bold + red + "no such function exists!" + w)
    elif "zsq clear" in cmd:
        while " " in cmd:
            cmd = cmd.replace(" ", "")
        if cmd == "zsqclear":
            os.system("clear")
            print("Z^2 0.1.0 (default, Dec 13 2021, "+time.strftime("%H:%M:%S")+")")
        else:
            os.system(str(cmd))
    elif "clear" in cmd:
        while " " in cmd:
            cmd = cmd.replace(" ", "")
        if cmd == "clear":
            os.system("clear")
            print("Z^2 0.1.0 (default, Dec 13 2021, "+time.strftime("%H:%M:%S")+")")
        else:
            os.system(str(cmd))
    elif "zsq version" in cmd:
      while " " in cmd:
        cmd = cmd.replace(" ", "")
      if cmd == "zsqversion":
        print(zsq_version())
    elif "zsq -v" in cmd:
      while " " in cmd:
        cmd = cmd.replace(" ", "")
      if cmd == "zsq-v":
        print(zsq_version())
    elif "zsq --version" in cmd:
      while " " in cmd:
        cmd = cmd.replace(" ", "")
      if cmd == "zsq--version":
        print(zsq_version())
    elif "zsq quit" in cmd:
      while " " in cmd:
        cmd = cmd.replace(" ", "")
      if cmd == "zsqquit":
        quit(red + bold + "program has been stopped" + w)
    elif "zsq exit" in cmd:
      while " " in cmd:
        cmd = cmd.replace(" ", "")
      if cmd == "zsqexit":
        quit(red + bold + "program has been stopped" + w)
    elif "zsq help" in cmd:
      while " " in cmd:
        cmd = cmd.replace(" ", "")
      if cmd == "zsqhelp":
        print("zsq\n\nUSAGE:\n\tzsq [SUBCOMMAND]\n\nOPTIONS:\n\t-c, --credits\tPrint credits\n\t-h, --help\tPrint helpful options\n\t-v, --version\tPrint current version of z^2\n\nSUBCOMMANDS:\n\thelp\t\t\t  Print helpful options\n\t[FILENAME].zsq\t  Run program and/or project\n\trun\t\t\t\t  Run program and/or project\n\tinstall [PACKAGE] Install packages or modules\n\tquit\t\t\t  Quit the z^2 console\n\texit\t\t\t  Quit the z^2 console\n\tclear\t\t\t  Clears the console\n\tcredits\t\t\t  Prints credits\n\tversion\t\t\t  Prints current version of Z^2")
    elif "zsq credits" in cmd:
      while " " in cmd:
        cmd = cmd.replace(" ", "")
      if cmd == "zsqcredits":
        print("Credits\n\n\tHead developer\tJBYT27")
    elif "zsq -c" in cmd:
      while " " in cmd:
        cmd = cmd.replace(" ", "")
      if cmd == "zsq-c":
        print("Credits\n\n\tHead developer\tJBYT27")
    elif "zsq --credits" in cmd:
      while " " in cmd:
        cmd = cmd.replace(" ", "")
      if cmd == "zsq--credits":
        print("Credits\n\n\tHead developer\tJBYT27")
    elif "zsq -h" in cmd:
      while " " in cmd:
        cmd = cmd.replace(" ", "")
      if cmd == "zsq-h":
        print("zsq\n\nUSAGE:\n\tzsq [SUBCOMMAND]\n\nOPTIONS:\n\t-c, --credits\tPrint credits\n\t-h, --help\tPrint helpful options\n\t-v, --version\tPrint current version of z^2\n\nSUBCOMMANDS:\n\thelp\t\t\t  Print helpful options\n\t[FILENAME].zsq\t  Run program and/or project\n\trun\t\t\t\t  Run program and/or project\n\tinstall [PACKAGE] Install packages or modules\n\tquit\t\t\t  Quit the z^2 console\n\texit\t\t\t  Quit the z^2 console\n\tclear\t\t\t  Clears the console\n\tcredits\t\t\t  Prints credits\n\tversion\t\t\t  Prints current version of Z^2")
    elif "zsq --help" in cmd:
      while " " in cmd:
        cmd = cmd.replace(" ", "")
      if cmd == "zsq--help":
        print("zsq\n\nUSAGE:\n\tzsq [SUBCOMMAND]\n\nOPTIONS:\n\t-c, --credits\tPrint credits\n\t-h, --help\tPrint helpful options\n\t-v, --version\tPrint current version of z^2\n\nSUBCOMMANDS:\n\thelp\t\t\t  Print helpful options\n\t[FILENAME].zsq\t  Run program and/or project\n\trun\t\t\t\t  Run program and/or project\n\tinstall [PACKAGE] Install packages or modules\n\tquit\t\t\t  Quit the z^2 console\n\texit\t\t\t  Quit the z^2 console\n\tclear\t\t\t  Clears the console\n\tcredits\t\t\t  Prints credits\n\tversion\t\t\t  Prints current version of Z^2")
    else:
        os.system(str(cmd))

red = "\033[0;91m"
w = "\033[0;37m"
black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bblack = "\033[0;90m"
bred = "\033[0;91m"
bgreen = "\033[0;92m"
byellow = "\033[0;93m"
bblue = "\033[0;94m"
bmagenta = "\033[0;95m"
bcyan = "\033[0;96m"
bwhite = "\033[0;97m"
bold = '\033[1m'
end = '\033[0m'
pink = '\033[95m'


#all errors
class InvalidVariableError(Exception):
  pass
class InvalidSyntaxError(Exception):
  pass
class InvalidIndentationError(Exception):
  pass
class InvalidModuleError(Exception):
  pass
class InvalidStringIntError(Exception):
  pass
class nonexistantfilepath(Exception):
  pass
class nonzsqfile(Exception):
  pass


fp = input('filepath: ')

if '.zsq' in fp:
  try:
    f = open(f'{fp}')
  except:
    raise nonexistantfilepath("no such file exists!")
else:
  raise nonzsqfile("the file isn't a '.zsq' file!")

os.system("clear")
print("Z^2 0.1.0 (default, Dec 13 2021, "+time.strftime("%H:%M:%S")+")")


content = f.read()
colist = content.split("\n")
load = 0
for i in colist:
    if i:
        load += 1

console()

num = 0
os.system("clear")
print("Compiling script")
time.sleep(1)
os.system("clear")
while num < load:
    print("Compiling... /")
    time.sleep(0.08)
    os.system("clear")
    print("Compiling... -")
    time.sleep(0.08)
    os.system("clear")
    print("Compiling... \ ")
    time.sleep(0.08)
    os.system("clear")
    num += 1

def check():
    df = re.findall("(?<=[AZaz])?(?!\d*=)[0-9.+-]+", lines)
    df = str(df)

def wait_until(somepredicate, timeout, period=0.25, *args, **kwargs):
    mustend = time.time() + timeout
    while time.time() < mustend:
      if somepredicate(*args, **kwargs): return True
      time.sleep(period)
    return False


allvars = {}
line = 0
read_line=0
PASS = False
getChar1 = "none"
getChar2 = "none"
getChar3 = "none"
var1 = "Undefined variable"
input1 = "Undefined input"
input2 = "Undefined input"
input3 = "Undefined input"
functions = ["print(", "prompt("]

def Print():#add f'string
  try:
    if '")' in lines or "')" in lines:
      wrd = "print("
      res = lines.partition(wrd)[2]
      # print(res)
      if res[-3] == "\"" and res[0] == "\'" or res[-3] == "'" and res[0] == "\"":
        raise InvalidSyntaxError("the 'print' starting quotations and ending quotations are different!")
      else:
        res = res.replace("\")","")
        res = res.replace('\')',"")
        res = res.replace("\\n", "\n")
        res = res.replace("\\t", "\t")
        if "\"" in res:
          split_string = res.split("\")", -1)
        elif "'" in res:
          split_string = res.split("\')", -1)
        else:
          raise InvalidSyntaxError("The 'print' statement is missing quotations!")
        res = split_string[0]
        res = res.replace("\")","")
        res = res.replace('\')',"")
        res = res.replace("\\n", "\n")
        res = res.replace("\\t", "\t")
        #colors: res = res.replace("{red}", red)
        res = res.replace('"', "")
        res = res.replace("'", "")
        res = res.replace(")","")
        # print(res)

        if "{{" in res:
          if "}}" in res:
            start = "{{"
            end = "}}"
            check = res[res.find(start) + len(start):res.rfind(end)]
            if check in allvars:
              res = res.replace("{{", "")
              res = res.replace("}}", "")
              dffdfdfdf = allvars[check]
              res = res.replace(check, str(dffdfdfdf))
            else:
                #print(var)
                #print(res)
              raise InvalidVariableError(f"'{var}' variable does not exist!")
        print(res)
    else:
      raise InvalidSyntaxError("the 'print' statement must have a closing \")\"!")
  except:
    raise InvalidSyntaxError("the 'print' statement must have a closing \")\"!")



newvar = 0
time_module = 0
file = open(fp)
readline2 = 0
for lines in file.readlines():
    #print(lines)

    if readline2 == 1:
      readline2 = 0
      continue
    if "//" in lines:
      readline2=1
    
    line+=1
    lines = lines.replace('\n','')
    lines = lines.replace('\t','')

    #print(lines)
    # print(lines)

    if lines == '': 
      pass
    """
    elif lines in string.whitespace:
      raise InvalidIndentationError("Your indentation does not fit the other statements!")
    elif "/#" in lines:
      wait_until("#/", 0)
      readline2 = 1"""
    if "//" in lines:
      pass
    lines = lines.rstrip()

    # print(lines[:2])

    '''
    elif " " in lines or "\t" in lines or "  " in lines:
      raise InvalidIndentationError(f"line {line}, the indentation does not fit the other statements!")
    '''
    
    if lines[:2] == "//" or "//" in lines:
      pass
      read_line = 0
    elif "import(\"time\")" in lines or "import('time')" in lines:
      time_module = 1
    elif "import(\"os\")" in lines or "import('os')" in lines:
      os_module = 1
    elif "var " in lines:
      wrd = "var "
      newvar = lines.partition(wrd)[2]
      split_string = newvar.split("\")", -1)
      newvar.replace(")","")
      newvar.replace('\"', '')
      newvar = split_string[0]
      #newvar = variable;
      
      if " " in newvar:
        if "=" in newvar:
          idk = []
          Continue = True
          for i in newvar:
            if Continue:
              if i == "=":
                idk.append(i)
                Continue = False
              else:
                idk.append(i)
            else:
              if i == " ":
                idk.append(i)
                break
              else:
                break
          idk = "".join(idk)
          newvar = newvar.replace(idk, "")
            
          if "'" in newvar or "\"" in newvar or "`" in newvar or "os.userinfo(" in newvar:
            if newvar in functions:
              if "print(" in newvar:
                Print()
              
              elif "prompt(" in newvar:
                pass

            else:
              newvar = str(newvar) # makes sure its a string
              if newvar[-1] == "'" and newvar[0] == "'" or newvar[-1] == "\"" and newvar[0] == "\"":
                newvar = newvar.replace(newvar[-1], "")
                #newvar = newvar.replace(newvar[0], "")
              else:
                raise InvalidSyntaxError("starting quotations and end quotations must be the same!")
              allvars[newvar] = newvar
          elif newvar == "true":
            allvars[newvar] = True
          elif newvar == "false":
            allvars[newvar] = False

          else:
            raise InvalidSyntaxError("variables must be named after there is a equal sign!")
        else:
          raise InvalidSyntaxError("variables cannot include spaces!")
      else:
        allvars[newvar] = 0
      
    elif "prompt(" in lines:
      wrd = "prompt("
      var = lines.partition(wrd)[2]
      split_string = var.split(");", -1)
      var.replace(')','')
      var.replace('\"',"")
      var.replace('\'',"")
      var = split_string[0]
      var.strip(")")

      if var in allvars:
        var = input()
        allvars[newvar] = var
      else:
        if var not in allvars:
          raise InvalidVariableError(f"'{var}' variable does not exist!")
        else:
          pass


    elif "print(" in lines:
      # print("e")
      Print()
    
    elif "if " in lines:
      pass

    elif "time.rest(" in lines:
      if time_module == 1:
        wrd = "time.rest("
        res = lines.partition(wrd)[2]
        try:
          res = res.replace(")","")
          for i in res:
            if i in ["1","2","3","4","5","6","7","8","9","0"]:
              time.sleep(int(res))
            else:
              raise InvalidStringIntError("strings cannot be inside integer values!")
        except:
          raise InvalidSyntaxError("an error occurred while trying to time.rest!")
      else:
        raise InvalidModuleError("the 'time' module isn't imported or it doesn't exist!")

    else:
      pass


console()
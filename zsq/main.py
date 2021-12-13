import time, os, sys, getpass, re, string

fp = input('filepath: ')

if '.zsq' in fp:#hmmmm
  try:
    f = open(f'{fp}')
  except:
    raise Exception("no such file exists!")
else:
  raise Exception("the file isn't a '.zsq' file!")

content = f.read()
colist = content.split("\n")

def check():
    df = re.findall("(?<=[AZaz])?(?!\d*=)[0-9.+-]+", lines)
    df = str(df)

def wait_until(somepredicate, timeout, period=0.25, *args, **kwargs):
    mustend = time.time() + timeout
    while time.time() < mustend:
      if somepredicate(*args, **kwargs): return True
      time.sleep(period)
    return False

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
class TemplateError(Exception):
  pass


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
        raise InvalidSyntaxError("the 'print starting quotations and ending quotations are different!")
      else:
        res = res.replace("\")","")
        res = res.replace('\')',"")
        res = res.replace("\n", "\n")
        res = res.replace("\t", "\t")
        if "\"" in res:
          split_string = res.split("\")", -1)
        elif "'" in res:
          split_string = res.split("\')", -1)
        else:
          raise InvalidSyntaxError("The 'print' statement is missing quotations!")
        res = split_string[0]
        res = res.replace("\")","")
        res = res.replace('\')',"")
        res = res.replace("\n", "\n")
        res = res.replace("\t", "\t")
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

    """if "/*" in lines:
      readline2=1
      #print(wait_until("*/", 0))
      wait_until("*/", 0)"""
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
                e

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
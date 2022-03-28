import time
import os
import sys
import getpass
import re
import click
import pymongo
from info import *

try:
  os.system('pip install dnspython')
except:
  print("could not download dnspython - try again later")
  exit()


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


      
# file errors
class nonexistantfilepath(Exception):
  pass
class nonzsqfile(Exception):
  pass


# db :pensive:
class database():
  def __init__(self):
    self.client = pymongo.MongoClient(os.getenv("connection_string"))
  
    return self.client["collection_all_db"]
  
  def create_database(self, db_name):
    db = database()
    collection = db[db_name]
    self.collection = collection
    return
  
  def insert_in(self, item_name, *content):
    if "{" not in content:
      raise Exception("'content' args must be a dict!")

    content = dict(content)
    content["_id"] = "COL" + # use database to keep track of collection number
    
    self.collection.insert_one(content)
    
    return 
    

@click.command()
@click.argument("fp", default="index.zsq")
def filepath(fp):
  global PASS
  
  if '.zsq' in fp:
    try:
      f = open(f'{fp}')
    except:
      raise nonexistantfilepath("no such file exists!")
  else:
    raise nonzsqfile("the file isn't a '.zsq' file!")

  content = f.read()
  colist = content.split("\n")
  # console is cleared here
  os.system("clear")
  
  
  def check():
    df = re.findall("(?<=[AZaz])?(?!\d*=)[0-9.+-]+", lines)
    df = str(df)
        
  
  allvars = {}
  what_if = {}
  all_packages = ["os", "time", "math", "color"]
  correct_syntax = False
  line = 0
  read_line = 0
  PASS = False
  functions = ["print(", "prompt(", "time.time(", "time.rest(", "time.curtime(", "version("]
  
  def error(the_error):
    print(red + bold + f'line {line}: {code}\n{the_error}' + w)
  
  def timeTime():
    if time_module == 1:
      wrd = "time.time("
      res = lines.partition(wrd)[2]
      try:
        res = res.replace(")", "")

        if "}" in res:
          return time.time()
        error("no arguments must be made inside of the function time.time!")
        exit()
      except:
        error("an error occurred while trying to time.time!")
        exit()
    else:
      error("the 'time' module isn't imported or it doesn't exist!")
      exit()

  def timeCurtime():
    if time_module == 1:
      wrd = "time.curtime("
      res = lines.partition(wrd)[2]
      try:
        res = res.replace(")", "")

        if res in ["", " "]:
          error("time argument must be made inside of the function time.curtime!")
        elif "}" in res:
          return None
        else:
          error("no arguments must be made inside of the function time.curtime!")
        exit()
      except:
        error("an error occurred while trying to time.curtime!")
        exit()
    else:
      error("the 'time' module isn't imported or it doesn't exist!")
      exit()

  def osSystem():
    if os_module == 1:
      wrd = "os.system("
      res = lines.partition(wrd)[2]
      try:
        res = res.replace(")", "")

        print(res)
      except:
        error("an error occurred while trying to os.system!")
        exit()
    else:
      error("the 'os' module isn't imported or it doesn't exist!")
      exit()
  
  def Print():
    global PASS
    #try:
    if '")' in lines or "')" in lines or ")" in lines:
      wrd = "print("
      res = lines.partition(wrd)[2]
      res2 = lines.partition(wrd)[2]
      if res[-3] == "\"" and res[0] == "\'" or res[-3] == "'" and res[0] == "\"":
        error("the 'print' starting quotations and ending quotations are different!")
        exit()
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
          for i in functions:
            if i not in res2:
              error("the 'print' function is missing quotations!")
              exit()

        res = split_string[0]

        sq_str = res[0] == "^"
        res = res.replace("\")","")
        res = res.replace('\')',"")
        res = res.replace("\\n", "\n")
        res = res.replace("\\t", "\t")
        res = res.replace("\\)", ")")
        res = res.replace("\\(", "(")
        res = res.replace('\\"', '"')
        res = res.replace("\\'", "'")
        if color_module == 1:
          res = res.replace("{color.red}", red)
          res = res.replace("{color.blue}", blue)
          res = res.replace("{color.yellow}", yellow)
          res = res.replace("{color.green}", green)
          res = res.replace("{color.purple}", magenta)
          res = res.replace("{color.cyan}", cyan)
          res = res.replace("{color.white}", white)
          res = res.replace("{color.reset}", w)
        elif "{color.red}" in res or "{color.blue}" in res or "{color.yellow}" in res or "{color.green}" in res or "{color.purple}" in res or "{color.cyan}" in res or "{color.white}" in res or "{color.reset}" in res:
          if color_module == 1:
            error("the 'color' module isn't imported or doesn't exist!")
            exit()
        res = res.replace('"', "")
        res = res.replace("'", "")
        if sq_str and "{" in res and "}" in res:
          start = "{"
          end = "}"
          check = res[res.find(start) + len(start):res.rfind(end)]
          # print(res)
          PASS = False
          # print(check)
          # print(allvars)
          if check in allvars:
            # print(check)
            res = res.replace("{", "")
            res = res.replace("}", "")
            dffdfdfdf = allvars[check]

            # print(allvars[check])
            # print(check)

            # print(res)
            res = res.replace(check, str(dffdfdfdf))
          elif "version(" in check:
            wrd = "version("
            res = lines.partition(wrd)[2]
            res = res.replace(")", "")
            if "}" not in res:
              error("'version()' function argument must be empty!")
              exit()
            print(f'z^2 version {Version}')

            PASS = True
          elif "time.time(" in check:
            # print(check)
            # print(res)
            timeTime()
            res = res.replace("{", "")
            res = res.replace("}", "")
            print(time.time())
            PASS = True
          elif "time.curtime(" in check:
            # print(PASS)
            # print(check)
            # print(res)
            timeCurtime()
            wrd = "time.curtime("
            # res = lines.partition(wrd)[2]

            res = res.replace("{", "")
            res = res.replace("}", "")
            res = res.replace("$YEAR", "%Y")
            res = res.replace("$MONTH", "%m")
            res = res.replace("$DAY", "%d")
            res = res.replace("$HOUR", "$H")
            res = res.replace("$MIN", "%M")
            res = res.replace("$SEC", "%S")
            # res = res.replace("$MISEC", "%f")
            parent = res.find("(")
            if parent != -1:
              a = int(parent)-1
              if res[a] == "e":
                res = res[parent+1:]
            print(time.strftime(res))
            # print(res)
            PASS = True
          else:
            error(f"'{varname}' variable does not exist!")
            exit()
        if not PASS:
          res = res.replace("^", "")
          print(res, end="")
          print()
    else:
      error("the 'print' statement must have a closing \")\"!")
      exit()
    #except:
      #print(bold + red + "the 'print' statement must have a closing \")\"!" + w)
      #exit()
  
  
  newvar = 0
  time_module = 0
  os_module = 0
  color_module = 0
  math_module = 0
  file = open(fp)
  readline2 = 0
  print(f"{yellow}{bold}>{w} zsq {fp}")
  for lines in file.readlines():
      line+=1
      if readline2 == 1:
        readline2 = 0
        continue
      # if "//" in lines:
      #   readline2=1
      
      lines = lines.replace('\n','')
      lines = lines.replace('\t','')
      code = lines
  
      #print(lines)
      # print(lines)
  
      if lines == '': 
        pass
      if "/*" in lines:
        Pass = True
        continue

      try:
        if "*/" in lines and Pass:
          continue
      except:
        error(f"{lines} is not defined!")
        exit()
      lines = lines.rstrip()
  
      # print(lines[:2])
      
      if lines[:2] == "//":
        continue
      elif "//" in lines:
          e = lines.find("//")
          if e != -1:
            lines = lines[:e]
      elif "/*" in lines:
        Pass = True
        continue

      elif "*/" in lines and Pass:
        continue
          
      if "import(\"time\")" in lines or "import('time')" in lines:
        time_module = 1
      if "import(\"os\")" in lines or "import('os')" in lines:
        os_module = 1
      if "import(\"math\")" in lines or "import('os')" in lines:
        math_module = 1
      if "import(\"color\")" in lines or "import('color')" in lines:
        color_module = 1

      elif "import(" in lines:
        wrd = "import("
        module = lines.partition(wrd)[2]
        try:
          split_string = module.split("\")", -1)
        except:
          split_string = newvar.split("')", -1)
        module = split_string[0]

        module = module.replace('"', '')
        module = module.replace("'", "")

        # print(module)

        if module in all_packages:
          pass
        else:
          error(f"'{module}' package does not exist!")
          exit()
  
      elif "var " in lines:
        wrd = "var "
        newvar = lines.partition(wrd)[2]
        split_string = newvar.split("\")", -1)
        newvar.replace(")","")
        newvar.replace('\"', '')
        newvar = split_string[0]

        # print(newvar)
        
        if " " in newvar:
          find_space = newvar.find("\"")
          if find_space == -1:
            find_space1 = newvar.find("\'")
            if find_space1 == -1:
              # print("hello")
              if "1" in newvar:
                newvar_type = int
                # print("hello")
              elif "2" in newvar:
                newvar_type = int
              elif "3" in newvar:
                newvar_type = int
              elif "4" in newvar:
                newvar_type = int
              elif "5" in newvar:
                newvar_type = int
              elif "6" in newvar:
                newvar_type = int
              elif "7" in newvar:
                newvar_type = int
              elif "8" in newvar:
                newvar_type = int
              elif "9" in newvar:
                newvar_type = int
              elif "0" in newvar:
                newvar_type = int
              else:
                if "true" in newvar or "false" in newvar:
                  newvar_type = bool
                else:
                  error("variables must be named!")
                  exit()
            else:
              newvar_type = str
          else:
            newvar_type = str
          if find_space != -1:
            newvar2 = newvar[find_space:]
          else:
            if find_space1 != -1:
              newvar2 = newvar[find_space:]
            else:
              if newvar_type == int or newvar_type == bool or newvar_type == float:
                a = newvar.find("=")
                if a != -1:
                  hm = newvar[a:]
                  hm = hm.replace(" ", "")
                  
                  # print(newvar)
                  # print(hm)
                else:
                  error("there was an error with encountering the variable! try again!")
                  exit()
              else:
                error("there was an error with encountering the variable! try again!")
                exit()
          
          newvar2 = newvar2.replace(" ", "")
          
          e = newvar.find("=")
          if e != -1:
            varname = newvar[:e]
            varname = varname.replace(" ", "")
            VALUE = newvar[e:]
            
          # print(newvar)
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
            FUNC = False
  
            for f in functions:
              if f in newvar:
                FUNC = True
                if "print(" in newvar:
                  Print()
                elif "prompt(" in newvar:
                  global value
                  
                  wrd = "prompt("
                  var = lines.partition(wrd)[2]
                  split_string = var.split(")", -1)
                  var = var.replace(')','')
                  var = var.replace('\"',"")
                  var = var.replace('\'',"")
                  var = var.replace("\\n", "\n")
                  var = var.replace("\\t", "\t")
                  var = var.replace("\\)", ")")
                  var = var.replace("\\(", "(")
                  var = var.replace('\\"', '"')
                  var = var.replace("\\'", "'")
                  # var = var = split_string[0]
                  # var = var.strip(")")
                  
                  value = input(var)
                  allvars[varname] = value
                  
                  FUNC = True
                elif "cprompt(" in newvar:
                  wrd = "prompt("
                  var = lines.partition(wrd)[2]
                  split_string = var.split(")", -1)
                  var = var.replace(')','')
                  var = var.replace('\"',"")
                  var = var.replace('\'',"")
                  var = var.replace("\\n", "\n")
                  var = var.replace("\\t", "\t")
                  var = var.replace("\\)", ")")
                  var = var.replace("\\(", "(")
                  var = var.replace('\\"', '"')
                  var = var.replace("\\'", "'")
                  # var = var = split_string[0]
                  # var = var.strip(")")
                  
                  value = getpass.getpass(prompt=var, stream=None)
                  allvars[varname] = value
                  
                  FUNC = True
  
            
            if "'" in newvar or "\"" in newvar:
                already = False
                if FUNC != True:
                  if newvar[-1] == "'" and newvar[0] == "'" or newvar[-1] == "\"" and newvar[0] == "\"":
                    newvar = newvar.replace(newvar[-1], "")
                    allvars[varname] = newvar
                    already = True
                  else:
                    if FUNC == True:
                      pass
                    else:
                      error("starting quotations and end quotations must be the same!")
                      exit()
                if already:
                  pass
                else:
                  if newvar[-1] == "'" and newvar[0] == "'" or newvar[-1] == "\"" and newvar[0] == "\"":
                    newvar = newvar.replace(newvar[-1], "")
                    #newvar = newvar.replace(newvar[0], "")
                  else:
                    if FUNC == True:
                      pass
                    else:
                      error("starting quotations and end quotations must be the same!")
                      exit()
            elif newvar == "true":
              allvars[varname] = "true"
            elif newvar == "false":
              allvars[varname] = "false"
            elif newvar_type == int:
              allvars[varname] = int(newvar)
              # print("ayo")
              # print(allvars[varname])
            else:
              error("variables must be named after there is a equal sign!")
              exit()
          else:
            try:
              if FUNC:
                pass
            except:
              error("variables cannot include spaces!")
              exit()
        
      elif "prompt(" in lines:
        wrd = "prompt("
        var = lines.partition(wrd)[2]
        split_string = var.split(")", -1)
        var = var.replace(')','')
        var = var.replace('\"',"")
        var = var.replace('\'',"")
        var = var.replace("\\n", "\n")
        var = var.replace("\\t", "\t")
        var = var.replace("\\)", ")")
        var = var.replace("\\(", "(")
        var = var.replace('\\"', '"')
        var = var.replace("\\'", "'")
        # var = var = split_string[0]
        # var = var.strip(")")
        
        input(var)

      elif "cprompt(" in lines:
        wrd = "cprompt("
        var = lines.partition(wrd)[2]
        split_string = var.split(")", -1)
        var = var.replace(')','')
        var = var.replace('\"',"")
        var = var.replace('\'',"")
        var = var.replace("\\n", "\n")
        var = var.replace("\\t", "\t")
        var = var.replace("\\)", ")")
        var = var.replace("\\(", "(")
        var = var.replace('\\"', '"')
        var = var.replace("\\'", "'")

        getpass.getpass(prompt=var, stream=None)
        
  
      elif "print(" in lines:
        Print()
      
      elif "whatif " in lines:
        wrd = "whatif "
        res = lines.partition(wrd)[2]
        symbols = ["!=", "==", "isin", ">=", "<=", ">", "<"]
        
        if symbols[0] in res:
          a = res.find(symbols[0])
          if a != -1: # a double check 
            vare = res[:a]
          vare = vare.replace(" ", "")
          try:
            var = allvars[vare]
          except:
            error(f"'{vare}' variable does not exist!")
            exit()
          vale = res[a+2:]

          # print(vale)
          # print(vare)
          
          e = vale.find("\"")
          if e == -1:
            e = vale.find("'")
            if e == -1:
              if "true" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")
                if vale == "true":
                  # vale = True

                  if var == "true":
                    what_if[vare] = False
                  else:
                    what_if[vare] = True
              elif "false" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")
                if vale == "false":
                  # vale = True

                  if var == "false":
                    what_if[vare] = False
                  else:
                    what_if[vare] = True
                # elif "string" in vale:
              elif "bool" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")

                if vale == "bool":
                  if var == "true" or var == "false":
                    what_if[vare] = False
                  else:
                    what_if[vare] = True
              elif "integer" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")

                if vale == "integer":
                  if var == int:
                    what_if[vare] = False
                  else:
                    what_if[vare] = True
                
              elif "float" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")

                if vale == "float":
                  if var == float:
                    what_if[vare] = False
                  else:
                    what_if[vare] = True

              elif 1 in vale or 2 in vale or 3 in vale or 4 in vale or 5 in vale or 6 in vale or 7 in vale or 8 in vale or 9 in vale or 0 in vale:
                if var != vale:
                  what_if[vare] = True
                else:
                  what_if[vare] = False

              else:
                error(f"'{vale}' is undefined!")
                exit()
                
            else:
              vale = vale[e+1:]
              b = vale.find("'")
              vale = vale[:b]
              vale = vale.replace("'", "")
              vale = vale.replace("\"", "")
              vale = vale.replace("'", "")
              vale = vale.replace("\\n", "\n")
              vale = vale.replace("\\t", "\t")
              vale = vale.replace("\\'", "'")
              vale = vale.replace('\\"', "")
              
              if var == str(vale):
                what_if[vare] = False
              else:
                what_if[vare] = True
              
          else:
            vale = vale[e+1:]
            b = vale.find('"')
            vale = vale[:b]
            vale = vale.replace("'", "")
            vale = vale.replace("\"", "")
            vale = vale.replace('"', "")
            vale = vale.replace("\\n", "\n")
            vale = vale.replace("\\t", "\t")
            vale = vale.replace("\\'", "'")
            vale = vale.replace('\\"', "")
            
            if var == str(vale):
              what_if[vare] = False
            else:
              what_if[vare] = True
              
          continue

        
        elif symbols[1] in res:
          a = res.find(symbols[1])
          if a != -1: # a double check 
            vare = res[:a]
          vare = vare.replace(" ", "")
          try:
            var = allvars[vare]
          except:
            error(f"'{vare}' variable does not exist!")
            exit()
          vale = res[a+2:]

          # print(vale)
          # print(vare)
          
          e = vale.find("\"")
          if e == -1:
            e = vale.find("'")
            if e == -1:
              if "true" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")
                if vale == "true":
                  # vale = True

                  if var == "true":
                    what_if[vare] = True
                  else:
                    what_if[vare] = False
              elif "false" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")
                if vale == "false":
                  # vale = True

                  if var == "false":
                    what_if[vare] = False
                  else:
                    what_if[vare] = True
                # elif "string" in vale:
              elif "bool" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")

                if vale == "bool":
                  if var == "true" or var == "false":
                    what_if[vare] = True
                  else:
                    what_if[vare] = False
              elif "integer" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")

                if vale == "integer":
                  if var == int:
                    what_if[vare] = True
                  else:
                    what_if[vare] = False
                
              elif "float" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")

                if vale == "float":
                  if var == float:
                    what_if[vare] = True
                  else:
                    what_if[vare] = False

              elif 1 in vale or 2 in vale or 3 in vale or 4 in vale or 5 in vale or 6 in vale or 7 in vale or 8 in vale or 9 in vale or 0 in vale:
                if var == vale:
                  what_if[vare] = True
                else:
                  what_if[vare] = False

              else:
                error(f"'{vale}' is undefined!")
                exit()
                
            else:
              vale = vale[e+1:]
              b = vale.find("'")
              vale = vale[:b]
              vale = vale.replace("'", "")
              vale = vale.replace("\"", "")
              vale = vale.replace("'", "")
              vale = vale.replace("\\n", "\n")
              vale = vale.replace("\\t", "\t")
              vale = vale.replace("\\'", "'")
              vale = vale.replace('\\"', "")
              
              if var == str(vale):
                what_if[vare] = True
              else:
                what_if[vare] = False
              
          else:
            vale = vale[e+1:]
            b = vale.find('"')
            vale = vale[:b]
            vale = vale.replace("'", "")
            vale = vale.replace("\"", "")
            vale = vale.replace('"', "")
            vale = vale.replace("\\n", "\n")
            vale = vale.replace("\\t", "\t")
            vale = vale.replace("\\'", "'")
            vale = vale.replace('\\"', "")
            
            if var == str(vale):
              what_if[vare] = True
            else:
              what_if[vare] = False

          continue

        elif symbols[2] in res:
          a = res.find(symbols[2])
          if a != -1: # a double check 
            vare = res[:a]
          vare = vare.replace(" ", "")
          try:
            var = allvars[vare]
          except:
            error(f"'{vare}' variable does not exist!")
            exit()
          vale = res[a+2:]

          # print(vale)
          # print(vare)
          
          e = vale.find("\"")
          if e == -1:
            e = vale.find("'")
            if e == -1:
              if "true" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")
                if vale == "true":
                  error("variables cannot be in a boolean!")
                  exit()
              elif "false" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")
                if vale == "false":
                  # vale = True
                  error("variables cannot be in a boolean!")
                  exit()
              elif "bool" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")

                if vale == "bool":
                  error("variables cannot be in a boolean!")
                  exit()
              elif "integer" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")

                if vale == "integer":
                  error("variables cannot be in the classifier 'integer'!")
                  exit()
                
              elif "float" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")

                if vale == "float":
                  error("variables cannot be in the classifier 'float'!")
                  exit()

              elif 1 in vale or 2 in vale or 3 in vale or 4 in vale or 5 in vale or 6 in vale or 7 in vale or 8 in vale or 9 in vale or 0 in vale:
                if var in vale:
                  what_if[vare] = True
                else:
                  what_if[vare] = False

              else:
                error(f"'{vale}' is undefined!")
                exit()
                
            else:
              vale = vale[e+1:]
              b = vale.find("'")
              vale = vale[:b]
              vale = vale.replace("'", "")
              vale = vale.replace("\"", "")
              vale = vale.replace("'", "")
              vale = vale.replace("\\n", "\n")
              vale = vale.replace("\\t", "\t")
              vale = vale.replace("\\'", "'")
              vale = vale.replace('\\"', "")
              
              if var in str(vale):
                what_if[vare] = True
              else:
                what_if[vare] = False
              
          else:
            vale = vale[e+1:]
            b = vale.find('"')
            vale = vale[:b]
            vale = vale.replace("'", "")
            vale = vale.replace("\"", "")
            vale = vale.replace('"', "")
            vale = vale.replace("\\n", "\n")
            vale = vale.replace("\\t", "\t")
            vale = vale.replace("\\'", "'")
            vale = vale.replace('\\"', "")
            
            if var in str(vale):
              what_if[vare] = True
            else:
              what_if[vare] = False

          continue

        elif symbols[3] in res:
          a = res.find(symbols[3])
          if a != -1: # a double check 
            vare = res[:a]
          vare = vare.replace(" ", "")
          try:
            var = allvars[vare]
          except:
            error(f"'{vare}' variable does not exist!")
            exit()
          vale = res[a+2:]

          # print(vale)
          # print(vare)
          
          e = vale.find("\"")
          if e == -1:
            e = vale.find("'")
            if e == -1:
              if "true" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")
                if vale == "true":
                  error("variables cannot be greater or less than a boolean!")
                  exit()
              elif "false" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")
                if vale == "false":
                  error("variables cannot be greater or less than a boolean!")
                  exit()
                # elif "string" in vale:
              elif "bool" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")

                if vale == "bool":
                  error("variables cannot be greater or less than a boolean!")
                  exit()
              elif "integer" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")

                if vale == "integer":
                  error("variables cannot be greater or less than the classifier 'integer'!")
                  exit()
                
              elif "float" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")

                if vale == "float":
                  error("variables cannot be greater or less than the classifier 'float'!")
                  exit()

              elif 1 in vale or 2 in vale or 3 in vale or 4 in vale or 5 in vale or 6 in vale or 7 in vale or 8 in vale or 9 in vale or 0 in vale:
                if var >= vale:
                  what_if[vare] = True
                else:
                  what_if[vare] = False

              else:
                error(f"'{vale}' is undefined!")
                exit()
                
            else:
              vale = vale[e+1:]
              b = vale.find("'")
              vale = vale[:b]
              vale = vale.replace("'", "")
              vale = vale.replace("\"", "")
              vale = vale.replace("'", "")
              vale = vale.replace("\\n", "\n")
              vale = vale.replace("\\t", "\t")
              vale = vale.replace("\\'", "'")
              vale = vale.replace('\\"', "")
              
              error("variables cannot be greater than or equal to a string!")
              exit()
              
          else:
            vale = vale[e+1:]
            b = vale.find('"')
            vale = vale[:b]
            vale = vale.replace("'", "")
            vale = vale.replace("\"", "")
            vale = vale.replace('"', "")
            vale = vale.replace("\\n", "\n")
            vale = vale.replace("\\t", "\t")
            vale = vale.replace("\\'", "'")
            vale = vale.replace('\\"', "")
            
            error("variables cannot be greater than or equal to a string!")
            exit()
              
          continue

        elif symbols[4] in res:
          a = res.find(symbols[4])
          if a != -1: # a double check 
            vare = res[:a]
          vare = vare.replace(" ", "")
          try:
            var = allvars[vare]
          except:
            error(f"'{vare}' variable does not exist!")
            exit()
          vale = res[a+2:]

          # print(vale)
          # print(vare)
          
          e = vale.find("\"")
          if e == -1:
            e = vale.find("'")
            if e == -1:
              if "true" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")
                
                if vale == "true":
                  error("variables cannot be less than or equal to a boolean!")
                  exit()
              elif "false" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")
                
                if vale == "false":
                  error("variables cannot be less than or equal to a boolean!")
                  exit()
                # elif "string" in vale:
              elif "bool" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")

                if vale == "bool":
                  error("variables cannot be less than or equal to a boolean!")
                  exit()
              elif "integer" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")

                if vale == "integer":
                  error("variables cannot be less than or equal to the classifier 'integer'!")
                  exit()
                
              elif "float" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")

                if vale == "float":
                  error("variables cannot be less than or equal to the classifier 'float'!")
                  exit()

              elif 1 in vale or 2 in vale or 3 in vale or 4 in vale or 5 in vale or 6 in vale or 7 in vale or 8 in vale or 9 in vale or 0 in vale:
                if var <= vale:
                  what_if[vare] = True
                else:
                  what_if[vare] = False

              else:
                error(f"'{vale}' is undefined!")
                exit()
                
            else:
              vale = vale[e+1:]
              b = vale.find("'")
              vale = vale[:b]
              vale = vale.replace("'", "")
              vale = vale.replace("\"", "")
              vale = vale.replace("'", "")
              vale = vale.replace("\\n", "\n")
              vale = vale.replace("\\t", "\t")
              vale = vale.replace("\\'", "'")
              vale = vale.replace('\\"', "")
              
              error("variables cannot be less than or equal to a string!")
              exit()
              
          else:
            vale = vale[e+1:]
            b = vale.find('"')
            vale = vale[:b]
            vale = vale.replace("'", "")
            vale = vale.replace("\"", "")
            vale = vale.replace('"', "")
            vale = vale.replace("\\n", "\n")
            vale = vale.replace("\\t", "\t")
            vale = vale.replace("\\'", "'")
            vale = vale.replace('\\"', "")
            
            error("variables cannot be less than or equal to a string!")
            exit()

          continue

        elif symbols[5] in res:
          a = res.find(symbols[5])
          if a != -1: # a double check 
            vare = res[:a]
          vare = vare.replace(" ", "")
          try:
            var = allvars[vare]
          except:
            error(f"'{vare}' variable does not exist!")
            exit()
          vale = res[a+2:]

          # print(vale)
          # print(vare)
          
          e = vale.find("\"")
          if e == -1:
            e = vale.find("'")
            if e == -1:
              if "true" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")
                
                if vale == "true":
                  error("variables cannot be greater or less than a boolean!")
                  exit()
              elif "false" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")
                
                if vale == "false":
                  error("variables cannot be greater or less than a boolean!")
                  exit()
                # elif "string" in vale:
              elif "bool" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")

                if vale == "bool":
                  error("variables cannot be greater or less than a boolean!")
                  exit()
              elif "integer" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")

                if vale == "integer":
                  error("variables cannot be greater or less than the classifier 'integer'!")
                  exit()
                
              elif "float" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")

                if vale == "float":
                  error("variables cannot be greater or less than the classifier 'float'!")
                  exit()

              elif 1 in vale or 2 in vale or 3 in vale or 4 in vale or 5 in vale or 6 in vale or 7 in vale or 8 in vale or 9 in vale or 0 in vale:
                if var < vale:
                  what_if[vare] = True
                else:
                  what_if[vare] = False

              else:
                error(f"'{vale}' is undefined!")
                exit()
                
            else:
              vale = vale[e+1:]
              b = vale.find("'")
              vale = vale[:b]
              vale = vale.replace("'", "")
              vale = vale.replace("\"", "")
              vale = vale.replace("'", "")
              vale = vale.replace("\\n", "\n")
              vale = vale.replace("\\t", "\t")
              vale = vale.replace("\\'", "'")
              vale = vale.replace('\\"', "")
              
              error("variables cannot be less than a string!")
              exit()

              
          else:
            vale = vale[e+1:]
            b = vale.find('"')
            vale = vale[:b]
            vale = vale.replace("'", "")
            vale = vale.replace("\"", "")
            vale = vale.replace('"', "")
            vale = vale.replace("\\n", "\n")
            vale = vale.replace("\\t", "\t")
            vale = vale.replace("\\'", "'")
            vale = vale.replace('\\"', "")
            
            error("variables cannot be less than a string!")
            exit()

          continue

        elif symbols[6] in res:
          a = res.find(symbols[6])
          if a != -1: # a double check 
            vare = res[:a]
          vare = vare.replace(" ", "")
          try:
            var = allvars[vare]
          except:
            error(f"'{vare}' variable does not exist!")
            exit()
          vale = res[a+2:]

          # print(vale)
          # print(vare)
          
          e = vale.find("\"")
          if e == -1:
            e = vale.find("'")
            if e == -1:
              if "true" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")
                
                if vale == "true":
                  error("variables cannot be greater or less than a boolean!")
                  exit()
              elif "false" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")
                
                if vale == "false":
                  error("variables cannot be greater or less than a boolean!")
                  exit()
                # elif "string" in vale:
              elif "bool" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")

                if vale == "bool":
                  error("variables cannot be greater or less than a boolean!")
                  exit()
              elif "integer" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")

                if vale == "integer":
                  error("variables cannot be greater or less than the classifier 'integer'!")
                  exit()
                
              elif "float" in vale:
                vale = vale.replace(" ", "")
                vale = vale.replace("{", "")

                if vale == "float":
                  error("variables cannot be greater or less than the classifier 'float'!")
                  exit()

              elif 1 in vale or 2 in vale or 3 in vale or 4 in vale or 5 in vale or 6 in vale or 7 in vale or 8 in vale or 9 in vale or 0 in vale:
                if var > vale:
                  what_if[vare] = True
                else:
                  what_if[vare] = False

              else:
                error(f"'{vale}' is undefined!")
                exit()
                
            else:
              vale = vale[e+1:]
              b = vale.find("'")
              vale = vale[:b]
              vale = vale.replace("'", "")
              vale = vale.replace("\"", "")
              vale = vale.replace("'", "")
              vale = vale.replace("\\n", "\n")
              vale = vale.replace("\\t", "\t")
              vale = vale.replace("\\'", "'")
              vale = vale.replace('\\"', "")
              
              error("variables cannot be greater than a string!")
              exit()
              
          else:
            vale = vale[e+1:]
            b = vale.find('"')
            vale = vale[:b]
            vale = vale.replace("'", "")
            vale = vale.replace("\"", "")
            vale = vale.replace('"', "")
            vale = vale.replace("\\n", "\n")
            vale = vale.replace("\\t", "\t")
            vale = vale.replace("\\'", "'")
            vale = vale.replace('\\"', "")
            
            error("variables cannot be greater than a string!")
            exit()

          continue

        else:
          error("'whatif' statement must have an operator!")
          exit()

      elif lines:
        """
        if what_if[vare] == True:
          pass
        else:
          continue
        """
        pass

      elif "}" in lines:
        correct_syntax = True
        continue

      elif "elseif " in lines:
        if correct_syntax:
          wrd = "elseif "
          res = lines.partition(wrd)[2]
          symbols = ["!=", "==", "isin", ">=", "<=", ">", "<"]
        else:
          error("'whatif' statement must have an ending '}'!")
          exit()
        

      elif "version(" in lines:
        wrd = "version("
        res = lines.partition(wrd)[2]
        res = res.replace(")", "")
        if res != "" or res != " ":
          error("'version()' function argument must be empty!")
          exit()

      elif "os.system(" in lines:
        # print("gello")
        if os_module == 1:
          osSystem()
        else:
          error("the 'os' module isn't imported or it doesn't exist!")
          exit()
  
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
                error("strings cannot be inside integer values!")
                exit()
          except:
            error("an error occurred while trying to time.rest!")
            exit()
        else:
          error("the 'time' module isn't imported or it doesn't exist!")
          exit()
      elif "time.time(" in lines:
        if time_module == 1:
          pass
        else:
          error("the 'time' module isn't imported or it doesn't exist!")
          exit()
      elif "time.curtime(" in lines:
        if time_module == 1:
          pass
        else:
          error("the 'time' module isn't imported or it doesn't exist!")
          exit()
  
      else:
        # print(lines)
        if lines == "" or lines == " " or lines == "  " or lines == "\n":
          pass
        else:
          for char in lines:
            for funcs in functions:
              if char != funcs: # add more args like "and if ..."
                error(f"{lines} is not defined!")
                exit()


if __name__ == "__main__":
  db = database()

  
  
  filepath()
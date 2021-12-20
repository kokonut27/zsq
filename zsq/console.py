def zsq_version():
  return "z^2 v0.1.0"

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
    elif "clear" in cmd:
        while " " in cmd:
            cmd = cmd.replace(" ", "")
        if cmd == "clear":
            os.system("clear")
            print("Z^2 0.1.0 (default, Dec 13 2021, "+time.strftime("%H:%M:%S")+")")
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
        print("zsq\n\nUSAGE:\n\tzsq [SUBCOMMAND]\n\nOPTIONS:\n\t-c, --credits\tPrint credits\n\t-h, --help\tPrint helpful options\n\t-v, --version\tPrint current version of z^2\n\nSUBCOMMANDS:\n\thelp\t\t\t  Print helpful options\n\t[FILENAME].zsq\t  Run program and/or project\n\trun\t\t\t\t  Run program and/or project\n\tinstall [PACKAGE] Install packages or modules\n\tquit\t\t\t  Quit the z^2 console\n\texit\t\t\t  Quit the z^2 console\n\tclear\t\t\t  Clears the console\n\tcredits\t\t\t  Prints credits\n\tversion\t\t\t  Prints current version of z^2")
    else:
      print(f"{cmd}: not found!")
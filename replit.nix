{ pkgs }: {
    deps = [
        pkgs.poetry
      
        pkgs.python38

        pkgs.python38Full
      
        pkgs.python38Packages.setuptools
        pkgs.python38Packages.click
        pkgs.python38Packages.pip
        pkgs.python38Packages.pymongo
        pkgs.python38Packages.dnspython
        # pkgs.python38Packages.replit
    ];
}
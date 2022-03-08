{ pkgs }: {
    deps = [
        pkgs.python38
        pkgs.python38Packages.setuptools
        pkgs.python38Packages.click
        pkgs.python38Packages.pip
        # pkgs.python38Packages.replit
    ];
}
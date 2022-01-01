{ pkgs }: {
    deps = [
        pkgs.python38
        pkgs.python38Packages.setuptools
        pkgs.python38Packages.click
    ];
}
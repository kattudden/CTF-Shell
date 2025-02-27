let
  nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-unstable";
  pkgs = import nixpkgs {
    config = {allowUnfree = true;};
    overlays = [];
  };
in
  pkgs.mkShellNoCC {
    packages = with pkgs; [
      cowsay
      lolcat
      gobuster
      burpsuite
      insomnia
      python312Packages.python
      python312Packages.uv
      python312Packages.requests
      php
    ];

    GREETING = "Let's find some flags...";
    shellHook = ''
      alias vim='nvim'
      source <(gobuster completion bash)
      echo $GREETING | cowsay | lolcat
    '';
  }

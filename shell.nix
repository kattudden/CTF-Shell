let
  nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-unstable";
  pkgs = import nixpkgs {
    config = {};
    overlays = [];
  };
in
  pkgs.mkShellNoCC {
    packages = with pkgs; [
      cowsay
      lolcat
      gobuster
    ];

    GREETING = "Let's find some flags...";
    shellHook = ''
      alias vim='nvim'
      source <(gobuster completion bash)
      echo $GREETING | cowsay | lolcat
    '';
  }

{ pkgs, ... }:

{

  packages = [ pkgs.git ];

  mach-nix.mkPython = {
    requirements = builtins.readFile ./requirements.txt;
  };
  
}

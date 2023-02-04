{ pkgs, ... }:

let
  myAppEnv = pkgs.poetry2nix.mkPoetryEnv {
    projectDir = ./.;

    overrides = pkgs.poetry2nix.defaultPoetryOverrides.extend
     (self: super: {
       fastapi-pagination = super.fastapi-pagination.overridePythonAttrs
       (
         old: {
           buildInputs = (old.buildInputs or [ ]) ++ [ super.poetry ];
         }
       );
     });

     editablePackageSources = {
      my-app = ./.;
    };
  };
in

{
  packages = [
    pkgs.poetry
    myAppEnv
  ];
}

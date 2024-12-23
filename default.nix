with import <nixpkgs> {};
stdenv.mkDerivation {
  name = "dev-environment";
  buildInputs = [
    pkg-config
    python3
    pylint
  ];
}

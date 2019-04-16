# AtCoderDir

## Installation

```sh
$ git clone https://github.com/iwatepu-cpc/AtCoderDir
$ ln -s -i $(readlink -f AtCoderDir/atcoder) $HOME/.local/bin/atcoder
```

## Usage

Requirements:
- python3
- requests
- bs4

```sh
# Fetch task samples of ABC124
$ atcoder https://atcoder.jp/contests/abc124

# Solve and then Test!
$ cd abc124/A
$ vim A.py
$ make bin='python3 A.py'
Running exec python A.py:

#1 AC 0m0.019s
#2 WA 0m0.029s
#3 WA 0m0.021s

Failure...
```

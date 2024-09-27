ro_crate_graph
==============

Script to convert an ro-crate-metadata.json into two csv files, one of nodes,
one of links..

## Installation

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) using
the instructions for your os.

Then git clone this repo, cd into it and use `uv run` to run the script 
(uv will install the dependencies in a venv for you)

```
	git clone FIXME
	cd ro_crate_graph
	uv run ro_crate_graph.py --crate your_crate --output ./
```

ro_crate_graph
==============

Script to load an [RO-Crate](https://www.researchobject.org/ro-crate/) and use the entities and relations to generate a list of nodes and relationships as two CSV files.

## Installation

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) using
the instructions for your operating system.

Then `git clone` this repo, cd into it and use `uv run` to run the script 
(uv will install the dependencies in a virtual environment automatically)

```
> git clone git@github.com:Sydney-Informatics-Hub/ro_crate_graph.git
> cd ro_crate_graph
> uv run ro_crate_graph.py --crate your_crate --output ./
Reading inline script metadata from: ro_crate_graph.py
Loading RO-Crate from your_crate
Found 116 entities with 68 relations
Wrote nodes.csv, links.csv to .
```

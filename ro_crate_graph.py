# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "rocrate",
# ]
# ///

from rocrate.rocrate import ROCrate
import re
from pathlib import Path
from argparse import ArgumentParser

# IDS = re.compile("^https://w3id.org/ldac/")

def write_csv(file, headers, items):
    with open(file, "w") as fh:
        fh.write(",".join(headers) + "\n")
        for i in items:
            try:
                fh.write(",".join(i) + "\n")
            except Exception as e:
                pass


def main(cratedir, outdir):
    crate = ROCrate(cratedir)
    nodes = []
    links = []
    print(f"Loading RO-Crate from {cratedir}")
    for e in crate.get_entities():
        n = e.properties().get("name", None)
        if n is not None:
            nodes.append((n, e.type))
            for p, v in e.properties().items():
                if type(v) is dict:
                    mid = v.get("@id", None)
                    target = crate.dereference(mid) 
                    if target:
                        tn = target.properties().get("name", None)
                        if tn is not None:
                            links.append((n, tn, p))
    nnodes = len(nodes)
    nlinks = len(links)
    write_csv(outdir / "nodes.csv", ("Name", "Type"), nodes)
    write_csv(outdir / "links.csv", ("Source", "Target", "Relation"), links)
    print(f"Found {nnodes} entities with {nlinks} relations")
    print(f"Wrote nodes.csv, links.csv to {outdir}")

if __name__ == "__main__":
    ap = ArgumentParser("RO-Crate to graph")
    ap.add_argument(
        "-c", "--crate",
        default="./Crate",
        type=Path,
        help="Directory containing the ro-crate-metadata.json",
    )
    ap.add_argument(
        "-o", "--output",
        default="./",
        type=Path,
        help="Directory to write the nodes.csv and links.csv files",
    )
    args = ap.parse_args()

    main(args.crate, args.output)

#!/usr/bin/env python3

import rdflib
from rdflib import Graph
import sys
import os
import subprocess

def convert_owl(input_path):
    # Load RDF/OWL file
    g = Graph()
    g.parse(input_path, format='xml')

    base_name = os.path.splitext(os.path.basename(input_path))[0]

    # JSON-LD
    jsonld_path = base_name + ".jsonld"
    g.serialize(destination=jsonld_path, format='json-ld')
    print(f"Saved JSON-LD to {jsonld_path}")

    # Turtle
    ttl_path = base_name + ".ttl"
    g.serialize(destination=ttl_path, format='turtle')
    print(f"Saved Turtle to {ttl_path}")

    # HTML using PyLODE
    html_path = "docs/" + base_name + ".html"
    subprocess.run(["pylode", input_path, "-o", html_path], check=True)
    print(f"Saved human-readable HTML with PyLODE to {html_path}")
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convert.py your_ontology.owl")
        sys.exit(1)

    convert_owl(sys.argv[1])


# RNA-Bi-Secondary-Structure-Validator

## About

This project implements computational methods to analyze and visualize RNA secondary structures and pseudoknots using the concept of book embeddings from graph theory.

The project reads RNA sequences and their basepairings, validates constraints, tests the existence of bi-secondary structures, and generates visualizations.


## Research Question

* Can we detect if an RNA basepairing forms a valid bi-secondary structure (a two-page book embedding)?
* **Bi-secondary structures**, as introduced by Haslinger & Stadler (1999), model RNA pseudoknots using two pages — arcs drawn both above and below the sequence line — and correspond to planar graphs.
* Detecting bi-secondary structures is equivalent to testing planarity of a “diagram graph” constructed from the RNA sequence and basepairs.


## Project Features

* Input: RNA sequences in FASTA format and basepair data in BPSEQ or dot bracket notation.
* Processing to determine if structure has a pseudoknot or not
* Output: Graph from the RNA sequence and its basepairs


## References

* Haslinger C, Stadler PF. RNA structures with pseudo-knots: graph-theoretical, combinatorial, and statistical properties. Bull Math Biol. 1999 May;61(3):437-67. doi: 10.1006/bulm.1998.0085. PMID: 17883226; PMCID: PMC7197269.
# Bioinformatics Algorithms Practice

Solutions to selected Rosalind Bioinformatics Stronghold problems, curated
around what actually feeds the rest of my computational biology roadmap —
not a full completion run of every problem on the platform.

## What this is

Standard-library-only Python implementations of the algorithms underlying
tools I currently use as black boxes: pairwise sequence alignment (the
logic inside MUSCLE/BLAST), genome assembly via de Bruijn graphs (JHU
Genomic Data Science, UCSD Bioinformatics Specialization), phylogenetic
tree combinatorics (EGFR capstone Module 7), and peptide inference from
mass spectra (the algorithmic core of MaxQuant/DIA-NN, ahead of Phase 3
proteomics work).

## What this is not

Not a from-scratch original research project — see
[`egfr-integrative-proteogenomics`](#) for that. Not a complete Rosalind
run-through; problems that duplicated work already done in
[`protein-python-foundations`](https://github.com/Afraim10/protein-python-foundations)
(GC content, transcription, translation, point mutations) were skipped
deliberately rather than re-solved for volume.

## Constraint

Python standard library only, no exceptions except `MPRT`, which fetches
a UniProt entry via `urllib.request`. The point of this repo is
implementing the algorithm, not calling a library that already implements
it — using `Bio.pairwise2` for an alignment problem, for example, would
defeat the exercise.

## Structure

| Folder | Problems | Feeds |
|---|---|---|
| `sequence-alignment/` | Edit distance, global/local/affine-gap alignment | MUSCLE/BLAST internals (Methods I/II) |
| `genome-assembly/` | k-mer composition, de Bruijn graphs, assembly from reads | JHU Genomic Data Science, UCSD Bioinformatics |
| `phylogenetics/` | Tree completion, ancestor counting, Newick distances | EGFR Module 7 |
| `proteomics-mass-spec/` | Peptide/protein inference from MS spectra | Phase 3 — MaxQuant/DIA-NN algorithmic core |
| `string-algorithms/` | KMP, tries, shared motifs, repeats | Phase 2 algorithms literacy |
| `foundational-sequence-analysis/` | ORFs, reverse translation, MSA consensus, UniProt motif query | Not yet covered elsewhere |

## Status

Ongoing, added to irregularly alongside the main roadmap — this is a
maintenance practice, not a scheduled deliverable.

# Assembly-breaking
Scripts related to assembly breaking

-Genome_cut.py

usage = """
Generate genome gff which can ranomly cut scaffolds into fixed n kb from genome length file with n kb specified,
usage:

python Genome_cut.py genome.len.txt n

Written by Dang, Academia sinica, Dec 28, 2016.

"""

-GeneIntoFrag.py

usage = """
Generate gene gff for Genome_cut.py output fragmented assemblies,
usage:

python GeneIntoFrag.py fragment.gff gene.gff


Written by Dang, Academia sinica, Jan 05, 2017.


"""


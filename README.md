# Assembly-breaking
Scripts related to assembly breaking

-Genome_cut.py

Input[1]: reference.genome.len.txt, as "Scaffold_ID[tab]Scaffold_length"

Input[2]: n (kb)

usage = """
Generate fragmented genome gff with scaffolds randomly broken into fixed size of n kb from genome length file with n kb specified,
usage:

python Genome_cut.py genome.len.txt n


Written by Dang, Academia sinica, Dec 28, 2016.


"""

-GeneIntoFrag.py

Input[1]: fragment.gff (output of Genome_cut.py)

Input[2]: reference gff

usage = """
Generate annotated gff for fragmented genome segments,
usage:

python GeneIntoFrag.py fragment.gff ref.gff


Written by Dang, Academia sinica, Jan 05, 2017.


"""


-Sample Dataset

c_elegans.ref.fa.len.txt and c_elegans.coding_gene.gff are processed from c_elegans.genome.fasta and c_elegans.gff downloaded from WS255 dataset in WormBase: http://www.wormbase.org/

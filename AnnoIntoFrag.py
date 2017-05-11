#!/usr/bin/python
## Assgin annotation info. from reference gff into fragments of genome from genome fragment gff

usage = """
Generate annotated gff for fragmented genome segments,
usage:

python GeneIntoFrag.py fragment.gff ref.gff


Written by Dang, Academia sinica, Jan 05, 2017.


"""

import sys, re


if __name__ == "__main__":
	if len(sys.argv) < 3:
		print usage
		sys.exit( 0 ) 

## Fragment file input
## Each line is a scaffold fragment
f1 = open(sys.argv[1], 'r')
#out_f = open(sys.argv[1] + '_gene.gff', 'w')
line1 = f1.readline()
while(line1):
	#print 'Hi'
	line1_s = re.split(r'\s+', line1)
	Scf1 = line1_s[0]
	Scf_n = line1_s[2]
	#print Scf1
	start1 = int(line1_s[3])
	end1 = int(line1_s[4])
	## read gene gff 
	f2 = open(sys.argv[2], 'r')
	line2 = f2.readline()
	while(line2):
		line2_s = re.split(r'\s+', line2)
		Scf2 = line2_s[0]
		## If the scf number is not the same, skip
		if (Scf2 != Scf1):
			#print 'Scf2!=Scf1'
			pass
		else:
			start2 = int(line2_s[3])
			end2 = int(line2_s[4])
			## If the range is not in fragment, skip
			if (start1 > start2 or end1 < end2):
				#print 'wrong position'
				pass
			else:
				## Trun the start and end into the start and end of that fragment
				print Scf_n + '\t' + line2_s[1] + '\t' + line2_s[2] + '\t' + str(start2-start1 + 1) + '\t' + str(end2-start1 + 1) + '\t' + line2_s[5] + '\t' + line2_s[6] + '\t' + line2_s[7] + '\t' + line2_s[8].replace('\n', '')
				#out_f.write('Scf.' + str(scf_n) + '\t' + line2_s[1] + '\t' + line2_s[2] + '\t' + str(start2-start1 + 1) + '\t' + str(end2-start1 + 1)  + line2_s[5] + '\t' + line2_s[6] + '\t' + line2_s[7] + '\t' + line2_s[8])
		line2 = f2.readline()
	line1 = f1.readline()

	
## All done !
# last_v20170110
# modify Scf_n

	

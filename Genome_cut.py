#!/usr/bin/python

# script to generate N50 = n kb gff from Genome length file

usage = """
Generate genome gff which can output N50=n scaffolds from genome length file with n kb specified,
usage:

python Genome_cut.py genome.len.txt n


Written by Dang, Academia sinica, Dec 28, 2016.


"""

import sys, re
import random


if __name__ == "__main__":
	if len(sys.argv) < 3:
		print usage
		sys.exit( 0 ) 

# human sorting
# sort numbers in string
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]


# Dict
G_dit = {}
Scf_dit = {}
Scf_n = 1
Out_l = []

# read genome len file
f = open(sys.argv[1], 'r')
line = f.readline()
while(line):
	line_s = re.split(r'\s+', line.replace('\n', ''))
	Scf = line_s[0]
	Scf_dit[Scf_n] = Scf
	start = 1
	end = int(line_s[1])
	G_dit[Scf_n] = []
	G_dit[Scf_n].append(start)
	G_dit[Scf_n].append(end)
	G_dit[Scf_n].append(Scf)
	Scf_n += 1	
	line = f.readline()
f.close()
print "len file was read"
# Generate random pieces with size n kb
# If the scaffold length is already < n kb, put it in output list directly 
# After make sure you can always randomly cut an n kb piece of region, there are 4 cases may encounter:
# 1: you left two pieces, both < n kb
# 2: you left two pieces, one < n kb and one > n kb *2 (left > n)
# 3: you left two pieces, one < n kb and one > n kb *2 (right > n)(one extreme case in this is cut from the first base)
# 4: you left two pieces, both > n kb
n = int(sys.argv[2])*1000
while(G_dit):
	G_key = random.sample(G_dit, 1)[0]
	print G_dit[G_key][0]
	print G_dit[G_key][1]-n
	print G_dit[G_key][2]
	if (G_dit[G_key][1]-n < 0):
		Out_l.append(G_dit[G_key][2] + ':' + str(G_dit[G_key][0]) + ':' + str(G_dit[G_key][1]))
		G_dit.pop(G_key, None)
		continue
	cut_start = random.randint(G_dit[G_key][0],G_dit[G_key][1]-n)
	cut_end = cut_start + n - 1
	Out_l.append(G_dit[G_key][2] + ':' + str(cut_start) + ':' + str(cut_end))
	if (((cut_start-1) - G_dit[G_key][0] + 1 < n) and (G_dit[G_key][1] - (cut_end+1) + 1 < n)):
		Out_l.append(G_dit[G_key][2] + ':' + str(cut_end+1) + ':' + str(G_dit[G_key][1]))
		Out_l.append(G_dit[G_key][2] + ':' + str(G_dit[G_key][0]) + ':' + str(cut_start-1))
		G_dit.pop(G_key, None)
		print "case 1 (left_left < n & left_right < n)"
	elif ((G_dit[G_key][1] - (cut_end+1) + 1 < n) and ((cut_start-1) - G_dit[G_key][0] + 1 > n)):
		Out_l.append(G_dit[G_key][2] + ':' + str(cut_end+1) + ':' + str(G_dit[G_key][1]))
		G_dit[G_key][1] = cut_start-1
		print "case 2 (left_left > n  & left_right < n)"
	elif (((cut_start-1) - G_dit[G_key][0] + 1 < n) and (G_dit[G_key][1] - (cut_end+1) + 1 > n)):
		Out_l.append(G_dit[G_key][2] + ':' + str(G_dit[G_key][0]) + ':' + str(cut_start-1))
		G_dit[G_key][0] = cut_end+1 
		print "case 3 (left_left < n  & left_right > n)"
	else:
		new_key = max(G_dit) + 1
		G_dit[new_key] = []
		G_dit[new_key].append(cut_end+1)
		G_dit[new_key].append(G_dit[G_key][1])
		G_dit[new_key].append(G_dit[G_key][2])
		G_dit[G_key][1] = cut_start-1
		print "case 4 (left_left > n  & left_right > n)"
#print Out_l

# prepare output
Out_dit = {}
for i in Out_l:
	split_item = i.split(':')
	out_scf = split_item[0]
	out_start = split_item[1]
	out_end = split_item[2]
	if (out_scf not in Out_dit):
		Out_dit[out_scf] = {}
		Out_dit[out_scf][out_start] = []
		Out_dit[out_scf][out_start].append(out_end)
	else:
		Out_dit[out_scf][out_start] = []
		Out_dit[out_scf][out_start].append(out_end)		

# sort for output gff
Out_dit2 = {}
	
for x in Out_dit:
        sort = sorted(Out_dit[x], key=int)
        Out_dit2[x] = sort

sort_scf_l = sorted(Out_dit2, key=natural_keys)

# output
n = 1
out_f = open(sys.argv[1] + '.CutInto' + str(sys.argv[2]) + 'kb.gff', 'w')
for x in sort_scf_l:
        for i in Out_dit2[x]:
        	#print x+'\tcut\tregion\t'+i+'\t'+Out_dit[x][i][0]+'\t.\t+\t.\t'+'ID=NA;Derives_from=genome_len_file'
        	out_f.write(x+'\tcut\tScf.'+str(n)+'\t'+i+'\t'+Out_dit[x][i][0]+'\t.\t+\t.\t'+'ID=NA;Derives_from=genome_len_file\n')
		n += 1
print "All done!"


# last_v20170110
# add scf number
	


import re
from math import log
from collections import defaultdict


dico_nb=defaultdict(lambda:defaultdict(int))
dico_donnee=defaultdict(list)

a=0
with open("info_genomes.tsv","r") as f1:
	for li in f1:
		a+=1
		lli=(li.split("\t")[5])
		if re.findall("viridae",lli):
			taxo=(re.findall("[A-Za-z]+viridae",lli)[0])
		else:
			taxo="Unknown"
		dico_nb[taxo][li.split("\t")[12]]+=1

with open("info_genomes.tsv","r") as f1:
	for li in f1:
		a+=1
		lli=(li.split("\t")[5])
		if re.findall("viridae",lli):
			taxo=(re.findall("[A-Za-z]+viridae",lli)[0])
		else:
			taxo="Unknown"
		if not li.startswith("Locus"):
			dico_donnee[a].append(li.split("\t")[0])
			dico_donnee[a].append(li.split("\t")[1])
			dico_donnee[a].append(li.split("\t")[2])
			dico_donnee[a].append(li.split("\t")[3])
			dico_donnee[a].append(li.split("\t")[4])
			dico_donnee[a].append(taxo)
			dico_donnee[a].append(li.split("\t")[6])
			dico_donnee[a].append(li.split("\t")[7])
			dico_donnee[a].append(li.split("\t")[8])
			dico_donnee[a].append(li.split("\t")[9])
			dico_donnee[a].append(li.split("\t")[10])
			dico_donnee[a].append(li.split("\t")[11])
			dico_donnee[a].append(li.split("\t")[12])
			dico_donnee[a].append(li.split("\t")[13])
			dico_donnee[a].append(li.split("\t")[14])
			dico_donnee[a].append(li.split("\t")[15])
			dico_donnee[a].append(li.split("\t")[16])
			dico_donnee[a].append(li.split("\t")[17])
			dico_donnee[a].append(li.split("\t")[18])
			dico_donnee[a].append(li.split("\t")[19])
			dico_donnee[a].append(li.split("\t")[20])
			dico_donnee[a].append(li.split("\t")[21])
			dico_donnee[a].append(li.split("\t")[22])
			dico_donnee[a].append(dico_nb[taxo][li.split("\t")[12]])
			dico_donnee[a].append(log(dico_nb[taxo][li.split("\t")[12]])**2)
		

with open("nouvelles_donnees.tsv","w") as f:
	print("Locus","Name","Definition","MolType","MolStruct","Taxonomy","DB_origin","Length","Host name","Superkingdom","phylum","class","order","family","genus","species","Full taxo","Full taxo with lvl","prophage","nb_prot","GC","nbMega","nbSing","value","log",sep="\t",file=f)
	for values in dico_donnee.values():
		valeurs=""
		for subvalues in values:
			valeurs+=str(subvalues)+'\t'
		print(valeurs,file=f)
f.close()







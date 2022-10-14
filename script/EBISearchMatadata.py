# -*- coding: utf-8 -*-

"""
Created on Thu Sep 29 14:55:26 2022

@author: kgy
"""

import os
import json
import webbrowser 
import sys

s = sys.argv
if len(s) < 3 :
	print ("Usage : \n\n$ python EBISearchMatadata.py --input directory/file.json  < --db DBname (Optional)>  < --fields fields (Optional) >")
	print ("\nNB : \n\tBy default :  \n\t\tDBname = biosamples \n\t\tfields = id,name,collection_date")
	print ("\n\nExamles\n")
	print ("\t1. python EBISearchMetadata.py --input /home/test.json")
	print ("\t2. python EBISearchMetadata.py --input /home/test.json --db biosamples")
	print ("\t3. python EBISearchMetadata.py --input /home/test.json --db biosamples --fields id,collection_date,...")
	print ("\t4. python EBISearchMetadata.py --input /home/test.json --fields id,name,...")
	sys.exit()

init1= ""
init2 = ""
end1 = ""
end2 = ""

if "--db" in s :
	init1 = "curl -X GET --header 'Accept: text/xml' 'https://www.ebi.ac.uk/ebisearch/ws/rest/"+s[s.index("--db")+1]+"?filter="
	init2 = "https://www.ebi.ac.uk/ebisearch/ws/rest/"+s[s.index("--db")+1]+"?filter="
else :
	init1="curl -X GET --header 'Accept: text/xml' 'https://www.ebi.ac.uk/ebisearch/ws/rest/biosamples?filter="
	init2= "https://www.ebi.ac.uk/ebisearch/ws/rest/biosamples?filter="

if "--fields" in s :
	end1 = "&fields="+s[s.index("--fields")+1]+"'"
	end2 = "&fields="+s[s.index("--fields")+1]
else:
	end1 = "&fields=id,name,collection_date'"
	end2 = "&fields=id,name,collection_date"

'''
this function allows to read the json file 
but also to get the taxon_id and to launch the results in the webbrowser.
'''

def requet (file_directory):
	with open(file_directory) as mf:
		file = json.load(mf)
	query1 = init1
	query2 = init2
	for i in range(len(file)):
		query1 += "%20TAXONOMY:"+str(file[i]["taxon_id"])
		query2 += "%20TAXONOMY:"+str(file[i]["taxon_id"])
	if i < len(file)-1:
		query1 += "%20OR"
		query2 += "%20OR"
	query1 += end1
	query2 += end2
	webbrowser.open_new_tab(query2)
	output = s[2].split(".json")[0]+".xml"
	os.system(query1 +" > " +output)


requet(s[2])

# requet('C:/Users/Dell/Desktop/taxon work/Colman_Work/input/hse_pathogens.bacteria_w_taxa.json')






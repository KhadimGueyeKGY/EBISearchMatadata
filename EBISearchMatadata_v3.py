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
	init1 = "curl -X GET --header 'Accept: application/json' 'https://www.ebi.ac.uk/ebisearch/ws/rest/"+s[s.index("--db")+1]+"?query="
	init2 = "https://www.ebi.ac.uk/ebisearch/ws/rest/"+s[s.index("--db")+1]+"?query="
else :
	init1="curl -X GET --header 'Accept: application/json' 'https://www.ebi.ac.uk/ebisearch/ws/rest/biosamples?query="
	init2= "https://www.ebi.ac.uk/ebisearch/ws/rest/biosamples?query="

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

def requet (file_directory,index_file,f):
    with open(file_directory) as mf:
        file = json.load(mf)
    query1 = init1
    query2 = init2
    if f != 0 :
        f += 1
    for i in range(f,len(file)):
        print(i)
        query1 += "\""+str(file[i]["name"]).replace(" ","%20")+"\""
        query2 += "\""+str(file[i]["name"]).replace(" ","%20")+"\""
        if i != f:
            if i%100 ==0:
                break
        if i < len(file)-1:
            query1 += "%20OR%20"
            query2 += "%20OR%20"
    query1 += end1
    query2 += end2
    output = s[2].split(".json")[0]+"_N"+str(index_file)+".xml"
    output2 = open(s[2].split(".json")[0]+"_request_url_N"+str(index_file)+".txt","w")
    output3 = open(s[2].split(".json")[0]+"_request_curl_N"+str(index_file)+".txt","w")
    os.system(query1 +" > " +output)
    output2.write(query2)
    output3.write(query1)
    output2.close()
    output3.close()
    print("\n\n\n")
    # webbrowser.open_new_tab(query2)

with open(s[2]) as mF:
    File = json.load(mF)
index_File = 0
for e in range(0,len(File),100):
    requet(s[2],index_File,e)
    index_File += 1

# requet('C:/Users/Dell/Desktop/taxon work/Colman_Work/input/hse_pathogens.bacteria_w_taxa.json')


'''
earch failed:maxClauseCount is set to 10240


'''

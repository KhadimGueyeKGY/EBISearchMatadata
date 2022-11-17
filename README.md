# EBISearchMatadata

This pipeline allows to extract metadata in the biosamples domain by default. 

## Installation 
  * git clone https://github.com/KhadimGueyeKGY/EBISearchMatadata.git 

## Usage:
for help or to know how to use this script type:

  ```
  python EBISearchMatadata.py 
  ```
  
 * By default :
 
    * Domain: biosamples
    * Fileds: id,name,collection_date

NB: you don't need to write it (damine and fields) if you don't change domain or fields. 

### Example:
```
 python EBISearchMatadata_v2.py --input ../input/hse_pathogens.fungi_w_taxa.json
```

## Output
After execution of the code, three files will be created in the same directory as the input file:
* \<file\>_N*.xml : containing the metadata
* \<file\>_request_url_N*.txt : containing the url
* \<file\>_request_curl_N*.txt : containing the command line 



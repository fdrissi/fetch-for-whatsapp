# fetch-for-whatsapp
I write this simple script to automatically getting links from a specific website.  
all you need to do, is modify the url inside the script and execute it like that:  
python getlinks.py  
if you are using mac os or linux, you can add this command after the execution, to filter only the urls, and save the output in "testlist" file  
python getlinks.py | grep -Eo "(http|https)://[a-zA-Z0-9./?=_-]*" | awk 'length>27' >> testlist

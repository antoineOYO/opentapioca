Start-Transcript -Path "C:\Users\Antoine\Documents\GitHub\opentapioca\logs_ps1\output.log"
tapioca train-bow D:\latest-all.json.bz2 ; 
tapioca preprocess D:\latest-all.json.bz2 ; 
wsl sort -n -k 1 latest-all.unsorted.tsv > wikidata_graph.tsv;
tapioca compile wikidata_graph.tsv ;
tapioca compute-pagerank wikidata_graph.npz
Stop-Transcript

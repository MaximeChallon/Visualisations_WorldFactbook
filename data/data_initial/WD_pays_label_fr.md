Requête SPARQL dans le SPARQL endpoint de Wikidata:
```
SELECT ?pays ?label_fr 
WHERE {
?pays wdt:P31 wd:Q3624078;
rdfs:label ?label_fr 
filter(lang(?label_fr) = 'fr')
}
```

Lien pour importer les données JSON dans Dataiku:
`https://query.wikidata.org/sparql?query=SELECT%20%3Fpays%20%3Flabel_fr%20%0AWHERE%20%7B%0A%3Fpays%20wdt%3AP31%20wd%3AQ3624078%3B%0Ardfs%3Alabel%20%3Flabel_fr%20%0Afilter%28lang%28%3Flabel_fr%29%20%3D%20%27fr%27%29%0A%7D&format=json`

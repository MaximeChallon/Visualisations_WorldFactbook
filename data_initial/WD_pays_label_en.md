Requête SPARQL dans le SPARQL endpoint de Wikidata:
```
SELECT ?pays ?label_en 
WHERE {
?pays wdt:P31 wd:Q3624078;
rdfs:label ?label_en
filter(lang(?label_en) = 'en')
}
```

Lien pour importer les données JSON dans Dataiku:
`https://query.wikidata.org/sparql?query=SELECT%20%3Fpays%20%3Flabel_en%20%0AWHERE%20%7B%0A%3Fpays%20wdt%3AP31%20wd%3AQ3624078%3B%0Ardfs%3Alabel%20%3Flabel_en%0Afilter%28lang%28%3Flabel_en%29%20%3D%20%27en%27%29%0A%7D&format=json`

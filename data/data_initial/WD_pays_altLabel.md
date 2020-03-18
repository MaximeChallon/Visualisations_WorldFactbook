Requête SPARQL dans le SPARQL endpoint de Wikidata:
```
SELECT DISTINCT ?paysLabel ?frLabel ?engLabel
WHERE {
?pays wdt:P31 wd:Q3624078;
SERVICE wikibase:label {
bd:serviceParam wikibase:language "en".
}
OPTIONAL {?pays skos:altLabel ?frLabel . FILTER (lang(?frLabel) = "fr") }
OPTIONAL {?pays skos:altLabel ?engLabel . FILTER (lang(?engLabel) = "en") }
}
```

Lien pour importer les données JSON dans Dataiku:
`https://query.wikidata.org/sparql?query=SELECT%20DISTINCT%20%3FpaysLabel%20%3FfrLabel%20%3FengLabel%0AWHERE%20%7B%0A%3Fpays%20wdt%3AP31%20wd%3AQ3624078%3B%0ASERVICE%20wikibase%3Alabel%20%7B%0Abd%3AserviceParam%20wikibase%3Alanguage%20%22en%22.%0A%7D%0AOPTIONAL%20%7B%3Fpays%20skos%3AaltLabel%20%3FfrLabel%20.%20FILTER%20%28lang%28%3FfrLabel%29%20%3D%20%22fr%22%29%20%7D%0AOPTIONAL%20%7B%3Fpays%20skos%3AaltLabel%20%3FengLabel%20.%20FILTER%20%28lang%28%3FengLabel%29%20%3D%20%22en%22%29%20%7D%0A%7D&format=json`

Lien pour importer les données en Json dans Dataiku:
`https://query.wikidata.org/sparql?query=SELECT%20DISTINCT%20%3ForgLabel%20%3FsiegeLabel%20%3FGPS%20%3FaltLabel%0AWHERE%20%7B%0A%20%20%3Fpays%20wdt%3AP31%20wd%3AQ6256.%0A%20%20%3Fpays%20wdt%3AP463%20%3Forg.%0A%20%20%3Forg%20wdt%3AP159%20%3Fsiege.%0A%20%20%3Fsiege%20wdt%3AP625%20%3FGPS.%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22en%22.%20%7D%0A%0AOPTIONAL%20%7B%20%3Forg%20skos%3AaltLabel%20%3FaltLabel%20.%20FILTER%20%28lang%28%3FaltLabel%29%20%3D%20%22en%22%29%20%7D%7D&format=json
https://query.wikidata.org/sparql?query=SELECT%20%3ForgLabel%20%3FsiegeLabel%20%3FGPS%20%3FaltLabel%0AWHERE%20%7B%0A%20%20%3Forg%20wdt%3AP31%20wd%3AQ245065.%0A%20%20%3Forg%20wdt%3AP159%20%3Fsiege.%0A%20%20OPTIONAL%7B%3Fsiege%20wdt%3AP625%20%3FGPS.%7D%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%0A%20%20%20%20bd%3AserviceParam%20wikibase%3Alanguage%20%22en%22.%0A%20%20%7D%0AOPTIONAL%20%7B%20%3Forg%20skos%3AaltLabel%20%3FaltLabel%20.%20FILTER%20%28lang%28%3FaltLabel%29%20%3D%20%22en%22%29%20%7D%7D&format=json
https://query.wikidata.org/sparql?query=SELECT%20%3ForgLabel%20%3FsiegeLabel%20%3FGPS%20%3FaltLabel%0AWHERE%20%7B%0A%20%20%3Forg%20wdt%3AP31%20wd%3AQ484652.%0A%20%20%3Forg%20wdt%3AP159%20%3Fsiege.%0A%20%20OPTIONAL%7B%3Fsiege%20wdt%3AP625%20%3FGPS.%7D%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%0A%20%20%20%20bd%3AserviceParam%20wikibase%3Alanguage%20%22en%22.%0A%20%20%7D%0AOPTIONAL%20%7B%20%3Forg%20skos%3AaltLabel%20%3FaltLabel%20.%20FILTER%20%28lang%28%3FaltLabel%29%20%3D%20%22en%22%29%20%7D%7D&format=json
https://query.wikidata.org/sparql?query=SELECT%20%3ForgLabel%20%3FsiegeLabel%20%3FGPS%20%3FaltLabel%0AWHERE%20%7B%0A%20%20%3Forg%20wdt%3AP31%20wd%3AQ7210356.%0A%20%20%3Forg%20wdt%3AP159%20%3Fsiege.%0A%20%20OPTIONAL%7B%3Fsiege%20wdt%3AP625%20%3FGPS.%7D%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%0A%20%20%20%20bd%3AserviceParam%20wikibase%3Alanguage%20%22en%22.%0A%20%20%7D%0A%0AOPTIONAL%20%7B%20%3Forg%20skos%3AaltLabel%20%3FaltLabel%20.%20FILTER%20%28lang%28%3FaltLabel%29%20%3D%20%22en%22%29%20%7D%7D&format=json`

En détail:
* pour les organisations intergouvernementales: 
```
	SELECT ?orgLabel ?siegeLabel ?GPS ?altLabel
	WHERE {
  	?org wdt:P31 wd:Q245065.
  	?org wdt:P159 ?siege.
  	OPTIONAL{?siege wdt:P625 ?GPS.}
  	SERVICE wikibase:label {
    	bd:serviceParam wikibase:language "en".
  	}
	OPTIONAL { ?org skos:altLabel ?altLabel . FILTER (lang(?altLabel) = "en") }}
 ```
* pour les organisations internationales:
```
	SELECT ?orgLabel ?siegeLabel ?GPS ?altLabel
WHERE {
  	?org wdt:P31 wd:Q484652.
  	?org wdt:P159 ?siege.
  	OPTIONAL{?siege wdt:P625 ?GPS.}
  	SERVICE wikibase:label {
    	bd:serviceParam wikibase:language "en".
  	}
	OPTIONAL { ?org skos:altLabel ?altLabel . FILTER (lang(?altLabel) = "en") }}
```
* pour les organisations politiques:
```
	SELECT ?orgLabel ?siegeLabel ?GPS ?altLabel
	WHERE {
  	?org wdt31 wd:Q7210356.
  	?org wdt159 ?siege.
  	OPTIONAL{?siege wdt625 ?GPS.}
  	SERVICE wikibase:label {
    	bd:serviceParam wikibase:language "en".
  	}
	OPTIONAL { ?org skos:altLabel ?altLabel . FILTER (lang(?altLabel) = "en") }}
```
* pour les organisations tirées des fiches pays:
```
	SELECT DISTINCT ?orgLabel ?siegeLabel ?GPS ?altLabel
	WHERE {
  	?pays wdt31 wd:Q6256.
  	?pays wdt463 ?org.
  	?org wdt159 ?siege.
  	?siege wdt625 ?GPS.
  	SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
	OPTIONAL { ?org skos:altLabel ?altLabel . FILTER (lang(?altLabel) = "en") }}
```

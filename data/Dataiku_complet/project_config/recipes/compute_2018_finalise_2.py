# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import re
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
in_pays = dataiku.Dataset("2011_pays_prets")
in_pays_df = in_pays.get_dataframe()
in_orgs = dataiku.Dataset("2018_toutes_organisations")
in_orgs_df = in_orgs.get_dataframe()

out_df = in_orgs_df
# renommage des colonnes de sortie
out_df = out_df.rename(columns = {'abbrev':'abbrev_org',
                                  'name':'name_org',
                                 "established": "date de création",
                                  "GPS.value_first": "GPS_siege",
                                  "longitude_first": "longitude_siege",
                                  "latitude_first": "latitude_siege",
                                  "point_palladio_first": "point_palladio",
                                  "siegeLabel.value_first": "nom_siege"
                                 })


# ajout d'une colonne avec tous les pays membres par organisation
dico_noms_pays_orgs = {}
for row in in_pays.iter_rows():
    dico_noms_pays_orgs[row["name"]]=re.split(r'\\', row["memberships"])

pays_des_orgs = []
for org in [une_org["abbrev"] for une_org in in_orgs.iter_rows()]:
    liste_des_pays = []
    for pays in dico_noms_pays_orgs:
        if org in dico_noms_pays_orgs.get(pays):
            liste_des_pays.append(pays)
    pays_des_orgs.append(liste_des_pays)

out_df["members"] = pays_des_orgs

# ajout de la somme des populations de chaque pays dans les organisations
dico_pop_pays_orgs = {}
for row in in_pays.iter_rows():
    dico_pop_pays_orgs[row["name"]]=row["population"]

population_orgs  = []
for org in pays_des_orgs:
    population_org = 0
    for pays in org:
        population_org += dico_pop_pays_orgs.get(pays)
    population_orgs.append(population_org)

out_df["population_org"] = population_orgs

# ajout du nombre de soldats par organisation

dico_soldats_pays_orgs = {}
for row in in_pays.iter_rows():
    dico_soldats_pays_orgs[row["name"]]=row["Soldats_2011"]

soldats_orgs  = []
for org in pays_des_orgs:
    soldats_org = 0
    for pays in org:
        soldats_org += dico_soldats_pays_orgs.get(pays)
    soldats_orgs.append(soldats_org)

out_df["soldats_org"] = soldats_orgs

# ajout du nombre de morts à la guerre par organisation

dico_morts_pays_orgs = {}
for row in in_pays.iter_rows():
    dico_morts_pays_orgs[row["name"]]=row["MortsGuerre_2011"]

morts_orgs  = []
for org in pays_des_orgs:
    morts_org = 0
    for pays in org:
        morts_org += dico_morts_pays_orgs.get(pays)
    morts_orgs.append(morts_org)

out_df["mortsGuerre_org"] = morts_orgs

# ajout des dépenses miliatires des pays membres par organisation

dico_depensesMil_pays_orgs = {}
for row in in_pays.iter_rows():
    dico_depensesMil_pays_orgs[row["name"]]=row["DepensesMilitairesPIB_2011"]

depenseMil_orgs  = []
for org in pays_des_orgs:
    depenseMil_org = 0
    for pays in org:
        depenseMil_org += dico_depensesMil_pays_orgs.get(pays)
    depenseMil_orgs.append(depenseMil_org)

out_df["depensesMilitairesPIB_org"] = depenseMil_orgs

# ajout du total des exportations des pays membres

dico_export_pays_orgs = {}
for row in in_pays.iter_rows():
    dico_export_pays_orgs[row["name"]]=row["Exportations_2011"]

export_orgs  = []
for org in pays_des_orgs:
    export_org = 0
    for pays in org:
        export_org += dico_export_pays_orgs.get(pays)
    export_orgs.append(export_org)

out_df["exportations_org"] = export_orgs

# ajout du total des importations des pays membres

dico_import_pays_orgs = {}
for row in in_pays.iter_rows():
    dico_import_pays_orgs[row["name"]]=row["Importations_2011"]

import_orgs  = []
for org in pays_des_orgs:
    import_org = 0
    for pays in org:
        import_org += dico_import_pays_orgs.get(pays)
    import_orgs.append(import_org)

out_df["importations_org"] = import_orgs

# ajout du total des superficies des pays membres

dico_area_pays_orgs = {}
for row in in_pays.iter_rows():
    dico_area_pays_orgs[row["name"]]=row["area"]

area_orgs  = []
for org in pays_des_orgs:
    area_org = 0
    for pays in org:
        area_org += dico_area_pays_orgs.get(pays)
    area_orgs.append(area_org)

out_df["superficie_org"] = area_orgs

# Write recipe outputs
out = dataiku.Dataset("2011_finalise")
out.write_with_schema(out_df)
import requests
import json

url = "https://estadisticas.comunidad.madrid/?module=API"
method = ["&method=Referrers.getSearchEngines","&method=Actions.getPageUrls","&method= Actions.getDownload"]
id_site = "&idSite=94"
date = "&date=2023-05"
period = "&period=month"
format = "&format=json"
token = "&token_auth=05ff6c34de5fcfa70388296d172cfd21"
for i in range(len(method)):
    # print("LLAMADA ",i)
    p = url + method[i] + id_site + date + period + format + token + "&flat=1&filter_limit=-1&translateColumnNames=1"
    response = requests.get(p)
    # data = json.dumps(json.loads(response.text), indent=4)
    dictionary =  json.loads(response.text)

    for item in dictionary :
        print(item['sum_daily_nb_uniq_visitors'])
    print(dictionary[1]['label'])

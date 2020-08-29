def jsonListToJson(jsonList, key, value):
    jsonObject = {}
    for item in jsonList:
        jsonObject[item[key]] = item[value]
    return jsonObject

import datetime
import json
import jsonpickle


def writeToJSONFile(filename, someDataObject):
    try:
        print("[TRACE] Attempting to write to JSON file:", type(someDataObject))
        #print("[TRACE] Data:", someDataObject)
        data_from_pickle = jsonpickle.encode(someDataObject)
        with open(filename, 'w') as resultsFile:
            json.dump(data_from_pickle, resultsFile, indent=4)
        return False
    except Exception as someErr:
        print("[ERROR] Writing to JSON file failed", someErr)
        return None

'''def convert_dict_to_json(someDataObject):
    with open(someDataObject, 'rb') as fpkl, open('%s.json' % someDataObject, 'w') as fjson:
        data = pickle.load(fpkl)
        json.dump(data, fjson, ensure_ascii=False, sort_keys=True, indent=4)'''
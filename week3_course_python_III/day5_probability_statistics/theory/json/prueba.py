import json, os, sys
print(os.getcwd())
ruta = os.path.dirname(os.getcwd())
sys.path.append(ruta)
#with open('./data_indented.json', 'r+') as outfile:
#    json_data_indented_readed = json.load(outfile)

#print(type(json_data_indented_readed))
#print(json_data_indented_readed)
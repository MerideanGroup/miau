from classificador import *
import json
import codecs

def read_texts(path_to_json_file, label_symbol):
	f = codecs.open(path_to_json_file, 'r', 'utf-8')
	json_file = json.load(f)
	contents = [item['content'] for item in json_file]
	contents = contents#[:100]
	labels = [label_symbol] * len(contents)
	print(path_to_json_file + '\t- ' + str(len(contents)))
	return contents, labels

#textos_Estrategia_y_liderazgo		, labels_Estrategia_y_liderazgo = read_texts('textsWikis_Anotados_Clean/Estrategia_y_liderazgo.json', 0)
textos_Innovación_y_flexibilidad	, labels_Innovación_y_flexibilidad = read_texts('textsWikis_Anotados_Clean/Innovación_y_flexibilidad.json', 0)
textos_Integridad					, labels_Integridad = read_texts('textsWikis_Anotados_Clean/Integridad.json', 1)
textos_Oferta						, labels_Oferta = read_texts('textsWikis_Anotados_Clean/Oferta.json', 2)
textos_Responsabilidad_social		, labels_Responsabilidad_social = read_texts('textsWikis_Anotados_Clean/Responsabilidad_social.json', 3)
textos_Situación_financiera			, labels_Situación_financiera = read_texts('textsWikis_Anotados_Clean/Situación_financiera.json', 4)
#textos_Trabajo 						, labels_Trabajo = read_texts('textsWikis_Anotados_Clean/Trabajo.json', 6)



#all_samples = textos_Estrategia_y_liderazgo + textos_Innovación_y_flexibilidad + textos_Integridad + textos_Oferta + textos_Responsabilidad_social + textos_Situación_financiera + textos_Trabajo
all_samples = textos_Innovación_y_flexibilidad + textos_Integridad + textos_Oferta + textos_Responsabilidad_social + textos_Situación_financiera

all_labels = labels_Innovación_y_flexibilidad + labels_Integridad + labels_Oferta + labels_Responsabilidad_social + labels_Situación_financiera
#all_labels = labels_Estrategia_y_liderazgo + labels_Innovación_y_flexibilidad + labels_Integridad + labels_Oferta + labels_Responsabilidad_social + labels_Situación_financiera + labels_Trabajo

#class_weight= {
#	 0: (len(all_samples) *1.0)/ len(textos_Estrategia_y_liderazgo),
#	 1: (len(all_samples) *1.0)/ len(textos_Innovación_y_flexibilidad),
#	 2: (len(all_samples) *1.0)/ len(textos_Integridad),
#	 3: (len(all_samples) *1.0)/ len(textos_Oferta),
#	 4: (len(all_samples) *1.0)/ len(textos_Responsabilidad_social),
#	 5: (len(all_samples) *1.0)/ len(textos_Situación_financiera),
#	 6: (len(all_samples) *1.0)/ len(textos_Trabajo)
#}

class_weight= {
	 0: (len(all_samples) *1.0)/ len(textos_Innovación_y_flexibilidad),
	 1: (len(all_samples) *1.0)/ len(textos_Integridad),
	 2: (len(all_samples) *1.0)/ len(textos_Oferta),
	 3: (len(all_samples) *1.0)/ len(textos_Responsabilidad_social),
	 4: (len(all_samples) *1.0)/ len(textos_Situación_financiera),
}

print('Entrenando...\n')

c = Classifier(all_samples, all_labels, weights=class_weight)

fr = codecs.open('data_test/Comentarios2_2000.json', 'r', 'utf-8')
json_file = json.load(fr)
fr.close()

fw = open('gold_files/gold.txt', 'w')

for label in json_file.keys():
	texts = json_file[label]
	for text in texts:
		label_predicted = c.classify(text)
		if label == label_predicted:
			fw.write(label + '\t' + label_predicted + '\t' + '1' + '\t' + text + '\n')
		else:
			fw.write(label + '\t' + label_predicted + '\t' + '0' + '\t' + text + '\n')	

fw.close()
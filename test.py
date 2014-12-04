from classificador import *
import json
import codecs

def read_texts(path_to_json_file, label_symbol):
	f = codecs.open(path_to_json_file, 'r', 'utf-8')
	json_file = json.load(f)
	contents = [item['content'] for item in json_file]
	contents = contents#[:100]
	labels = [label_symbol] * len(contents)
	print(len(contents))
	return contents, labels

print("Estrategia_y_liderazgo, 0")
print("Innovación_y_flexibilidad, 1")
print("Integridad, 2")
print("Oferta, 3")
print("Responsabilidad_social, 4")
print("Situación_financiera, 5")
print("Trabajo, 6")

textos_Estrategia_y_liderazgo		, labels_Estrategia_y_liderazgo = read_texts('texts2/Estrategia_y_liderazgo.json', 0)
textos_Innovación_y_flexibilidad	, labels_Innovación_y_flexibilidad = read_texts('texts2/Innovación_y_flexibilidad.json', 1)
textos_Integridad					, labels_Integridad = read_texts('texts2/Integridad.json', 2)
textos_Oferta						, labels_Oferta = read_texts('texts2/Oferta.json', 3)
textos_Responsabilidad_social		, labels_Responsabilidad_social = read_texts('texts2/Responsabilidad_social.json', 4)
textos_Situación_financiera			, labels_Situación_financiera = read_texts('texts2/Situación_financiera.json', 5)
textos_Trabajo 						, labels_Trabajo = read_texts('texts2/Trabajo.json', 6)



all_samples = textos_Estrategia_y_liderazgo + textos_Innovación_y_flexibilidad + textos_Integridad + textos_Oferta + textos_Responsabilidad_social + textos_Situación_financiera + textos_Trabajo

all_labels = labels_Estrategia_y_liderazgo + labels_Innovación_y_flexibilidad + labels_Integridad + labels_Oferta + labels_Responsabilidad_social + labels_Situación_financiera + labels_Trabajo

class_weight= {
	 0: (len(all_samples) *1.0)/ len(textos_Estrategia_y_liderazgo),
	 1: (len(all_samples) *1.0)/ len(textos_Innovación_y_flexibilidad),
	 2: (len(all_samples) *1.0)/ len(textos_Integridad),
	 3: (len(all_samples) *1.0)/ len(textos_Oferta),
	 4: (len(all_samples) *1.0)/ len(textos_Responsabilidad_social),
	 5: (len(all_samples) *1.0)/ len(textos_Situación_financiera),
	 6: (len(all_samples) *1.0)/ len(textos_Trabajo)
}

c =Classifier(all_samples, all_labels, weights=class_weight)

c.classify("el pago del salario. el Trabajo es dificil, los horarios son largos, los derechos laborales demasiadas horas")
c.classify("iPhone tiene muchas aplicaciones")
c.classify("Android tiene muchas aplicaciones y la store")
c.classify("@Telefonica_Col ha movilizado en 2013 un un 0,74 del PIB del país. Lee más en su Informe de #Sostenibilidad http://t.co/NtQN2rgH5e #RSC")
c.classify("Telefónica Movistar movilizó $5,2 billones en Colombia http://t.co/HTkI0re477")
c.classify("Telefónica cierra la compra de la brasileña GVT y vende Telecom Italia http://t.co/Vo3zUKDdP5")
c.classify("RT @Xtreme_techno: Presente en #ExpoCaribe Emprendimiento Corporativo @InnpulsaCol @Caribetic @Camarabaq @ClaroColombia http://t.co/0Up0enp?")
c.classify("@ClaroTeAyuda Como adquiero otro decodificador HD, y aumento la velocidad de mi banda ancha, tengo 3play 5 MB, 40 C HD y Telefonia. Gracias")
c.classify("@ClaroColombia Buenas tardes qué está pasando con la señal de Claro en los iPhone?")
c.classify(" España comunicó esta semana a los sindicatos la aprobación de la subida salarial del 1% para 2014, acordada en el convenio")
c.classify("Slim y  participan en una subasta de  en Argentina http://t.co/xzGAGzR9iR")
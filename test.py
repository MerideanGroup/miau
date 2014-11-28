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

print("oferta, 0")
print("trabajo, 1")
print("finanza, 2")
print("innovacion, 3")

textos_telefonia, labels_telefonia = read_texts('texts/celularis_content.json', 0)
textos_trabajo, labels_trabajo = read_texts('texts/wikipedia_trabajo.json', 1)
textos_finanzas, labels_finanzas = read_texts('texts/finanzas.json', 2)
textos_innovacion, labels_innovacion = read_texts('texts/innovacion.json', 3)


all_samples = textos_telefonia+ textos_trabajo + textos_finanzas + textos_innovacion

class_weight= {	
	 0: (len(all_samples) *1.0)/ len(textos_telefonia),
	 1: (len(all_samples) *1.0)/ len(textos_trabajo),
	 2: (len(all_samples) *1.0)/ len(textos_finanzas),
	 3: (len(all_samples) *1.0)/ len(textos_innovacion)
}

c =Classifier(all_samples, labels_telefonia+ labels_trabajo + labels_finanzas + labels_innovacion, weights=class_weight)
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
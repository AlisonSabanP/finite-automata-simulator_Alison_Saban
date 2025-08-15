# finite-automata-simulator_Alison_Saban

Esta es una aplicación de python la cual procesa automatas finitos definidos por json, valida la estructura, genera su diagrama de transición con Graphviz y valida las cadenas de prueba.

--Tecnología usada--
Python 3.12.2
Flask -> RESTApi
Graphviz -> Generación de diagramas
Unittest -> Pruebas Unitarias 

--dependencias--
pip install unittest
pip install graphviz
pip install flask


--Ejecución--
python main.py

El servidor esta inicializado en el puerto: 1804
y se inicia en: http://localhost:1804

--Api--
Endpoint: /process-automata

el api recibe un json con una lista de automatas, valida, valida las cadenas de prueba y devuelve resultados.

--Diagramas--
los diagramas se guardan de la siguiente forma: generated_diagrams/automata_{id}_{timestamp}.png

ejemplo de un diagrama generado: generated_diagrams/automata_1_1723456789.png

--Archivo json de ejemplo--
JSON_example/JSON_entry.json es un archivo de ejemplo que contiene 10 automatas, el cual tiene 2 que son no validos (el automata 6 y el 9)


--pruebas unitarias--
ejecutar pruebas unitarias: python -m unittest tests/test_automata.py

pruebas unitarias con detalle: python -m unittest tests/test_automata.py -v


--probar api en postman--
1. ejecutar la app con: python main.py
2. crear un request en postman.
3. utilizar el método POST
4. URL: http://localhost:1804/process-automata
5. en body utilizar -> form-data.
6. agregar Key -> "file" (exactamente como esta escrito, con minuscula)
    -cambiamos el tipo de text a file 
    -en select file, selecciona el archivo: JSON_entry.json
7. presiona send y espera la respuesta
8. revisa la carpeta generated_diagrams paraver los diagramas que se generaron.

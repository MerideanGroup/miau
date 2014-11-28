# Miau (necesitamos un mejor nombre ;D)

## Requerimientos
- Python3.4
- Virtualenv

## Instalacion
- `pip install -r requierements.txt`


## Usage

- `python test.py`


### Extraer urls

Extrae una lista de urls dado un dominio. i.e queremos extraer articulos de celularis.com:

- `ruby extractor.rb URL >> archivo_donde_se_guardan urls`
   - i.e: `ruby extractor.rb http://www.celularis.com/\?utm_source\=self\&utm_medium\=nav\&utm_campaign\=Nav%2BBlogs%2BHeader >> celularis`

**nota**:

hacer `gem install anemone` primero ;).

### Scraper

Extrae contenido de todas las urls en el archivo `texts/finanzas` y las guarda en: `texts/finanzas.json`:

```
python scraper.py texts/finanzas texts/finanzas.json
```


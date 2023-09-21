#Notas
1. odoo 15 funciona con python 3.8
2. teniendo el entorno virtual levantado con las dependencias y postgres instalado (ver la documentacion de odoo) corro el siguiente comando
por primera vez
```sh
python3.8 odoo-bin --addons-path=addons -d [una base de datos] --limit-memory-hard 0 -i base
```
luego utilizo el siguiente
```sh
python3.8 odoo-bin --addons-path=addons -d [una base de datos] --limit-memory-hard 0 -u alumno
```

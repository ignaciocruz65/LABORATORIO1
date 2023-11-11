@echo off
echo Agregando cambios...
git add .
echo Cambios agregados correctamente.

echo Subiendo cambios...
git commit -m "Agregando cambios"
git push origin master
echo Cambios subidos correctamente.

echo Proceso completado.
pause
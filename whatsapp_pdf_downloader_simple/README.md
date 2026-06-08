# WhatsApp PDF Downloader Simple

Automatizacion local para Windows. No usa movil, no usa ADB y no intenta iniciar sesion.

## Objetivo

Con WhatsApp Business ya abierto en el ordenador en:

```text
Contenido multimedia > Documentos
```

El programa busca por imagen:

- `check.png`: el cuadradito/check de seleccion del documento.
- `download.png`: la flecha hacia abajo de descarga.

Luego hace:

```text
seleccionar PDFs visibles -> descargar -> esperar -> bajar lista -> repetir
```

Los PDFs descargados se mueven a:

```text
C:\ENTRADA_WHATSAPP\PDFS_ABRIL_MAYO_JUNIO
```

## Uso

1. Instala Python si no lo tienes.
2. Ejecuta `01_instalar.bat`.
3. Abre WhatsApp Business en `Contenido multimedia > Documentos`.
4. Ejecuta `02_capturar_imagenes.bat`.
5. Prueba una pantalla con `03_probar_una_pantalla.bat`.
6. Si funciona, ejecuta `04_ejecutar_500.bat`.

## Importante

- No tapes la ventana de WhatsApp mientras se ejecuta.
- Para abortar, mueve el raton a la esquina superior izquierda.
- Primero prueba una pantalla antes de hacer 500 repeticiones.
- Si no detecta bien, repite `02_capturar_imagenes.bat` y captura mejor el check y la flecha.

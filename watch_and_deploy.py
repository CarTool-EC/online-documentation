#!/usr/bin/env python3
"""
watch_and_deploy.py — Vigila la carpeta docs/ y reacciona a cada cambio.

Cada vez que guardas un .rst (o cualquier archivo dentro de docs/):
  1. Reconstruye el HTML con Sphinx.
  2. Usa -W --keep-going, es decir: cualquier warning se trata como error,
     pero sigue revisando el resto de páginas para mostrarte TODOS los
     problemas de una vez (no se detiene en el primero).
  3. Si el build sale limpio (sin errores ni warnings): te avisa "Build OK".
  4. Si además pasas --publish: publica automáticamente ese HTML en gh-pages.
  5. Si el build falla: NO publica nada, y te muestra el error en la terminal.

Uso:
  Solo comprobar que no hay errores mientras editas (recomendado mientras escribes):
    python watch_and_deploy.py

  Comprobar Y publicar automáticamente en gh-pages en cada guardado:
    python watch_and_deploy.py --publish

Requiere:
    pip install watchdog ghp-import
    (Sphinx y sus temas ya deberían estar instalados via requirements.txt)
"""

import subprocess
import sys
import time
from pathlib import Path

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

DOCS_DIR = "docs"
# IMPORTANTE: el build vive FUERA de docs/, para que el propio build
# no dispare nuevas reconstrucciones al escribir sus archivos ahi dentro.
BUILD_DIR = "_preview_build/html"


class DocsHandler(PatternMatchingEventHandler):
    def __init__(self, auto_publish: bool):
        # Vigila archivos de contenido y configuración típicos de Sphinx.
        # ignore_patterns es un cinturón de seguridad extra: aunque el build
        # ya vive fuera de docs/, esto evita sorpresas si algún día cambia
        # la configuración y el build vuelve a caer dentro de la carpeta vigilada.
        super().__init__(
            patterns=["*.rst", "*.md", "*.py", "*.css", "*.png", "*.jpg", "*.svg"],
            ignore_patterns=["*_build*", "*_preview_build*"],
            ignore_directories=True,
        )
        self.auto_publish = auto_publish
        self.busy = False  # evita que se solapen varios builds si guardas rápido

    def on_modified(self, event):
        self._trigger(event.src_path)

    def on_created(self, event):
        self._trigger(event.src_path)

    def _trigger(self, changed_path):
        if self.busy:
            return
        self.busy = True
        try:
            print(f"\n{'=' * 60}")
            print(f"Cambio detectado: {changed_path}")
            print("Construyendo documentacion...")

            result = subprocess.run(
                [
                    "sphinx-build",
                    "-b", "html",
                    "-q",                   # modo silencioso: solo muestra warnings/errores
                    "-W", "--keep-going",  # tratar warnings como error, sin detenerse
                    DOCS_DIR,
                    BUILD_DIR,
                ]
            )

            if result.returncode == 0:
                print("Build OK, sin errores ni warnings.")

                if self.auto_publish:
                    print("Publicando en gh-pages...")
                    publish = subprocess.run(
                        ["ghp-import", "-n", "-p", "-f", BUILD_DIR]
                    )
                    if publish.returncode == 0:
                        print("Publicado en gh-pages correctamente.")
                    else:
                        print("Fallo al publicar en gh-pages, revisa el mensaje de arriba.")
                else:
                    print("(Modo solo-comprobacion: no se publico nada. Usa --publish para publicar automaticamente)")
            else:
                print("El build tiene errores o warnings. Corrige el .rst y guarda de nuevo.")
                print("No se publico nada en gh-pages.")

        finally:
            self.busy = False


def main():
    auto_publish = "--publish" in sys.argv

    if not Path(DOCS_DIR).is_dir():
        print(f"No encuentro la carpeta '{DOCS_DIR}'. Ejecuta este script desde la raiz del repo.")
        sys.exit(1)

    observer = Observer()
    observer.schedule(DocsHandler(auto_publish), path=DOCS_DIR, recursive=True)
    observer.start()

    modo = "COMPROBAR + PUBLICAR" if auto_publish else "SOLO COMPROBAR"
    print(f"Vigilando cambios en '{DOCS_DIR}/' -- modo: {modo}")
    print("Guarda cualquier .rst para probar. Ctrl+C para salir.\n")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nDeteniendo vigilancia...")
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
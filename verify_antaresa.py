from __future__ import annotations

import json
import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HTML = ROOT / "index.html"

class Parser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.images: list[tuple[str, str]] = []
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        if "id" in data and data["id"]:
            self.ids.append(data["id"])
        if tag == "img":
            self.images.append((data.get("src", ""), data.get("alt", "")))
        if tag in {"a", "link", "script"}:
            value = data.get("href") or data.get("src")
            if value:
                self.links.append(value)


def local_asset(url: str) -> bool:
    return not url.startswith(("http://", "https://", "mailto:", "tel:", "data:", "#", "javascript:"))


def run(cmd: list[str]) -> None:
    result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        raise SystemExit(result.returncode)


def main() -> None:
    if not HTML.exists():
        raise SystemExit("No existe index.html")
    html = HTML.read_text(encoding="utf-8")

    # Extract normal scripts, excluding JSON-LD.
    scripts = re.findall(r"<script(?![^>]*application/ld\+json)[^>]*>(.*?)</script>", html, re.S)
    tmp_js = ROOT / ".antaresa-extracted.js"
    tmp_js.write_text("\n".join(scripts), encoding="utf-8")
    try:
        run(["node", "--check", str(tmp_js)])
        run(["node", "--check", "service-worker.js"])
    finally:
        tmp_js.unlink(missing_ok=True)

    parser = Parser()
    parser.feed(html)
    parser.close()

    duplicate_ids = sorted({item for item in parser.ids if parser.ids.count(item) > 1})
    if duplicate_ids:
        raise SystemExit(f"IDs duplicados: {duplicate_ids}")

    missing: list[str] = []
    for url in re.findall(r"(?:src|href)=\"([^\"]+)\"", html):
        if local_asset(url) and (url.startswith("assets/") or url in {"manifest.webmanifest", "service-worker.js"}):
            if not (ROOT / url).exists():
                missing.append(url)
    if missing:
        raise SystemExit(f"Assets faltantes: {missing}")

    empty_alt = [src for src, alt in parser.images if not alt.strip() and "detailImage" not in html]
    if empty_alt:
        raise SystemExit(f"Imágenes sin alt: {empty_alt}")

    required_tokens = [
        'id="catalogo"',
        'id="club"',
        'id="eventos"',
        'id="qr-mesa"',
        'id="opiniones"',
        'id="reservas"',
        'id="detailModal"',
        'id="checkoutWhatsApp"',
        'data-whatsapp="general"',
        'application/ld+json',
        'Av. Españasa entre 9 dejulios y Alemse',
        'id="adminPanel"',
        'id="adminLauncher"',
        'ADMIN_PIN',
        'ADMIN_STORAGE_KEY',
        'adminExport',
        'adminApplyBulk',
    ]
    missing_tokens = [token for token in required_tokens if token not in html]
    if missing_tokens:
        raise SystemExit(f"Faltan tokens requeridos: {missing_tokens}")

    product_count = len(re.findall(r'<article class="menu-card"', html.split('<script>')[0]))
    menu_images = sorted(set(re.findall(r'assets/(menu-[^"\']+\.jpg)', html)))
    if len(menu_images) < 20:
        raise SystemExit(f"Imágenes nuevas insuficientes: {len(menu_images)}")
    if product_count < 32:
        raise SystemExit(f"Catálogo insuficiente: {product_count} productos")

    with open(ROOT / "manifest.webmanifest", encoding="utf-8") as file:
        manifest = json.load(file)
    if manifest.get("short_name") != "ANTARESa":
        raise SystemExit("Manifest short_name incorrecto")

    print("QA OK · ANTARESa verificado")
    print(f"Productos: {product_count}")
    print(f"Imágenes nuevas de menú: {len(menu_images)}")
    print(f"IDs únicos: {len(parser.ids)}")
    print("Assets locales: OK")
    print("JS index/service-worker: OK")
    print("Manifest: OK")

if __name__ == "__main__":
    main()

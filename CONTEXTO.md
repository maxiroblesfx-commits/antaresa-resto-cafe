# CONTEXTO — ANTARESa (RestoBar Antaresa)

## Qué es
Web premium de una sola página para **ANTARESa · Resto Café de Autor**: catálogo digital ampliado (carta), pedidos por WhatsApp, reservas, QR de mesa y experiencia mobile-first. Es el proyecto "RestoBar Antaresa" (que no estaba en la carpeta Antigravity, sino acá).

Es un sitio estático premium (HTML/CSS/JS embebidos, sin frameworks ni build), instalable como PWA, pensado para que un resto-café opere su carta y reciba pedidos/reservas sin app ni backend, todo vía WhatsApp.

## Estructura del proyecto
- `index.html` — página completa (~3460 líneas), con CSS y JavaScript embebidos (incluye el Panel Admin).
- `manifest.webmanifest` — configuración PWA instalable.
- `service-worker.js` — cache offline básico de assets locales.
- `verify_antaresa.py` — script de auditoría técnica del proyecto (valida assets, sintaxis, conteo de productos).
- `IMAGE_CREDITS.md` — créditos/origen de las imágenes demo (generadas para ANTARESa + Wikimedia Commons).
- `assets/` — identidad y catálogo: hero, perfil de marca, favicon, QR de mesa premium, y ~20 fotos `menu-*.jpg` de productos demo.
- `README.md` — documentación completa de personalizaciones, mejoras y verificación.

## Stack
HTML/CSS/JS vanilla (sin dependencias, sin build) + PWA (manifest + service worker). Paleta premium espresso/cobre/oro/oliva. Datos de la carta persistidos en `localStorage` (operación demo/local).

## Qué está hecho
- **Carta de 32 productos demo** con 20 imágenes nuevas (bebidas, brunch, comidas, aperitivos, pastelería), precios de referencia en pesos argentinos.
- **Pedidos por WhatsApp:** carrito con cantidades, total y envío del pedido por `wa.me` con mensaje prearmado; recomendaciones de upselling en el carrito.
- **Reservas por WhatsApp:** nombre, fecha, horario, personas y comentario; sin fechas pasadas; estado abierto/cerrado dinámico según horarios.
- **Panel Admin sin tocar código** (dentro de la web): se abre con el link "Panel admin" del pie, atajo `Ctrl+Shift+A` o `#admin` en la URL. PIN demo: `antaresa2026`. Permite alta/edición/duplicado/ocultar productos, ajuste masivo de precios por %, export/import JSON de la carta y preview. Guarda en `localStorage`.
- **Experiencia premium:** modal de detalle por producto (maridaje, perfil, alérgenos, tiempo, tags), favoritos persistentes, filtros (Veggie, 0.0 alcohol, Favoritos, Livianos), galería (ambiente/platos), FAQ con acordeón.
- **Comercial:** Club ANTARESa (captura de email + código `ANTARES10`), sección de Eventos/Catering, testimonios de prueba social, QR de mesa descargable para imprimir.
- **Técnico:** SEO (canonical, Open Graph apaisado, JSON-LD Restaurant + FAQPage), PWA (manifest + service worker), impresión optimizada de carta, lazy-loading + `decoding="async"` en imágenes.
- **Verificación realizada:** `node --check` sobre el JS de `index.html` y `service-worker.js`, parseo HTML, validación del manifest, assets locales sin faltantes, conteo confirmado de 32 productos y 20 imágenes nuevas.

## Qué quedaba pendiente
Todo es para pasar a producción (hoy hay placeholders demo):
1. Reemplazar el teléfono demo `5491112345678` por el WhatsApp real (en `CONFIG` dentro de `index.html`).
2. Completar la **dirección real** del local (hoy "a confirmar"): en `CONFIG.address`, el schema y el link de Google Maps.
3. Reemplazar la URL del menú `https://antaresa.com/menu` por la final publicada.
4. Ajustar redes (Instagram demo `@antaresa.cafe`), horarios definitivos y precios/productos reales.
5. Revisar `IMAGE_CREDITS.md` y reemplazar imágenes demo de terceros por fotos propias del local antes de uso comercial.
6. Cargar fotos reales en la sección Galería (ambiente y platos).
7. **Persistencia global:** el Panel Admin guarda en `localStorage` (solo en ese navegador/dispositivo). Para que los cambios de carta sean globales entre dispositivos, conectar a un backend/CMS (Firebase, Supabase, Google Sheets, etc.).

## Estado de git
Repositorio ya inicializado, con historial activo y árbol de trabajo limpio. Último commit previo: `c11698f feat: galería, FAQ con schema, lazy-loading y SEO para cerrar la venta`. Solo se agregó y commiteó este CONTEXTO.md.

---
*Documento de contexto generado el 16/06/2026.*

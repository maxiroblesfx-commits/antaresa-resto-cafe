# CONTEXTO — ANTARESa (RestoBar Antaresa)

<!-- ENCABEZADO FIJO -->
| Campo | Valor |
|---|---|
| **Proyecto** | ANTARESa · Resto Café de Autor (web premium PWA, demo RestoBar) |
| **Ruta absoluta** | `C:\Users\Flia.Robles\Desktop\ANTARESA` |
| **Deploy** | GitHub Pages — https://maxiroblesfx-commits.github.io/antaresa-resto-cafe/ |
| **Repo** | GitHub `maxiroblesfx-commits/antaresa-resto-cafe` (rama `main`) |
| **Estado de git** | Repo con remoto. Rama `main`, **1 commit adelante de origin** (CONTEXTO.md sin pushear). |
| **Última actualización** | 2026-06-16 |
<!-- /ENCABEZADO FIJO -->

> Última actualización: 2026-06-16 · Estado: **LIVE en GitHub Pages**, demo premium presentable a cliente. Pendiente sólo datos reales del negocio.

## Qué es
Web premium de una sola página para **ANTARESa · Resto Café de Autor**: catálogo digital ampliado (carta), pedidos por WhatsApp, reservas, QR de mesa y experiencia mobile-first. Es el proyecto "RestoBar Antaresa" (que no estaba en la carpeta Antigravity como sugería una consigna, sino acá, en su propia carpeta).

Es un sitio estático premium (HTML/CSS/JS embebidos, sin frameworks ni build), instalable como PWA, pensado para que un resto-café opere su carta y reciba pedidos/reservas sin app ni backend, todo vía WhatsApp. Sirve como **modelo de negocio para mostrar a potenciales clientes de RestoBar** (vía MR Soluciones).

**Repo GitHub:** `maxiroblesfx-commits/antaresa-resto-cafe` (público, individual, totalmente independiente del pelotero Veo Veo).
**URL en producción:** https://maxiroblesfx-commits.github.io/antaresa-resto-cafe/ (live, HTTPS, redeploy en cada push).

## Decisiones tomadas
- **Pulido fino, NO rediseño:** al auditarlo en vivo (desktop/tablet/mobile) ya estaba premium, responsive, sin overflow ni errores de consola. Se decidió pulir, no rehacer.
- **Proyecto 100% separado de Veo Veo:** repo git propio, nunca se mezcló nada con el pelotero. (Nota: la barra del editor mostraba "veo-veo-diversiones main" porque ese era el directorio principal de la sesión; ANTARESA entró como carpeta adicional pero quedó aparte.)
- **Dirección rota → placeholder neutro:** el README tenía una dirección real con typos ("Av. Españasa entre 9 dejulios y Alemse"). No se inventó una falsa; se puso `Dirección del local · a confirmar` hasta tener la correcta.
- **Palabra "demo/ejemplo" quitada de la copia pública** (restaba impacto premium ante un cliente); se dejó dentro del panel admin privado donde es legítima.
- **Acceso Admin movido al footer** (link discreto "Panel admin") en vez de un botón flotante visible — no es algo que deba ver el cliente final.
- **Sobre "control remoto":** el usuario preguntó por controlar la PC a distancia; se aclaró que Claude Code web (claude.ai/code) corre en la nube sobre los repos de GitHub (no controla esta PC). Por eso fue clave subir los proyectos a GitHub.

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

## Bugs / problemas resueltos
- **Dirección con texto basura** en 4 lugares (schema, contacto, `CONFIG.address`, `CONFIG.mapUrl`) → placeholder neutro `a confirmar`; el mapUrl ahora busca la marca en Maps.
- **Capa de botones flotantes chocaba con el contenido** (lo que hacía "sentir" la página mal diseñada): el strip de 4 iconos de la izquierda se montaba sobre tarjetas del hero/especialidades/catálogo/contacto, y el botón **ADMIN tapaba el CTA "Enviar reserva por WhatsApp"**. → Se quitó el strip (sus accesos ya están en nav/hero/contacto/catálogo) y se movió Admin al footer. Verificado con screenshots antes/después.
- **Quick-actions amontonadas en mobile** (≤640px) → ocultas en mobile (estaban duplicadas en otros lados).
- **Reservas permitían fechas pasadas** → `min` = hoy.
- **Estado "Abierto/Cerrado" quedaba congelado** si la página seguía abierta → se refresca cada 60s.
- **Horario de madrugada (franja 00:00–00:30 tras viernes/sábado) mostraba "Cerrado"** por error de cruce de medianoche → corregido; probado con 7 casos de horario.
- **CTAs WhatsApp/Reservar se ocultaban en el menú mobile** → agregados dentro del menú hamburguesa (visibles solo en mobile).
- **og:image cuadrada** (logo) poco vendedora al compartir → cambiada a la foto apaisada del hero (1376×768) + Twitter meta + canonical.
- **Service worker (PWA) cacheaba fuerte** y servía la versión vieja al actualizar → gotcha conocido: hacer **Ctrl+Shift+R** o incógnito tras cada deploy.

## Mejoras para "cerrar venta" agregadas
- **Galería** (ambiente + platos, masonry, lazy-load).
- **FAQ** con acordeón + schema **FAQPage** (rich results en Google).
- Lazy-loading en las 32 imágenes del catálogo.
- Canonical + Open Graph apaisado.

## Qué quedaba pendiente
Todo es para pasar a producción (hoy hay placeholders demo):
1. Reemplazar el teléfono demo `5491112345678` por el WhatsApp real (en `CONFIG` dentro de `index.html`).
2. Completar la **dirección real** del local (hoy "a confirmar"): en `CONFIG.address`, el schema y el link de Google Maps.
3. Reemplazar la URL del menú `https://antaresa.com/menu` por la final publicada.
4. Ajustar redes (Instagram demo `@antaresa.cafe`), horarios definitivos y precios/productos reales.
5. Revisar `IMAGE_CREDITS.md` y reemplazar imágenes demo de terceros por fotos propias del local antes de uso comercial.
6. Cargar fotos reales en la sección Galería (ambiente y platos).
7. **Persistencia global:** el Panel Admin guarda en `localStorage` (solo en ese navegador/dispositivo). Para que los cambios de carta sean globales entre dispositivos, conectar a un backend/CMS (Firebase, Supabase, Google Sheets, etc.).
8. **Fotos repetidas en el catálogo:** varias tarjetas de bebidas/brunch comparten la misma foto. Es falta de assets, no código; se reemplazan desde el panel admin (campo Imagen) con fotos reales.
9. **Seguridad del panel Admin:** el PIN `antaresa2026` está hardcodeado client-side. Para una demo está perfecto (el README lo aclara); para producción real necesita backend.

## Próximos pasos concretos
1. Cuando haya cliente: cargar **datos reales** (WhatsApp, dirección, URL del menú, Instagram, horarios, precios/productos) en el objeto `CONFIG` de `index.html`.
2. Reemplazar **fotos demo por fotos propias** del local y los platos (desde el panel admin).
3. Opcional: **dominio propio** (ej. `antaresa.com.ar`) apuntado a GitHub Pages.
4. Opcional: (1 pág.) guía de presentación al cliente (qué incluye, beneficios, cómo lo maneja).
5. Para producción real del admin: backend para persistencia global + auth real.

## Estado de git
Repo en GitHub `maxiroblesfx-commits/antaresa-resto-cafe` (público), historial activo, árbol limpio. Último commit: `abccea1 docs: agrega CONTEXTO.md`. Commits clave: `139dd35` (repo inicial + pulido), `4802847` (fechas/estado), `62605e9` (preview social/CTAs/horario), `e79c30d` (fix colisión capa flotante), `c11698f` (galería/FAQ/SEO para cerrar venta).

---

## CÓMO RETOMAR

3 próximos pasos concretos para la próxima sesión:

1. **Cargar datos reales del negocio** en el objeto `CONFIG` de `index.html`: WhatsApp real (hoy `5491112345678`), dirección (hoy "a confirmar"), URL del menú, Instagram, horarios y precios/productos.
2. **Reemplazar las fotos demo** por fotos propias del local y los platos (desde el Panel Admin, campo Imagen) y revisar `IMAGE_CREDITS.md`.
3. **Hacer `git push`** de `main` a GitHub (queda 1 commit local sin subir) para que GitHub Pages redespliegue.

---
*Combina las transcripciones de auditoría/pulido/venta con el estado real del código, el deploy y git.*

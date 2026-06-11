# ANTARESa · Catálogo digital premium

Web premium de una página para **ANTARESa · Resto Café de Autor**, con catálogo digital ampliado, identidad visual, pedidos por WhatsApp, reservas, QR de mesa, experiencia mobile-first y assets gastronómicos coherentes con el rubro.

## Archivos principales

- `index.html` — página web completa, responsive, con CSS y JavaScript embebidos.
- `manifest.webmanifest` — configuración PWA instalable.
- `service-worker.js` — cache offline básico para assets locales.
- `verify_antaresa.py` — auditoría técnica del proyecto.
- `IMAGE_CREDITS.md` — créditos/origen de imágenes adicionales de demo.
- `assets/profile-antaresa.png` — imagen de perfil creada para la marca ANTARESa.
- `assets/favicon.png` — ícono del sitio.
- `assets/qr-menu-antaresa.png` — QR premium de ejemplo para mesa.
- `assets/hero-antaresa.jpg` — imagen hero gastronómica.
- `assets/coffee-drinks.jpg` — imagen de bebidas/café.
- `assets/food-brunch.jpg` — imagen de comidas/brunch.
- `assets/dessert-bar.jpg` — imagen de pastelería/postres.
- `assets/menu-*.jpg` — 20 imágenes nuevas para productos demo del menú.

## Personalizaciones implementadas

- Carta ampliada a **32 productos demo**.
- **20 imágenes adicionales** para nuevas opciones de bebidas, brunch, comidas, aperitivos y pastelería.
- Dirección: **placeholder "a confirmar"** (se completa con la dirección real del local antes de publicar, en `CONFIG.address`, el schema y el link de Maps).
- Precios de referencia en pesos argentinos.
- WhatsApp conectado a links `wa.me` con mensajes prearmados.
- Instagram demo: `@antaresa.cafe`.
- Link a Google Maps con búsqueda del local y la dirección cargada.
- Horarios visibles y estado abierto/cerrado dinámico.
- Reserva por WhatsApp con nombre, fecha, horario, personas y comentario.
- Pedido avanzado desde carrito con cantidades, total y envío por WhatsApp.

> Para datos reales, editar el objeto `CONFIG` dentro de `index.html`: teléfono, Instagram, URL del menú, dirección, mapa y horarios.

## Nuevos productos demo agregados

1. Cold Brew Naranja & Canela.
2. Matcha Latte Ceremonial.
3. Chai Especiado ANTARESa.
4. Limonada de Frutos Rojos.
5. Copa Malbec & Tapas.
6. Shakshuka de la Casa.
7. Croque Madame Premium.
8. Bagel de Salmón Ahumado.
9. Omelette Trufado.
10. Focaccia Caprese.
11. Polenta Cremosa & Hongos.
12. Risotto de Hongos.
13. Burger Bistro ANTARESa.
14. Ensalada de Peras & Azul.
15. Sopa de Calabaza Asada.
16. Carrot Cake de la Casa.
17. Tiramisú al Café.
18. Pavlova de Frutos Rojos.
19. Alfajor Sablé Premium.
20. Panna Cotta de Vainilla.


## Nueva etapa: panel Admin sin tocar código

Se agregó un **Panel Admin ANTARESa** dentro de la propia web para poder cambiar carta y precios sin editar HTML/JS.

### Cómo abrirlo

- Botón flotante **Admin** en la web.
- Atajo: `Ctrl + Shift + A`.
- URL directa: abrir la página con `#admin` al final.

### PIN demo

```txt
antaresa2026
```

> Importante: este panel es una solución estática/local. Guarda cambios en `localStorage` del navegador. Para que los cambios sean globales entre dispositivos se debería conectar a un backend, Google Sheets, Firebase, Supabase o un CMS.

### Qué permite editar

- Nombre del producto.
- Precio.
- Categorías/filtros.
- Etiqueta visual.
- Descripción comercial.
- Imagen usando assets existentes o URL.
- Texto alternativo.
- Tags.
- Medida/nota del producto.
- Palabras de búsqueda.
- Maridaje.
- Perfil de sabor.
- Alérgenos.
- Tiempo estimado.
- Visibilidad en carta.

## 10 mejoras nuevas implementadas en esta etapa

1. **Panel Admin premium con PIN** para gestionar la carta sin tocar código.
2. **Editor completo de producto**: nombre, precio, descripción, tags, categorías e imagen.
3. **Publicación instantánea**: al guardar, la carta pública se actualiza en vivo.
4. **Persistencia local** mediante `localStorage`, útil para pruebas y operación demo.
5. **Alta de productos nuevos** desde el panel.
6. **Duplicado de productos** para cargar variantes rápidamente.
7. **Eliminar/ocultar productos** sin borrar código.
8. **Ajuste masivo de precios por porcentaje** para actualizar la carta completa.
9. **Exportar/importar JSON** para backup o migración de carta.
10. **Preview visual del producto** antes de publicarlo, con selector de imágenes existentes.

## 10 mejoras premium adicionales implementadas por el equipo

1. **Detalle premium de producto**  
   Modal por producto con maridaje, perfil, alérgenos, tiempo estimado y tags.

2. **Favoritos persistentes**  
   Cada producto puede guardarse como favorito usando `localStorage`.

3. **Filtros inteligentes**  
   Chips rápidos: Veggie, 0.0 alcohol, Favoritos y Livianos.

4. **Recomendaciones inteligentes en carrito**  
   Sugerencias de alto ticket para sumar productos complementarios.

5. **Checkout directo por WhatsApp**  
   El carrito genera un mensaje listo con cantidades y total estimado.

6. **QR de mesa descargable**  
   Asset `assets/qr-menu-antaresa.png` listo para imprimir y usar como demo.

7. **Club ANTARESa**  
   Captura de email con código de bienvenida `ANTARES10`.

8. **Eventos y catering**  
   Sección comercial para cotizar eventos privados, lanzamientos y desayunos corporativos.

9. **Prueba social / testimonios**  
   Reseñas de ejemplo para reforzar confianza y percepción premium.

10. **SEO + PWA + print menu**  
   Open Graph, JSON-LD Restaurant, manifest, service worker e impresión optimizada de carta.

## Equipo de agentes conceptuales utilizado

1. **CEO / Director de Proyecto (+20 años)** — coordinación general, calidad, foco comercial y coherencia final.
2. **Director de Marca Gastronómica (+20 años)** — identidad visual, tono premium, paleta espresso/cobre/oro/oliva.
3. **UX/UI Designer Premium (+20 años)** — arquitectura, navegación, mobile-first, filtros, carrito y CTAs.
4. **Food Stylist & Art Director (+20 años)** — coherencia visual de imágenes de café, brunch, bebidas y pastelería.
5. **Front-End Developer Senior (+20 años)** — implementación responsive, JS sin dependencias, PWA y performance.
6. **Copywriter Gastronómico (+20 años)** — descripciones de carta, secciones comerciales y narrativa de marca.
7. **Especialista en Conversión Horeca (+20 años)** — ticket promedio, upselling, WhatsApp y reservas.
8. **QA / Auditor de Calidad (+20 años)** — validación de enlaces, assets, sintaxis, coherencia y usabilidad.

## Verificación realizada

- Sintaxis JavaScript de `index.html` validada con `node --check`.
- Sintaxis JavaScript de `service-worker.js` validada con `node --check`.
- Parseo HTML básico validado con `html.parser`.
- Verificación de assets locales referenciados: sin archivos faltantes.
- Manifest JSON validado.
- Revisión de secciones clave: catálogo, club, eventos, QR, opiniones, reservas y modal de producto.
- Confirmación de **32 productos** en catálogo.
- Confirmación de **20 imágenes nuevas** de menú referenciadas en la carta.
- Confirmación de panel Admin, PIN demo, export/import y edición sin tocar código.

## Próximos ajustes recomendados cuando tengas datos reales

- Reemplazar el teléfono demo `5491112345678` por el WhatsApp real.
- Reemplazar `https://antaresa.com/menu` por la URL final publicada.
- Ajustar redes, horarios definitivos y precios/productos reales.
- Revisar `IMAGE_CREDITS.md` antes de uso comercial definitivo de imágenes demo provenientes de terceros.

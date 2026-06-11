const CACHE_NAME = 'antaresa-premium-v4';
const ASSETS = [
  './',
  './index.html',
  './manifest.webmanifest',
  './assets/profile-antaresa.png',
  './assets/favicon.png',
  './assets/hero-antaresa.jpg',
  './assets/coffee-drinks.jpg',
  './assets/food-brunch.jpg',
  './assets/dessert-bar.jpg',
  './assets/qr-menu-antaresa.png',
  './assets/menu-alfajor-sable.jpg',
  './assets/menu-bagel-salmon.jpg',
  './assets/menu-burger-bistro.jpg',
  './assets/menu-carrot-cake.jpg',
  './assets/menu-chai-especiado.jpg',
  './assets/menu-cold-brew-naranja.jpg',
  './assets/menu-copa-malbec-tapas.jpg',
  './assets/menu-croque-madame.jpg',
  './assets/menu-ensalada-peras-azules.jpg',
  './assets/menu-focaccia-caprese.jpg',
  './assets/menu-hongos-polenta.jpg',
  './assets/menu-limonada-frutos-rojos.jpg',
  './assets/menu-matcha-latte.jpg',
  './assets/menu-omelette-trufado.jpg',
  './assets/menu-panna-cotta.jpg',
  './assets/menu-pavlova-frutos-rojos.jpg',
  './assets/menu-risotto-hongos.jpg',
  './assets/menu-shakshuka.jpg',
  './assets/menu-sopa-calabaza.jpg',
  './assets/menu-tiramisu-cafe.jpg'
];

self.addEventListener('install', event => {
  event.waitUntil(caches.open(CACHE_NAME).then(cache => cache.addAll(ASSETS)));
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => Promise.all(keys.filter(key => key !== CACHE_NAME).map(key => caches.delete(key))))
  );
  self.clients.claim();
});

self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;
  event.respondWith(
    caches.match(event.request).then(cached => cached || fetch(event.request).catch(() => caches.match('./index.html')))
  );
});

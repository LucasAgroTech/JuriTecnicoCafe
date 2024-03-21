var CACHE_NAME = 'meu-app-cache-v1';
var urlsToCache = [

  // Adicione outros recursos que deseja armazenar em cache
];

self.addEventListener('install', function(event) {
  // Realiza o cache dos arquivos
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request)
      .then(function(response) {
        // Retorna os recursos do cache ou busca na rede se não estiver em cache
        return response || fetch(event.request);
      }
    )
  );
});

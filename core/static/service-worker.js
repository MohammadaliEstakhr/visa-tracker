self.addEventListener("install", function (event) {
  console.log("Service Worker installing.");
});

self.addEventListener("fetch", function (event) {
  event.respondWith(fetch(event.request));
});

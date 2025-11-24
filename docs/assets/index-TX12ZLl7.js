(function () {
  const e = document.createElement("link").relList;
  if (e && e.supports && e.supports("modulepreload")) return;
  for (const t of document.querySelectorAll('link[rel="modulepreload"]')) r(t);
  new MutationObserver((t) => {
    for (const i of t)
      if (i.type === "childList")
        for (const u of i.addedNodes)
          u.tagName === "LINK" && u.rel === "modulepreload" && r(u);
  }).observe(document, { childList: !0, subtree: !0 });
  function s(t) {
    const i = {};
    return (
      t.integrity && (i.integrity = t.integrity),
      t.referrerPolicy && (i.referrerPolicy = t.referrerPolicy),
      t.crossOrigin === "use-credentials"
        ? (i.credentials = "include")
        : t.crossOrigin === "anonymous"
          ? (i.credentials = "omit")
          : (i.credentials = "same-origin"),
      i
    );
  }
  function r(t) {
    if (t.ep) return;
    t.ep = !0;
    const i = s(t);
    fetch(t.href, i);
  }
})();
const o = {
    images: [],
    zoom: 1,
    pan: { x: 0, y: 0 },
    isDragging: !1,
    dragStart: { x: 0, y: 0 },
    currentImageIndex: null,
  },
  p = document.getElementById("gallery"),
  y = document.getElementById("empty-state"),
  l = document.getElementById("lightbox"),
  d = document.getElementById("lightbox-img"),
  L = document.getElementById("close-lightbox"),
  m = document.getElementById("zoom-in"),
  g = document.getElementById("zoom-out"),
  v = document.getElementById("zoom-level");
console.log("Image Viewer initialized");
function w() {
  (["dragenter", "dragover", "dragleave", "drop"].forEach((e) => {
    document.body.addEventListener(e, z, !1);
  }),
    ["dragenter", "dragover"].forEach((e) => {
      document.body.addEventListener(e, D, !1);
    }),
    ["dragleave", "drop"].forEach((e) => {
      document.body.addEventListener(e, B, !1);
    }),
    document.body.addEventListener("drop", k, !1));
}
function z(n) {
  (n.preventDefault(), n.stopPropagation());
}
function D() {
  document.body.classList.add("drop-active");
}
function B() {
  document.body.classList.remove("drop-active");
}
function k(n) {
  const e = n.dataTransfer,
    s = e.items;
  if (s)
    for (let r = 0; r < s.length; r++) {
      const t = s[r].webkitGetAsEntry();
      t && b(t);
    }
  else {
    const r = [...e.files];
    E(r);
  }
}
function b(n) {
  if (n.isFile)
    n.file((e) => {
      E([e]);
    });
  else if (n.isDirectory) {
    const e = n.createReader(),
      s = () => {
        e.readEntries((r) => {
          r.length !== 0 && (r.forEach((t) => b(t)), s());
        });
      };
    s();
  }
}
function E(n) {
  const e = n.filter(
    (s) => s.type.startsWith("image/") || s.type.startsWith("video/"),
  );
  e.length !== 0 &&
    e.forEach((s) => {
      const r = new FileReader();
      (r.readAsDataURL(s),
        (r.onloadend = function () {
          const t = s.type.startsWith("video/"),
            i = {
              src: r.result,
              name: s.name,
              type: t ? "video" : "image",
              id: Date.now() + Math.random().toString(36).substr(2, 9),
            };
          (o.images.push(i), A());
        }));
    });
}
function A() {
  (o.images.length > 0
    ? (y.style.display = "none")
    : (y.style.display = "flex"),
    p.querySelectorAll(".gallery-item").forEach((e) => e.remove()),
    o.images.forEach((e, s) => {
      const r = document.createElement("div");
      if (
        ((r.className = "gallery-item"),
        (r.onclick = () => x(s)),
        e.type === "video")
      ) {
        const t = document.createElement("video");
        ((t.src = e.src),
          (t.muted = !0),
          (t.loop = !0),
          (t.onmouseover = () => t.play()),
          (t.onmouseout = () => {
            (t.pause(), (t.currentTime = 0));
          }),
          r.appendChild(t));
        const i = document.createElement("div");
        ((i.innerHTML = "▶"),
          (i.style.cssText =
            "position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; font-size: 2rem; pointer-events: none; text-shadow: 0 2px 4px rgba(0,0,0,0.5);"),
          r.appendChild(i));
      } else {
        const t = document.createElement("img");
        ((t.src = e.src),
          (t.alt = e.name),
          (t.loading = "lazy"),
          r.appendChild(t));
      }
      p.appendChild(r);
    }));
}
w();
const a = document.getElementById("lightbox-video");
function x(n) {
  o.currentImageIndex = n;
  const e = o.images[n];
  ((o.zoom = 1),
    (o.pan = { x: 0, y: 0 }),
    e.type === "video"
      ? ((d.style.display = "none"),
        (a.style.display = "block"),
        (a.src = e.src),
        a.play(),
        (m.disabled = !0),
        (g.disabled = !0),
        (v.textContent = ""),
        (a.style.cursor = "default"),
        (a.style.transform = "none"))
      : ((a.style.display = "none"),
        a.pause(),
        (a.src = ""),
        (d.style.display = "block"),
        (d.src = e.src),
        (d.alt = e.name),
        (m.disabled = !1),
        (g.disabled = !1),
        f()),
    l.classList.add("active"),
    l.setAttribute("aria-hidden", "false"),
    (document.body.style.overflow = "hidden"));
}
function I() {
  (l.classList.remove("active"),
    l.setAttribute("aria-hidden", "true"),
    (document.body.style.overflow = ""),
    (o.currentImageIndex = null),
    a.pause(),
    (a.src = ""));
}
function f() {
  o.images[o.currentImageIndex]?.type !== "video" &&
    ((d.style.transform = `translate(${o.pan.x}px, ${o.pan.y}px) scale(${o.zoom})`),
    (v.textContent = `${Math.round(o.zoom * 100)}%`),
    o.zoom > 1
      ? (d.style.cursor = o.isDragging ? "grabbing" : "grab")
      : (d.style.cursor = "default"));
}
function c(n) {
  const e = o.zoom + n;
  e >= 0.1 && e <= 5 && ((o.zoom = e), f());
}
L.addEventListener("click", I);
m.addEventListener("click", () => c(0.1));
g.addEventListener("click", () => c(-0.1));
document.addEventListener("keydown", (n) => {
  if (l.classList.contains("active"))
    switch (n.key) {
      case "Escape":
        I();
        break;
      case "ArrowLeft":
        h(-1);
        break;
      case "ArrowRight":
        h(1);
        break;
      case "+":
      case "=":
        c(0.1);
        break;
      case "-":
      case "_":
        c(-0.1);
        break;
    }
});
function h(n) {
  if (o.currentImageIndex === null) return;
  let e = o.currentImageIndex + n;
  (e < 0 && (e = o.images.length - 1), e >= o.images.length && (e = 0), x(e));
}
l.addEventListener(
  "wheel",
  (n) => {
    n.preventDefault();
    const e = n.deltaY > 0 ? -0.1 : 0.1;
    c(e);
  },
  { passive: !1 },
);
d.addEventListener("mousedown", (n) => {
  o.zoom <= 1 ||
    (n.preventDefault(),
    (o.isDragging = !0),
    (o.dragStart = { x: n.clientX - o.pan.x, y: n.clientY - o.pan.y }),
    d.classList.add("grabbing"));
});
window.addEventListener("mousemove", (n) => {
  o.isDragging &&
    (n.preventDefault(),
    (o.pan.x = n.clientX - o.dragStart.x),
    (o.pan.y = n.clientY - o.dragStart.y),
    f());
});
window.addEventListener("mouseup", () => {
  ((o.isDragging = !1), d.classList.remove("grabbing"));
});

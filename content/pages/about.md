---
title: "About me"
url: "/about/"
author: "⠀"
hidemeta: true
disableShare: true
searchHidden: true
---

i like norepinephrine.

<div class="pg-section">
  <!-- Hero Showcase Banner -->
  <div class="pg-hero">
    <div class="pg-hero-header">
      <div class="pg-title-group">
        <h2>
          <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="color: #6366f1;">
            <path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z"></path>
            <circle cx="12" cy="13" r="3"></circle>
          </svg>
          <span class="pg-title-gradient">Visual Stories & Frames</span>
        </h2>
        <p class="pg-subtitle">Capturing light, shadows, and fleeting moments across cityscapes and wilderness. Welcome to my personal photograph exhibition gallery.</p>
      </div>
    </div>

    <div class="pg-stats-bar">
      <div class="pg-stat-chip">
        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"></path><circle cx="12" cy="13" r="4"></circle></svg>
        <span id="statCount">6 Shots Captured</span>
      </div>
      <div class="pg-stat-chip">
        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
        <span>Global Locations</span>
      </div>
      <div class="pg-stat-chip">
        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
        <span>RAW & 35mm Format</span>
      </div>
      <div class="pg-stat-chip">
        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
        <span>High-Res Master</span>
      </div>
    </div>
  </div>

  <!-- Controls & Category Filters -->
  <div class="pg-controls-bar">
    <div class="pg-controls-top">
      <div class="pg-filter-tabs" id="pgFilterTabs">
        <button class="pg-tab-btn active" data-category="all">All Photos</button>
        <button class="pg-tab-btn" data-category="urban">Urban & City</button>
        <button class="pg-tab-btn" data-category="nature">Nature & Wilderness</button>
        <button class="pg-tab-btn" data-category="street">Street & Mood</button>
        <button class="pg-tab-btn" data-category="architecture">Architecture</button>
        <button class="pg-tab-btn" data-category="night">Night & Astrophotography</button>
      </div>

      <div class="pg-tools-right">
        <div class="pg-search-box">
          <svg class="pg-search-icon" xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          <input type="text" class="pg-search-input" id="pgSearchInput" placeholder="Search photos..." />
        </div>

        <div class="pg-view-switcher">
          <button class="pg-view-btn active" id="btnViewMasonry" title="Pinterest Masonry View">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="9"></rect><rect x="14" y="3" width="7" height="5"></rect><rect x="14" y="12" width="7" height="9"></rect><rect x="3" y="16" width="7" height="5"></rect></svg>
          </button>
          <button class="pg-view-btn" id="btnViewGrid" title="Instagram Square Grid View">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>
          </button>
          <button class="pg-view-btn" id="btnViewEditorial" title="Editorial Wide View">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="6" rx="1"></rect><rect x="3" y="14" width="18" height="6" rx="1"></rect></svg>
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- Interactive Photo Grid Container -->
  <div class="pg-grid view-masonry" id="pgGrid">
    <!-- Rendered dynamically by JavaScript -->
  </div>

  <!-- Photo Drag & Drop Upload Zone -->
  <div class="pg-upload-container" id="pgUploadZone">
    <input type="file" id="pgFileInput" accept="image/*" multiple style="display: none;" />
    <div class="pg-upload-icon">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="17 8 12 3 7 8"></polyline><line x1="12" y1="3" x2="12" y2="15"></line></svg>
    </div>
    <h3 class="pg-upload-title">Drop your photos here or click to preview</h3>
    <p class="pg-upload-desc">Drag & drop your photography files here to instantly see them rendered in this interactive gallery.</p>
    <button class="pg-upload-btn" onclick="document.getElementById('pgFileInput').click()">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
      <span>Select Photo Files</span>
    </button>
    <div style="margin-top: 1rem;">
      <span class="pg-folder-hint">
        📁 Dedicated Storage Directory: <code>static/photos/</code>
      </span>
    </div>
  </div>
</div>

<!-- Fullscreen Cinematic Lightbox Modal -->
<div class="pg-lightbox" id="pgLightbox">
  <div class="pg-lb-nav-top">
    <div class="pg-lb-counter" id="pgLbCounter">1 / 6</div>
    <div class="pg-lb-actions">
      <button class="pg-lb-btn" id="pgLbZoomBtn" title="Toggle Zoom (Z)">
        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="11" y1="8" x2="11" y2="14"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg>
        <span>Zoom</span>
      </button>
      <button class="pg-lb-btn" id="pgLbDownloadBtn" title="Download High-Res">
        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
        <span>Download</span>
      </button>
      <button class="pg-lb-btn pg-lb-close-btn" id="pgLbCloseBtn" title="Close (Esc)">
        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
        <span>Close</span>
      </button>
    </div>
  </div>

  <div class="pg-lb-main">
    <button class="pg-lb-arrow prev" id="pgLbPrevBtn">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>
    </button>

    <div class="pg-lb-img-container" id="pgLbImgWrapper">
      <img src="" alt="" class="pg-lb-img" id="pgLbImage" />
    </div>

    <button class="pg-lb-arrow next" id="pgLbNextBtn">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
    </button>

    <!-- EXIF HUD Inspector Drawer -->
    <div class="pg-exif-hud" id="pgExifHud">
      <div class="pg-exif-item">
        <span class="pg-exif-label">Title:</span>
        <span class="pg-exif-val" id="exifTitle">-</span>
      </div>
      <div class="pg-exif-item">
        <span class="pg-exif-label">Camera:</span>
        <span class="pg-exif-val" id="exifCamera">-</span>
      </div>
      <div class="pg-exif-item">
        <span class="pg-exif-label">ISO:</span>
        <span class="pg-exif-val" id="exifIso">-</span>
      </div>
      <div class="pg-exif-item">
        <span class="pg-exif-label">Shutter:</span>
        <span class="pg-exif-val" id="exifShutter">-</span>
      </div>
      <div class="pg-exif-item">
        <span class="pg-exif-label">Aperture:</span>
        <span class="pg-exif-val" id="exifAperture">-</span>
      </div>
      <div class="pg-exif-item">
        <span class="pg-exif-label">Location:</span>
        <span class="pg-exif-val" id="exifLocation">-</span>
      </div>
    </div>
  </div>

  <div class="pg-lb-filmstrip" id="pgLbFilmstrip">
    <!-- Thumbnails generated dynamically -->
  </div>
</div>

<script>
document.addEventListener("DOMContentLoaded", function () {
  // Photography Master Data Set
  const INITIAL_PHOTOS = [
    {
      id: "photo-1",
      title: "Cyberpunk Tokyo Rain",
      category: "urban",
      categoryName: "Urban & City",
      src: "/photos/urban-neon-rain.jpg",
      location: "Shinjuku, Tokyo",
      camera: "Sony A7IV • 35mm f/1.4",
      iso: "800",
      shutter: "1/160s",
      aperture: "f/1.4",
      likes: 142
    },
    {
      id: "photo-2",
      title: "Dawn Over Alpine Misty Waters",
      category: "nature",
      categoryName: "Nature & Wilderness",
      src: "/photos/misty-alpine-lake.jpg",
      location: "Dolomites, Italy",
      camera: "Fujifilm X-T5 • 16-55mm",
      iso: "160",
      shutter: "1/500s",
      aperture: "f/8.0",
      likes: 218
    },
    {
      id: "photo-3",
      title: "Geometric Shadow Play",
      category: "architecture",
      categoryName: "Architecture",
      src: "/photos/minimalist-architecture.jpg",
      location: "Copenhagen, Denmark",
      camera: "Leica Q2 • 28mm Summilux",
      iso: "100",
      shutter: "1/1000s",
      aperture: "f/5.6",
      likes: 95
    },
    {
      id: "photo-4",
      title: "The Umbrellas of Midnight",
      category: "street",
      categoryName: "Street & Mood",
      src: "/photos/noir-street-portrait.jpg",
      location: "Paris, France",
      camera: "Ricoh GR III • 28mm",
      iso: "1600",
      shutter: "1/125s",
      aperture: "f/2.8",
      likes: 184
    },
    {
      id: "photo-5",
      title: "Lantern Glow in Memory Alley",
      category: "night",
      categoryName: "Night & Astrophotography",
      src: "/photos/tokyo-cyber-alley.jpg",
      location: "Omoide Yokocho, Tokyo",
      camera: "Sony A7IV • 50mm f/1.2",
      iso: "640",
      shutter: "1/200s",
      aperture: "f/1.8",
      likes: 312
    },
    {
      id: "photo-6",
      title: "Fiery Sunset Horizon",
      category: "nature",
      categoryName: "Nature & Wilderness",
      src: "/photos/coastal-sunset-drift.jpg",
      location: "Big Sur, California",
      camera: "Canon R5 • 24-70mm f/2.8",
      iso: "100",
      shutter: "1/250s",
      aperture: "f/11",
      likes: 276
    }
  ];

  let photos = [...INITIAL_PHOTOS];
  let currentCategory = "all";
  let searchQuery = "";
  let currentLightboxIndex = 0;
  let isZoomed = false;

  // DOM Elements
  const gridEl = document.getElementById("pgGrid");
  const searchInput = document.getElementById("pgSearchInput");
  const filterTabs = document.querySelectorAll(".pg-tab-btn");
  const viewMasonryBtn = document.getElementById("btnViewMasonry");
  const viewGridBtn = document.getElementById("btnViewGrid");
  const viewEditorialBtn = document.getElementById("btnViewEditorial");
  const statCountEl = document.getElementById("statCount");

  // Lightbox Elements
  const lightbox = document.getElementById("pgLightbox");
  const lbImage = document.getElementById("pgLbImage");
  const lbCounter = document.getElementById("pgLbCounter");
  const lbCloseBtn = document.getElementById("pgLbCloseBtn");
  const lbPrevBtn = document.getElementById("pgLbPrevBtn");
  const lbNextBtn = document.getElementById("pgLbNextBtn");
  const lbFilmstrip = document.getElementById("pgLbFilmstrip");
  const lbZoomBtn = document.getElementById("pgLbZoomBtn");
  const lbDownloadBtn = document.getElementById("pgLbDownloadBtn");
  const lbImgWrapper = document.getElementById("pgLbImgWrapper");

  // EXIF Elements
  const exifTitle = document.getElementById("exifTitle");
  const exifCamera = document.getElementById("exifCamera");
  const exifIso = document.getElementById("exifIso");
  const exifShutter = document.getElementById("exifShutter");
  const exifAperture = document.getElementById("exifAperture");
  const exifLocation = document.getElementById("exifLocation");

  // Render Grid Cards
  function renderGallery() {
    const filtered = photos.filter(p => {
      const matchCat = currentCategory === "all" || p.category === currentCategory;
      const matchSearch = p.title.toLowerCase().includes(searchQuery) ||
                          p.location.toLowerCase().includes(searchQuery) ||
                          p.camera.toLowerCase().includes(searchQuery);
      return matchCat && matchSearch;
    });

    statCountEl.textContent = `${filtered.length} Shots ${currentCategory !== 'all' ? 'in ' + currentCategory : 'Total'}`;

    if (filtered.length === 0) {
      gridEl.innerHTML = `
        <div style="grid-column: 1/-1; text-align: center; padding: 4rem 1rem; color: var(--secondary);">
          <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="color: #6366f1; margin-bottom: 1rem;"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
          <h3 style="margin: 0 0 0.5rem 0; color: var(--primary);">No photos found</h3>
          <p style="margin: 0;">Try adjusting your search query or filter category.</p>
        </div>
      `;
      return;
    }

    gridEl.innerHTML = filtered.map((photo, idx) => `
      <div class="pg-card" data-id="${photo.id}" data-index="${idx}">
        <div class="pg-img-wrapper">
          <img src="${photo.src}" alt="${photo.title}" class="pg-img" loading="lazy" />
          <div class="pg-card-overlay">
            <div class="pg-overlay-top">
              <span class="pg-category-tag">${photo.categoryName}</span>
              <div class="pg-action-btns">
                <button class="pg-icon-btn btn-like" data-id="${photo.id}" title="Like photo">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="${isLiked(photo.id) ? 'currentColor' : 'none'}" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="${isLiked(photo.id) ? 'color:#ef4444;' : ''}"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
                </button>
                <button class="pg-icon-btn btn-quickview" data-index="${idx}" title="Fullscreen Lightbox">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" y1="3" x2="14" y2="10"></line><line x1="3" y1="21" x2="10" y2="14"></line></svg>
                </button>
              </div>
            </div>
            <div class="pg-overlay-bottom">
              <h3 class="pg-photo-title">${photo.title}</h3>
              <div class="pg-photo-meta">
                <span class="pg-meta-item">
                  <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                  ${photo.location}
                </span>
                <span class="pg-meta-item">
                  <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
                  <span class="like-count-${photo.id}">${getLikes(photo)}</span>
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    `).join("");

    // Attach Click Events to Cards
    document.querySelectorAll(".pg-card").forEach((card, i) => {
      card.addEventListener("click", function(e) {
        if (!e.target.closest(".btn-like")) {
          openLightbox(i);
        }
      });
    });

    document.querySelectorAll(".btn-like").forEach(btn => {
      btn.addEventListener("click", function(e) {
        e.stopPropagation();
        const id = this.getAttribute("data-id");
        toggleLike(id);
        renderGallery();
      });
    });
  }

  // LocalStorage Likes Handler
  function getLikes(photo) {
    const customLikes = localStorage.getItem("likes_" + photo.id);
    return customLikes ? parseInt(customLikes) : photo.likes;
  }

  function isLiked(id) {
    return localStorage.getItem("liked_" + id) === "true";
  }

  function toggleLike(id) {
    const photo = photos.find(p => p.id === id);
    if (!photo) return;
    const liked = isLiked(id);
    if (liked) {
      localStorage.setItem("liked_" + id, "false");
      localStorage.setItem("likes_" + id, getLikes(photo) - 1);
    } else {
      localStorage.setItem("liked_" + id, "true");
      localStorage.setItem("likes_" + id, getLikes(photo) + 1);
    }
  }

  // Filter Tabs Event Listeners
  filterTabs.forEach(tab => {
    tab.addEventListener("click", function() {
      filterTabs.forEach(t => t.classList.remove("active"));
      this.classList.add("active");
      currentCategory = this.getAttribute("data-category");
      renderGallery();
    });
  });

  // Search Input Event Listener
  searchInput.addEventListener("input", function(e) {
    searchQuery = e.target.value.trim().toLowerCase();
    renderGallery();
  });

  // View Mode Switcher
  viewMasonryBtn.addEventListener("click", () => setViewMode("masonry"));
  viewGridBtn.addEventListener("click", () => setViewMode("grid"));
  viewEditorialBtn.addEventListener("click", () => setViewMode("editorial"));

  function setViewMode(mode) {
    gridEl.className = "pg-grid view-" + mode;
    viewMasonryBtn.classList.toggle("active", mode === "masonry");
    viewGridBtn.classList.toggle("active", mode === "grid");
    viewEditorialBtn.classList.toggle("active", mode === "editorial");
  }

  // Lightbox Implementation
  function openLightbox(index) {
    currentLightboxIndex = index;
    updateLightboxContent();
    lightbox.classList.add("active");
    document.body.style.overflow = "hidden";
  }

  function closeLightbox() {
    lightbox.classList.remove("active");
    document.body.style.overflow = "";
    resetZoom();
  }

  function updateLightboxContent() {
    const p = photos[currentLightboxIndex];
    if (!p) return;

    lbImage.src = p.src;
    lbImage.alt = p.title;
    lbCounter.textContent = `${currentLightboxIndex + 1} / ${photos.length}`;

    // Update EXIF HUD
    exifTitle.textContent = p.title;
    exifCamera.textContent = p.camera;
    exifIso.textContent = p.iso;
    exifShutter.textContent = p.shutter;
    exifAperture.textContent = p.aperture;
    exifLocation.textContent = p.location;

    // Render Filmstrip
    lbFilmstrip.innerHTML = photos.map((photo, i) => `
      <div class="pg-film-thumb ${i === currentLightboxIndex ? 'active' : ''}" data-index="${i}">
        <img src="${photo.src}" alt="${photo.title}" />
      </div>
    `).join("");

    document.querySelectorAll(".pg-film-thumb").forEach(thumb => {
      thumb.addEventListener("click", function() {
        currentLightboxIndex = parseInt(this.getAttribute("data-index"));
        updateLightboxContent();
      });
    });

    resetZoom();
  }

  function resetZoom() {
    isZoomed = false;
    lbImgWrapper.classList.remove("zoomed");
    lbImage.style.transform = "scale(1)";
  }

  function toggleZoom() {
    isZoomed = !isZoomed;
    if (isZoomed) {
      lbImgWrapper.classList.add("zoomed");
      lbImage.style.transform = "scale(2.2)";
    } else {
      resetZoom();
    }
  }

  // Lightbox Controls
  lbCloseBtn.addEventListener("click", closeLightbox);
  lbPrevBtn.addEventListener("click", () => {
    currentLightboxIndex = (currentLightboxIndex - 1 + photos.length) % photos.length;
    updateLightboxContent();
  });
  lbNextBtn.addEventListener("click", () => {
    currentLightboxIndex = (currentLightboxIndex + 1) % photos.length;
    updateLightboxContent();
  });

  lbZoomBtn.addEventListener("click", toggleZoom);
  lbImage.addEventListener("click", toggleZoom);

  lbDownloadBtn.addEventListener("click", () => {
    const p = photos[currentLightboxIndex];
    const link = document.createElement("a");
    link.href = p.src;
    link.download = p.title.replace(/\s+/g, "_") + ".jpg";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  });

  // Keyboard Shortcuts
  document.addEventListener("keydown", function(e) {
    if (!lightbox.classList.contains("active")) return;
    if (e.key === "Escape") closeLightbox();
    if (e.key === "ArrowLeft") lbPrevBtn.click();
    if (e.key === "ArrowRight") lbNextBtn.click();
    if (e.key.toLowerCase() === "z") toggleZoom();
  });

  // Drag & Drop Live Preview Upload Zone
  const uploadZone = document.getElementById("pgUploadZone");
  const fileInput = document.getElementById("pgFileInput");

  ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    uploadZone.addEventListener(eventName, preventDefaults, false);
  });

  function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
  }

  ['dragenter', 'dragover'].forEach(eventName => {
    uploadZone.addEventListener(eventName, () => uploadZone.classList.add('drag-over'), false);
  });

  ['dragleave', 'drop'].forEach(eventName => {
    uploadZone.addEventListener(eventName, () => uploadZone.classList.remove('drag-over'), false);
  });

  uploadZone.addEventListener('drop', handleDrop, false);
  fileInput.addEventListener('change', function() {
    handleFiles(this.files);
  });

  function handleDrop(e) {
    const dt = e.dataTransfer;
    const files = dt.files;
    handleFiles(files);
  }

  function handleFiles(files) {
    Array.from(files).forEach((file, index) => {
      if (!file.type.startsWith('image/')) return;

      const reader = new FileReader();
      reader.onload = function(e) {
        const newPhoto = {
          id: 'photo-user-' + Date.now() + '-' + index,
          title: file.name.replace(/\.[^/.]+$/, ""),
          category: 'urban',
          categoryName: 'Uploaded Photo',
          src: e.target.result,
          location: 'Local Upload',
          camera: 'User Upload • ' + Math.round(file.size / 1024) + ' KB',
          iso: 'Auto',
          shutter: '1/200s',
          aperture: 'f/2.8',
          likes: 1
        };

        photos.unshift(newPhoto);
        renderGallery();
      };
      reader.readAsDataURL(file);
    });
  }

  // Initial Render
  renderGallery();
});
</script>

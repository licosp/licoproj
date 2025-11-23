import './style.css'

// State
const state = {
    images: [],
    zoom: 1,
    pan: { x: 0, y: 0 },
    isDragging: false,
    dragStart: { x: 0, y: 0 },
    currentImageIndex: null
};

// DOM Elements
const gallery = document.getElementById('gallery');
const emptyState = document.getElementById('empty-state');
const lightbox = document.getElementById('lightbox');
const lightboxImg = document.getElementById('lightbox-img');
const closeBtn = document.getElementById('close-lightbox');
const zoomInBtn = document.getElementById('zoom-in');
const zoomOutBtn = document.getElementById('zoom-out');
const zoomLevel = document.getElementById('zoom-level');

console.log('Image Viewer initialized');

// Drag & Drop Logic
function setupDragAndDrop() {
    const events = ['dragenter', 'dragover', 'dragleave', 'drop'];

    // Prevent default defaults for all drag events
    events.forEach(eventName => {
        document.body.addEventListener(eventName, preventDefaults, false);
    });

    // Highlight drop zone
    ['dragenter', 'dragover'].forEach(eventName => {
        document.body.addEventListener(eventName, highlight, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        document.body.addEventListener(eventName, unhighlight, false);
    });

    // Handle dropped files
    document.body.addEventListener('drop', handleDrop, false);
}

function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}

function highlight() {
    document.body.classList.add('drop-active');
}

function unhighlight() {
    document.body.classList.remove('drop-active');
}

function handleDrop(e) {
    const dt = e.dataTransfer;
    const items = dt.items;

    if (items) {
        // Use DataTransferItemList interface to access the file(s)
        for (let i = 0; i < items.length; i++) {
            const item = items[i].webkitGetAsEntry();
            if (item) {
                scanFiles(item);
            }
        }
    } else {
        // Use DataTransfer interface to access the file(s)
        const files = [...dt.files];
        handleFiles(files);
    }
}

function scanFiles(item) {
    if (item.isFile) {
        item.file(file => {
            handleFiles([file]);
        });
    } else if (item.isDirectory) {
        const dirReader = item.createReader();
        const readEntries = () => {
            dirReader.readEntries(entries => {
                if (entries.length === 0) return;
                entries.forEach(entry => scanFiles(entry));
                readEntries(); // Continue reading until empty
            });
        };
        readEntries();
    }
}

function handleFiles(files) {
    // Accept images and videos
    const validFiles = files.filter(file => file.type.startsWith('image/') || file.type.startsWith('video/'));

    if (validFiles.length === 0) return;

    validFiles.forEach(file => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onloadend = function () {
            const isVideo = file.type.startsWith('video/');
            const itemObj = {
                src: reader.result,
                name: file.name,
                type: isVideo ? 'video' : 'image',
                id: Date.now() + Math.random().toString(36).substr(2, 9)
            };
            state.images.push(itemObj);
            renderGallery();
        }
    });
}

// Gallery Rendering
function renderGallery() {
    if (state.images.length > 0) {
        emptyState.style.display = 'none';
    } else {
        emptyState.style.display = 'flex';
    }

    const existingItems = gallery.querySelectorAll('.gallery-item');
    existingItems.forEach(item => item.remove());

    state.images.forEach((itemData, index) => {
        const item = document.createElement('div');
        item.className = 'gallery-item';
        item.onclick = () => openLightbox(index);

        if (itemData.type === 'video') {
            const video = document.createElement('video');
            video.src = itemData.src;
            video.muted = true;
            video.loop = true;
            // Play on hover logic could be added here
            video.onmouseover = () => video.play();
            video.onmouseout = () => {
                video.pause();
                video.currentTime = 0;
            };
            item.appendChild(video);

            // Add a video indicator icon
            const indicator = document.createElement('div');
            indicator.innerHTML = '▶';
            indicator.style.cssText = 'position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; font-size: 2rem; pointer-events: none; text-shadow: 0 2px 4px rgba(0,0,0,0.5);';
            item.appendChild(indicator);
        } else {
            const img = document.createElement('img');
            img.src = itemData.src;
            img.alt = itemData.name;
            img.loading = 'lazy';
            item.appendChild(img);
        }

        gallery.appendChild(item);
    });
}

// Initialize
setupDragAndDrop();

// Lightbox Logic
const lightboxVideo = document.getElementById('lightbox-video');

function openLightbox(index) {
    state.currentImageIndex = index;
    const item = state.images[index];

    state.zoom = 1;
    state.pan = { x: 0, y: 0 };

    if (item.type === 'video') {
        lightboxImg.style.display = 'none';
        lightboxVideo.style.display = 'block';
        lightboxVideo.src = item.src;
        lightboxVideo.play();

        // Disable zoom/pan for video for now as it complicates controls
        zoomInBtn.disabled = true;
        zoomOutBtn.disabled = true;
        zoomLevel.textContent = '';
        lightboxVideo.style.cursor = 'default';
        lightboxVideo.style.transform = 'none';
    } else {
        lightboxVideo.style.display = 'none';
        lightboxVideo.pause();
        lightboxVideo.src = ''; // Clear source

        lightboxImg.style.display = 'block';
        lightboxImg.src = item.src;
        lightboxImg.alt = item.name;

        zoomInBtn.disabled = false;
        zoomOutBtn.disabled = false;
        updateImageTransform();
    }

    lightbox.classList.add('active');
    lightbox.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
}

function closeLightbox() {
    lightbox.classList.remove('active');
    lightbox.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    state.currentImageIndex = null;

    lightboxVideo.pause();
    lightboxVideo.src = '';
}

function updateImageTransform() {
    if (state.images[state.currentImageIndex]?.type === 'video') return;

    lightboxImg.style.transform = `translate(${state.pan.x}px, ${state.pan.y}px) scale(${state.zoom})`;
    zoomLevel.textContent = `${Math.round(state.zoom * 100)}%`;

    if (state.zoom > 1) {
        lightboxImg.style.cursor = state.isDragging ? 'grabbing' : 'grab';
    } else {
        lightboxImg.style.cursor = 'default';
    }
}

function handleZoom(delta) {
    const newZoom = state.zoom + delta;
    // Limit zoom between 0.1x and 5x
    if (newZoom >= 0.1 && newZoom <= 5) {
        state.zoom = newZoom;
        updateImageTransform();
    }
}

// Event Listeners for Lightbox
closeBtn.addEventListener('click', closeLightbox);
zoomInBtn.addEventListener('click', () => handleZoom(0.1));
zoomOutBtn.addEventListener('click', () => handleZoom(-0.1));

// Keyboard Navigation
document.addEventListener('keydown', (e) => {
    if (!lightbox.classList.contains('active')) return;

    switch (e.key) {
        case 'Escape':
            closeLightbox();
            break;
        case 'ArrowLeft':
            navigateImage(-1);
            break;
        case 'ArrowRight':
            navigateImage(1);
            break;
        case '+':
        case '=':
            handleZoom(0.1);
            break;
        case '-':
        case '_':
            handleZoom(-0.1);
            break;
    }
});

function navigateImage(direction) {
    if (state.currentImageIndex === null) return;

    let newIndex = state.currentImageIndex + direction;
    if (newIndex < 0) newIndex = state.images.length - 1;
    if (newIndex >= state.images.length) newIndex = 0;

    openLightbox(newIndex);
}

// Mouse Wheel Zoom
lightbox.addEventListener('wheel', (e) => {
    e.preventDefault();
    const delta = e.deltaY > 0 ? -0.1 : 0.1;
    handleZoom(delta);
}, { passive: false });

// Pan Logic
lightboxImg.addEventListener('mousedown', (e) => {
    if (state.zoom <= 1) return;
    e.preventDefault();
    state.isDragging = true;
    state.dragStart = { x: e.clientX - state.pan.x, y: e.clientY - state.pan.y };
    lightboxImg.classList.add('grabbing');
});

window.addEventListener('mousemove', (e) => {
    if (!state.isDragging) return;
    e.preventDefault();
    state.pan.x = e.clientX - state.dragStart.x;
    state.pan.y = e.clientY - state.dragStart.y;
    updateImageTransform();
});

window.addEventListener('mouseup', () => {
    state.isDragging = false;
    lightboxImg.classList.remove('grabbing');
});

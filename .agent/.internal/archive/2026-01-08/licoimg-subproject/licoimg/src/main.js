import './style.css'

const app = document.querySelector('#app')

app.innerHTML = `
  <h1>LicoImg</h1>
  <p>Image viewer application</p>
  <div class="image-drop-zone">
    <p>Drag and drop images here or click to select</p>
    <input type="file" id="file-input" multiple accept="image/*" style="display: none;">
    <button onclick="document.getElementById('file-input').click()">Select Images</button>
  </div>
  <div id="image-gallery"></div>
`

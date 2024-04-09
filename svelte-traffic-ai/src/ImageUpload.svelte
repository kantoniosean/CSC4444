<script>
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();
  
    let imageFile;
    let imageUrl = '';
  
    function handleFileChange(event) {
      const file = event.target.files[0];
      if (file) {
        imageFile = file;
        imageUrl = URL.createObjectURL(file);
        dispatch('imageSelected', { file });
      }
    }
  </script>
  
  <style>
    .upload-container {
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 20px;
      border: 2px dashed #ccc;
      border-radius: 10px;
      margin: 10px;
    }
  
    .upload-input {
      opacity: 0;
      width: 0.1px;
      height: 0.1px;
      position: absolute;
    }
  
    .upload-label {
      display: inline-block;
      padding: 10px 20px;
      background-color: #007bff;
      color: white;
      border-radius: 5px;
      cursor: pointer;
    }
  
    .upload-label:hover {
      background-color: #0056b3;
    }
  
    .image-preview {
      margin-top: 10px;
      max-width: 100%;
      max-height: 300px;
      border-radius: 5px;
    }
  </style>
  
  <div class="upload-container">
    <input type="file" accept="image/*" id="file-upload" class="upload-input" on:change={handleFileChange}>
    <label for="file-upload" class="upload-label">Choose an image</label>
    {#if imageUrl}
      <img src={imageUrl} alt="Image preview" class="image-preview">
    {/if}
  </div>
  
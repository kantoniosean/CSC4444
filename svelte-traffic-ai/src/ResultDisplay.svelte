<script>
    export let result = '';
  </script>
  
  <style>
    .result-container {
      margin-top: 20px;
      padding: 15px;
      border-radius: 5px;
      background-color: #f7f7f7;
      border: 1px solid #d1d1d1;
      text-align: center;
    }
  
    .result-text {
      color: #333;
      font-size: 18px;
      font-family: Arial, sans-serif;
    }
  
    .no-result {
      color: #888;
    }
  </style>
  
  <div class="result-container">
    {#if result}
      <p class="result-text">Classification Result: <strong>{result}</strong></p>
    {:else}
      <p class="result-text no-result">No result yet</p>
    {/if}
  </div>
  
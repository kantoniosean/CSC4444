<script>
	import ImageUpload from './ImageUpload.svelte';
	import ResultDisplay from './ResultDisplay.svelte';
	import * as tf from '@tensorflow/tfjs';
  
	let model;
	let result = '';
  
	async function loadModel() {
	  model = await tf.loadLayersModel('/tf_model/model.json');
	}
  
	function handleImageSelected(event) {
	  const file = event.detail.file;
	  const reader = new FileReader();
	  reader.onload = async () => {
		const img = new Image();
		img.src = reader.result;
		img.onload = async () => {
		  const tensor = tf.browser.fromPixels(img)
			.resizeNearestNeighbor([240, 240])
			.toFloat()
			.expandDims();
		  const prediction = await model.predict(tensor);
		  result = prediction.toString(); // Simplified, you may want to process the prediction result
		};
	  };
	  reader.readAsDataURL(file);
	}
  
	loadModel();
</script>

<style>
	.app-container {
		padding: 40px;
	}

	.title {
		font-size: 24px;
		text-align: center;
		color: #333;
		margin-bottom: 20px;
		font-weight: bold;
	}
</style>

<div class="app-container">
	<div class="title">Traffic Image Classifier</div>
	<ImageUpload on:imageSelected={handleImageSelected} />
	<ResultDisplay {result} />
</div>

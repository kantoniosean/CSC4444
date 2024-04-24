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
		  updateResult(prediction);
		};
	  };
	  reader.readAsDataURL(file);
	}

	// Helper function to process the prediction tensor and set the result
	function updateResult(prediction) {
	  prediction.array().then(array => {
	    const results = [
	      "This image is a car",
	      "This image is a merge",
	      "This image is a stop sign",
	      "This image is a traffic cone",
	      "This image is a traffic light"
	    ];
	    const maxIndex = array[0].indexOf(Math.max(...array[0]));
	    result = results[maxIndex] || "No result yet";
	  });
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

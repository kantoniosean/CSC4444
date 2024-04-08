import App from './App.svelte';
import * as tf from '@tensorflow/tfjs';

const app = new App({

	target: document.body,
	props: {
		name: 'world'
	}
});

export default app;
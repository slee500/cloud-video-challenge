# cloud-video-challenge
Our attempt at learning more about the Google Cloud 8M+ Video Challenge.

Updates 4/23: 
- We will now study about Optical Flow and how we can use that to track features over time. We will track the segmented objects over time to track the movement of objects we are trying to classify and then use this to trak and build the potential terms between each of the nodes. This will help us build a dense CRF in the time domain. 
- To build a CRF in the spatial domain, we will use the pixel value as the unary term, and the relation between one pixel to the other as the potential term. 

Updates 4/22:
- I tried documenting the given train.py file from the starter code (which allows us to process the data at a scale that can be accomplished within a reasonable amount of time), but progress is slow.
Some notes about the frame-level data:
- The frames from the video are sampled at 1 frame/second and passed through Google's Le-Net Image Network.
- The output from the network has dimension 2048; PCA is used to reduce the dimensions to 1024; following that, the components are quantized to 8-bits [0 255].
- Conclusion is that we can't actually visualize the frame data and won't be able to construct motion features. 

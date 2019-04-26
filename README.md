# BasicPixelplanetFunBot
It was only made for fun, so the code wasn't written with the intention of anyone seeing this.

## The whole process of making this bot:

1. Went to pixelplanet.fun, opened dev console (ctrl + shift + c) -> Network tab
2. Placed a pixel and the request that was sent to the server was recorded.
3. Right clicked on it -> Copy -> Copy as curl
4. Converted curl to python [here](https://curl.trillworks.com/)
5. Pasted the python code to my python IDE.
6. Got RGB values for each available pixel colour on pixelplanet.fun and put them in a list
7. Added image reading function to my python code.
8. Found a dithering library for this project to convert image to a different colorspace.
9. Implemented dithering in this code
10. Implemented a function that loops through all the pixels in the new dithered image and sends a modified request to place each pixel, then after getting the response, waiting a certain amount of time till the timer hits 0 and it can place a new pixel.

# ImageToGreyscaleText

**A note on PIL:** Since PIL is an older package, you have to install pillow, and PIL will be packaged within that. (`pip3 install pillow`) You don't need to change any of the code though. `import PIL` should run just fine after you have install the `pillow` package.

### A Quick Description

The main.py file converts inputimage image files into outputimage html files that show the input image in repeated greyscale letters.

### Transformation example

<img src="https://github.com/MarwariTheHorse/ImageToGreyscaleText/blob/master/readme-images/landscape.jpg?raw=true" width="400"/>

will convert to

<img src="https://github.com/MarwariTheHorse/ImageToGreyscaleText/blob/master/readme-images/screenshot.png?raw=true" width="400"/>

using these inputs (make sure to move `landscape.jpg` from `readme-images` into your `inputimages` folder)

<img src="https://github.com/MarwariTheHorse/ImageToGreyscaleText/blob/master/readme-images/process.png?raw=true" width="400"/>

(`.012` is a good starting point, but feel free to lower or increase it if your want more or less letters in your image. The .html file can get large enough to crash search engines though, so there is definitely a limit.)


### Inputs

Place an image file into the inputimages folder (it will work without any code modification as long as the inputimages folder is in the same directory as the .py file)

### Outputs

All output .html files will be stored in outputimages under the file name and extension you provide.

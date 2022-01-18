# Logogram_Translator_with_TensorFlow
A Chinese Logo-gram Translating Bot with TensorFlow

## Short Description
This Bot can provide the translated result whenever you input the Handwriting image file.(Only for Chrome browser users)

## What you need to do to use it
You need four packages and one additional program to run this program.

* Selenium

You need this to run the webdriver.
```
$ python -m pip install selenium
```
* Webdriver

The webdriver has different versions for each browser : Chrome, FireFox, Edge etc.

You should check this link for it: https://www.makeuseof.com/how-to-install-selenium-webdriver-on-any-computer-with-python/

(This link would not be preferable for Chrome users. The site directed here announced that it will be deprecated soon.)

You can revise the code to run in other browser if you can handle the browser dirver.


Because I am Chrome User, this Bot is for Chrome Users and if you are as well, check your version of Chrome and go to this link to install: https://sites.google.com/chromium.org/driver/

This tutorial setting instruction is the best way to follow. Otherwise, please consider changing the webdriver path

Tutorial video for Chrome Webdriver: https://www.youtube.com/watch?v=dz59GsdvUF8


* Tensorflow and NumPy
This is the main part of this program. The package is required for loading the saved Keras model.

The version of TensorFlow for this Bot is 2.7.0

TensorFlow installation
```
$ pip install tensorflow==2.7.0
```
NumPy Installation
```
$ pip install numpy
```

Suggestion : Looking up TensorFlow offical site is good option if you have something to figure out regarding loading model

* Tkinter
This is the package of the tools for application window. It is already installed in Python. No action for it is needed.

## Something important to know
* Input file 
* 
I included the file(Logogram examples) containing letter images drawn in Paint app.

If you want to try other letters, you should draw in same way. (64X64 .jpg file drawn with white think pen and black background paint)

Example:

![image1](https://user-images.githubusercontent.com/84373345/149867828-362da2ea-446b-44bb-85e4-8423750df80f.jpg)

* What it can recognize

This Bot can understand 15 Logograms: 零, 一 ,二, 三, 四, 五, 六, 七, 八, 九, 十, 百, 千, 万, 亿 

For rest of chinese characters, other model is required. 

## Demo video


https://user-images.githubusercontent.com/84373345/149871458-e70de21e-27fa-4287-ab99-156850513d0f.mp4

First, open the Handwritten LogoGram Translator.py and run it.

Then, go File-> Open and open the . jpg file you want to read and wait few seconds. The result will appear in few seconds.

If you want to erase the text in the textbox, go File->New

Or, if you want to input another character, go File->Open and input the image character you want.

You may want to save the text, then go File-> Save as and save the .txt file at the location you want to.


## Future Plan
I am thinking of creating .exe file but need to figure out the Pyinstaller issues.

Currently, TensorFlow packages are not applied well when put all the things into the .exe file.

If there is no option to solve this problem, I have to consider C++ version of this project.

## Contact me
If you have any ideas or issues, please contact me by email: waterloocanucks1@gmail.com

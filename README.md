# SmallProjects
Repo for some small projects, one project one branch. Master branch is used as the release branch.

Last Update: 2021/2/22

## AnimalCrossingRingCon

Using Titan2 to enable users to play Animal Crossing by using Ring Con.

For detailed How-To instruction, please refer to [this page](https://www.controllerbend.com/animalcrossing_ringfit.html).


## Connect 4:

A connect 4 game in python, with an AI built in.

Last update: 18 May 2020

Example usage:\
In Connect4 directory:
```
python3 connect4.py
```

Code tested in Windows 10 with:\
Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32

## Clock Angle
Solutions in python and java for clock angle problem.

Last update: 17 May 2020

Example usage:\
In python directory:
```
python3 main.py
```
In java directory:
```
./run
```

Currently the program is running an infinite while
loop, which will increase current time by 1 second and re-calculate every angle,
a bit like a show-off mode.

To use it as a clock angle calculator, please comment out current main method
and uncomment the other, which will get a time in string representation
(format: hh:mm:ss) from command line argument.

Code tested in Windows 10 with:\
java 11.0.6 2020-01-14 LTS\
Java(TM) SE Runtime Environment 18.9 (build 11.0.6+8-LTS)\
Java HotSpot(TM) 64-Bit Server VM 18.9 (build 11.0.6+8-LTS, mixed mode)\
and\
Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32


## PDFTranslator
Extract text content from a pdf file, and then use Google translation api to translate it into chinese.

Last update: 17 May 2020

Example usage:
```
python3 pdf_translator.py test.pdf
```

Code is tested under Windows 10 and MacOS with python 3.8.2, works as expected.

Possible improvements:
* pdfminer writes extracted text information into a disk file, and in translation phase, this program reads from disk
again. Disk operation is slow and I want to avoid it. Is it possible to store the output of pdfminer in memory?
* googletrans API sets limitations on number of queries one IP can send per day, if exceeded, google refuse to give any
result, and this tool becomes meaningless.
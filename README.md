# SmallProjects
Repo for some small projects, one project one branch. Master branch is used as the release branch.


# PDFTranslator
Extract text content from a pdf file, and then use Google translation api to translate it into chinese.

Example usage:
```
python3 test.pdf
```

Code is tested under Windows 10 and MacOS with python 3.8.2, works as expected.

Possible improvements:
* pdfminer writes extracted text information into a disk file, and in translation phase, this program reads from disk
again. Disk operation is slow and I want to avoid it. Is it possible to store the output of pdfminer in memory?
* googletrans API sets limitations on number of queries one IP can send per day, if exceeded, google refuse to give any
result, and this tool becomes meaningless.
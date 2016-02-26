# ophage
Add page labels to a PDF file

## Installation
#### Debian / Ubuntu
You can download the (alpha-quality) [deb package](https://github.com/lovasoa/ophage/releases/download/0.1-2/ophage_0.1-2_all.deb).
#### Others
```bash
$ git clone --recursive https://github.com/lovasoa/ophage.git
```

## Usage
```bash
$ ophage file.pdf n
```
Where `n` can be :
 - a positive number : the number of the page that you want to become page №1
 - a negative number : the opposite of the page number you want to give to the first page

It will create a copy of `file.pdf` named `renumbered.file.pdf` in the current directory.

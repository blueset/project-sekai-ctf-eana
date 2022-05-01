# Broken converter

� finally finished his assignment and ready to submit it, but for some reasons the school requires all assignments to be submitted as XPS files. � found a converter online and used the converted file for submission. The file looks good at first, but it seems like there’s something broken in the converter. Can you help him figure out what is wrong here?

## Writeup

Similar to that of CMAP, but in XPS format. (this was designed before the cmap challenge)
https://sekai.team/blog/ugra-ctf-quals-2022/cmap/

Method 1: open the document, copy the text, and manually match up each letter with the copied text. Sort the mappings by the copied characters in ASCII order to find the flag.

Method 2: Extract the font from the document (method can be found on Wikipedia), open it and find the flag.
https://en.wikipedia.org/wiki/ODTTF

<code>f\@g:<u>SEKAI{sCR4MBLeD_a5ci1-FONT+GlYPHZ,W3|!.d0n&}</u>"#$%'()*/26789;&lt;=&gt;?JQUVX[]^`bhjkmopqrtuvwxyz~</code>

![Comparing ASCII with the font’s output](screenshot.png)

## Credit

Typeface used: [Cascadia Code](https://github.com/microsoft/cascadia-code) by Microsoft, licensed under the SIL Open Font License.
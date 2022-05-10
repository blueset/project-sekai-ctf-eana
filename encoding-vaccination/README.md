# Somebody just got vaccinated

No stegano required.

## Writeup

With hint on the picture “COVID-19 vaccination”, and the `shc://` header of the text stored in the QR code. We can know that this is a https://smarthealth.cards/ card. Googling _SHC QR code decoder_ we find find plenty of tools to decode it. 

Once decoded, the flag can be found in the JSON payload.

[CyberChef decode recipe](https://gchq.github.io/CyberChef/#recipe=Parse_QR_Code(false)Find_/_Replace(%7B'option':'Regex','string':'%5B%5E%5C%5Cd%5D'%7D,'',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'(%5C%5Cd%5C%5Cd)'%7D,'$1%5C%5Cn',true,false,true,false)From_Decimal('Line%20feed',false)ADD(%7B'option':'Hex','string':'2d'%7D)Find_/_Replace(%7B'option':'Regex','string':'(%5E%5B%5E%5C%5C.%5D%2B%5C%5C.%7C%5C%5C.%5B%5E%5C%5C.%5D%2B$)'%7D,'',true,false,true,false)From_Base64('A-Za-z0-9-_',true)Raw_Inflate(0,0,'',false,false)JSON_Beautify('%20',false))

[Cyberchef encode recipe](https://gchq.github.io/CyberChef/#recipe=JSON_Minify()Raw_Deflate('Dynamic%20Huffman%20Coding')To_Base64('A-Za-z0-9-_')Find_/_Replace(%7B'option':'Regex','string':'%5E'%7D,'eyJhbGciOiJFUzI1NiIsInppcCI6IkRFRiIsImtpZCI6IlZwak80UEp1ODRndUt2VHZrT1JGUkd3U1hmc1I2QkxUbmhkUFF2d2lSeiJ9.',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'$'%7D,'.5MPi0nkGlZPZhtMoixn3C0higq4vb2iaOwQUZHTugnqLdS1kVTaaUW1phNkR8T/pAXmNl/uknuq7UShzK1amVw',true,false,true,false)SUB(%7B'option':'Hex','string':'2D'%7D)To_Decimal('Space',false)Find_/_Replace(%7B'option':'Regex','string':'(?%3C%3D%20%7C%5E)(%5C%5Cd)(?%3D%20%7C$)'%7D,'0$1',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'%20'%7D,'',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'%5E'%7D,'shc:/',true,false,true,false))

# Somebody just got vaccinated

No stegano required.

## Writeup

With hint on the picture “COVID-19 vaccination”, and the `shc://` header of the text stored in the QR code. We can know that this is a https://smarthealth.cards/ card. Googling _SHC QR code decoder_ we find find plenty of tools to decode it. 

Once decoded, the flag can be found in the JSON payload.
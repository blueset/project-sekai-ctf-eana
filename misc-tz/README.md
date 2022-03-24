# (4-2-2)'T'(2:2:2)'Z'

`201404091329372009012420040120280121160145199805172305121992012117463619970425041349`

Flag format (regex): `^SEKAI\{[~~\}]+\}$`

## Writeup

Title of the challenge hints that the chunk of numbers are ISO 8601 time format.
Flag format hints that we need to convert the dates into ASCII bytes.
The most common way of representing dates as a single piece of data is Unix Timestamp.

Convert the dates to Unix Timestamps, then to hex decimal, we can decode it in ASCII and see the flag, 

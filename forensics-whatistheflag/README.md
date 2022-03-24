# whatistheflag

Flag format (regex): `^SEKAI\{[A-Z]+\}$`

## Writeup

Open the PDF file, we can see a big line of text saying _SEKAI{whatistheflag}_ where _SEKAI{_ and _}_ is modifiable text box.
Look closely and we can see that each letter of _whatistheflag_ are a bit different from each other.

Open it with Adobe Acrobat Reader, and we can see there are 13 fonts embedded in the PDF, matching the number of letters in _whatistheflag_. Matching the font used with each letter, we have
- Karla
- Noto Sans
- Open Sans
- Work Sans
- Yaldevi
- Overpass
- Ubuntu
- Raleway
- FiraGO
- Oxygen
- Nunito Sans
- Telex
- Source Sans Pro

Joining the first letter of the names, we have `SEKAI{KNOWYOURFONTS}` as the flag
# Spoken2Written
This is a Python module which may that may convert a paragraph of spoken english to written english.

For example, "two dollars" ought to be regenerate to $2. Abbreviations spoken as "C M" or "Triple A" ought to be written as "CM" and "AAA" severally.
You can install the module using Python Package Index using the below command

        python3 setup.py install

Usage:

Correct one:

        python3 from spoken2written import sp2wr sp2wr.convert_sp_to_wr()

[IN]:Enter Your paragraph of spoken english:

Hi! My name is Bruce. I am a Programmer. I try to wake up before 6 A M. I always come home after 7 P M. I earn hundred dollars per day. My contact number contains double 5, quadruple 8, single 9 and triple 4. Recently, My weight got double the weight of my friend whom I call C M.

[OUT]:The input Spoken English Paragraph:

" Hi! My name is Bruce. I am a Programmer. I try to wake up before 6 A M. I always come home after 7 P M. I earn hundred dollars per day. My contact number contains double 5, quadruple 8, single 9 and triple 4. Recently, My weight got double the weight of my friend whom I call C M. "

Converted Written English Paragraph:

" Hi! My name is Bruce. I am a Programmer. I try to wake up before 6 AM. I always come home after 7 PM. I earn $100 per day. My contact number contains 55, 8888, 9 and 444. Recently, My weight got double the weight of my friend whom I call CM. "

Wrong One:

        python3 from spoken2written import sp2wr sp2wr.convert_sp_to_wr()

[IN]:Enter Your paragraph of spoken english: Hi! My name is Bruce.I am a Programmer.I try to wake up before 6 A M.I always come home after 7 P M.I earn hundred dollars per day.My contact number contains double 5,quadruple 8, single 9 and triple 4.Recently, My weight got double the weight of my friend whom I call C M.

[OUT]:The input Spoken English Paragraph:

" Hi! My name is Bruce.I am a Programmer.I try to wake up before 6 A M.I always come home after 7 P M.I earn hundred dollars per day.My contact numbe number contains double 5,quadruple 8, single 9 and triple 4.Recently, My weight got double the weight of my friend whom I call C M."

Converted Written English Paragraph:

" Hi! My name is Bruce.I am a Programmer.I try to wake up before 6 A M.I always come home after 7 P M.I earn $100 per day.My contact numbe number contains 5,quadruple5,quadruple 8, 9 and 4.Recently4.Recently4.Recently, My weight got the weight of my friend whom I call CM."

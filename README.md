Okay so I did this just as a part of my curiosity. I mean how cool it would be to know the status of your court case if you have any. <br
I went through the official website of Indian Court Cases i.e <b>courtnic.nic.in</b> and saw that it's pretty easy to extract the data out of it.<br>
All I needed to do was to submit the information in their server through the form they provided and get the data out of it.
I just needed to know the number which represents a particular case type and then WHAM!!!<br>
1 hr. of coding and a bit of searching the site and the work was done.

<h1>How to use it:</h1><br>
Make sure you have root access in your PC and then type this in your terminal :- <br>
<b>>>>python</b><br>
<b>>>>from case_status import *</b><br>
<b>>>>get_case_status(case_type,case_number,year)</b><br>
And then just wait for a few seconds.. and you will get a dictionary containing <br>
<b>is_disposed</b>: this will display the information about the status of the case. If it is disposed(the case is closed) it will be true, otherwise false<br>
<b>respondent</b>:respondent of the case<br>
<b>petitioner</b>:petitioner of the case<br>
<b>pet_advocate</b>:Advocate for petitioner<br>
<b>res_advocate</b>:Advocate for respondent<br>
<b>converted_case</b>:Some times the case is converted into other type..so if it happens, it will show that.<br>

Hope it will help some people now :-D.

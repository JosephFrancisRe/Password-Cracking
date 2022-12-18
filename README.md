# Password-Cracking
<b>Language:</b> Python<br>
<b>Lines of Code:</b> 161

<b>Purpose:</b> The purpose of this project was to crack a salted hash password. The hash function was created using sha256.
In addition to creating a python file that uses a dictionary attack to identify a password crack match, the project's
Part 2 is meant to explore how a requests library can be used to achieve the same end by cracking through a web site's
form.

<b>Result:</b> The solution shows that cracking a salted hash function is much faster on a system than through a web
application.

<b>Description</b> of other files:
	screenshots folder	Contains a screenshot for both Parts 1 and 2 of the project. Each screenshot
				serves as proof of the performance results that are outlined in both part1.txt
				and part2.txt.

	templates folder	Contains index.html which is an extremely basic form with a post method to
				facilitate Part 2 of the project.

	part1.txt		Write up with information specific to the Part 1 submission.

	part2.txt		Write up with information specific to the Part 2 submission.

	pwcrack.py		Python file that encodes every word in the wordlist using sha256 and then
				compares that to the initial hash. Once a match is found the plain text
				password is provided concluding the dictionary attack.

	pwcrack_online.py	Python file that encodes every word in the wordlist using sha256 and then
				compares that to the initial hash. Once a match is found the plain text
				password is provided concluding the dictionary attack. Unlike pwcrack.py,
				this file submits each potential match as a separate Post request through
				the Flash web application.

	webapp.py		An extremely simple Flask web application to run a dictionary attack on.
				The web application is intentially created as simple as possible so any
				differences in the run speed between pwcrack.py and pwcrack_online.py are
				exclusively due to the slower speed of a web application processing Post
				requests versus performing the attack on a local non-web based machine.

<b>Missing file as it is too large:</b>
	wordlist.txt<br>		This word list is the crackstation human only wordlist. It is a commonly used
				dictionary of real world plain text passwords used by actual application users.
        
Download the 15GB file here: https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm

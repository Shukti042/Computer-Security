# Cross-Site Scripting (XSS) Attack

Cross-site scripting (XSS) is a type of vulnerability commonly found in web applications. This vulnerability makes it possible for attackers to inject malicious code (e.g. JavaScript programs) into victim’s web browser. Using this malicious code, attackers can steal a victim’s credentials, such as session cookies. The access control policies (i.e., the same origin policy) employed by browsers to protect those credentials can be bypassed by exploiting XSS vulnerabilities.
To demonstrate what attackers can do by exploiting XSS vulnerabilities, we used a web application named Elgg provided in our pre-built Ubuntu VM image. In this assignment, we needed to exploit this vulnerability to launch an XSS attack on the modified Elgg. This assignment covers the following topics:
• Cross-Site Scripting attack
• XSS worm and self-propagation
• Session cookies
• HTTP GET and POST requests
• JavaScript and Ajax

The details about the tasks are described in CSE 406 Web Security Assignment.
# phishingtrack
Solution for tracking user clicks during security check-ups.

Did you find yourself in a position at your workplace where you’re expected to not only devise a phishing security test and statistic but also to track link clicks of specific users? Then you might find my solution helpful. While it is far from ideal, my Python script will definitely prove to be useful even if you decide not to use the rest of my solution.

## How I track user clicks
To track which user clicked the link in my test-phishing email, I use a URL with an appended ID specific to the user.

So this:

> https://www.pavelkadera.cz/phishing

Becomes this:

> https://www.pavelkadera.cz/phishing?id=cniryxnqren

While the string in the *id* value might seem random, it is not. it is generated from the email address of the user. How do we get that address, you ask? Well, we already know it since we’re using it to send the email to the user. 😉

We can send emails using an SMTP server, whether you choose to use Gmail like I did is up to you. I use Gmail to give users the opportunity to recognize a potentially hazardous email address.

## Python side
The script *sendmail.py* uses the given receiver’s email address, removes the domain and @ from the string, and „encodes“ the new string using a simple ROT13 „encryption“. I wouldn’t really go as far as to call it encryption, but it isn’t there to secure data, it is there to make the ID unrecognizable at first glance. You can of course use key encryption if you wish to do so. I was too lazy to implement it.

The script then uses the new string and modifies the link in the HTML and plaintext body for each email sent.

The script works with a list of addresses. You can either enter the list manually into the code or export the addresses from an Excel file using the commented-out function in *sendmail.py*. The function is imported from *getlist.py*. That code will of course have to be modified as well. You need to enter the path to the Excel file, sheet name and cell range.

It pops the first value from the list and uses the return (pop function returns the „popped“ value) to generate the *id* string. After sending the email it loops until the length value of the list equals 0 (until there are no addresses left).

### MIMEText
We’re then using the MIMEText library. I won’t go into much detail here, as many others already have. Just remember to use the 465 port for SSL. Alternatively, find the corresponding ports for TSL or others.

### SMTP server, Gmail
If you wish to use your own SMTP server or a different one, parts of this guide might still help you. This is, however, specifically written to assist with sending emails through Gmail.

To use the script in my repo, you do not need to modify anything below the email body line (line 62). A specific thing, when it comes to using the Gmail SMTP server, is that you cannot log in using the account password. You will need to generate an „app passkey“ which is allowed only after setting up two-factor authentication. So:

* create a Gmail account,
* setup two-factor authentication,
* generate a passkey in the two-factor auth settings tab.
* Use the generated passkey in the epass value in *sendmail.py*.

## Collecting the data
So, we sent our emails and someone clicked our link. What happens now? A short JavaScript code will grab the *id* in the URL and simply send it as a comment to WordPress. **You will need to change the action value** which is now set to „https://www.yourweb.com/wp-comments-post2.php“ **to your path to the modified comments PHP file in the repo**. The file is the same as the original WordPress file, except it redirects the user to a given URL (default set to google.com).

The script additionally appends 2 random characters at the end of the string to bypass the „duplicate comment“ error.

To allow users to click the link repeatedly in a short time you should also disallow WordPress‘ [comment flooding protection](http://r3quie.com/comment-flood-protection/).

## Why WordPress comments?
My web hosting does not allow me access to the Apache logs, I do however have access to the FTP in the www directory. Feel free to use Apache logs of course.

Using WordPress comments also allows you to collect data through SQL.

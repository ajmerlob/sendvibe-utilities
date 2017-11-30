import math
import sys
import smtplib
import re
import base64

class Util:
  def __init__(self):
    self.address_search = re.compile(r'([\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4})')

  def interpret(self,message):
    msg_str = base64.urlsafe_b64decode(message.encode('ASCII'))
    return msg_str

  def timestamp_mod(self,ts):
    return ts.replace(":","-").replace(".","-").replace("+","-")

  def mail(self,sender,recipient,message,password):
    self.s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    self.s.starttls()
    self.s.login(sender, password)
    self.s.sendmail(sender,recipient,message)
    self.s.quit()

  def scrub(self,txt):
    addresses = [m.group(1) for m in self.address_search.finditer(txt)]
    print addresses
    if len(addresses) = 0:
      return ['']
    ## Return the shortest email address
    return min(addresses, key=len)

if __name__ == "__main__":
  u = Util()
  assert u.scrub('"Jill McGee" Jill@McGee.com  ') == "Jill@McGee.com"
  assert u.scrub("<aa@bb.com> Babbots Babbots") == "aa@bb.com"
  assert u.scrub("(Bob) Cool@cool.com") == "Cool@cool.com"
  assert u.scrub("(SillyJim)Silly@cool.com") == "Silly@cool.com"

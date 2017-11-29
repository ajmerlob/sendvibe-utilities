import math
import sys
import smtplib
import re

class Util:
  def __init__(self):
    pass

  def mail(self,sender,recipient,message,password):
    self.s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    self.s.starttls()
    self.s.login(sender, password)
    self.s.sendmail(sender,recipient,message)
    self.s.quit()

  def scrub(self,txt):
    def _scrub(pattern,txt):
      try:
        email = re.search(pattern,txt).group(1)
        if '@' in email:
          return email
        else:
          email2 = email.replace(email,"").strip()
          if '@' in email2
            return email2
          else:
            return txt
      except:
        return txt
 
    if "<" in txt and ">" in txt:
      return _scrub("<(.*)>",txt)
    elif "(" in txt and ")" in txt:
      return _scrub("\((.*)\)",txt)
    elif '"' in txt:
      return _scrub('"(.*)"',txt)
    return txt

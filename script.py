#Script File

import twil as fv
go("http://127.0.0.1:5500/verification.html") # URL of the web application

from twill.commands import *
fv("1", "passcode", "1234")
submit()
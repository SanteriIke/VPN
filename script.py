#Script File

import twil as fv
go("http://localhost:8080/") # URL of the web application

from twill.commands import *
fv("1", "passcode", "1234")
submit()
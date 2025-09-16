Get-ADUser -Filter {GivenName -eq "Bob"} -Properties GivenName, Surname | Select-Object GivenName, Surname, SamAccountName

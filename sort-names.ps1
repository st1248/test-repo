# Save this as sort-names.ps1
# Usage: .\sort-names.ps1 -InputFile "input.tsv" -OutputFile "sorted.tsv"

param(
    [string]$InputFile = "input.tsv",
    [string]$OutputFile = "sorted.tsv"
)

# Read the data, split by tab, and sort by last name (second word in first column)
$data = Import-Csv -Delimiter "`t" -Path $InputFile -Header "FullName","SSN","DOB"
$sorted = $data | Sort-Object { ($_.FullName -split ' ')[1] }

# Output to file
$sorted | Export-Csv -Delimiter "`t" -Path $OutputFile -NoTypeInformation
Write-Host "Sorted data written to $OutputFile"

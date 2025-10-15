# Save as find-gcd.ps1
# Usage: .\find-gcd.ps1

# Data
 $data = @"
612-20-6832	5293-8502-0071-3058
Victor Faulkner	300-62-3266	5548-0246-6336-5664
Lisa Garrison	660-03-8360	4539-5385-7425-5825
Marjorie Green	213-46-8915	4916-9766-5240-6147
James Heard	559-81-1301	4532-4220-6922-9909
489-36-8350	
559-81-1301	
660-03-8360	
489-36-8352	
489-36-8350	
514-14-8905	
"@ -split "`n"

# Function to compute GCD
function Get-GCD($a, $b) {
    while ($b -ne 0) {
        $temp = $b
        $b = $a % $b
        $a = $temp
    }
    return [math]::Abs($a)
}

# Extract credit card numbers and convert to integers
$ccNumbers = $data | ForEach-Object {
    $fields = $_ -split "\t"
    $cc = $fields[-1] -replace '[^0-9]', ''
    if ($cc) { $cc -as [bigint] }
} | Where-Object { $_ }

# Find GCD of all credit card numbers
if ($ccNumbers.Count -gt 1) {
    $gcd = $ccNumbers[0]
    for ($i = 1; $i -lt $ccNumbers.Count; $i++) {
        $gcd = Get-GCD $gcd $ccNumbers[$i]
    }
    Write-Host "GCD of credit card numbers: $gcd"
} else {
    Write-Host "Not enough credit card numbers to compute GCD."
}

$SaveFile = $PSScriptRoot+"\save00.ff7"

# Get User ID
$UserIdScript = $PSScriptRoot+"\ff7_get_user_id.ps1"
$UserId = &$UserIdScript

# Calculate checksum
# Checksum = md5(save_file + user_id)
$md5 = New-Object -TypeName System.Security.Cryptography.MD5CryptoServiceProvider
$utf8 = New-Object -TypeName System.Text.UTF8Encoding
$bytes = [System.IO.File]::ReadAllBytes($SaveFile) + $utf8.GetBytes($UserId)
$hash = [System.BitConverter]::ToString($md5.ComputeHash($bytes))
$hash = $hash.replace("-", "").ToLower()

# print checksum
Write-Output $hash

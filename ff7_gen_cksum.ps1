$SaveFile = "save00.ff7"
$md5File  = "save.md5"

# Get User ID
$UserIdScript = $PSScriptRoot+"\ff7_get_user_id.ps1"
$UserId = &$UserIdScript

# Calculate checksum
# Checksum = md5(save_file + user_id)
Copy-Item -Path $SaveFile -Destination $md5File
Add-Content -Path $md5File -Value $UserID -NoNewline
$Hash = (Get-FileHash -Path $md5File -Algorithm md5).Hash.ToLower()
Remove-Item -Path $md5File

# print checksum
Write-Output $Hash

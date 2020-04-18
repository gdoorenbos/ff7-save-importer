$SaveFile = "save00.ff7.pc-orig"
$UserID   = "20419459"
$MD5Salt  = "md5salt.bin"
$md5File  = "save.md5"

Copy-Item -Path $SaveFile -Destination $md5File
Add-Content -Path $md5File -Value $UserID -NoNewline
Get-FileHash -Path $md5File -Algorithm md5
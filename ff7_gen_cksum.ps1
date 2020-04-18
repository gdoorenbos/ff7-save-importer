$SaveFile = "save00.ff7"
$UserID   = "20419459"
$md5File  = "save.md5"

Copy-Item -Path $SaveFile -Destination $md5File
Add-Content -Path $md5File -Value $UserID -NoNewline
$Hash = (Get-FileHash -Path $md5File -Algorithm md5).Hash.ToLower()
Remove-Item -Path $md5File

Write-Output $Hash
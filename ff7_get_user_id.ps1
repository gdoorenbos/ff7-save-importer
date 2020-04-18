$SteamDir = Get-ChildItem ([environment]::getfolderpath("mydocuments"))"Square Enix\Final Fantasy VII Steam\"
$UserId = ""

foreach ($child in $SteamDir) {
    if ($child.Name -match "user_[0-9]+") {
        $UserId = $child.Name.trim("user_")
    }
}
Write-Output $UserId
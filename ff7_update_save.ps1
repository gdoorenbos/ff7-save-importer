# Calculate checksum with new save file
$cksumScript = $PSScriptRoot+"\ff7_gen_cksum.ps1"
$cksum = &$cksumScript
if ($cksum -eq "") {
    Write-Error -Message "Could not calculate checksum" -Category InvalidData -ErrorId "cksum_empty"
    break
}

# Get user directory
$userDir = ""
$steamDir = Get-ChildItem ([environment]::getfolderpath("mydocuments"))"Square Enix\Final Fantasy VII Steam\"
foreach ($child in $steamDir) {
    if ($child.Name -match "user_*") {
        $userDir = $child.FullName
    }
}
if($userDir -eq "" -or !(Test-Path -Path $userDir)) {
    Write-Error -Message "Could not find valid user dir" -Category InvalidData -ErrorId "invalid_user_dir"
}

# backup metadata file
$metaFile = $userDir + "\metadata.xml"
$metaFileBackup = $PSScriptRoot + "\metadata.xml.bak"
Copy-Item -Path $metaFile -Destination $metaFileBackup

# find signature field in metadata file
$i = 0
$sigLineNum = 0
$metaContent = Get-Content -Path $metaFile
foreach ($line in $metaContent) {
    if ($sigLineNum -eq 0 -and $line -match "    <signature>\w+</signature>") {
        $sigLineNum = $i
    }
    $i = $i + 1
}
if ($sigLineNum -eq 0) {
    Write-Error -Message "Could not find signature field in metadata.xml" -Category InvalidData -ErrorId "no_sig_in_metadata"
    break
}

# replace checksum in metadatafile
$metaContent[$sigLineNum] = "    <signature>" + $cksum + "</signature>"
$metaContent | Set-Content -Path $metaFile

# Copy new save, backing up existing save
$oldSave = $userDir + "\save00.ff7"
$newSave = $PSScriptRoot + "\save00.ff7"
$backupSave = $PSScriptRoot + "\save00.ff7.bak"
if (Test-Path -Path $oldSave) {
    Copy-Item -Path $oldSave -Destination $backupSave
}
Copy-Item -Path $newSave -Destination $oldSave

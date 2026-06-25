# Lab 07.2 - Windows Authentication Review - Sanitized
# Run on the Windows host of the lab.
# Read-only. Exports counts only, not usernames, IPs or raw messages.

$SyncPath = "C:\Carrera_Ciberseguridad\05_Capturas"
$LabBase = "C:\Carrera_Ciberseguridad\07_Windows_Event_Log_Defensive_Review"
$EvidencePath = Join-Path $LabBase "evidencias"

New-Item -ItemType Directory -Force -Path $SyncPath | Out-Null
New-Item -ItemType Directory -Force -Path $EvidencePath | Out-Null

$Out = Join-Path $SyncPath "lab07_02_windows_authentication_review_sanitized.txt"
$FormalOut = Join-Path $EvidencePath "lab07_02_windows_authentication_review_sanitized.txt"
$StartTime = (Get-Date).AddDays(-7)

"LAB 07 - MISSION 7.2 - WINDOWS AUTHENTICATION REVIEW" | Set-Content $Out -Encoding UTF8
"Evidence type: Sanitized Windows authentication event review" | Add-Content $Out
"Collection time: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" | Add-Content $Out
"Scope: Windows Security log, last 7 days" | Add-Content $Out
"Privacy note: usernames, IP addresses, workstation names and raw messages are not exported." | Add-Content $Out
"Time window start: $($StartTime.ToString('yyyy-MM-dd HH:mm:ss'))" | Add-Content $Out
"" | Add-Content $Out

"### Authentication Event IDs reviewed" | Add-Content $Out
"4624 - Successful logon" | Add-Content $Out
"4625 - Failed logon" | Add-Content $Out
"4634 - Logoff" | Add-Content $Out
"4648 - Explicit credentials used" | Add-Content $Out
"4672 - Special privileges assigned to new logon" | Add-Content $Out
"" | Add-Content $Out

$Ids = @{
    4624 = "Successful logon"
    4625 = "Failed logon"
    4634 = "Logoff"
    4648 = "Explicit credentials used"
    4672 = "Special privileges assigned"
}

"### Event ID counts - last 7 days, max 1000 each" | Add-Content $Out

foreach ($id in $Ids.Keys | Sort-Object) {
    try {
        $count = @(Get-WinEvent -FilterHashtable @{LogName="Security"; Id=$id; StartTime=$StartTime} -MaxEvents 1000 -ErrorAction Stop).Count
        "Event ID $id - $($Ids[$id]): $count" | Add-Content $Out
    }
    catch {
        "Event ID $id - $($Ids[$id]): not available or no readable events" | Add-Content $Out
    }
}

"" | Add-Content $Out
"### Basic SOC interpretation" | Add-Content $Out
"Authentication visibility is available through the Windows Security log." | Add-Content $Out
"Successful logons, failed logons, logoffs, explicit credential use and privileged logons are reviewed as count-based indicators." | Add-Content $Out
"Counts are triage indicators, not proof of compromise." | Add-Content $Out
"No raw event messages or personal identifiers are exported." | Add-Content $Out
"Recommended next action: review System and Application health events and prepare a short SOC triage summary." | Add-Content $Out
"" | Add-Content $Out
"Mission 7.2 completed pending analyst review." | Add-Content $Out

Copy-Item $Out $FormalOut -Force

Write-Host "Evidence created:"
Write-Host $Out
Write-Host ""
Get-Content $Out -TotalCount 25

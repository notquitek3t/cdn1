# firefox one liner install, irm https://snippets.k3t.xyz/windows/scripts/firefox.ps1
Start-BitsTransfer -Source "https://download.mozilla.org/?product=firefox-msi-latest-ssl&os=win64&lang=en-US" -Destination $env:TEMP\firefox.msi
Start-Process $env:TEMP\firefox.msi /passive
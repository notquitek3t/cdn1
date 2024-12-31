Start-BitsTransfer `
    -Source "https://globalcdn.nuget.org/packages/microsoft.ui.xaml.2.7.3.nupkg?packageVersion=2.7.3" `
    -Destination $env:TEMP\xaml.zip
New-Item -ItemType Directory -Path $env:TEMP\xaml
Expand-Archive -Path $env:TEMP\xaml.zip -DestinationPath $env:TEMP\xaml
Add-AppxPackage -Path $env:TEMP\"xaml\tools\AppX\x64\Release\Microsoft.UI.Xaml.2.7.appx"
Remove-Item $env:TEMP\xaml.zip
Remove-Item $env:TEMP\xaml -Recurse

Start-BitsTransfer `
    -Source "https://download.microsoft.com/download/4/7/c/47c6134b-d61f-4024-83bd-b9c9ea951c25/Microsoft.VCLibs.x64.14.00.Desktop.appx" `
    -Destination $env:TEMP\UWPDesktop.appx
Add-AppxPackage $env:TEMP\UWPDesktop.appx
Remove-Item $env:TEMP\UWPDesktop.appx

# Get the download URL of the latest winget installer from GitHub:
$API_URL = "https://api.github.com/repos/microsoft/winget-cli/releases/latest"
$DOWNLOAD_URL = $(Invoke-RestMethod $API_URL).assets.browser_download_url |
    Where-Object {$_.EndsWith(".msixbundle")}

# Download the installer:
Start-BitsTransfer -Source $DOWNLOAD_URL -Destination $env:TEMP\winget.msixbundle

# Install winget:
Add-AppxPackage $env:TEMP\winget.msixbundle
echo "Winget is installed."
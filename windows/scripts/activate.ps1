# activation one liner, irm https://snippets.k3t.xyz/windows/scripts/activate.ps1 | iex
Set-ExecutionPolicy Unrestricted
[Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12
& ([ScriptBlock]::Create((irm https://get.activated.win))) /HWID /Ohook
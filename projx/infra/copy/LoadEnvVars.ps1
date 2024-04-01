# LoadEnvVars.ps1
Get-Content .env | ForEach-Object {
    if ($_ -match '^[^#]\w+=') {
        $key, $value = $_.Split('=',2)
        [System.Environment]::SetEnvironmentVariable($key, $value, [System.EnvironmentVariableTarget]::Process)
        Write-Host "Set environment variable: $key"
    }
}

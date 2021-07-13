
$watcher = New-Object System.IO.FileSystemWatcher
$watcher.IncludeSubdirectories = $true
$watcher.Path = 'E:\test\'
$watcher.EnableRaisingEvents = $true

$action = {
    $path = $event.SourceEventArgs.FullPath
    $changetype = $event.SourceEventArgs.Changetype
    New-Item -path E:\test\hello.txt -ItemType File -Value "New file detected $path, $changetype"
}

Register-ObjectEvent $watcher "Created" -Action $action
Get-EventSubscriber

New-Item -path E:\test\hello.txt -ItemType File

Unregister-Event -SubscriptionId 2

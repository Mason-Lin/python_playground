# Start-Job -FilePath ./mouseclick.ps1
$signature = @'
            [DllImport("user32.dll",CharSet=CharSet.Auto, CallingConvention=CallingConvention.StdCall)]
            public static extern void mouse_event(long dwFlags, long dx, long dy, long cButtons, long dwExtraInfo);
'@

$SendMouseClick = Add-Type -memberDefinition $signature -name "Win32MouseEventNew" -namespace Win32Functions -passThru

function mooseClick {
    $SendMouseClick::mouse_event(0x00000002, 0, 0, 0, 0); #Left Mouse Down
    $SendMouseClick::mouse_event(0x00000004, 0, 0, 0, 0); #Left Mouse Up
    return
}


Start-Sleep -Seconds 1
mooseClick
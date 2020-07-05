from pywinauto.application import Application
import pywinauto
import sys
import os

# start app
os.system('start ms-settings:notifications')
app = Application(backend='uia').connect(title_re="Settings")
print(app.is_process_running(), type(app))
framewin = app.window(class_name='ApplicationFrameWindow')
print(framewin.exists())

# corewin = framewin.window(class_name='Windows.UI.Core.CoreWindow')
# print(corewin.exists())

# targetwin = corewin.window(class_name='LandmarkTarget')
# print(targetwin.exists())

# control = targetwin.window(auto_id='ItemsControlScrollViewer')
# print(control.exists())

# notifications = control.window(title='Notifications', class_name='GroupItem')
# print(notifications.exists())

# toggle_btn = notifications.window(auto_id='SystemSettings_Notifications_ShowAppNotifications_ToggleSwitch')
# print(toggle_btn.exists())

toggle_btn_fast = framewin.window(auto_id='SystemSettings_Notifications_ShowAppNotifications_ToggleSwitch')
print(toggle_btn_fast.exists())

print('====')
print(toggle_btn_fast, toggle_btn_fast.wrapper_object(), toggle_btn_fast.wrapper_object().get_toggle_state())
# print(toggle_btn, toggle_btn.wrapper_object(), toggle_btn.wrapper_object().get_toggle_state())

toggle_btn_fast.toggle()


# Name	Get notifications from apps and other senders
# PS
# $registryPath = "HKCU:\Software\Microsoft\Windows NT\CurrentVersion\Windows\Pen"
# $GetValue = {Get-ItemPropertyValue -Path $registryPath -Name 'PenArbitrationType'}
# Set-ItemProperty -Path $registryPath -Name 'PenArbitrationType' -Value 1
# HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced
# EnableBalloonTips / 32-bit DWORD


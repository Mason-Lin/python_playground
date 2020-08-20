from pprint import pprint

import wmi


class VWMI:
    def __init__(self, **kwargs):
        self.wmi = wmi.WMI(**kwargs)

    def get_all_namespaces_under_current(self):
        return self.wmi.instances("__namespace")

    def __getattr__(self, attrName):
        if attrName not in self.__dict__:
            return getattr(self.wmi, attrName)
        return self.__dict__[attrName]


if __name__ == "__main__":
    vwmi = VWMI()
    print(vwmi)
    pprint(vwmi.get_all_namespaces_under_current())
    assert (
        wmi.WMI().Win32_SystemBIOS
        == vwmi.wmi.Win32_SystemBIOS
        == vwmi.Win32_SystemBIOS
    )
    assert (
        wmi.WMI().Win32_SystemBIOS()
        == vwmi.wmi.Win32_SystemBIOS()
        == vwmi.Win32_SystemBIOS()
    )

    for pnp in vwmi.Win32_PnPEntity(
        Manufacturer="Microsoft", Caption="X3S Stereo"
    ):
        print(pnp)
    # instance of Win32_PnPEntity
    # {
    #         Caption = ***
    #         ClassGuid = ***
    #         CompatibleID = ***
    #         ConfigManagerErrorCode = ***
    #         ConfigManagerUserConfig = ***
    #         CreationClassName = ***
    #         Description = ***
    #         DeviceID = ***
    #         HardwareID = ***
    #         Manufacturer = ***
    #         Name = ***
    #         PNPClass = ***
    #         PNPDeviceID = ***
    #         Present = ***
    #         Service = ***
    #         Status = ***
    #         SystemCreationClassName = ***
    #         SystemName = ***
    # }
    for pnp in vwmi.Win32_PnPEntity(
        ["Caption", "Name"], Manufacturer="Microsoft", Caption="X3S Stereo"
    ):
        print(pnp)
    # instance of Win32_PnPEntity
    # {
    #         Caption = "X3S Stereo";
    #         DeviceID = ***;
    #         Name = "X3S Stereo";
    # };
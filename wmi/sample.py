from pprint import pprint

import wmi


class VWMI:
    def __init__(self, **kwargs):
        self.wmi = wmi.WMI(**kwargs)

    def get_all_namespaces(self):
        return self.instances("__namespace")

    def get_all_classes(self):
        return [c for c in self.classes]

    def get_all_cim_classes(self):
        return [c for c in self.classes if c.lower().startswith("cim")]

    def get_all_win32_classes(self):
        return [c for c in self.classes if c.lower().startswith("win32")]

    def get_all_msft_classes(self):
        return [c for c in self.classes if c.lower().startswith("msft")]

    def get_all_associated_classes(self, class_name):
        return getattr(self, class_name).associated_classes

    def get_all_instances(self, class_name):
        return getattr(self, class_name)()

    def __getattr__(self, attrName):
        if attrName not in self.__dict__:
            return getattr(self.wmi, attrName)
        return self.__dict__[attrName]


if __name__ == "__main__1":
    vwmi = VWMI()
    print(vwmi)
    pprint(vwmi.get_all_namespaces())
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

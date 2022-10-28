from abc import ABC, abstractmethod


class StatusBar(ABC):
    def __init__(self, system: str):
        self._system = system

    @abstractmethod
    def create(self):
        """abstract method for creation of a status bar"""


class MainMenu(ABC):
    def __init__(self, system: str):
        self._system = system

    @abstractmethod
    def create(self):
        """abstract method for creation of a main menu"""


class MainWindow(ABC):
    def __init__(self, system: str):
        self._system = system

    @abstractmethod
    def create(self):
        """abstract method for creation of a main window"""


class WindowsStatusBar(StatusBar):
    def __init__(self):
        super().__init__("Windows")

    def create(self):
        print(f"Created status bar for {self._system}")


class WindowsMainMenu(MainMenu):
    def __init__(self):
        super().__init__("Windows")

    def create(self):
        print(f"Created main menu for {self._system}")


class WindowsMainWindow(MainWindow):
    def __init__(self):
        super().__init__("Windows")

    def create(self):
        print(f"Created main window for {self._system}")


class LinuxStatusBar(StatusBar):
    def __init__(self):
        super().__init__("Linux")

    def create(self):
        print(f"Created status bar for {self._system}")


class LinuxMainMenu(MainMenu):
    def __init__(self):
        super().__init__("Linux")

    def create(self):
        print(f"Created main menu for {self._system}")


class LinuxMainWindow(MainWindow):
    def __init__(self):
        super().__init__("Linux")

    def create(self):
        print(f"Created main window for {self._system}")


class GuiAbstractFactory(ABC):
    """
    Abstract factory base class
    """

    @abstractmethod
    def get_status_bar(self) -> StatusBar:
        """abstract method for calling the creation of a status bar"""

    @abstractmethod
    def get_main_menu(self) -> MainMenu:
        """abstract method for calling the creation of a main menu"""

    @abstractmethod
    def get_main_window(self) -> MainWindow:
        """abstract method for calling the creation of a main window"""


class WindowsGuiFactory(GuiAbstractFactory):
    def get_status_bar(self) -> StatusBar:
        """method for calling the creation of a Windows status bar"""
        return WindowsStatusBar()

    def get_main_menu(self) -> MainMenu:
        """method for calling the creation of a Windows main menu"""
        return WindowsMainMenu()

    def get_main_window(self) -> MainWindow:
        """method for calling the creation of a Windows main window"""
        return WindowsMainWindow()


class LinuxGuiFactory(GuiAbstractFactory):
    def get_status_bar(self) -> StatusBar:
        """method for calling the creation of a Linux status bar"""
        return LinuxStatusBar()

    def get_main_menu(self) -> MainMenu:
        """method for calling the creation of a Linux main menu"""
        return LinuxMainMenu()

    def get_main_window(self) -> MainWindow:
        """method for calling the creation of a Linux main window"""
        return LinuxMainWindow()


class Application:
    def __init__(self, factory: GuiAbstractFactory):
        self._gui_factory = factory

    def create_gui(self):
        status_bar = self._gui_factory.get_status_bar()
        main_menu = self._gui_factory.get_main_menu()
        main_window = self._gui_factory.get_main_window()
        status_bar.create()
        main_menu.create()
        main_window.create()


def create_factory(system: str) -> GuiAbstractFactory:
    factory_dict = {
        "Windows": WindowsGuiFactory,
        "Linux": LinuxGuiFactory,
    }
    return factory_dict[system]()


if __name__ == "__main__":
    for system_type in ("Windows", "Linux"):
        print(f"---->Loading app for {system_type}<----")
        ui = create_factory(system=system_type)
        app = Application(ui)
        app.create_gui()

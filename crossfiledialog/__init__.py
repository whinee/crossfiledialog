import sys
from shutil import which
from typing import Optional

from crossfiledialog.exceptions import NoImplementationFoundException

# Global variable to store picker preferences
default_picker_preferences = ["kdialog", "pygobject", "qt", "zenity"]


def file_dialog(picker_preference: Optional[list[str]] = None):  # noqa: C901
    if sys.platform == "linux":
        kdialog_binary = which("kdialog")
        zenity_binary = which("zenity")

        # Get preferences
        preferred_picklers = (
            picker_preference if picker_preference else default_picker_preferences
        )

        # Import pickers based on preferences
        for picker in preferred_picklers:
            if picker == "kdialog" and kdialog_binary:
                from crossfiledialog.file_pickers.kdialog import (  # type: ignore[assignment]
                    FileDialog,
                )

                return FileDialog

            if picker == "pygobject":
                from crossfiledialog.file_pickers.pygobject import (  # type: ignore[assignment]
                    FileDialog,
                )

                return FileDialog

            if picker == "qt":
                from crossfiledialog.file_pickers.qt import (  # type: ignore[assignment]
                    FileDialog,
                )

                return FileDialog

            if picker == "zenity" and zenity_binary:
                from crossfiledialog.file_pickers.zenity import (  # type: ignore[assignment]
                    FileDialog,
                )

                return FileDialog

        raise NoImplementationFoundException

    if sys.platform == "win32":
        print("win32")
        from crossfiledialog.file_pickers.win32 import (  # type: ignore[assignment]
            FileDialog,
        )

        return FileDialog

    raise NoImplementationFoundException

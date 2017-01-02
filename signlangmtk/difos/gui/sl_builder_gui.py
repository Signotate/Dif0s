import os
import sys
import signal
from signlangmtk.difos.gui.sl_builder_app import SignLanguageBuilderApp
from signlangmtk.util import setup_logging


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    setup_logging()
    app = SignLanguageBuilderApp()
    sys.exit(app.run(sys.argv))

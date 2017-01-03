import sys
import signal
import logging
import gi
from signlangmtk.util import setup_logging

logger = logging.getLogger(__name__)


def run_difos(log_level=logging.INFO):
    setup_logging(log_level)
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    gi.require_version('Gtk', '3.0')

    logger.info('Starting Difos')

    from signlangmtk.difos.gui.difos_app import DifosApp
    difos = DifosApp()
    return difos.run(sys.argv)


if __name__ == '__main__':
    sys.exit(run_difos(log_level=logging.DEBUG))

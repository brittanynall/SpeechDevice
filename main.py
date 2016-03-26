from PyQt5 import QtWidgets
from NetworkService import NetworkService
from RpcService import RpcServer
from threading import Thread
import logging
import MainWindow

debug_logger = logging.getLogger(__name__)

if __name__ == '__main__':
    import sys
 
    app = QtWidgets.QApplication(sys.argv)

    # instantiate the application window
    main_window = MainWindow.Main()
    main_window.show()

    try:
        server = RpcServer(callbacks=main_window.create_dispatcher())

        # Start Rpc server over http in a separate thread
        server_thread = Thread(target=server.start)
        server_thread.start()

        # Start listening to network discovery
        network_service = NetworkService()
        network_service.start_service()

        # wait for the application
        sys.exit(app.exec_())

        # @todo: add safe shutdown here
    except KeyboardInterrupt:
        pass
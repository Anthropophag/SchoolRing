import sys

from PyQt6 import uic
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow
)

from datacheking import LoginChecker, RegistrChecker
from services import LoginData, RegistrData, RingManager
from bd_work import DataBaseManager


class Window(QMainWindow):
    def __init__(self):
        """Create mainwindow"""

        super().__init__()
        uic.loadUi('ui/main.ui', self)
        self.is_logined = False
        self.load_ui()

        self.connect_button()
        self.bd_manager = DataBaseManager()
        self.ring()

    def load_ui(self):
        self.login_window = uic.loadUi('ui/logining.ui')
        self.registration_window = uic.loadUi('ui/registration.ui')
        self.sucsesfuly_window = uic.loadUi('ui/sucsesfully.ui')
        self.error_window = uic.loadUi('ui/error.ui')
        self.authorization_window = uic.loadUi('ui/authorization.ui')

    def connect_button(self):
        """Connect button in main window"""

        # menu tab
        self.home_button.clicked.connect(self.go_home)
        self.timetable_button.clicked.connect(self.go_timetable)
        self.template_button.clicked.connect(self.go_template)
        # authorization
        self.login_button_cerkle.clicked.connect(self.authorization)
        self.login_button_text.clicked.connect(self.authorization)

    def go_home(self):
        """Switching tub to Home page"""

        self.stackedWidget.setCurrentIndex(0)

    def go_timetable(self):
        """Switching tub to Timetable page"""

        self.stackedWidget.setCurrentIndex(1)

    def go_template(self):
        """Switching tub to Template page"""

        self.stackedWidget.setCurrentIndex(2)

    def authorization(self):
        """Open authorization dialog window"""

        self.authorization_window.show()
        self.authorization_window.start_login_button.clicked.connect(self.logining)
        self.authorization_window.start_regisration_button.clicked.connect(self.registring)

    def logining(self):
        """Open login dialog window"""

        self.authorization_window.hide()
        self.login_window.show()
        self.finish_logining()

    def registring(self):
        """Open registration dialog window and hide authorization_dialog"""

        self.authorization_window.hide()
        self.registration_window.show()
        self.registration_window.go_sistem_button_reg.clicked.connect(self.finish_registration)

    def sucsesfully_login(self):
        self.sucsesfuly_window.show()
        self.sucsesfuly_window.suc_button.clicked.connect(self.closing_windows)
        self.is_logined = True
        # self.change_interface(self.data.FIO)

    def sucsesfully_registration(self):
        """Finsh sucsesfuly authorization process"""

        self.sucsesfuly_window.show()
        self.sucsesfuly_window.suc_button.clicked.connect(self.closing_windows)
        self.bd_manager.add_user(self.data)
        self.is_logined = True
        self.change_interface(self.data.FIO)

    def closing_windows(self):
        """Close login-window after authorization"""

        if self.login_window.isHidden():
            self.registration_window.hide()
            self.sucsesfuly_window.hide()
        else:
            self.login_window.hide()
            self.sucsesfuly_window.hide()

    def error_authorization(self):
        """Show error message"""

        self.error_window.show()
        self.error_window.er_button.clicked.connect(self.error_window.hide)

    def finish_registration(self):
        """Connect finfish-button for registr and login"""

        self.data = self.get_reg_data()
        checker = RegistrChecker(self.data)
        if checker.is_correct:
            self.sucsesfully_registration()
        else:
            self.error_authorization()

    def finish_logining(self):
        self.data = self.get_log_data()
        checker = LoginChecker(self.data)
        if checker.is_correct:
            self.login_window.go_sistem_button_log.clicked.connect(self.sucsesfully_login)
        else:
            self.login_window.go_sistem_button_log.clicked.connect(self.error_authorization)

    def get_log_data(self) -> LoginData:
        """Get user log-data for us checking"""

        return LoginData(
            self.login_window.login_lineEdit.text(),
            self.login_window.password_lineEdit.text()
        )

    def get_reg_data(self) -> RegistrData:
        """Get user reg-data for us checking"""

        return RegistrData(
            self.registration_window.FIO_lineEdit.text(),
            self.registration_window.login_lineEdit.text(),
            self.registration_window.concoct_pw_lineEdit.text(),
            self.registration_window.repeat_pw_lineEdit.text(),
            self.registration_window.school_num_lineEdit.text(),
            self.registration_window.building_num_lineEdit.text(),
            self.registration_window.phone_num_lineEdit.text()
        )

    def interface_change(self):
        """Change login-interface after successful authorization"""

        if self.is_logined:
            user_name = self.bd_manager.get_user_name()
            self.chonge_login_button_text(user_name)
            self.chonge_login_button_circle(user_name)

    def change_interface(self, FIO: str):
        """Change interface after successful authorization"""
        name = FIO.strip().split()[1]
        if len(name) > 8:
            name = name[0:7] + '...'
        self.login_button_text.setText(name)
        self.login_button_cerkle.setText(name[0])

    def ring(self):
        rm = RingManager()
        rm.ring()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

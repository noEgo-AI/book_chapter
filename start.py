import sys
from tkinter.messagebox import askyesno

import database

from PySide6.QtWidgets import QApplication
from restart import back_main


print(1)
app = QApplication()
window = back_main()
window.show()
app.exec()

database.connection.commit()

database.cursor.close()
database.connection.close()
sys.exit()

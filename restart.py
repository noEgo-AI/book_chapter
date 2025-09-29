import UI_background
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import UI_mainscreen
import UI_login_screen
import UI_create_screen
import threading
import database
import requests
import time

count = 0
print(3)

hello = "hello 입니다."
pri_info = []


def msgbox(title, detail):
    box = QMessageBox()
    box.setWindowTitle("알림창")
    box.setText(title)
    box.setInformativeText(detail)
    box.addButton("확인", QMessageBox.ButtonRole.YesRole)
    return box.exec()


# 로그인 화면
class scr_login(QMainWindow, UI_login_screen.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("LOGIN")

        self.num_switch = 0

        self.win = 1
        self.win1 = 1
        self.sql = ""
        self.login_name = ""
        self.password_name = ""

        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        # login = QLineEdit()
        # login.textEdited
        # self.login.textEdited.connect(self.t_login)
        self.btn_login.pressed.connect(self.btn_pressed)
        # self.password.textEdited.connect(self.t_password)
        # self.btn_login.pressed.connect(self.cls_mode)
        # self.login.editingFinished.connect(self.t_login)
        self.btn_exit.clicked.connect(self.ab_exit)
        self.btn_create.clicked.connect(self.new_create)
        self.login.textChanged.connect(self.only_tab)

    def only_tab(self):
        self.num_switch = 1

    def keyReleaseEvent(self, event):
        if self.num_switch == 0 and event.key() == Qt.Key.Key_Tab:
            self.login.setFocus()
            self.num_switch = 1
        elif event.key() == Qt.Key.Key_Tab:
            self.password.setFocus()
            self.num_switch = 0

        if event.key() == Qt.Key.Key_Return:
            self.btn_pressed()

    def btn_pressed(self):
        self.sql = (f"select ifnull(max(access_id),'#a1a1') as access_id from information where access_id = "
                    f"'{self.login.text()}'")
        database.cursor.execute(self.sql)
        tag_info = database.cursor.fetchall()
        global count
        count += 1
        print(f"count : {count}\ntag_info :{tag_info[0]['access_id']}\nself.login : {self.login.text()}")

        if not tag_info[0]['access_id'] == '#a1a1':
            self.sql = (f"select ifnull(local_id,0) as local_id, ifnull(access_id,0) as access_id,"
                        f"ifnull(password,0) as password, ifnull(name,0) as name,ifnull(age,'write your age') as age,"
                        f"ifnull(prefer,'something to write') as prefer "
                        f"from information where access_id = '{self.login.text()}'")
            database.cursor.execute(self.sql)
            tag_info = database.cursor.fetchall()

            if tag_info[0]['password'] == self.password.text():
                global pri_info
                pri_info = tag_info

                self.win = scr_main()
                self.win.show()
                self.close()
                # main_window = Main()
                # main_window.exec_()
            else:
                msgbox("경고", "아이디와 비번을 잘못 입력하였습니다.")

    # def t_login(self, text):
    #     self.login_name = text
    #
    # def t_password(self, text):
    #     self.password_name = text

    def new_create(self):
        self.win1 = cr_main()
        self.win1.show()

    def ab_exit(self):
        self.close()


# 메인 화면
class scr_main(QMainWindow, UI_mainscreen.Ui_MainWindow):
    count = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lb_mean.setText("<i>hello</i>")
        self.win = 1

        if self.stackedWidget.currentWidget().objectName() == "page_profile":
            self.btn_profile2.setChecked(True)
            self.btn_profile1.setChecked(True)
            self.btn_calendar1.setChecked(False)
            self.btn_calendar2.setChecked(False)
            self.btn_iword1.setChecked(False)
            self.btn_iword2.setChecked(False)
        elif self.stackedWidget.currentWidget().objectName() == "page_calendar":
            self.btn_calendar1.setChecked(True)
            self.btn_calendar2.setChecked(True)
            self.btn_profile2.setChecked(False)
            self.btn_profile1.setChecked(False)
            self.btn_iword1.setChecked(False)
            self.btn_iword2.setChecked(False)
        elif self.stackedWidget.currentWidget().objectName() == "page_iword":
            self.btn_iword1.setChecked(True)
            self.btn_iword2.setChecked(True)
            self.btn_profile2.setChecked(False)
            self.btn_profile1.setChecked(False)
            self.btn_calendar1.setChecked(False)
            self.btn_calendar2.setChecked(False)

        self.widget_3.setHidden(True)
        self.sbox_year.setHidden(True)

        self.edit_name.setText(pri_info[0]['name'])
        self.edit_pw.setText(pri_info[0]['password'])
        self.edit_age.setText(str(pri_info[0]['age']))
        self.edit_detail.setText(pri_info[0]['prefer'])

        self.edit_name_text = self.edit_name.text()
        self.edit_age_text = self.edit_age.text()
        self.edit_detail_text = self.edit_detail.text()
        self.edit_pw_text = self.edit_pw.text()

        self.btn_profile1.clicked.connect(self.switch_profile)
        self.btn_profile2.clicked.connect(self.switch_profile)

        self.btn_calendar1.clicked.connect(self.switch_calendar)
        self.btn_calendar2.clicked.connect(self.switch_calendar)

        self.btn_iword2.clicked.connect(self.switch_iword)
        self.btn_iword1.clicked.connect(self.switch_iword)

        self.btn_logout1.clicked.connect(self.logout)
        self.btn_logout2.clicked.connect(self.logout)

        self.btn_exit1.clicked.connect(self.ab_exit)
        self.btn_exit2.clicked.connect(self.ab_exit)

        self.btn_save.hide()
        self.btn_cancel.hide()
        self.check_mf.toggled.connect(self.profile_modify)
        self.btn_save.clicked.connect(self.profile_save)
        self.btn_cancel.clicked.connect(self.profile_cancel)

        if self.lb_state.text() == "저장하였습니다." or self.lb_state.text() == "취소하였습니다.":
            self.time_lag()

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key.Key_Alt and self.save_toggle.isChecked():
            self.save_toggle.setChecked(False)
        elif event.key() == Qt.Key.Key_Alt:
            self.save_toggle.setChecked(True)

        if event.key() == Qt.Key.Key_Return and self.stackedWidget.currentWidget().objectName() == "page_iword":
            self.inner_search(self.insertword.text())

    def keyPressEvent(self, event):
        if event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            if event.key() == Qt.Key.Key_T:
                self.insertword.setFocus()
                self.insertword.selectAll()

        if event.key() == Qt.Key.Key_F2:
            self.enter_save()

    # def keyPressEvent(self, event):

    def inner_search(self, word):
        sql = f"select * from mword where word like '{word}'"
        database.cursor.execute(sql)
        exit_word = database.cursor.fetchone()
        # print(exit_word)
        if exit_word is None:
            self.crawling_dic_daum(word)
            b = self.lb_mean.text().replace("\'","\\\'")
            # print(b)
            sql = f"insert into mword (word, mean) values('{self.insertword.text()}', '{b}')"
            database.cursor.execute(sql)
            database.connection.commit()
        # else:
            # msgbox("경고","모름")
            # for i in exit_word:


    def crawling_dic_naver(self, word):
        self.lb_mean.setText("")
        driver = webdriver.Edge()
        driver.get("https://en.dict.naver.com/#/search?query=" + word + "&range=all")
        response1 = driver.page_source
        soup = BeautifulSoup(response1, "html.parser")

        #
        with open('naver_dic1.txt', 'w', encoding='utf-8') as f:
            f.write(response1)

        div = soup.select_one('div.origin').find('a').get('href')
        print(div)

    def crawling_dic_daum(self, word):
        self.lb_mean.setText("")
        respond1 = requests.get("https://dic.daum.net/search.do?q=" + word)
        # r.raise_for_status()
        time.sleep(2)
        soup = BeautifulSoup(respond1.text, 'html.parser')
        div = soup.select_one('div.search_box').find('a').get('href')
        # respond2 = div.select('div > div > strong > a')

        # respond2 = requests.get("https://dic.daum.net/"+div)
        # soup2 = BeautifulSoup(respond2.text, 'html.parser')
        # div2 = soup2.find_all('div', class_='detail_top')

        driver = webdriver.Edge()
        driver.get("https://dic.daum.net" + div + '&q=' + word)
        respond2 = driver.page_source
        soup2 = BeautifulSoup(respond2, 'html.parser')
        # mean_type = soup2.select_one('div.wrap_extit').find_all()
        mean_property1 = soup2.select('div.fold_ex > div')

        ex_list = []
        short_text = ""
        short_num = 0
        short_count = 0

        for index, element in enumerate(mean_property1):
            # ex_list.append(index)
            ex_list.append(element.text)

        # print(ex_list)

        for list_text in ex_list:
            for ss in list_text:
                if ss == "\n":
                    short_num += 1
                    pass
                elif ss == "뜻" or ss == "별" or ss == "예" or ss == "문" or ss == "열" or ss == "기":
                    pass
                elif self.byte_size(short_text) - short_count > 75:
                    short_text += ss
                    short_text += "<br>"
                    short_count += 75
                else:
                    short_text += ss
            if short_num == 3:
                short_text += " "
                short_num = 0
                short_count = 0
            elif short_num == 1 and len(short_text) < 6:
                self.lb_mean.setText(self.lb_mean.text() + "<span style='font-size:24pt; font-style:italic;'>" +
                                     short_text + "</span>" + " " + "<br><br>")
                # print(str(self.byte_size(short_text)))
                # print(f"{short_text} : {len(short_text)}")
                short_text = ""
                short_num = 0
                short_count = 0
            else:
                self.lb_mean.setText(self.lb_mean.text() + short_text + "<br><br>")
                # print(str(self.byte_size(short_text)))
                # print(short_text)
                short_text = ""
                short_num = 0
                short_count = 0

        # print(mean_auto1)

        # elements = soup.select('div.esg-entry-content a > span') 예제

        # for index, element in enumerate(mean_property1):
        #
        #     print("{} 번째 {}".format(index, element.text))

        # print(soup2)

        # respond2
        # print(div2)
        # data = soup
        # .select('#course_list .course')

        # with open('daum_dic5.txt', 'w', encoding='utf-8') as f:
        #     f.write(soup2.prettify())

        # print(type(data), data, '\n')
        # print(soup.find('a'))

    @staticmethod
    def byte_size(string):
        return len(string.encode('utf-8'))

    def switch_profile(self):
        self.stackedWidget.setCurrentIndex(2)
        self.btn_calendar2.setChecked(False)
        self.btn_calendar1.setChecked(False)
        self.btn_profile2.setChecked(True)
        self.btn_profile1.setChecked(True)
        self.btn_iword2.setChecked(False)
        self.btn_iword1.setChecked(False)

    def switch_calendar(self):
        self.stackedWidget.setCurrentIndex(3)
        self.btn_calendar2.setChecked(True)
        self.btn_calendar1.setChecked(True)
        self.btn_profile2.setChecked(False)
        self.btn_profile1.setChecked(False)
        self.btn_iword2.setChecked(False)
        self.btn_iword1.setChecked(False)

    def switch_iword(self):
        self.stackedWidget.setCurrentIndex(0)
        self.btn_calendar2.setChecked(False)
        self.btn_calendar1.setChecked(False)
        self.btn_profile2.setChecked(False)
        self.btn_profile1.setChecked(False)
        self.btn_iword2.setChecked(True)
        self.btn_iword1.setChecked(True)

    def profile_modify(self):

        if self.check_mf.isChecked():
            self.edit_name.setReadOnly(False)
            self.edit_detail.setReadOnly(False)
            self.edit_age.setReadOnly(False)
            self.edit_pw.setReadOnly(False)
            self.btn_save.show()
            self.btn_cancel.show()
            self.lb_state.setText("수정 중...")
        self.check_mf.hide()

    def enter_save(self):
        if self.save_toggle.isChecked():
            msgbox("정보", "성공")
            msgbox("정보", self.insertword.text())
        else:
            msgbox("정보", "실패")
            msgbox("정보", self.insertword.text())

    def profile_save(self):
        if not self.edit_name_text == self.edit_name.text():
            sql = (f"update information set name = '{self.edit_name.text()}' where local_id = "
                   f"{int(pri_info[0]['local_id'])}")
            database.cursor.execute(sql)
            # print(f"{self.edit_name_text} : {self.edit_name.text()}")
            self.edit_name_text = self.edit_name.text()
            # print("name")

        if not self.edit_age_text == self.edit_age.text():
            sql = (f"update information set age = {int(self.edit_age.text())} where local_id = "
                   f"{int(pri_info[0]['local_id'])}")
            database.cursor.execute(sql)
            self.edit_age_text = self.edit_age.text()

            # print("age")

        if not self.edit_pw_text == self.edit_pw.text():
            sql = (f"update information set password = '{self.edit_pw.text()}' where local_id = "
                   f"{int(pri_info[0]['local_id'])}")
            database.cursor.execute(sql)
            self.edit_pw_text = self.edit_pw.text()
            # print("password")

        if not self.edit_detail_text == self.edit_detail.text():
            sql = (f"update information set prefer = '{self.edit_detail.text()}' where local_id = "
                   f"{int(pri_info[0]['local_id'])}")
            database.cursor.execute(sql)
            self.edit_detail_text = self.edit_detail.text()
            print("prefer")

        self.btn_save.hide()
        self.btn_cancel.hide()
        self.edit_name.setReadOnly(True)
        self.edit_age.setReadOnly(True)
        self.edit_pw.setReadOnly(True)
        self.edit_detail.setReadOnly(True)
        self.check_mf.setCheckable(True)
        self.check_mf.setChecked(False)
        self.check_mf.show()
        self.lb_state.setText("저장하였습니다.")
        self.time_lag()

    def profile_cancel(self):
        self.btn_save.hide()
        self.btn_cancel.hide()
        self.edit_name.setReadOnly(True)
        self.edit_age.setReadOnly(True)
        self.edit_pw.setReadOnly(True)
        self.edit_detail.setReadOnly(True)
        self.check_mf.setCheckable(True)
        self.check_mf.setChecked(False)
        self.check_mf.show()

        self.edit_name.setText(pri_info[0]['name'])
        self.edit_pw.setText(pri_info[0]['password'])
        self.edit_age.setText(str(pri_info[0]['age']))
        self.edit_detail.setText(pri_info[0]['prefer'])

        self.lb_state.setText("취소하였습니다.")
        self.time_lag()

    def time_lag(self):
        if self.count == 1:
            self.count = 0
            self.lb_state.setText("")
        else:
            self.count += 1
            threading.Timer(0.7, self.time_lag).start()

    def logout(self):
        self.win = scr_login()
        self.win.show()
        self.close()

    def ab_exit(self):
        self.close()


# background 화면
class back_main(QMainWindow, UI_background.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("background")

        self.win = 1
        self.login_win.clicked.connect(self.print_login)
        self.main_win.clicked.connect(self.print_main)

    def print_login(self):
        self.win = scr_login()
        self.win.show()
        self.close()

    def print_main(self):
        self.win = scr_main()
        self.win.show()
        self.close()


class cr_main(QWidget, UI_create_screen.Ui_create_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("회원가입")

        self.setFixedWidth(300)
        self.setFixedHeight(450)

        self.widget_pw.hide()
        self.widget_age.hide()
        self.widget_name.hide()
        self.create_pw.hide()
        self.create_age.hide()
        self.create_name.hide()
        self.description.hide()
        self.create_save.hide()

        self.create_check.clicked.connect(self.checking)
        self.create_save.clicked.connect(self.upload_data)

    def checking(self):
        sql = (f"select ifnull(max(access_id),'#a1a1') as access_id from information where access_id = "
               f"'{self.create_id.text()}'")
        database.cursor.execute(sql)
        check_info = database.cursor.fetchall()
        # print(f"{self.create_id.text()} : {check_info[0]["access_id"]}")
        # print(check_info)

        if check_info[0]["access_id"] == "#a1a1":
            self.create_id.setReadOnly(True)
            self.create_check.hide()

            self.widget_pw.show()
            self.widget_age.show()
            self.widget_name.show()
            self.create_pw.show()
            self.create_age.show()
            self.create_name.show()
            self.description.show()
            self.create_save.show()
        else:
            msgbox("경고", "중복된 아이디입니다.\n다른 아이디로 시도하세요")

    def upload_data(self):
        sql = (f"insert into information(access_id, password, name, age) values ('{self.create_id.text()}',"
               f"'{self.create_pw.text()}', '{self.create_name.text()}', '{int(self.create_age.text())}')")
        database.cursor.execute(sql)

        msgbox("완료", "정상적으로 저장되었습니다")
        self.close()

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C108156122.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import yF_Kbar

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(931, 495)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(30, 20, 441, 411))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(500, 30, 401, 391))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(390, 450, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 450, 91, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(140, 450, 113, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "K線圖畫面"))
        self.pushButton.setText(_translate("Dialog", "確認"))
        self.label_2.setText(_translate("Dialog", "請輸入資料筆數"))

        # 按下按鈕後，觸發 onclick 函數
        self.pushButton.clicked.connect(self.onclick)
        
    def onclick(self):
        amount = self.lineEdit.text() # 讀取 lineEdit 中的文字
        # 根據lineEdit 中的文字，呼叫 yF_Kbar 製作 K 線圖
        df = yF_Kbar.get_data(amount) 
        #print(df)
        self.change_data(amount, df)
    
    def change_data(self,amount, df):
        # 根據lineEdit 中的文字，呼叫 yF_Kbar 製作 K 線圖
        yF_Kbar.draw_candle_chart(df) 
        self.label.setPixmap(QtGui.QPixmap("stock_Kbar.png")) # label 置換圖片

        columns_num = df.shape[1] # DataFrame 的 欄位數
        index_num = df.shape[0] # DataFrame 的 列數
        df_columns = df.columns # DataFrame 的 欄位名稱
        df_index = df.index # DataFrame 的 索引列表
        
        self.tableWidget.setColumnCount(columns_num) # 修改 Table Wedget 的欄位數
        self.tableWidget.setRowCount(index_num) # 修改 Table Wedget 的列數
        
        _translate = QtCore.QCoreApplication.translate
        
        # 修改欄位相關資訊
        for c in range(columns_num):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(c, item) # 依據欄位列表依序建構欄位
            
            item = self.tableWidget.horizontalHeaderItem(c) # 選取該欄位
            item.setText(_translate("MainWindow", df_columns[c])) # 修改欄位標題文字
            
        for i in range(index_num):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item) # 依據索引列表依序建構欄位
            
            item = self.tableWidget.verticalHeaderItem(i) # 選取該索引
            item.setText(_translate("MainWindow", str(df_index[i]) )) # 修改索引標題文字
            
        for c in range(columns_num): # 走訪欄位
            for i in range(index_num): # 走訪索引
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(i, c, item) # 建構儲存格

                item = self.tableWidget.item(i, c) # 選取儲存格
                item.setText(_translate("MainWindow", str(df.iloc[i, c]))) # 修改儲存格文字


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


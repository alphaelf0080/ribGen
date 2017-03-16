# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha/Documents/GitHub/ribGen/publishTool/createbranchtest_01.ui'
#
# Created: Fri Mar 17 00:34:42 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 648)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_createNewBranch = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_createNewBranch.setGeometry(QtCore.QRect(260, 120, 221, 41))
        self.pushButton_createNewBranch.setObjectName("pushButton_createNewBranch")
        self.lineEdit_branchName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_branchName.setGeometry(QtCore.QRect(260, 50, 221, 41))
        self.lineEdit_branchName.setObjectName("lineEdit_branchName")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 10, 161, 21))
        self.label.setObjectName("label")
        self.treeWidget_branches = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget_branches.setGeometry(QtCore.QRect(10, 10, 221, 391))
        self.treeWidget_branches.setObjectName("treeWidget_branches")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_branches)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_branches)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_branches)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_branches)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_branches)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.pushButton_createNewBranch.setText(QtWidgets.QApplication.translate("MainWindow", "new Branch", None, -1))
        self.lineEdit_branchName.setText(QtWidgets.QApplication.translate("MainWindow", "master", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Branch Name", None, -1))
        self.treeWidget_branches.headerItem().setText(0, QtWidgets.QApplication.translate("MainWindow", "branch Info", None, -1))
        __sortingEnabled = self.treeWidget_branches.isSortingEnabled()
        self.treeWidget_branches.setSortingEnabled(False)
        self.treeWidget_branches.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "master", None, -1))
        self.treeWidget_branches.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "branch_01", None, -1))
        self.treeWidget_branches.topLevelItem(1).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "branch_01_ext01", None, -1))
        self.treeWidget_branches.topLevelItem(1).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "branch_01_ext02", None, -1))
        self.treeWidget_branches.topLevelItem(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "branch_02", None, -1))
        self.treeWidget_branches.topLevelItem(3).setText(0, QtWidgets.QApplication.translate("MainWindow", "extra", None, -1))
        self.treeWidget_branches.topLevelItem(3).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "extra_test_01", None, -1))
        self.treeWidget_branches.topLevelItem(3).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "extra_test_02", None, -1))
        self.treeWidget_branches.topLevelItem(3).child(1).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "extra_test_02_v1", None, -1))
        self.treeWidget_branches.topLevelItem(3).child(1).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "extra_test_02_v2", None, -1))
        self.treeWidget_branches.topLevelItem(4).setText(0, QtWidgets.QApplication.translate("MainWindow", "temp", None, -1))
        self.treeWidget_branches.topLevelItem(4).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "temp_AO", None, -1))
        self.treeWidget_branches.topLevelItem(4).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "temp_lightPass", None, -1))
        self.treeWidget_branches.topLevelItem(4).child(1).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "temp_Key", None, -1))
        self.treeWidget_branches.topLevelItem(4).child(1).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "temp_spec", None, -1))
        self.treeWidget_branches.setSortingEnabled(__sortingEnabled)

class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #self.QTITEM.ACTION.connect(self.MODDEF)
        self.setupUi(self)
    #def self.MODDEF(self):
    
    
        self.pushButton_createNewBranch.clicked.connect(self.createBranchDict)
        
        
    def getBranchInfoDict(self):
        
        self.branchInfoDict = {'master':{},
                              'branch_01':{},
                              'branch_02_alpha':{},
                              'test_01':{},
                              'extea_01':{},
                              'temp':{}
                              }
            
    def getBranchTopFromTreeList(self):
        self.getBranchInfoDict()
        
        print "getBranchTopFromTreeList"
        
        
        
        self.treeWidget_branches.clear()   #get assetDict 
        
        self.currentLevelItems = self.branchInfoDict.keys()
        self.createCurrentLevelItems(self,depth)
        #print topLevelItem
       # print "create topLevel Items"
       # self.itemCount = len(self.itemList)
       # print self.itemCount
        #print self.itemList
        
    def createCurrentLevelItems(self,currentLevelItems):
        
        self.itemCount = len(self.currentLevelItems)
        
        num_item_0 =1
        while num_item_0 < (self.itemCount +1):
            item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_assetTree)
            num_item_0 = num_item_0 +1

        for i in range(0,self.itemCount):
            #print i
            topLevelItem = self.treeWidget_assetTree.topLevelItem(i)
            tempName = "tempName"
            topLevelItem.setText(0,QtWidgets.QApplication.translate("MainWindow",tempName))  #topLevelItem named "tempName"
            
        print topLevelItem
           # print self.itemList[i]
           # topLevelItem.setText(self.itemList[i])  #change tempName to folder Name , in isDirList
        print self.treeWidget_assetTree.topLevelItem()[0]
       
        
        
        
    def createBranchDict(self):
        print "create New Branch"
        self.newBranch = self.lineEdit_branchName.text()
        print self.newBranch
        
        self.getBranchTopFromTreeList()



def main():
    global ui
    app = QtWidgets.QApplication.instance()
    if app == None: app = QtWidgets.QApplication(sys.argv)
    try:
        ui.close()
        ui.deleteLater()
    except: pass
    ui = mod_MainWindow()
    ui.show()
 
if __name__ == '__main__':
    main()


 
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/alpha/Documents/GitHub/ribGen/publishTool/publishToolPreVer_02_UI.ui'
#
# Created: Mon Mar 06 22:29:07 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1141, 789)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 205, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(95, 134, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 101, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(151, 125, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(158, 164, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 205, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 224, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 101, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(151, 125, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(158, 164, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 101, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 205, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 224, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 101, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(151, 125, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 101, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 101, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton_Master = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_Master.setGeometry(QtCore.QRect(210, 30, 48, 16))
        self.radioButton_Master.setObjectName("radioButton_Master")
        self.radioButton_branches = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_branches.setGeometry(QtCore.QRect(270, 30, 65, 16))
        self.radioButton_branches.setObjectName("radioButton_branches")
        self.radioButton_temp = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_temp.setGeometry(QtCore.QRect(340, 30, 69, 16))
        self.radioButton_temp.setObjectName("radioButton_temp")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 30, 141, 41))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, -1, -1, 0)
        self.formLayout.setSpacing(5)
        self.formLayout.setObjectName("formLayout")
        self.radioButton_assets = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton_assets.setObjectName("radioButton_assets")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.radioButton_assets)
        self.radioButton_shots = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton_shots.setObjectName("radioButton_shots")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.radioButton_shots)
        self.radioButton_published = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton_published.setObjectName("radioButton_published")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.radioButton_published)
        self.pushButton_assets = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_assets.setGeometry(QtCore.QRect(40, 100, 131, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        self.pushButton_assets.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton_assets.setFont(font)
        self.pushButton_assets.setAcceptDrops(False)
        self.pushButton_assets.setAutoFillBackground(False)
        self.pushButton_assets.setInputMethodHints(QtCore.Qt.ImhNone)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/number_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_assets.setIcon(icon)
        self.pushButton_assets.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_assets.setObjectName("pushButton_assets")
        self.pushButton_shots = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_shots.setGeometry(QtCore.QRect(40, 140, 131, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 76, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        self.pushButton_shots.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton_shots.setFont(font)
        self.pushButton_shots.setAcceptDrops(False)
        self.pushButton_shots.setAutoFillBackground(False)
        self.pushButton_shots.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton_shots.setIcon(icon)
        self.pushButton_shots.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_shots.setObjectName("pushButton_shots")
        self.listWidget_assetProj = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_assetProj.setGeometry(QtCore.QRect(260, 100, 181, 341))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget_assetProj.setFont(font)
        self.listWidget_assetProj.setInputMethodHints(QtCore.Qt.ImhNone)
        self.listWidget_assetProj.setLineWidth(2)
        self.listWidget_assetProj.setMidLineWidth(1)
        self.listWidget_assetProj.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget_assetProj.setObjectName("listWidget_assetProj")
        #QtWidgets.QListWidgetItem(self.listWidget_assetProj)
        #QtWidgets.QListWidgetItem(self.listWidget_assetProj)
        #QtWidgets.QListWidgetItem(self.listWidget_assetProj)
        #QtWidgets.QListWidgetItem(self.listWidget_assetProj)
        #QtWidgets.QListWidgetItem(self.listWidget_assetProj)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1141, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.radioButton_Master.setText(QtWidgets.QApplication.translate("MainWindow", "Master", None, -1))
        self.radioButton_branches.setText(QtWidgets.QApplication.translate("MainWindow", "Branches", None, -1))
        self.radioButton_temp.setText(QtWidgets.QApplication.translate("MainWindow", "temp", None, -1))
        self.radioButton_assets.setText(QtWidgets.QApplication.translate("MainWindow", "Assets", None, -1))
        self.radioButton_shots.setText(QtWidgets.QApplication.translate("MainWindow", "Shots", None, -1))
        self.radioButton_published.setText(QtWidgets.QApplication.translate("MainWindow", "Published", None, -1))
        self.pushButton_assets.setText(QtWidgets.QApplication.translate("MainWindow", "  Assets", None, -1))
        self.pushButton_shots.setText(QtWidgets.QApplication.translate("MainWindow", "  Shots", None, -1))
        __sortingEnabled = self.listWidget_assetProj.isSortingEnabled()
        self.listWidget_assetProj.setSortingEnabled(False)
       # self.listWidget_assetProj.item(0).setText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
       # self.listWidget_assetProj.item(1).setText(QtWidgets.QApplication.translate("MainWindow", "2", None, -1))
       # self.listWidget_assetProj.item(2).setText(QtWidgets.QApplication.translate("MainWindow", "3", None, -1))
        #self.listWidget_assetProj.item(3).setText(QtWidgets.QApplication.translate("MainWindow", "4", None, -1))
        #self.listWidget_assetProj.item(4).setText(QtWidgets.QApplication.translate("MainWindow", "5", None, -1))
        self.listWidget_assetProj.setSortingEnabled(__sortingEnabled)


    ##------------------------------------sign---------------------------------------------
        
        self.pushButton_assets.clicked.connect(self.modpushButton_assets)
        
        self.pushButton_shots.clicked.connect(self.modpushButton_shots)



class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #self.QTITEM.ACTION.connect(self.MODDEF)
        self.setupUi(self)
    #def self.MODDEF(self):
            
            
    def modpushButton_assets(self):
        print "aaaaaaaaaaaaaa"
       # self.num = 3
       ## self.printNum(self.num)
        self.getProjInfo()
        #self.getFileInfor()
        #self.num = self.ObjsCount

        self.dirGive = 'assets'
        self.treeList(self.dirGive)  
        print self.topLevelItem    #return keys,topLevelItems under Projects
        #print self.topLevelItem                
       # print self.topLevelItemCount 
        self.itemCount = self.topLevelItemCount
        self.itemList = self.topLevelItem
        #print self.itemCount, self.itemList
        
        self.assetItemListCreate(self.itemCount,self.itemList)  #create topLevelItem form self.TreeTopLeveItemCreate module, self.itemCount 'int',self.itemList = 'list'
        
        
        
    def modpushButton_shots(self):
        self.getProjInfo()
        
        self.dirGive = 'shots'
        self.treeList(self.dirGive)  
        
        self.itemCount = self.topLevelItemCount
        self.itemList = self.topLevelItem
        #print self.itemCount, self.itemList
        
        self.assetItemListCreate(self.itemCount,self.itemList) 
        
        

    #------------------------- create TopLevelItem Start -------------------------------------------------------------------------
    def TreeTopLeveItemCreate(self,itemCount,itemList):
        print self.itemCount
        print self.itemList
        print "create topLevel Items"
        num_item_0 =1
        while num_item_0 < self.itemCount:
            item_0 = QtWidgets.QTreeWidgetItem(self.treeWidgetDir)
            num_item_0 = num_item_0 +1

        for i in range(0,self.itemCount):
            topLevelItem = self.treeWidgetDir.topLevelItem(i)
            tempName = "tempName"
            topLevelItem.setText(QtWidgets.QApplication.translate("MainWindow",tempName))  #topLevelItem named "tempName"
            #topLevelItem.setText(self.itemList[i])  #change tempName to folder Name , in isDirList
            
            
            
    #-------------------------create Item List, projectBase ,from assets,shots, publish,global 
    def assetItemListCreate(self,itemCount,itemList):
        self.listWidget_assetProj.clear()
        
        num_item_0 =0
        while num_item_0 < self.itemCount:
            # create number of itemCount items in List
            QtWidgets.QListWidgetItem(self.listWidget_assetProj)

            num_item_0 = num_item_0 +1        
        


        for i in range(0,self.itemCount):
            print i
            #print self.itemCount
            print self.itemList[i]
            tempName = "tempName"
            #try:
            listItem = self.listWidget_assetProj.item(i)
            listItem.setText(QtWidgets.QApplication.translate("MainWindow",tempName))
            listItem.setText(self.itemList[i])
           # except:
               # pass

        
        
    def temp(self):
        print "create topLevel Items"
        for i in range(0,self.itemCount):
            print i
            print self.isDirList[i]
            topLevelItemName = self.isDirList[i]
            print topLevelItemName
            #name = topLevelItemName
            tempName = "tempName"
           # self.treeWidget.topLevelItem(i).setText(0, QtWidgets.QApplication.translate("MainWindow", name, None, -1))
            topLevelItem = self.treeWidget.topLevelItem(i)
            topLevelItem.setText(0, QtWidgets.QApplication.translate("MainWindow",tempName))  #topLevelItem named "tempName"
            topLevelItem.setText(0,topLevelItemName)  #change tempName to folder Name , in isDirList
                    
        
        
        
    def callTest(self,caller):
        print self.caller
        
    def getProjInfo(self):
        
        
       # self.path = cmds.fileDialog2(fm=2)[0]
        self.path = "C:/mayaProjs/projectPP"

        print self.path
        
    def getFileInfor(self):

        self.dirObjs = os.listdir(self.path)
        self.ObjsCount = len(self.dirObjs)
        #collect files that as the file filter
        self.isDirList = []
        self.isFileList = []
        self.fileFilter = ['.ma','.mb','.rib','.abc']
        for obj in self.dirObjs:
            pathObj = self.path + '/'+u'%s'%obj
            print pathObj
            if os.path.splitext(pathObj)[1] in self.fileFilter:                 
                self.isFileList.append(obj)
            elif os.path.splitext(pathObj)[1] == "":
                self.isDirList.append(obj)
                
        print self.path
        print self.dirObjs
        print self.ObjsCount
        print "isDirList:    ", self.isDirList
        print "isFileList:    ", self.isFileList
        
        
        

    def treeList(self,dirGive):
        #this module, will return dirTree, self.treeInfoDict,
        #self.path = "C:/mayaProjs/vdbDevelop"

        #--------------------get dirTree info from workspace Start-------------------------------------------
        self.rootList = []
        self.treeInfoDict ={}
        pathTextList = self.path.split('/')
        levelCount = len(pathTextList)   # get the depth  of root, search in self.treeInfoDict

        for root, dirs, files in os.walk(self.path):

            rootRemix = self.path+'/'.join(root.split(self.path)[-1].split('\\'))

            self.rootList.append(rootRemix)

        for item in self.rootList:
            p = self.treeInfoDict
            for x in item.split('/'):
                p = p.setdefault(x, {})
                
        #for i in range (0,len(self.path.split('/')):
                
        #print self.treeInfoDict
        #--------------------get dirTree info from workspace END-------------------------------------------
        
        #--------------------Return dir info from self.treeIndoDict ------------------------------------------
        
        i=0
        #newDict=treeInfoDict.keys()[0]
        while i < levelCount:

            #cmd =['%s'%pathTextList[i]]
            
            #newDict = treeInfoDict['%s'%pathTextList[i]]
            self.treeInfoDict = self.treeInfoDict['%s'%self.treeInfoDict.keys()[0]]

            i=i+1
            
        self.dirUnderSelectPath = self.treeInfoDict                    #return dict under project
        #print self.dirUnderSelectPath['%s'%self.dirGive]                #return dict under select dir under project
        print self.dirGive

        self.topLevelItem = self.dirUnderSelectPath[self.dirGive].keys()           #return keys,topLevelItems under Projects
        #print self.topLevelItem                
        self.topLevelItemCount = len(self.topLevelItem)                #return counts of topLevelItems
        #print self.topLevelItemCount



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


 
 
#!/usr/bin/env python
#-*- coding:utf8 -*-
import os
import sys
import Ui_backup
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import locale
import time
import datetime
import re 
import thread

class backupWindow(QtWidgets.QDialog, Ui_backup.Ui_Dialog):
    def __init__(self, parent=None):
        locale.setlocale(locale.LC_ALL, "tr_TR.UTF-8")
        super(backupWindow, self).__init__(parent)
        self.setupUi(self)
        self.path = ""
        self.list = []
        self.backupList = []

        self.kayitYeriSec.clicked.connect(self.pathSave)
        self.ara.clicked.connect(self.search)
        self.yedekle.clicked.connect(self.yedekal)
        self.listView.itemClicked.connect(self.getsize)
    
    def getsize(self):
        self.size = 0
        for i in self.listView.selectedItems():
            self.size += os.stat(self.backupfolder+"/"+i.text()).st_size
        self.size = self.size/1024/1024
        self.log.setText(str(self.size)+" MB")

    def copy(self):
        self.getsize()
        
        _copied = 0
        length=16*1024*1024
        
        self.progressBar.setMaximum(self.size)
        for i in self.listView.selectedItems():
            srcFile = self.backupfolder+"/"+i.text()
            destFile = self.lineEdit.text()+"/"+i.text()
            with open(srcFile, 'rb') as fsrc:
                with open(destFile, 'wb') as fdst:
                    while 1:
                        buf = fsrc.read(length)
                        if not buf:
                            break
                        fdst.write(buf)
                        _copied += len(buf)
                        # self.progressBar.setValue(_copied+"/"+self.size)
                        self.progressBar.setValue(_copied/1024/1024)
                        self.progressBar.setFormat(str(_copied/1024/1024)+" MB /"+str(self.size)+" MB")
    def yedekal(self):
        thread.start_new_thread(self.copy, ())
        

    def search(self):
        self.listView.clear()

        date1 = self.dateTimeEdit.dateTime().toTime_t()
        date2 = self.dateTimeEdit_2.dateTime().toTime_t()
        self.list = []
        for item in self.listLocalDir(self.backupfolder):
            avi = re.sub("cam_(.*?)_","",item.replace(".avi",""))
            if avi != "..":
                try:
                    timestamp = int(time.mktime(datetime.datetime.strptime(avi, "%d.%m.%Y-%X").timetuple()))
                    if timestamp > date1 and timestamp < date2:
                        self.list.append(item)
                        print item
                except:
                    print "error"

        self.listView.addItems(self.list)

        
    def listLocalDir(self, dir):
        array = []
        array.append("..")
        if dir == "":
            dir = "/"
        dirs = os.listdir(dir)
        dirs = sorted(dirs)
        for item in dirs:
            array.append(item)
        return array

    def setPath(self, path):
        self.backupfolder = path

    def pathSave(self):
        fileDialog = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select USB Drive Location')
        try:
            self.path = fileDialog
            self.lineEdit.setText(self.path)
        except IOError:
            print "io error"
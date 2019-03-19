import sys, os, codecs
from player import *
from PyQt5 import QtCore, QtWidgets, QtGui, QtMultimedia

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.m_playListModel = QtGui.QStandardItemModel(self)
        self.ui.playlistView.setModel(self.m_playListModel)
        self.m_playListModel.setHorizontalHeaderLabels(["Audio Track", "File Path"])
        self.ui.playlistView.hideColumn(1)
        self.ui.playlistView.verticalHeader().setVisible(False)
        self.ui.playlistView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.playlistView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ui.playlistView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.playlistView.horizontalHeader().setStretchLastSection(True)

        self.m_player = QtMultimedia.QMediaPlayer(self)
        self.m_playlist = QtMultimedia.QMediaPlaylist(self.m_player)
        self.m_player.setPlaylist(self.m_playlist)
        self.m_playlist.setPlaybackMode(QtMultimedia.QMediaPlaylist.Loop)
        self.ui.Back.clicked.connect(self.m_playlist.previous)
        self.ui.Next.clicked.connect(self.m_playlist.next)
        self.ui.Play.clicked.connect(self.m_player.play)
        self.ui.Add.clicked.connect(self.Add)
        self.ui.playlistView.doubleClicked.connect(self.SetCurrentIndex)

        self.RowCount = 0


    def Add(self):
        temp = QtWidgets.QFileDialog.getOpenFileNames(self, '', '', "*.mp3")
        for i in range(0,len(temp[0])):
            item = QtGui.QStandardItem(QtCore.QDir(temp[0][i]).dirName())
            self.m_playListModel.setItem(self.RowCount + i, 0, item)
            item = QtGui.QStandardItem(temp[0][i])
            self.m_playListModel.setItem(self.RowCount + i, 1, item)

            url = QtCore.QUrl(temp[0][i])
            self.m_playlist.addMedia(QtMultimedia.QMediaContent(url))
        self.RowCount += len(temp[0])

    def SetCurrentIndex(self):
        index = self.ui.playlistView.selectedIndexes()
        self.m_playlist.setCurrentIndex(index[0].row())

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
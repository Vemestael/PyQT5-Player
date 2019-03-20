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
        self.ui.Play.clicked.connect(self.Play)
        self.ui.Add.clicked.connect(self.Add)
        self.ui.Stop.clicked.connect(self.Stop)
        self.ui.playlistView.doubleClicked.connect(self.SetCurrentIndex)
        self.m_playlist.currentIndexChanged.connect(self.DisplaySongName)
        self.m_playlist.currentIndexChanged.connect(self.CurrentRow)

        self.RowCount = 0
        self.Play = False
        
    def Play(self):
        if(self.Play == False):
            self.m_player.play()            
            self.ui.Play.setIcon(QtGui.QIcon("Pause.png"))
            self.Play = True
        else:
            self.m_player.pause()
            self.ui.Play.setIcon(QtGui.QIcon("Play.png"))
            self.Play = False
    
    def Stop(self):
        self.m_player.stop()
        self.ui.Play.setIcon(QtGui.QIcon("Play.png"))
        self.Play = False
        
    def Add(self):
        self.RowCount = self.m_playlist.mediaCount()
        temp = QtWidgets.QFileDialog.getOpenFileNames(self, '', '', "*.mp3")
        for i in range(0,len(temp[0])):
            item = QtGui.QStandardItem(QtCore.QDir(temp[0][i]).dirName())
            self.m_playListModel.setItem(self.RowCount + i, 0, item)
            item = QtGui.QStandardItem(temp[0][i])
            self.m_playListModel.setItem(self.RowCount + i, 1, item)

            url = QtCore.QUrl(temp[0][i])
            self.m_playlist.addMedia(QtMultimedia.QMediaContent(url))

    def SetCurrentIndex(self):
        index = self.ui.playlistView.selectedIndexes()
        self.m_playlist.setCurrentIndex(index[0].row())

    def DisplaySongName(self):
        index = self.CurrentIndex()
        Name = self.GetPlaylistModelData(index)
        self.ui.currentTrack.setText(Name)
        self.setFocus()
    
    def GetPlaylistModelData(self, index):
        data = self.m_playListModel.index(index, 0)
        return self.m_playListModel.data(data)

    def CurrentIndex(self):
        return self.m_playlist.currentIndex()

    def CurrentRow(self):
        index = self.CurrentIndex()
        self.ui.playlistView.selectRow(index)

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
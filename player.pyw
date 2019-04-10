import sys, os
from player import *
import keyboard
from PyQt5 import QtCore, QtWidgets, QtGui, QtMultimedia
from ia256utilities import filesystem


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.TableView(self.ui.playlistView)
        self.TableView(self.ui.songsView)

        self.m_player = QtMultimedia.QMediaPlayer(self)
        self.m_playlist = QtMultimedia.QMediaPlaylist(self.m_player)
        self.m_player.setPlaylist(self.m_playlist)
        self.m_playlist.setPlaybackMode(QtMultimedia.QMediaPlaylist.Loop)

        self.all_songs()

        self.ui.Back.clicked.connect(self.m_playlist.previous)
        self.ui.Next.clicked.connect(self.m_playlist.next)
        self.ui.Play.clicked.connect(self.Play)
        self.ui.Add.clicked.connect(self.Add)
        self.ui.Stop.clicked.connect(self.Stop)
        self.ui.playlistView.doubleClicked.connect(self.SetCurrentIndex)
        self.m_playlist.currentIndexChanged.connect(self.DisplaySongName)
        self.m_playlist.currentIndexChanged.connect(self.CurrentRow)
        self.ui.Volume.valueChanged.connect(self.SetVolume)
        self.m_player.positionChanged.connect(self.ProgressBar)
        self.ui.Clear.clicked.connect(self.Clear)
        self.ui.actionSelect.triggered.connect(self.directory_selection)
        self.ui.actionClear.triggered.connect(self.clear_song_view)

        self.RowCount = 0
        self.play_status = False

        def Fun(key):
            if(key.scan_code == -179):
                self.Play()
            elif (key.scan_code == -177):
                self.m_playlist.previous()
            else:
                self.m_playlist.next()

        keyboard.on_press_key(-176, Fun)
        keyboard.on_press_key(-177, Fun)
        keyboard.on_press_key(-179, Fun)

    def TableView(self, table):
        table.setColumnCount(2)
        table.setRowCount(0)
        table.setHorizontalHeaderLabels(["Audio Track", "File Path"])
        table.setColumnHidden(1, True)
        table.verticalHeader().setVisible(False)
        table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        table.horizontalHeader().setStretchLastSection(True)

    def Play(self):
        if (self.play_status == False):
            self.m_player.play()
            self.ui.Play.setIcon(QtGui.QIcon("Pause.png"))
            self.play_status = True
        else:
            self.m_player.pause()
            self.ui.Play.setIcon(QtGui.QIcon("Play.png"))
            self.play_status = False

    def Stop(self):
        self.m_player.stop()
        self.ui.Play.setIcon(QtGui.QIcon("Play.png"))
        self.play_status = False

    def Add(self):
        self.RowCount = self.ui.playlistView.rowCount()
        temp = QtWidgets.QFileDialog.getOpenFileNames(self, '', '', "*.mp3")
        self.ui.playlistView.setRowCount(self.RowCount+len(temp[0]))
        for i in range(0, len(temp[0])):
            item = QtWidgets.QTableWidgetItem(QtCore.QDir(temp[0][i]).dirName())
            self.ui.playlistView.setItem(self.RowCount + i, 0, item)
            item = QtWidgets.QTableWidgetItem(temp[0][i])
            self.ui.playlistView.setItem(self.RowCount + i, 1, item)

            print(temp[0][i])
            url = QtCore.QUrl(temp[0][i])
            self.m_playlist.addMedia(QtMultimedia.QMediaContent(url))
        if(self.play_status == False):
            self.Play()

    def SetCurrentIndex(self):
        index = self.ui.playlistView.selectedIndexes()
        self.m_playlist.setCurrentIndex(index[0].row())
        if (self.play_status == False):
            self.Play()

    def DisplaySongName(self):
        index = self.CurrentIndex()
        Name = str(self.GetPlaylistModelData(index).text())
        self.ui.currentTrack.setText(Name)
        self.setFocus()

    def GetPlaylistModelData(self, index):
        return self.ui.playlistView.item(index,0)

    def CurrentIndex(self):
        return self.m_playlist.currentIndex()

    def CurrentRow(self):
        index = self.CurrentIndex()
        self.ui.playlistView.selectRow(index)

    def SetVolume(self):
        volume = self.ui.Volume.value()
        self.m_player.setVolume(volume)

    def Clear(self):
        self.m_playlist.clear()
        self.ui.playlistView.clear()
        self.PlayListView()
        self.ui.currentTrack.setText("")
        if(self.play_status == True):
            self.Play()

    def Converting(self, milliseconds):
        minute = int(milliseconds / 60000)
        seconds = int((milliseconds % 60000) / 1000)
        return str(minute) + ":" + str(seconds)

    def ProgressBar(self):
        milliseconds = self.m_player.duration() - 2000
        duration = self.Converting(milliseconds)

        lasting = milliseconds

        milliseconds = self.m_player.position()
        position = self.Converting(milliseconds)

        time = position + " / " + duration
        self.ui.progressBar.setFormat(time)

        percent = int((milliseconds * 100) / lasting)
        self.ui.progressBar.setValue(percent)

    def directory_selection(self):
        dir = QtWidgets.QFileDialog.getExistingDirectory()
        dir = {"dir": dir}
        filesystem.save_json(dir, "json/dir.json")
        self.all_songs()

    def directory_read(self):
        dir = filesystem.load_json("json/dir.json")
        if len(dir) == 0:
            return 1
        else:
            return dir.get("dir")

    def folder_traversal(self):
        temp = [[], []]
        dir = self.directory_read()
        if dir == 1:
            return 1
        else:
            self.TableView(self.ui.songsView)
            for root, dirs, files in os.walk(dir):
                for file in files:
                    if file.endswith(".mp3"):
                        temp[0].append(file)
                        temp[1].append(root + "/" + file)

            return temp

    def all_songs(self):
        temp = self.folder_traversal()
        self.ui.songsView.clear()
        if temp == 1:
            self.ui.songsView.setHorizontalHeaderLabels(["Audio Track"])
            self.ui.songsView.setRowCount(1)
            self.ui.songsView.setColumnCount(1)
            btn_select = QtWidgets.QPushButton()
            btn_select.setText("Select songs")
            self.ui.songsView.setCellWidget(0, 0, btn_select)
            btn_select.clicked.connect(self.directory_selection)
        else:
            self.TableView(self.ui.songsView)
            self.ui.songsView.setColumnCount(3)
            self.ui.songsView.setHorizontalHeaderLabels(["Audio Track", "", "File Path"])
            self.ui.songsView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self.ui.songsView.setColumnWidth(0, 193)
            self.ui.songsView.setColumnWidth(1, 5)
            self.ui.songsView.setColumnHidden(1, False)
            self.ui.songsView.setColumnHidden(2, True)
            self.ui.songsView.setRowCount(len(temp[0]))
            btn = []
            for i in range(0, len(temp[0])):
                btn.append(QtWidgets.QPushButton())
                self.button_format(btn[i])
                item = QtWidgets.QTableWidgetItem(temp[0][i])
                self.ui.songsView.setItem(i, 0, item)
                self.ui.songsView.setCellWidget(i, 1, btn[i])
                item = QtWidgets.QTableWidgetItem(temp[1][i])
                self.ui.songsView.setItem(i, 2, item)

    def clear_song_view(self):
        self.ui.songsView.clear()
        self.TableView(self.ui.songsView)

    def button_format(self, btn):
        btn.setText("+")
        btn.setMinimumWidth(0)
        btn.setMinimumWidth(5)
        btn.clicked.connect(self.add_in_playlist)

    def add_in_playlist(self):
        index = self.ui.songsView.currentRow()
        row_count = self.ui.playlistView.rowCount()
        self.ui.playlistView.setRowCount(row_count + 1)
        item = self.ui.songsView.item(index, 0).text()
        item = QtWidgets.QTableWidgetItem(item)

        self.ui.playlistView.setItem(row_count, 0, item)

        item = url = self.ui.songsView.item(index, 2).text()
        item = QtWidgets.QTableWidgetItem(item)

        self.ui.playlistView.setItem(row_count, 1, item)

        url = QtCore.QUrl(url)
        self.m_playlist.addMedia(QtMultimedia.QMediaContent(url))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()

    sys.exit(app.exec_())

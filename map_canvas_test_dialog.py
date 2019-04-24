# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MapCanvasTestDialog
                                 A QGIS plugin
 Map Canvas Test
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-04-22
        git sha              : $Format:%H$
        copyright            : (C) 2019 by Eric Brelsford
        email                : ebrelsford@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt5 import uic
from PyQt5 import QtWidgets

from qgis.core import (
    Qgis,
    QgsApplication,
    QgsCoordinateReferenceSystem,
    QgsRectangle,
    QgsVectorLayer
)
from qgis.gui import QgsMapCanvas, QgsMapToolPan

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'map_canvas_test_dialog_base.ui'))


class MapCanvasTestDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(MapCanvasTestDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        layerPath = QgsApplication.instance().pkgDataPath() + '/resources/data/world_map.shp'
        self.mapLayers = [QgsVectorLayer(layerPath)]

    def show(self):
        self.mAreaCanvas.setLayers(self.mapLayers)
        self.mAreaCanvas.zoomToFullExtent()
        super().show()

# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ExtractPolygon
                                 A QGIS plugin
 extract polgon based on color from geotiff
                             -------------------
        begin                : 2018-02-21
        copyright            : (C) 2018 by Joost Deen
        email                : jdeen@vrnhn.nl
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ExtractPolygon class from file ExtractPolygon.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .extract_polygon import ExtractPolygon
    return ExtractPolygon(iface)

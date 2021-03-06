#!/usr/bin/python3
#­*­coding: utf­8 -­*­



#JolieBulle 2.8
#Copyright (C) 2010-2013 Pierre Tavares

#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 3
#of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.


import PyQt4
import sys
import logging
from PyQt4 import QtGui
from PyQt4 import QtCore
from outilEvaporation_ui import *

logger = logging.getLogger(__name__)


class DialogEvaporation(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_DialogEvaporation()
        self.ui.setupUi(self)
        
        self.connect(self.ui.doubleSpinBoxPreVol, QtCore.SIGNAL("valueChanged(QString)"), self.calculEvaporation)
        self.connect(self.ui.doubleSpinBoxPreSg, QtCore.SIGNAL("valueChanged(QString)"), self.calculEvaporation)
        self.connect(self.ui.doubleSpinBoxTauxEvap, QtCore.SIGNAL("valueChanged(QString)"), self.calculEvaporation)
        self.connect(self.ui.spinBoxEbu, QtCore.SIGNAL("valueChanged(QString)"), self.calculEvaporation)
        self.connect(self.ui.doubleSpinBoxTauxRefroi, QtCore.SIGNAL("valueChanged(QString)"), self.calculEvaporation)
        
 
 
        
    def calculEvaporation (self): 
        
        self.volPre = self.ui.doubleSpinBoxPreVol.value()
        self.sgPre = self.ui.doubleSpinBoxPreSg.value()
        self.tauxEvap = self.ui.doubleSpinBoxTauxEvap.value()
        self.tempsEbu = self.ui.spinBoxEbu.value()
        self.tauxRefroi = self.ui.doubleSpinBoxTauxRefroi.value()
        self.volFinal = self.ui.doubleSpinBoxVolF.value()
        
        #volume evapore :
        self.volEvap = self.volPre * self.tauxEvap / 100
        
        #volume apres ebu :
        self.volPost = self.volPre - self.volEvap
        
        #pertes refroidissement :
        self.volRefroi = self.volPost * self.tauxRefroi /100
        
        #volume apres refroidissement :
        self.volFinal = self.volPost - self.volRefroi
        
        
        #sg finale * volume final = (sg preEbu * vol preEbu) - vol manquant
        #sg finale :
        
        self.sgFinale = ((self.sgPre * self.volPre) - (self.volEvap+self.volRefroi))/ self.volFinal
        
        self.ui.labelEvapEbu.setText("<b>%.1f</b>" %self.volEvap)
        self.ui.labelEvapRefroi.setText("<b>%.1f</b>" %self.volRefroi) 
        self.ui.doubleSpinBoxVolF.setValue(self.volFinal)
        self.ui.labelSg.setText("<b>%.3f</b>" %self.sgFinale)
        
        
        
    def calculVolPre (self) :
 

        self.volFinal = self.ui.doubleSpinBoxVolF.value()
        
        
        
        self.volPre = ((self.sgFinale * self.volFinal) + (self.volEvap * self.volRefroi)) / self.sgPre


        logger.debug (self.volPre)
        
        
        

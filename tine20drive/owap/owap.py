import info

import configparser
import os
import io
import re
import sys
import subprocess
import glob

class subinfo(info.infoclass):

    def setTargets(self):
        self.svnTargets["master"] = "git@github.com:owncloud/client-desktop-owap.git"
        self.defaultTarget  = "master"

    def setDependencies(self):
        self.buildDependencies["craft/craft-blueprints-tine20Drive"] = None
        self.buildDependencies["dev-utils/cmake"] = None
        self.buildDependencies["kde/frameworks/extra-cmake-modules"] = None

        #actually a runtime dep but for now we only wan't to deploy the binary
        self.buildDependencies["tine20/tine20Drive"] = None
        self.runtimeDependencies["libs/qt5/qtbase"] = None

from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)

    def createPackage(self):
        self.addExecutableFilter(r"bin/(?!(owap)).*")
        return super().createPackage()
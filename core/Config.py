import os
from os.path import expanduser

class Config(object):
	"""Runner configurations"""
	def __init__(self):
		defects4jRepairRoot = os.path.join(os.path.dirname(__file__),'../..' )
		self.defects4jRepairRoot = defects4jRepairRoot
		self.projectsRoot = os.path.join(defects4jRepairRoot, "tmp")
		self.defects4jRoot = os.path.join(defects4jRepairRoot, "defects4j")
		self.resultsRoot = os.path.join(defects4jRepairRoot, "results/")
		self.z3Root = os.path.join(defects4jRepairRoot, "nopol/nopol/", "lib", "z3")
		self.javaHome = "/usr/lib/jvm/java-7-openjdk-i386/bin"
		self.javaHome8 = expanduser("")#Not needed by NoPol
		self.javaArgs = "-Xmx1024m"

	def __repr__(self):
		print self.defects4jRepairRoot
		print self.projectsRoot
		print self.defects4jRoot
		print self.resultsRoot
		print self.z3Root
		print self.javaHome
		print self.javaHome8
		print self.javaArgs

	def setHeapSize(self, heapsize):
		self.javaArgs = heapsize


conf = Config()

from core.tools.Nopol import Nopol

class BrutpolC(Nopol):
	"""docstring for BrutpolC"""
	def __init__(self):
		super(BrutpolC, self).__init__("BrutpolC")

	def run(self, project, id):
		self.runNopol(project, id, mode="repair", type="condition", oracle="angelic", synthesis="brutpol")
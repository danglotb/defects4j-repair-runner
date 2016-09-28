from core.tools.Nopol import Nopol

class BrutpolPC(Nopol):
	"""docstring for BrutpolPC"""
	def __init__(self):
		super(BrutpolPC, self).__init__("BrutpolPC")

	def run(self, project, id):
		self.runNopol(project, id, mode="repair", type="precondition", oracle="angelic", synthesis="brutpol")
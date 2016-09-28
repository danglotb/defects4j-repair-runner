from core.tools.Nopol import Nopol

class NopolC(Nopol):
	"""docstring for NopolC"""
	def __init__(self):
		super(NopolC, self).__init__("NopolC")

	def run(self, project, id):
		self.runNopol(project, id, mode="repair", type="condition", oracle="angelic")
from core.tools.Nopol import Nopol

class NopolPC(Nopol):
	"""docstring for NopolPC"""
	def __init__(self):
		super(NopolPC, self).__init__("NopolPC")

	def run(self, project, id):
		self.runNopol(project, id, mode="repair", type="precondition", oracle="angelic")
"""
Feat1 :::: Disparate change
"""

import os

if __name__ == "__main__":
	print("Enlisting the NOT-so hidden directory contents ...\n")
	
	for dirname, _, filenames in os.walk(os.getcwd()):
		if "git" not in dirname:
			for filename in filenames:
				print(os.path.join(dirname, filename))

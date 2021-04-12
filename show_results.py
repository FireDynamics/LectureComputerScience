"""
Hide or reveal the solutions to the exercies. 
"""


import sys
import nbformat as nbf
from glob import glob

# Collect a list of all notebooks in the content folder

hide = False
if len(sys.argv) >1 and sys.argv[1] == 'hide':
    hide = True
path = "./book/content/Exercises/"
print("The path can further be specified. Finish with Return.")
while True:
    folder = input("Change all notebooks in " + path)
    if folder is '':
        break
    path += folder + "/"
notebooks = glob(path + "**/*.ipynb", recursive=True)

# Search through each notebook and look for the loesung tag
for ipath in notebooks:
    ntbk = nbf.read(ipath, nbf.NO_CONVERT)

    for cell in ntbk.cells:
        cell_tags = cell.get('metadata', {}).get('tags', [])
        if 'loesung' in cell_tags:
            if hide and 'remove_cell' not in cell_tags:
                cell_tags.append('remove_cell')
            elif not hide:
                if 'remove_cell' in cell_tags:
                    cell_tags.remove('remove_cell')
            print(cell_tags)
        if len(cell_tags) > 0:
            cell['metadata']['tags'] = cell_tags

    nbf.write(ntbk, ipath)

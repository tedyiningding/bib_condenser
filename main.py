import json
import bibtexparser
from bibtexparser.bwriter import BibTexWriter

# read source json file
with open('source.json') as f:
    source = json.load(f)
fields_to_keep = source['fields'][0]
conference_mappings = source['mappings'][0]['conferences']
journal_mappings = source['mappings'][0]['journals']

# read bib file
with open('original_bib.bib') as bibtex_file:
    bib_original = bibtexparser.load(bibtex_file)

# refine bib
bib_refined = bib_original
for entry in bib_refined.entries:
    entry_type = entry['ENTRYTYPE'].lower()
    # delete unnecessary fields
    keys_to_keep = fields_to_keep[entry_type]
    keys_to_keep.append('ENTRYTYPE')
    keys_to_keep.append('ID')
    keys_to_remove = set(entry.keys()).difference(set(keys_to_keep))
    for key_to_remove in keys_to_remove:
        del entry[key_to_remove]
    # use abbreviation if available
    match entry_type:
        case 'inproceedings':
            for keyword, short in zip(conference_mappings['keywords'], conference_mappings['abbreviations']):
                if keyword in entry['booktitle'].lower():
                    entry['booktitle'] = short
                    break
        case 'article':
            for keyword, short in zip(journal_mappings['keywords'], journal_mappings['abbreviations']):
                if keyword in entry['journal'].lower():
                    entry['journal'] = short
                    break

# print entries before and after
# print(bib_original.entries)
# print(bib_refined.entries)

# export to bib
writer = BibTexWriter()
writer.indent = '    '     # indent entries with 4 spaces instead of one
with open('refined_bib.bib', 'w') as bibfile:
    bibfile.write(writer.write(bib_refined))
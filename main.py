import argparse
import json
import bibtexparser
from bibtexparser.bwriter import BibTexWriter


def capitalise_string(s: str, exemption_list: list = []):
    """Capitalise each word in a string subject to exemption or all upper case

    Args:
        s (str): input string
        exemption_list (list, optional): words that are exempt from being capitalised. Defaults to [].

    Returns:
        str: output string
    
    e.g., given exemption_list=['in', 'on', 'of', 'for', 'and', 'the']
    'IEEE transactions on vehicular technology' -> 'IEEE Transactions on Vehicular Technology'
    '2012 IEEE intelligent vehicles symposium' -> '2012 IEEE Intelligent Vehicles Symposium'
    'SIAM journal on imaging sciences' -> 'SIAM Journal on Imaging Sciences'
    'the univeristy of edinburgh' -> 'The Univeristy of Edinburgh'
    """

    word_list = s.split()
    if len(word_list) > 0:
        first_word = word_list[0] if word_list[0].isupper() else word_list[0].capitalize()
        if len(word_list) == 1:
            return first_word
        else:
            rest_words = " ".join(w if w in exemption_list or w.isupper() else w.capitalize() for w in word_list[1:])
            return first_word + " " + rest_words
    else:
        return ''


def main():
    parser = argparse.ArgumentParser(description='source and target bib files')
    parser.add_argument('--source_bib', type=str, help='the source bib file', default='./original_bib.bib')
    parser.add_argument('--target_bib', type=str, help='the target bib file', default='./refined_bib.bib')
    args = parser.parse_args()

    source_bib = args.source_bib
    target_bib = args.target_bib

    # read setup json file
    with open('./setup.json') as f:
        setup = json.load(f)
    fields_to_keep = setup['fields'][0]
    conference_mappings = setup['mappings'][0]['conferences']
    journal_mappings = setup['mappings'][0]['journals']
    words_do_not_capitalise = setup['words_do_not_capitalise']

    # read bib file
    with open(source_bib) as bibtex_file:
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
        # use abbreviation if available, else capitalise words
        match entry_type:
            case 'inproceedings':
                for keyword, short in zip(conference_mappings['keywords'], conference_mappings['abbreviations']):
                    if keyword in entry['booktitle'].lower():
                        entry['booktitle'] = short
                        break
                if entry['booktitle'] != short:
                    entry['booktitle'] = capitalise_string(entry['booktitle'], words_do_not_capitalise)
            case 'article':
                for keyword, short in zip(journal_mappings['keywords'], journal_mappings['abbreviations']):
                    if keyword in entry['journal'].lower():
                        entry['journal'] = short
                        break
                if entry['journal'] != short and not 'arXiv' in entry['journal']:
                    entry['journal'] = capitalise_string(entry['journal'], words_do_not_capitalise)
            case 'book':
                entry['title'] = capitalise_string(entry['title'], words_do_not_capitalise)
                entry['publisher'] = capitalise_string(entry['publisher'], words_do_not_capitalise)
            case 'phdthesis':
                entry['title'] = capitalise_string(entry['title'], words_do_not_capitalise)
                entry['school'] = capitalise_string(entry['school'], words_do_not_capitalise)

    # export to bib
    writer = BibTexWriter()
    writer.indent = '    '     # indent entries with 4 spaces instead of one
    with open(target_bib, 'w') as bibfile:
        bibfile.write(writer.write(bib_refined))


if __name__ == "__main__":
    main()

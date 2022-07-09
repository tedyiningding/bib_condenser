# bib_condenser
## What does it do
A simple python script that condenses and neatens bib entries by discarding unnecessary fields and abbreviates conference/journal names (currently covering the area of **computer vision**, **robotics** and **machine/deep learning**). See the json file for details.

It changes bib files from
```
@article{hirschmuller2007stereo,
  title={Stereo processing by semiglobal matching and mutual information},
  author={Hirschmuller, Heiko},
  journal={IEEE Transactions on pattern analysis and machine intelligence},
  volume={30},
  number={2},
  pages={328--341},
  year={2007},
  publisher={IEEE}
}
@inproceedings{chang2018pyramid,
  title={Pyramid stereo matching network},
  author={Chang, Jia-Ren and Chen, Yong-Sheng},
  booktitle={Proceedings of the IEEE conference on computer vision and pattern recognition},
  pages={5410--5418},
  year={2018}
}
```
to
```
@article{hirschmuller2007stereo,
    author = {Hirschmuller, Heiko},
    journal = {PAMI},
    title = {Stereo processing by semiglobal matching and mutual information},
    year = {2007}
}
@inproceedings{chang2018pyramid,
    author = {Chang, Jia-Ren and Chen, Yong-Sheng},
    booktitle = {CVPR},
    title = {Pyramid stereo matching network},
    year = {2018}
}
```

The corresponding rendered Reference section in your paper will change from

> [1] Heiko Hirschmuller. Stereo processing by semiglobal matching and mutual information. *IEEE Transactions on pattern analysis and machine intelligence*, 30(2):328–341, 2007.
> 
>[2] Jia-Ren Chang and Yong-Sheng Chen. Pyramid stereo matching network. In *Proceedings of the IEEE conference on computer vision and pattern recognition*, pages 5410–5418, 2018.

to;

>[1] Heiko Hirschmuller. Stereo processing by semiglobal matching and mutual information. *PAMI*, 2007.
>
>[2] Jia-Ren Chang and Yong-Sheng Chen. Pyramid stereo matching network. In *CVPR*, 2018.


## How to use
```
python main.py --source_bib <source bib file> --target_bib <target bib file>
```
For example
```
python main.py --source_bib ./original_bib.bib --target_bib ./target_bib.bib
```


## Requirements
- Python>=3.10 that supports [structural pattern matching](https://docs.python.org/3.10/whatsnew/3.10.html#pep-634-structural-pattern-matching)
- The [BibtexParser](https://bibtexparser.readthedocs.io/en/master/index.html) package
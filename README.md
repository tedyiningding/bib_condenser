# bib_condenser
## What does it do
A simple [python script](./main.py), together with a [json file](./setup.json), that condenses and neatens bib entries by
* discarding redundant fields;
* abbreviating conference/journal names if avaialble (currently covering the area of **computer vision**, **robotics** and **machine/deep learning**)
* capitalising words in conference and journal name, book title and publisher, and PhD thesis title and school.

It changes bib files from [original_bib.bib](./original_bib.bib)
```bib
@inproceedings{chang2018pyramid,
  title={Pyramid stereo matching network},
  author={Chang, Jia-Ren and Chen, Yong-Sheng},
  booktitle={Proceedings of the IEEE conference on computer vision and pattern recognition},
  pages={5410--5418},
  year={2018}
}
@phdthesis{hannah1974computer,
  title={Computer matching of areas in stereo images},
  author={Hannah, Marsha Jo},
  year={1974},
  school={Stanford University}
}
@book{hartley2003multiple,
  title={Multiple view geometry in computer vision},
  author={Hartley, Richard and Zisserman, Andrew},
  year={2003},
  publisher={Cambridge university press}
}
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
```
to [refined_bib.bib](./refined_bib.bib):
```bib
@inproceedings{chang2018pyramid,
    author = {Chang, Jia-Ren and Chen, Yong-Sheng},
    booktitle = {CVPR},
    title = {Pyramid stereo matching network},
    year = {2018}
}
@phdthesis{hannah1974computer,
    author = {Hannah, Marsha Jo},
    school = {Stanford University},
    title = {Computer Matching of Areas in Stereo Images},
    year = {1974}
}
@book{hartley2003multiple,
    author = {Hartley, Richard and Zisserman, Andrew},
    publisher = {Cambridge University Press},
    title = {Multiple View Geometry in Computer Vision},
    year = {2003}
}
@article{hirschmuller2007stereo,
    author = {Hirschmuller, Heiko},
    journal = {PAMI},
    title = {Stereo processing by semiglobal matching and mutual information},
    year = {2007}
}

```

The corresponding rendered Reference section in your paper will change (depending on the bibliography style) from something like

> [1] Jia-Ren Chang and Yong-Sheng Chen. Pyramid stereo matching network. In *Proceedings of the IEEE conference on computer vision and pattern recognition*, pages 5410–5418, 2018.
>
> [2] Marsha Jo Hannah. *Computer matching of areas in stereo images*. PhD thesis, Stanford University, 1974.
>
> [3] Richard Hartley and Andrew Zisserman. *Multiple view geometry in computer
vision*. Cambridge university press, 2003.
>
> [4] Heiko Hirschmuller. Stereo processing by semiglobal matching and mutual information. *IEEE Transactions on pattern analysis and machine intelligence*, 30(2):328–341, 2007.

to something like:

> [1] Jia-Ren Chang and Yong-Sheng Chen. Pyramid stereo matching network. In *CVPR*, 2018.
>
> [2] Marsha Jo Hannah. *Computer Matching of Areas in Stereo Images*. PhD thesis, Stanford University, 1974.
>
> [3] Richard Hartley and Andrew Zisserman. *Multiple View Geometry in Computer Vision*. Cambridge University Press, 2003.
>
> [4] Heiko Hirschmuller. Stereo processing by semiglobal matching and mutual information. *PAMI*, 2007. 

## Requirements
- Python>=3.10 that supports [structural pattern matching](https://docs.python.org/3.10/whatsnew/3.10.html#pep-634-structural-pattern-matching)
- The [BibtexParser](https://bibtexparser.readthedocs.io/en/master/index.html) package

## How to use it
```
python main.py --source_bib <source bib file> --target_bib <target bib file>
```
For example
```
python main.py --source_bib ./original_bib.bib --target_bib ./refined_bib.bib
```
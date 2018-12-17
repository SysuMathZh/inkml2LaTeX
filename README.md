# inkML formula to LaTeX
Extract formula in LaTeX from inkml

# Guide
### inkML file should contain ```XML <annotation type="true">$ LaTeX formula $</annotation> ```
### database from CROHME, in which training data & test data with ground truth(testGT) already contain the thing above
### NOTE: data in directory CROHME_test does NOT contain any annotation, but pure coordinates

## Single File Extraction:
edit corresponding path in main.py and run it
or simply
``` python
import inkml2ltx as i2l
i2l.inkml2ltx('origin_path', 'dest_path')
```
## Batch Extrations:
edit corresponding path in batch_main.py and run it
---
CROHME website(and data download as well): https://www.isical.ac.in/~crohme/

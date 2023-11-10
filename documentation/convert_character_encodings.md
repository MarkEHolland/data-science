# Convert between character encodings

`UTF-8` is the encoding that is most common (and set as default), e.g. Bigquery data ingestion can only handle csvs encoded in either `UTF-8` or `latin1`. However, there are cases when a file ended up with a wrong encoding. 

To fix this:

## Detect file encoding
Python has a handy library to do this: [chardet](https://chardet.readthedocs.io/en/latest/index.html)

For example, this snippet will print out the name of each csv file and a result dict like `{'encoding': 'EUC-JP', 'confidence': 0.99}`

```python
import glob
from chardet.universaldetector import UniversalDetector

detector = UniversalDetector()
for filename in glob.glob('*.csv'):
    print(filename.ljust(60), end='')
    detector.reset()
    for line in open(filename, 'rb'):
        detector.feed(line)
        if detector.done: break
    detector.close()
    print(detector.result)

```

## Convert to utf-8
This can be done using `iconv` in bash

```bash
!iconv -c -f utf-16 -t utf-8 'somefilename.csv'  > 'somefilename_cleaned.csv'
```

- `-f` is the source file's encoding
- `-t` is the target file's encoding

*Note that the input filename cannot be the same as the output filename, otherwise the outputfile will be empty


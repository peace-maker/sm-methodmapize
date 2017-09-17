# Update SourcePawn code to use the new methodmap API
RegEx replace all calls in a SourcePawn file with their methodmap equivalent.

Only added for the standard library shipped with SourceMod yet.

## Usage
```
python methodmapize.py file.sp file2.sp file3.sp ...
```

The script will do some regular expression replacements and save the new file in the same directory with `.m` appended to the file name.
The source file itself isn't changed.
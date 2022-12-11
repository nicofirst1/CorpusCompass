# TranscriptionTagger
Use to convert trasnscription into csv.

## COLAB
If you know nothing about programming, I highly advise you to use the [colab notebook](https://colab.research.google.com/github/nicofirst1/TranscriptionTagger/blob/main/main.ipynb).


## Usage
To run the program simply write
```
python3 main.py
```
in the terminal. 
The program will ask you for the path to the transcription file. When the program finished it will notify you with a message. 

The csv file will be saved in the same directory as the transcription file with the format 
`[file_name]_output.csv`.


## Adding variables
The files `dependent_variables.json` and `independent_variables.json` contain the variables that are used to tag the transcription.
To add a variable simply add a new entry to the json file. The key is the name of the category and the value is either:
- a single variable, in this case use the format `"variable_name"`
- a list of variables, in this case use the format `["variable_name_1", "variable_name_2", ...]`

Remember that the last line of a json file must not have a comma at the end.

## Changing tagging format
Tags are in the format `[$TAG1.TAG2.TAG-n.word]` where `$` is the start tag, `.` is the separator and `]` is the end tag.
To change the format (or regex) simply replace line 7/8 in the [main.py](./main.py) (variables `square_regex` and `feat_regex`) file with the new format.

To come up with a new tag REGEX you can use [regex101](https://regex101.com/). To check out how it works copy paste the 
content of `square_regex` into the regular expression bar `(\[\$[\S ]*?\])` and a sample paragraph in the test string, e.g.:
```
S    akiid, akiid, bi l [$G-OTH.fooxinende], aa, yaʕni il jumʕa la bass ʕidna sabit uu aħħad iħna [$DEM-HAAY.haay] [$G-OTH.daayrakt] leen il alwaad ʕidna       aa, iða j jaww [$IA.kulliʃ] [$IA.zeen] insawwi maʃaawi, w iða j jaww mu [$IA.zeen], insawwi yaʕni l aklaat illi tijmaʕ il ʕaaʔila, tiðakkiriin iħna l ʕiraaqiyiin         id dooLMa, w is [$CK.simaC], (laughing), w il lamma l ħilwa w il aħfaad, fa insawwi [$IA.CK.hiiCi]          bass il yoom la yaʕni innu aani w il ħajji [$GQ.gaaʕdiin], akθar il marraat nugʕud iS SuBiħ [$IA.nitrayyag], baʕdeen il, il gahwa uu baʕdeen nuqʕud insoolif, inʃuuf [$IA.ʃinu] ʕidna maʃaariiʕ, niTLaʕ maθalan irruuħ nimʃi [$IA.fadd] niSS saaʕa saaʕa   
```
# TranscriptionTagger
Use to convert trasnscription into csv.

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
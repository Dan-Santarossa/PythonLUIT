import json

# This uses a json string as an input 
json_string = """
{
    "Input":[
        {
        "Text":"I am learning to code in AWS",
        "SourceLanguageCode":"en",
        "TargetLanguageCode":"it"
        }
    ]
}
"""

json_input = json.loads(json_string) # We use loads as we are loading from a string.

# Defines two variables to store the language code from the input.
SourceLanguageCode = json_input['Input'][0]['SourceLanguageCode']
TargetLanguageCode = json_input['Input'][0]['TargetLanguageCode']

# The if statement checks to see if the language code is the same as the source code
if SourceLanguageCode == TargetLanguageCode:
    print("The SourceLanguageCode is the same as the TargetLanguageCode - stopping")
else:
    print("The Source Language and Target Language codes are different - proceeding")

# Operator	Meaning
# ==	is equivalent to
# !=	is not equivalent to
# >	is greater than
# <	is less than
# >=	is equal to or greater than
# <=	is equal to or less than

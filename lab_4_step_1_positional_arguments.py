import boto3

#def translate_text():
#    client = boto3.client('translate')
#    response = client.translate_text(
#        Text='I am learning to code in AWS', 
#        SourceLanguageCode='en', 
#        TargetLanguageCode='it' 
#    )
#    print(response) 

#def main():
#    translate_text()

#if __name__=="__main__":
#    main()

#^^^kept above code to have comaprison with below

def translate_text(text, source_language_code, target_language_code): # we define the positional arguments in the ()
    client = boto3.client('translate')
    response = client.translate_text(
        Text=text, # we remove the hard coded value
        SourceLanguageCode=source_language_code, # we used the positional argument instead
        TargetLanguageCode=target_language_code
    )
    print(response) 

def main():
    translate_text('I am learning to code in AWS','en','fr') # we provide the value for the arguments when we call the function in the correct positional order.

if __name__=="__main__":
    main()

# What did we do above?
# We removed the hard coded parameter values and replaced them with the argument names:

# text
# source_language_code
# target_language_code.
# We defined the argument names as inputs in the order of the parameters in between the brackets ().

# When we called the function we used the actual values in the correct position.

# What did python do?
# Python substituted the actual values we provided when we called the function for the positional arguments and passed them to the parameters.
# How did this improve our code?
# By removing the hard coded values we can now call the function multiple times using different values. This makes our code flexible and reusable.
# Try running the program again but this time amend the following line:

# translate_text('I am learning to code in AWS','en','fr')

# Change the values for:

# The text
# The source language code
# The target language code
# What happens if you mix up the order?
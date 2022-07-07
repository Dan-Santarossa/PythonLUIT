import boto3

# def translate_text(text, source_language_code, target_language_code): 
#     client = boto3.client('translate')
#     response = client.translate_text(
#         Text=text, 
#         SourceLanguageCode=source_language_code, 
#         TargetLanguageCode=target_language_code
#     )
#     print(response) 

# def main():
#     translate_text('I am learning to code in AWS','en','it')

# if __name__=="__main__":
#     main()

#^^^kept above code to have comaprison with below

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

def main():
    translate_text(Text='I am learning to code in AWS',SourceLanguageCode='en',TargetLanguageCode='it')

if __name__=="__main__":
    main()

# What did we do?
# We replaced the positional arguments with keyword arguments. This is done using the **kwargs.
# We removed all the parameters such as Text=text which shortens our code and replaced it with response = client.translate_text(**kwargs).
# We defined the keyword arguments when we called the function using the syntax Text='I am learning to code in AWS'.
# What did python do?
# Python used the keyword arguments defined when we called the function and passed them to the function as variables.

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

### Change below this line only ###

kwargs={
    "Text":"I am learning to code in AWS",
    "SourceLanguageCode":"en",
    "TargetLanguageCode":"it"
    }

def main():
    translate_text(**kwargs)

if __name__=="__main__":
    main()

# What did we do?
# We defined a variable called kwargs containing a dictionary of key\:value pairs.
# We replaced the keyword arguments when we called the function with **kwargs. The ** tells python that it is an arbitrary number of arguments, kwargs is the function name we defined.
# We put each key\:value pair on a separate line to make it easy to read

# What did python do?
# Python used the key\:value pairs defined in the dictionary in place of the keyword arguments
# Being able to pass a dictionary of key\:value pairs rather than keyword pairs is useful because in AWS inputs to programs often use dictionaries.
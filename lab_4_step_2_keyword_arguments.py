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
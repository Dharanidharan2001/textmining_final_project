import boto3

translate = boto3.client('translate')
result = translate.translate_text(Text="MY NAME DHARANIDHARAN  A STUDENT FROM KALASALINGAM UNIVERSITY",
                                  SourceLanguageCode="en",
                                  TargetLanguageCode="ta")
print(f'TranslatedText:     {result["TranslatedText"]}')
print(f'SourceLanguageCode: {result["SourceLanguageCode"]}')
print(f'TargetLanguageCode: {result["TargetLanguageCode"]}')
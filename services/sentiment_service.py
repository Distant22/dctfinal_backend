from google.cloud import language_v2
from models.content_model import Content

async def sentiment_analyze_service(content: Content) -> None:
    
    client = language_v2.LanguageServiceClient()

    document_type_in_plain_text = language_v2.Document.Type.PLAIN_TEXT

    language_code = "zh-TW"
    document = {
        "content": content.text,
        "type_": document_type_in_plain_text,
        "language_code": language_code,
    }

    encoding_type = language_v2.EncodingType.UTF8

    response = client.analyze_sentiment(
        request={"document": document, "encoding_type": encoding_type}
    )
    # Get overall sentiment of the input document
    print(f"Document sentiment score: {response.document_sentiment.score}")
    print(f"Document sentiment magnitude: {response.document_sentiment.magnitude}")
    # Get sentiment for all sentences in the document
    for sentence in response.sentences:
        print(f"Sentence text: {sentence.text.content}")
        print(f"Sentence sentiment score: {sentence.sentiment.score}")
        print(f"Sentence sentiment magnitude: {sentence.sentiment.magnitude}")

    print(f"Language of the text: {response.language_code}")

    print("\nResponse\n",response,"Sentiment object",response.sentences)

    return response.sentences[0].sentiment.score


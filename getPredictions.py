from .classifier import SentimentClassifier, MODEL_NAME
import torch
from transformers import BertTokenizer

def get_sentiment(review_text, model_path='model/final_model.bin', class_names=['negative', 'neutral', 'positive']):
    
    model = SentimentClassifier(len(class_names))
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    model = model.to(device)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()
    
    tokenizer = BertTokenizer.from_pretrained(MODEL_NAME)
    MAX_LEN = 160
    
    encoded_review = tokenizer.encode_plus(
        review_text,
        max_length=MAX_LEN,
        add_special_tokens=True,
        return_token_type_ids=False,
        padding='max_length',
        return_attention_mask=True,
        return_tensors='pt',
    )
    
    input_ids = encoded_review['input_ids'].to(device)
    attention_mask = encoded_review['attention_mask'].to(device)
    
    with torch.no_grad():
        output = model(input_ids, attention_mask)
        _, prediction = torch.max(output, dim=1)
        
        # Calculate the percentage of each sentiment class
        softmax_output = torch.nn.functional.softmax(output, dim=1)
        percentages = (softmax_output * 100).cpu().numpy()
    
    prediction = prediction.cpu().numpy()

    return class_names[prediction[0]], {class_names[i]: percentages[0][i] for i in range(len(class_names))}


get_sentiment('I am a good boy')
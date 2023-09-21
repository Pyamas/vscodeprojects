import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from transformers import AutoTokenizer
from transformers import AutoModel
import pandas as pd 
### define a custom dataset class
###encodingtrying wtf
encodings_to_try = ['utf-8','latin-1','ISO-8859-1']
for encoding in encodings_to_try:
    try:
        df = pd.read_csv('spam.csv', encoding=encoding)

        break
    except UnicodeDecodeError:
        print(f"Failed to read with encoding {encoding}")
print(df.head())
class EmailDataset(Dataset):
    def __init__(self, text, labels, tokenizer, max_length):
        self.text = text
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.text)

    def __getitem__(self, idx):
        text = str(self.text[idx])
        label = self.labels[idx]

        encoding = self.tokenizer(text, truncation=True, padding ='max_length', max_length=self.max_length, return_tensors='pt')
        # Map labels to numeric values
        label_mapping = {'ham': 0, 'spam': 1, 'other': 2}
        label = label_mapping[label]

        # Create a tensor
        
        return {
            'input_ids': encoding['input_ids'].squeeze(),
            'attention_mask': encoding['attention_mask'].squeeze(),
            'labels': torch.tensor(label, dtype=torch.long)



        }
    

    ### split data into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(df['v1'], df['v2'])

### Create a tokenizer data (for text to numerical convertion)
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

### define max length sequence
max_length = 128

train_dataset = EmailDataset(X_train, y_train, tokenizer, max_length)
test_dataset = EmailDataset(X_test, y_test, tokenizer, max_length)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

### import necessary libraries for the model
class EmailClassifier(nn.Module):
    def __init__(self, pretrained_model_name, num_classes):
        super(EmailClassifier, self).__init__()
        self.bert = AutoModel.from_pretrained(pretrained_model_name)
        self.fc = nn.Linear(self.bert.config.hidden_size, num_classes)
    
    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids, attention_mask = attention_mask)
        logits = self.fc(outputs.pooler_output)
        return logits
    
### Create model 
num_classes = 2 ### spam or not spam 
model = EmailClassifier("bert-base-uncased",num_classes)

### Define loss and optimizer

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-5)


### training loops

num_epochs = 5 ### give as much as you want 

for epoch in range(num_epochs):
    model.train()
    total_loss = 0.0
    
    for batch in train_loader:
        input_ids = batch['input_ids']
        attention_mask = batch['attention_mask']
        labels = batch['label']

        optimizer.zero_grad()

        outputs = model(input_ids, attention_mask=attention_mask)
        loss = criterion(outputs, labels)

        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    average_loss = total_loss / len(train_loader)
    print(f"epoch {epoch+1}/{num_epochs}, Loss: {average_loss:.4f}")


    # Model evaluation 
    model.eval()
    correct = 0
    total = 0 
    with torch.no_grad():
        for batch in test_loader:
            input_ids = batch['input_ids']
            attention_mask = batch['attention_mask']
            labels = batch['label']

            outputs = model(input_ids, attention_mask = attention_mask)
            _, predicted = torch.max(outputs, 1)

            total += labels.size(0)
            correct += (predicted ==labels).sum().item()
accuracy = 100 * correct / total
print(f"Accuracy on the test set: {accuracy:.2f}%") 
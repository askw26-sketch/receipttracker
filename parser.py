import re

class ReceiptParser:
    def __init__(self, text):
        self.text = text

    def parse_receipt(self):
        # Example of extracting useful information (like price, date, etc.) from the receipt text
        items = re.findall(r'\d+\.\d{2}', self.text)  # Matches prices like 12.34
        return items

    def judge_genre(self):
        # Placeholder logic for genre judgment - can be expanded as needed
        if 'food' in self.text.lower():
            return 'Food'
        elif 'clothes' in self.text.lower():
            return 'Clothing'
        else:
            return 'Miscellaneous'

# Example usage
if __name__ == '__main__':
    sample_receipt = '''\n    Item: Coffee  \n    Price: 2.50  \n    '''
    parser = ReceiptParser(sample_receipt)
    print(f'Parsed items: {parser.parse_receipt()}')
    print(f'Genre: {parser.judge_genre()}')
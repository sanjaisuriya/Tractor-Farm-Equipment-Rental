from html.parser import HTMLParser

with open('rates-pricing.html', 'r', encoding='utf-8') as f:
    page_content = f.read()

class TagValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []
        self.void_tags = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr', '!doctype'}

    def handle_starttag(self, tag, attrs):
        if tag.lower() not in self.void_tags:
            self.stack.append(tag.lower())

    def handle_endtag(self, tag):
        t = tag.lower()
        if t in self.void_tags:
            return
        if not self.stack:
            self.errors.append(f"Unexpected closing tag </{t}> with empty stack")
        elif self.stack[-1] == t:
            self.stack.pop()
        else:
            if t in self.stack:
                while self.stack and self.stack[-1] != t:
                    unclosed = self.stack.pop()
                    if unclosed not in ['p', 'li', 'td', 'th', 'tr']:
                        self.errors.append(f"Unclosed tag <{unclosed}> before </{t}>")
                if self.stack and self.stack[-1] == t:
                    self.stack.pop()
            else:
                self.errors.append(f"Unexpected closing tag </{t}>, expected </{self.stack[-1]}>")

validator = TagValidator()
validator.feed(page_content)
print(f"Validation completed. Non-void errors: {len(validator.errors)}")
for err in validator.errors[:10]:
    print(" -", err)
print("Remaining open tags in stack:", validator.stack)

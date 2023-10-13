class BrowserHistory:
    def __init__(self, homepage) -> None:
        self.history = [homepage] #maintains the list of pages visited
        self.curr = 0 # represents the curr page index from the pages visited
        self.length = 1 # represents actual length of the history array[with valid pages not the soft deleted ones], default =1 cz of homepage

    def visit(self, url):
        if len(self.history) < self.curr + 2:
            self.history.append(url) # to take care of cases when we are visiting pages and would like to append to array
        else:
            self.history[self.curr+1] = url #to overwrite the array when you have come back in history and essentially means soft deleting fporward history
        self.curr += 1
        self.length  = self.curr + 1 # does not count the soft deleted forward urls needed so that we know while going forward how much we have to go
                                  # because it is 1 + self.curr
    # To simplify above index method, we could simply delete the non necessary items
    # def visit(self, url):
    #     """
    #     :type url: str
    #     :rtype: None
    #     """
        
    #     del self.history[self.curr+1:]
    #     self.history.append(url)
    #     self.curr += 1

    def back(self, steps):
        self.curr = max(self.curr-steps, 0)
        return self.history[self.curr]

    def forward(self, steps):
        self.curr = min(self.curr+steps, self.length - 1)
        return self.history[self.curr]

b = BrowserHistory("url1")
b.visit("url2")
b.visit("url3")
b.visit("url4")
print(b.history)
print("current",b.curr)
b.back(3)
print("current after going back", b.curr)
b.visit("url5")
print("curr after visit in back", b.curr)
print(b.history)
b.forward(1)
print(b.curr)
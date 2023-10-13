# You have a browser of one tab where you start on the homepage and you can visit another url, 
# get back in the history number of steps or move forward in the history number of steps.

# Implement the BrowserHistory class:

# 1. BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
# 2. void visit(string url) Visits url from the current page. It clears up all the forward history.
# 3. string back(int steps) Move steps back in history. If you can only return x steps in the history and 
#    steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
# 4. string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and 
#    steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.

# implementation using linked list
class ListNode:
    def __init__(self, url, next=None, prev=None) -> None:
        self.url = url
        self.next = next
        self.prev = prev

class BrowserHistory:
    def __init__(self, homepage) -> None:
        self.cur  = ListNode(homepage)
    
    def visit(self, url):
        self.cur.next = ListNode(url, prev=self.cur)
        self.cur = self.cur.next
    
    def back(self, steps):
        while self.cur.prev and steps >0:
            self.cur = self.cur.prev
            steps -=1
        return self.cur.url

    def forward(self, steps):
        while self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.url

b = BrowserHistory("google.com")
print(b.cur.url)
b.visit("abc1.com")
b.visit("abc2.com")
print(b.cur.url, b.cur.prev.url, b.cur.prev.prev.url)
back = b.back(4)
print(back.url)
forw = b.forward(1)
print(forw.url)


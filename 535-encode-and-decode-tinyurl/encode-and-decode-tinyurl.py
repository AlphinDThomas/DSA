class Codec:
    def __init__(self):
        self.encodemap = {}
        self.decodemap = {}
        self.base = "https://tinyurl.com/"
    def encode(self, longUrl: str) -> str:
        if longUrl not in self.encodemap:
            shortUrl = self.base + str(len(self.encodemap)+1)
            self.encodemap[longUrl] = shortUrl
            self.decodemap[shortUrl] = longUrl
        return self.encodemap[longUrl]
        

    def decode(self, shortUrl: str) -> str:
        return self.decodemap[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
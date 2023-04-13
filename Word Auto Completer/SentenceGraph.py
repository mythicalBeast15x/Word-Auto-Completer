class Vertex:
    def __init__(self, key):
        self.key = key
        self.connections = {}

    def add_neighbor(self, vertex, weight = 0):
        self.connections[vertex] = weight

    def get_connections(self):
        return list(self.connections.keys())

    def get_key(self):
        return self.key

    def get_weight(self, key):
        return self.connections[key]
class Graph:
    def __init__(self):
        self.vertices = {}
        self.total_vertices = 0

    def add_vertex(self, key):
        self.vertices[key] = Vertex(key)
        self.total_vertices += 1

    def get_vertex(self,key):
        if self._contains(key):
            return self.vertices[key]

    def _contains(self, key):
        if key in self.vertices.keys():
            return True
        else:
            return False
    def add_edge(self,key1, key2, weight = 0):
        if not self._contains(key1):
            self.add_vertex(key1)
        '''
        if not self._contains(key2):
            self.add_vertex(key2)
        '''
        if not key2 in self.vertices[key1].get_connections():
            self.vertices[key1].add_neighbor(self.vertices[key2], weight)
            #self.vertices[key2].add_neighbor(self.vertices[key1], weight)
    def remove_edge(self, key1, key2):
        if self._contains(key1) and self._contains(key2):
            if key2 in [a.get_key() for a in self.vertices[key1].get_connections()]:
                del self.vertices[key1].connections[self.get_vertex(key2)]
                #del self.vertices[key2].connections[self.get_vertex(key1)]

    def remove_vertex(self, key1):
        if self._contains(key1):
            delete = [a.get_key() for a in self.get_vertex(key1).get_connections()]
            for vertex_key in delete:
                self.remove_edge(vertex_key, key1)

            del self.vertices[key1]
    def get_vertices(self):
        return self.vertices.keys()
    #this makes sure that graph has directions i -> am != am -> i
    def update_edge(self, key1, key2):
        if self.vertices[key2] in self.vertices[key1].get_connections():
            self.vertices[key1].connections[self.vertices[key2]] +=1
        else:
            self.add_edge(key1, key2, 1)

    def add_sentence(self, sentence):
        #print(sentence)
        for word in sentence.split(' '):
            #print(word)
            #space for word verification
            if word not in self.get_vertices():
                self.add_vertex(word)
        words = [word for word in sentence.split()]
        for x in range(len(words)-1):
            self.update_edge(words[x], words[x+1])

    def find_next_word(self, word):
        if word in self.get_vertices():
            vertex = self.vertices[word]
            return max(vertex.connections, key = vertex.connections.get).key

    def find_next_word_in_sentence(self, sentence):
        words = sentence.split(' ')
        print( words)
        last_word = words[-1]
        if last_word in self.get_vertices():
            if last_word not in words[:-1]:
                return self.find_next_word(last_word)
            else:
                vertex = self.vertices[last_word]
                return [word for word in sorted(vertex.connections, key = vertex.connections.get) if word not in words][0].key

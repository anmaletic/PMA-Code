



class Node():
    def __init__(self, value) -> None:
        self.data = value
        self.prev = None
        self.next = None


class DoubleLinkedList():
    def __init__(self) -> None:
        self.firstNode = None
        self.lastNode = None

    def count(self):
        if self.firstNode == None:
            return 0
        else:            
            counter = 1
            currentNode = self.firstNode
            while currentNode.next != None:
                counter += 1
                currentNode = currentNode.next
            return counter

    def append(self, value):
        newNode = Node(value)
        if self.firstNode == None:
            self.firstNode = newNode
            self.lastNode = newNode
        else:
            # currentNode = self.firstNode
            # while currentNode.next != None:
            #     currentNode = currentNode.next
            # self.lastNode = currentNode.next = newNode
            # newNode.prev = currentNode

            self.lastNode.next = newNode
            newNode.prev = self.lastNode
            self.lastNode = newNode

    def insert(self, value, index):
        newNode = Node(value)

        count = self.count()

        if(index < count // 2):
            currentNode = self.firstNode
            _index = 0
            while _index < index-1:
                currentNode = currentNode.next
                _index += 1
            newNode.next = currentNode.next
            currentNode.next = newNode
            newNode.prev = currentNode
        else:
            currentNode = self.lastNode
            _index = count-1
            while _index > index-1:
                currentNode = currentNode.prev
                _index -= 1
            newNode.next = currentNode.next
            currentNode.next = newNode
            newNode.prev = currentNode
            
            if newNode.next == None:
                self.lastNode = newNode
            elif newNode.prev == None:
                self.firstNode = newNode
                
    def insertFirst(self, value):
        newNode = Node(value)

        newNode.next = self.firstNode
        self.firstNode.prev = newNode
        self.firstNode = newNode

    def insertBefore(self, value, node:Node):
        newNode = Node(value)
        currentNode:Node = node.prev

        if currentNode == None:
            newNode.next = self.firstNode
            self.firstNode.prev = newNode
            self.firstNode = newNode
        else:
            newNode.next = currentNode.next
            currentNode.next = newNode
            newNode.prev = currentNode 
                
    def insertAfter(self, value, node:Node):
        newNode = Node(value)
        currentNode = node

        newNode.next = currentNode.next
        currentNode.next = newNode
        newNode.prev = currentNode 

        if newNode.next == None:
            self.lastNode = newNode

    def pop(self, index):
        _index = 0
        currentNode = self.firstNode       
        while _index < index:
            previousNode = currentNode
            currentNode = currentNode.next
            _index += 1
        previousNode.next = currentNode.next
        currentNode.prev = previousNode

    def remove(self, value):
        currentNode = self.firstNode       
        while currentNode.data != value:
            previousNode = currentNode
            currentNode = currentNode.next
        previousNode.next = currentNode.next
        currentNode.prev = previousNode

    def __str__(self) -> str:
        outString = ""
        currentNode = self.firstNode
        if currentNode == None:
            return outString
        else:
            while currentNode != None:
                outString += str(currentNode.data) + ", "
                currentNode = currentNode.next
        return outString[:-2]

    def ToList(self):
        lista = []
        currentNode = self.firstNode
        if currentNode == None:
            return lista
        else:
            while currentNode != None:
                lista.append(currentNode)
                currentNode = currentNode.next
        return lista

def main():
    dll = DoubleLinkedList()
    
    print(dll.count())

    dll.append(12)
    dll.append(15)
    dll.append(5)
    dll.append(98)
    dll.append(26)
    dll.append(14)
    dll.append(48)
    dll.append(56)
    dll.append(32)
    print(dll)


    dll.pop(7)
    dll.pop(5)
    dll.pop(1)

    dll.remove(48)

    dll.insert(3, 6)
    print(dll)

    dll.insertBefore(999, dll.lastNode)
    print(dll)

    dll.insertAfter(999, dll.firstNode)
    print(dll)

    dll.insertFirst(333)
    print(dll)

    dll.insertBefore(999, dll.firstNode)
    print(dll)

    dll.insertAfter(999, dll.lastNode)
    print(dll)

    lista = dll.ToList()

    listData = []
    for item in lista:
        item:Node
        listData.append(item.data)

    print(listData)

    stop = ""

main()
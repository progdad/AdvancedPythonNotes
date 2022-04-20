class Indexer:
    def __getitem__(self, index):
        return index ** 2


child = Indexer()  # child.__getitem__() is called out for child[index]
print(child[3])  # 9

for ix in range(5):
    print(child[ix])  # 0 1 4 9 16


print([1, 2, 3, 4, 5, 6, 7, 8, 9][slice(1, 7, 2)])  # [2, 4, 6]


class IndexerAndSlicer:
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, index):  # It is called out for indexing or slicing
        print('getitem:', index, end=' ; ')
        return self.data[index]


child1 = IndexerAndSlicer()
print(child1[0])  # getitem: 0 ; 5
print(child1[2:4])  # getitem: slice(2, 4, None) ; [7, 8]
print(child1[::-2])  # getitem: slice(None, None, -2) ; [9, 7, 5]

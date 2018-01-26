class Hash:
    hash = {}
    list = [4,7,12,99,35,24,23,45,13,33]   #查找的目标
    hash_length = 20                    #hash表 长度
    def __init__(self,x):               #x为要查找的值
        hash = self.hash
        list = self.list
        hash_length = self.hash_length
        for i in list:
            self.get_hash_address(i,hash,hash_length)

        address = self.search_hash(x,hash,hash_length)
        if address:
            print('存在该数字，在hash表第',address,'位')
        else:
            print('不存在')

    def get_hash_address(self,n,hash,hash_length):
        hashaddress = n % hash_length
        try:
            while (hash[hashaddress]):       #如果hash表上已有关键字，放开寻址法 寻找没有关键字的hash表
                hashaddress +=1
        except:
            pass
        hash[hashaddress] = n

    def search_hash(self,data,hash,hash_length):
        yu = data % hash_length
        while hash.get(yu) and hash.get(yu)!=data:
            yu += 1
            yu = yu % hash_length
        if hash.get(yu) == None:
            return
        return yu
        pass


myhash = Hash(int(input('要检索的数字:')))


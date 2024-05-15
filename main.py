import random 
import time 

class QuickSort:

    def __init__(self,kargolar): 
        self.list = kargolar

    def sorter(self):
        # kullanılacak verileri içeren liste
        unsortedList = self.list

        # Adım 5
        # eğer listenin eleman sayısı 1 veya 0 ise listenin kendisi döner
        # ayırma işlemi gerçekleşmez
        if len(unsortedList) == 1 or len(unsortedList) == 0 :
            return unsortedList 

        # Adım 1
        # listedeki diğer elemanlar ile kıyaslamak için
        # listenin ortasından bir elemanı pivot olarak seçer
        half = len(unsortedList) // 2
        pivot = unsortedList[half]

        # Adım 2
        # ele aldığı listeyi 3 ayrı listeye dönüştürür
        left = []
        right = []
        middle = []

        # Adım 3
        # Eğer sıralanmamış listedeki eleman pivot elemandan:
        # küçük ise sol listeye
        # büyük ise sağ listeye atar
        # eşit ise ortanca listeye atar
        for element in unsortedList:
            if pivot > element:
                left.append(element)
            elif pivot < element:
                right.append(element)
            else:
                middle.append(element)

        # Adım 4
        # daha sonra aynı uygulamayı ayırdığı listelere
        # içerisinde tek 1 eleman veya hiç eleman kalmayana kadar tekrarlar

        # Adım 6 
        # Bütün listeler birleşir
        sorted = QuickSort(left).sorter() + middle + QuickSort(right).sorter()
        return sorted


class RunTime:
    def __init__(self):
        pass

    def tester(self):
        n = int(input("\nEleman sayısı gir: ").rstrip())

        unsorted = [int(input(f"{i+1}. elemanı gir: ")) for i in range(n)]

        print()
        print("Sıralanmamış liste:", unsorted)
        print()

        start = time.time() 
        sorted = QuickSort(unsorted).sorter()
        stop = time.time()

        print("Sıralanmış liste:", sorted)
        print()

        elapsed = stop - start

        print("Performans Analizi")
        print("-" * 30)
        print(f"Test sonucu geçen süre: {elapsed}")

        return elapsed 

    def randomTest(self):
        n = int(input("\nEleman sayısı gir: "))

        unsorted = [random.randint(1,100000) for i in range(n)]

        print()
        print("Sıralanmamış liste:", unsorted)
        print()

        start = time.time() 
        sorted = QuickSort(unsorted).sorter()
        stop = time.time()

        print("Sıralanmış liste:", sorted)
        print()

        elapsed = stop - start

        print("Performans Analizi")
        print("-" * 30)
        print(f"Test sonucu geçen süre: {elapsed}")

        return elapsed 

    def quickTest(self):
        ex1 = [random.randint(1, 100000) for i in range(10)]
        ex2 = [random.randint(1, 100000) for i in range(100)]
        ex3 = [random.randint(1, 100000) for i in range(1000)]
        ex4 = [random.randint(1, 100000) for i in range(2500)]

        conditions = [ex1, ex2, ex3, ex4]
        performance = []
        for instance in conditions:
            unsorted = instance
            print()
            print("Sıralanmamış liste:", unsorted)
            print("-" * 150)

            start = time.time()  
            sorted = QuickSort(unsorted).sorter()
            stop = time.time()

            print("Sıralanmış liste:", sorted)
            print()
            elapsed = stop - start
            performance.append(elapsed)

        print("Performans Analizi")
        print("-" * 30)
        print("10, 100, 1000 ve 2500 elemanlı testler ve sonuçları:")
        print()
        for i in range(4):
            print(f"{i+1}. test sonucu geçen süre: {performance[i]}")

        return performance

    def menu(self):
        print("-----------------")
        print("Kullanıcı Menüsü")
        print("-----------------")
        print("1- Eleman Girdisi ile Test")
        print("2- Rastgele Elemanlar ile Test")
        print("3- Hızlı Test")
        print()
        secim = input("Seçim: ").lower().rstrip()
        print()

        if secim == "1":
            RunTime().tester()
        elif secim == "2":
            RunTime().randomTest()
        elif secim == "3":
            RunTime().quickTest()
        else:
            RunTime().menu()



RunTime().menu()

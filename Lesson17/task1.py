sites_list = ["for_dogs", "lading", "for sales", "for sales2", "for game", "navigator"]
done_list = []
def change_list() :
    while sites_list :
        a = sites_list.pop(0)
        done_list.append(a)
        print(f"{a} в разработке")
        print(done_list)
change_list()
for i in done_list :
    print(f"{i} - готов")






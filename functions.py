a= input('Please enter a string ')
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    print_out=sorted(d,key=d.get,reverse=True)
    for each in print_out :
        print(each,'=',d[each])
most_frequent(a)

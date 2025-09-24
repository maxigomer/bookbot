def count_words(content):
    words = content.split()
    return len(words)

def count_character(text):
    result = {}
    aux = list(text)

    for c in aux:
        x = c.lower()
        if x in result:
            result[x] += 1
        elif x not in result:
            result[x] = 1
    return result
     
def sort_on(items):
    return items["num"]

def sort_dictionary(dictionary):
    result = []

    for d in dictionary:
        aux = {
            "char": d,
            "num": dictionary[d]
        }
        result.append(aux)
    result.sort(reverse=True,key=sort_on)
    return result
def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    for i, num in enumerate(items):
        try:
            if items[i+1] < num:
                items[i] = items[i+1]
                items[i+1] = num
                bubble_sort(items)
        except IndexError:
            pass
    return items



def merge(l1, l2, out=[]):


    '''Return array of items, sorted in ascending order'''

    if l1==[]: return out+l2
    if l2==[]: return out+l1
    if l1[0]<l2[0]: return merge(l1[1:], l2, out+l1[0:1])
    return merge(l1, l2[1:], out+l2[0:1])


def quick_sort(arr):


    if len(arr) <= 1:
        return arr
    else:
         return quick_sort([x for x in arr[1:] if x<arr[0]]) + [arr[0]] + qsort([x for x in arr[1:] if x>=arr[0]])

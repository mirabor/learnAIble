from summarizer import Summarizer
from multi_rake import Rake
from to_images import show_images
import cv2 as cv
import os, shutil

path = os.path.dirname(os.path.abspath("summarize.py")) + "/images"
for filename in os.listdir(path):
    file_path = os.path.join(path, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print("Failed to delete %s. Reason: %s" % (file_path, e))

rake = Rake()

model = Summarizer()
body = """ In this chapter, we introduce another sorting algorithm: heapsort. Like merge sort,
 but unlike insertion sort, heapsort’s running time is O.nlg n/. Like insertion sort,
 but unlike merge sort, heapsort sorts in place: only a constant number of array
 elements are stored outside the input array at any time. Thus, heapsort combines
 the better attributes of the two sorting algorithms we have already discussed.
 Heapsort also introduces another algorithm design technique: using a data struc
ture, in this case one we call a “heap,” to manage information. Not only is the heap
 data structure useful for heapsort, but it also makes an efficient priority queue. The
 heap data structure will reappear in algorithms in later chapters.
 The term “heap” was originally coined in the context of heapsort, but it has since
 come to refer to “garbage-collected storage,” such as the programming languages
 Java and Lisp provide. Our heap data structure is not garbage-collected storage,
 and whenever we refer to heaps in this book, we shall mean a data structure rather
 than an aspect of garbage collection."""
result = model(body)
print(result)

keywords = rake.apply(result)
n_query = 4
for query in keywords:
    print(str(query[0]))
    show_images(str(query[0]), n_query)

x = 0

for filename in os.listdir(path):
    try:
        img = cv.imread(os.path.join(path, filename))
        cv.namedWindow("win" + str(x), cv.WINDOW_NORMAL)
        cv.imshow("win" + str(x), img)
    except:
        continue
    x += 1

cv.waitKey(0)

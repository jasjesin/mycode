# Basic file input / output
# pretty common mistake to invoke wrong name or path of file
testfile = open('test.txt')  # open the file for operations
print(testfile)
print(testfile.read())
print('Reading 2nd time: ', testfile.read())
print('Reading after setting seek to 0: ', testfile.seek(0), testfile.read(), sep='\n')
print(testfile.seek(0), testfile.readlines(), sep='\n')
print(testfile.seek(0), testfile.readlines()[2], sep='\n')
testfile.close()   # close once done working wid it

with open('test.txt') as test_file:  # default mode is ready only
    print(test_file.read())
    test_file.close()

with open('test.txt', mode='a') as a:
    a.write('\nwaheguru ji plss help')
    a.close()

with open('test.txt') as f:
    print(f.read())
    f.close()

with open('test1.txt', mode='w') as w:
    w.write('gimme strength n focus to upskill myself\n')
    w.close()

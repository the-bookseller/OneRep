list_of_ID = []
counter = 0
numbers_of_ID = int(input('Enter the numbers of ID: '))
for _ in range(1, numbers_of_ID+1):
    appending_ID = int(input('Enter the ID`s what on the work: '))
    list_of_ID.append(appending_ID)
need_ID = int(input('What ID is need find: '))
for ID in list_of_ID:
    if ID == need_ID:
        counter += 1
if counter == 1:
    print('He`s on the work')
else:
    print('None on work')






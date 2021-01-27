import random


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list):

    # Shuffle the input in place
    
    last_index = len(the_list) -1 
    
    for i in range(len(the_list)):
        random_index = get_random(i, last_index)
        if random_index != i:
            the_list[i], the_list[random_index] = the_list[random_index], the_list[i]
        

    pass


sample_list = [1, 2, 3, 4, 5]
print('Sample list:', sample_list)

print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)

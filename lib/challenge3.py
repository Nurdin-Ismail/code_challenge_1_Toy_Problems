# Challenge 3: Consonant value
# Given a lowercase string that has alphabetic characters only 
# and no spaces, return the highest value of consonant substrings.
# Consonants are any letters of the alphabet except "aeiou".
# We shall assign the following values: a = 1, b = 2, c = 3, 
# .... z = 26.

# Examples;
# For the word "zodiacs", solve("zodiacs") = 26

# For example, for the word "zodiacs", let's cross out the vowels.
#  We get: "z d cs"

# -- The consonant substrings are: "z", "d" and "cs" and the 
# values are z = 26, d = 4 and cs = 3 + 19 = 22. The highest is 26.

# For the word "strength", solve("strength") = 57.

# The consonant substrings are: "str" and "ngth" with values 
# "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. 
# The highest is 57.


def consonant_value(str1):
    alphabetic_number_position = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}

    vowels = "aeiou"

    return_value = None

    #split string by character.

    print('a' in vowels)
    print('u' in vowels)
    print('b' in vowels)
    print('a' in vowels)

    #replace vowels with empty space
    
    
    test_str = str1
    res2 = []
    for j in test_str:
        print(j)
        if j in vowels:
          test_str = test_str.replace(j,"*")
          res=test_str.split('*')
         
          
         
          print("The splitted string : " + str(res))
        
          result = ' '.join(res)
          res2 = result.split(' ')
          res2.pop()
          print(result)
          print(res2)
        else:
            continue
           
        
    
            
    print(res2)   
    numbers = []

    for j in res2:
        # if j == alphabetic_number_position[j]:
        #     print(alphabetic_number_position[j])
        print(j)
        # print(alphabetic_number_position[j])

        if len(j) > 1:
            print(len(j))
            lst = []
            for item in j:
                print(item)
                lst.append(alphabetic_number_position[item])
                print(lst)
                sum_of_nums = sum(lst)
                print(sum_of_nums)
                numbers.append(sum_of_nums)
        else:
            if j in alphabetic_number_position:
              numbers.append(alphabetic_number_position[j])
              print(alphabetic_number_position[j])

              print(numbers)


    return_value = max(numbers)
    print(return_value)

    return return_value


        
 
        
 
        




    

consonant_value('zodiac')
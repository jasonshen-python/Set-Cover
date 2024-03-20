import random

#亂數產生隨機個數的set
def generate_set():
    set_number = random.randint(3,15)

    all_list = []

    print('set_content :')
    for i in range(set_number):

        element_number = random.randint(1,10)

        locals()['set'+str(i)] = set()

        for j in range(element_number) :

            locals()['set'+str(i)].add(random.randint(1,10))
        
        print('set'+str(i), locals()['set'+str(i)])

        aug = list(locals()['set'+str(i)])
        all_list.append(aug)

    return all_list

#各個set有多少個元素在其中，由大排到小
def set_inf(set_list : list):
    list_tuple = []

    for i in range(len(set_list)):

        tmp_tuple = (i , len(set_list[i]))

        list_tuple.append(tmp_tuple)

    list_tuple = sorted(list_tuple, key = lambda x : x[1], reverse = True)
    
    return list_tuple

#檢查共含有多少個獨立元素

def ind_num(set_list: list):
    
    all_element = set()
    
    for i in set_list:
        all_element = all_element | set(i)
    
    return all_element

#----------------------------------------------------------------------

def greedy_setcover(set_list : list):
    all_element = ind_num(set_list) #檢查含有多少獨立元素
    set_info = set_inf(set_list) #計算各個set裡面的元素個數，並由大排到小
    
    set_greedy = set()
    answer_list_greedy = []
    dum = 0

    for i in set_info:
            
            set_greedy = set_greedy.union(set_list[i[0]])

            answer_list_greedy.append(i[0])

            if set_greedy == all_element :
                break
    
    return answer_list_greedy

def randomized_rounding(set_list : list):
    
    all_element = ind_num(set_list) #檢查含有多少獨立元素
    
    set_random = set()
    answer_list_random = []

    for i in range(50):
        set_prob = []
        for j in range(len(set_list)):
            set_prob.append(random.random())
        print('{}_set_prob = '.format(i), set_prob)
        
        for h in range(len(set_list)):
            if set_prob[h] >= 0.6 and h not in answer_list_random:
                
                set_random = set_random.union(set_list[h])
                
                answer_list_random.append(h)
        
        # print('set_random = ', set_random)
        # print('answer_list_random', answer_list_random)

        if set_random == all_element:
            break
    
    return answer_list_random


if __name__ == '__main__':
    #prepared data

    set_list = generate_set()
    print('set_list = ', set_list)
    print('\n')
    print('greedy_answer = ', greedy_setcover(set_list))
    print('\n')
    print('randomized_answer = ',randomized_rounding(set_list))
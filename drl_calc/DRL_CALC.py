# FIND THE STRING
# CONTINUE FROM HERE

def obj_tieu_chi_index(tieu_chi_index):
    '''
        input : (int) index of a tieu chi
        output: (Tieu_chi) that Tieu_chi
    '''
    for tieu_chi_obj in tieu_chi_objs:
        if tieu_chi_obj.index == tieu_chi_index:
            return tieu_chi_obj 
            

class Tieu_chi(object):
    def __init__(self, name):
        '''
            Example: self = tieu_chi_objs[0]:
            
            self.name = '100. Điểm học tập (Tối đa: 30)'
            self.index = 100
            self.point = 30
            self.description = '(30) Điểm học tập'
            __str__() = '100. (30) Điểm học tập'
        '''
        self.name = name
        self.index = int(name[:3])
        self.max_point = int( self.name.split()[-1].strip(')') )
        self.description = '(%i) ' % self.max_point + \
                           ' '.join(self.name.split()[1:-3])
        self.current_point = 0
        
        
    def __str__(self):
        '''
            __str__() = '    420. (4) Có các thành tích trong học tập và rèn luyện'
        '''
        indent_str = ''
        if self.index % 10 != 0:
            indent_str += ' ' * 8
        elif self.index % 100 != 0:
            indent_str += ' ' * 4
            
        shorten_name_str = self.name.split()[0] + ' '
        shorten_name_str += str('(%i) ' % self.max_point)
        shorten_name_str += ' '.join(self.name.split()[1:-3])
        
        return indent_str + shorten_name_str


class Hoat_dong(object):
    def __init__(self, name, dict_of_indexes_point):
        self.name = name
        self.dict_of_indexes_point = dict_of_indexes_point
    
    # CONTINUE FROM HERE 1


# READ TIEU_CHI, create tieu_chi_objs
tieu_chi_objs = list()
with open('TIEU_CHI_utf8.txt', mode = 'r', encoding = 'utf-8') as f:
    for line in f:
        if line[0].isnumeric():
            tieu_chi_objs.append(Tieu_chi(line.rstrip()))
            
            
# READ HOAT_DONG, create hoat_dong_objs
hoat_dong_objs = list()
with open('HOAT_DONG_utf8.txt', mode = 'r', encoding = 'utf-8') as f:
    while True:
        try:
            dict_of_indexes_point = dict()
            
            hoat_dong_name = f.readline().rstrip()
            print(hoat_dong_name)
            
            amount_tieu_chi = int(f.readline().rstrip())
            print(amount_tieu_chi)
            

                            
            for i in range(amount_tieu_chi):
                
                tieu_chi_index = int(f.readline().rstrip())
                dict_of_indexes_point[tieu_chi_index] = 0
                print(tieu_chi_index, ': ', end = '')
                print(obj_tieu_chi_index(tieu_chi_index).description)
            
            hoat_dong_objs.append(Hoat_dong(hoat_dong_name, dict_of_indexes_point))
            print(dict_of_indexes_point)
            
            # CONTINUE FROM HERE 2
         
        except:
            break
             

# RUN ALGORITHM
tieu_chi_list 





             
'''
for ele in tieu_chi_objs:
    print(ele)
'''







'''
        if len(self.name.split()) < 6 + 5:
            shorten_name_str += self.name
        else:
            shorten_name_str += ' '.join(self.name.split()[1:7]) + ' ... ' 
            shorten_name_str += ' '.join(self.name.split()[-12:-3])
'''


'''
def calc_sum_drl():
    for tieu_chi_obj in tieu_chi_objs:
        if tieu_chi_obj.index % 10 != 0: # 311
            sub_tieu_chi_index = tieu_chi_obj.index // 10 * 10 # 310
            obj_tieu_chi_index(sub_tieu_chi_index).current_point += \
                (tieu_chi_obj.index).

def test_each_tieu_chi(number_of_hoat_dong):
    hoat_dong_obj = hoat_dong_objs[number_of_hoat_dong]
    
    for tieu_chi_index in hoat_dong_obj.dict_of_indexes_point:
        max_point_of_this_index = obj_tieu_chi_index(tieu_chi_index).max_point
        obj_tieu_chi_index(tieu_chi_index).current_point = max_point_of_this_index            
        hoat_dong_obj.dict_of_indexes_point[tieu_chi_index] = max_point_of_this_index
            
        for loop_index in hoat_dong_obj.dict_of_indexes_point:
            if loop_index != tieu_chi_index:
                obj_tieu_chi_index(loop_index).current_point = 0
                hoat_dong_obj.dict_of_indexes_point[loop_index] = 0
        
        sum_drl = calc_sum_drl()
        if sum_drl > max_sum_drl:
            max_sum_drl = sum_drl
        
        
        if available_test_each_tieu_chi:
            try:
                test_each_tieu_chi(number_of_hoat_dong + 1)
            except:
                available_test_each_tieu_chi = False
            
        
        print(hoat_dong_obj.dict_of_indexes_point)

max_sum_drl = 0
available_test_each_tieu_chi = True
test_each_tieu_chi(0)
'''

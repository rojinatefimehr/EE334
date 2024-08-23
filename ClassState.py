
#hex base in order to convert it later to an integer 
hex_base =16
# 10 bit used for indexing 
index_bites =10 
# extract the index bit 
index_ex =(1 << index_bites)-1  
# shift to right for ajusting the indexing 
shift =2 

class BTBEntry:
    def __init__(self, current_pc, target_pc):
        self.current_pc = current_pc
        self.target_pc = target_pc
        self.prediction = '00'  # default prediction state set to '00'
    
    def taken_prediction(self):
        # Update prediction state when branch is taken
        if self.prediction == '00':
            self.prediction = '00'
        elif self.prediction == '01':
            self.prediction = '00'
        elif self.prediction == '10':
            self.prediction = '01'
        elif self.prediction == '11':
            self.prediction = '10'

    def not_taken_prediction(self):
        # Update prediction state when branch is not taken
        if self.prediction == '00':
            self.prediction = '01'
        elif self.prediction == '01':
            self.prediction = '10'
        elif self.prediction == '10':
            self.prediction = '11'
        elif self.prediction == '11':
            self.prediction = '11'
            
    # set the current pc
    def get_current_pc(entry, current_pc):
        entry.current_pc = current_pc
# set the target pc
    def get_target_pc(entry, target_pc):
        entry.target_pc = target_pc

def is_taken (p, target_pc_int):
   if  p+4 != target_pc_int:
       return True

def is_not_taken (p, target_pc_int):
   if  p+4 ==target_pc_int:
       return True


def get_btb_index(pc):
    # calculte the index and conver the hexdecimal 
    full_pc = int(pc, hex_base)
    return (full_pc >>shift) & index_ex

def simulate_BTB():
    # intilize btb from 0 and index 1024
    btb = [None] * (1<<index_bites)
    instruction_count = 0 
    hit = 0
    miss = 0
    right =0
    wrong = 0
    wrong_addr =0
    collision = 0
    taken_predictions =0 

    with open("trace.txt", "r") as file:
        lines = file.readlines()
        current_pc = lines[0].strip()
        # if the target pc is not in btb break
        for target_pc in lines[1:]:
            target_pc = target_pc.strip()
            if not target_pc:
                break
            instruction_count += 1
            btb_index = get_btb_index(current_pc)
            current_pc_int = int(current_pc, hex_base)
            target_pc_int = int(target_pc, hex_base)
            entry = btb[btb_index]
            # if the entities matches the current pc
            if entry and entry.current_pc == current_pc_int:
                hit += 1
                pred_PC = entry.target_pc
                # taken 
                # if taken right+1 , taken+1, and update BTB
                if entry.prediction in ['00', '01']:
                    if target_pc_int == pred_PC:
                        entry.taken_prediction()
                        taken_predictions += 1
                        right += 1
                    else:
                        wrong += 1
                        if is_not_taken (current_pc_int, target_pc_int):
                            entry.not_taken_prediction()
                        else:
                            wrong_addr += 1
                            taken_predictions += 1
                            entry.target_pc = target_pc_int    
                else:
                    if is_not_taken (current_pc_int, target_pc_int):
                        entry.not_taken_prediction()
                        right += 1
                        
                    else:
                        entry.taken_prediction()
                        taken_predictions += 1
            
                        wrong += 1
            else:
                # if it is taken update the btb 
                if is_taken(current_pc_int, target_pc_int):
                    btb[btb_index] = BTBEntry(current_pc_int, target_pc_int)
                    collision += 1
                    taken_predictions += 1
                    miss += 1
            current_pc = target_pc

    # Output results
    print(f"Total Instructions: {instruction_count}")
    print(f"Hit: {hit}")
    print(f"Miss: {miss}")
    print(f"Right: {right}")
    print(f"Wrong: {wrong}")
    print(f"Taken_Branch: {taken_predictions}")
    print(f"Collision: {collision}")
    print(f"Hit Rate: {hit / (hit + miss) * 100:.2f}%")
    print(f"Accuracy: {right / hit * 100:.2f}%")
    print(f"Wrong Percentage: {wrong_addr / wrong * 100:.2f}%")
    # print the entities
    for i, entry in enumerate(btb):
        if entry:
            print(f"{i}    {entry.current_pc:x}    {entry.target_pc:x}    {entry.prediction}")

if __name__ == "__main__":
    simulate_BTB()


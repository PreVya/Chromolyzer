#FOR QUESTION SET 7-9
import random

def assign_weights_linearly(color):
    color_order = ['Blue', 'Purple', 'Pink','Red', 'Orange', 'Yellow','Green']
    
    # Find the index of the color in the order
    index = color_order.index(color)
    
    # Linear distribution
    max_weight = 97
    min_weight = 5 
    weight = max_weight - (index * ((max_weight - min_weight) / (len(color_order) - 1)))
    weight = max(min_weight, weight)
    return round(weight,2) 

#next function
def weights_cal(u1,u2,u3):
    hues = {'Red': 1, 'Orange': 30, 'Yellow': 60, 'Green': 120, 'Blue': 240, 'Purple': 276.9, 'Pink': 349.5}
    #3 inputs 3 questions
    user_ip1=u1
    user_ip2=u2
    user_ip3=u3
    user_ips=[user_ip1,user_ip2,user_ip3]

    for user_ip in user_ips:
        color_range=[]
        print(user_ip)
        if user_ip > max(hues.values()):
            color_range.append((list(hues.keys())[0],360+list(hues.values())[0],abs(360+list(hues.values())[0]-user_ip)))
            color_range.append((list(hues.keys())[-1],list(hues.values())[-1],abs(list(hues.values())[-1]-user_ip)))
        else:
            color_range_sorted = sorted(hues.keys(), key=lambda x: abs(hues[x] - user_ip))[:2]
            color_range = [
                (color_range_sorted[0], hues[color_range_sorted[0]], round(abs(hues[color_range_sorted[0]] - user_ip), 2)),
                (color_range_sorted[1], hues[color_range_sorted[1]], round(abs(hues[color_range_sorted[1]] - user_ip), 2))
            ]
        print(color_range, end=" ")
        if color_range[0][2] == color_range[1][2]:
            closest=color_range[0]
            farthest=color_range[1]
        else:
            closest= min(color_range, key=lambda x:x[2])
            farthest= max(color_range, key=lambda x:x[2])

        print("Closest:",closest, end=" ")
        print("Farther:",farthest, end=" ")
        
        lower_bound = closest[1]
        upper_bound = farthest[1]

        # Calculate the percentage in range
        total_diff = abs(farthest[1]-closest[1])  
        percentage_in_range = abs((user_ip - lower_bound) / total_diff) * 100

        print(f"\nPercentage in range: {percentage_in_range}%", end=" ")
        
        weight_closest = weights_dict[closest[0]]
        weight_farthest = weights_dict[farthest[0]]
        if user_ip < closest[1]:
            weight_user_ip = weight_closest + (percentage_in_range / 100) * abs(weight_farthest - weight_closest)
        else:
            weight_user_ip = weight_closest + (percentage_in_range / 100) * (weight_farthest - weight_closest)
        print(f"Weight : {weight_user_ip}")
        wts.append((round(weight_user_ip,2),closest[0]))
        print()

    print(wts)
    emp_per=calculate_social_incli(wts)
    if emp_per > 97:
        emp_per = 97 - abs(97 - emp_per)
    print('%.2f'%emp_per)
    return emp_per


# Function to calculate emotional resilience percentage for each set
def calculate_social_incli(wts):
    emp_per=[]
    for i in range(3):
        tpl=wts[i]
        hue_weight=tpl[0]
        color=tpl[1]
        total_score = 0
        total_weight = 0
        if i==0:
            score = scoring_dict['Ques1'].get(color, 0)
            question_weight = ques_wt['Ques1']
            contribution = score * question_weight * hue_weight
            total_score += contribution
            total_weight += question_weight * hue_weight
            
        elif i==1:
            score = scoring_dict['Ques2'].get(color, 0)
            question_weight = ques_wt['Ques2']
            contribution = score * question_weight * hue_weight
            total_score += contribution
            total_weight += question_weight * hue_weight
            
        elif i==2:
            score = scoring_dict['Ques3'].get(color, 0)
            question_weight = ques_wt['Ques3']
            contribution = score * question_weight * hue_weight
            total_score += contribution
            total_weight += question_weight * hue_weight
    
        # Calculate the weighted average
        max_score = max(scoring_dict['Ques1'].values())
        percentage = (total_score / total_weight) / max_score * 100
        percentage += random.uniform(-1, 1)
    
    # Ensure the final percentage is within the desired range
        percentage = max(0, min(percentage, 100))
        emp_per.append(percentage)  
    print(emp_per)
    return round(sum(emp_per)/3 ,2 )


#main
scoring_dict = {
    'Ques1': {'Red': 4, 'Orange': 3, 'Yellow':2, 'Green':1, 'Blue': 7, 'Purple':6,'Pink': 5},
    'Ques2': {'Red': 4, 'Orange': 3, 'Yellow':2, 'Green':1, 'Blue': 7, 'Purple':6,'Pink': 5},
    'Ques3': {'Red': 4, 'Orange': 3, 'Yellow':2, 'Green':1, 'Blue': 7, 'Purple':6,'Pink': 5}
} 
ques_wt={
    'Ques1':2,
    'Ques2':3,
    'Ques3':1
}
colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Pink']
wts=[]
weights_dict = {}
for color in colors:
    weight = assign_weights_linearly(color)
    weights_dict[color] = weight

print("Weights dictionary:", dict(sorted(weights_dict.items(), key=lambda item: item[1])))
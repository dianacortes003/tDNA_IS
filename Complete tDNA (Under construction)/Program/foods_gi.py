'''
COMPLETE VERSION

The program contains dictionaries representing different food categories
with their glycemic indices. 
It classifies each dictionary into a corresponding list of
high, medium, or low glycemic index.
Contains functions to format lists.

Input: No external input used
Output: 3 lists containin 5-7 dictionaries depending on filtering criteria
'''

#FUNCTIONS

def classify_foods_by_gi(food_categories):
    high_gi = []
    med_gi = []
    low_gi = []

    #Classify each food item into high med or low
    for category_name, foods in food_categories.items():
        high_dict = {}
        med_dict = {}
        low_dict = {}
        for food, gi in foods.items():
            if gi >= 70:
                high_dict[food] = gi
            elif 56 <= gi <= 69:
                med_dict[food] = gi
            elif gi <= 55:
                low_dict[food] = gi
        if high_dict:
            high_gi.append({category_name: high_dict})
        if med_dict:
            med_gi.append({category_name: med_dict})
        if low_dict:
            low_gi.append({category_name: low_dict})
    
    return high_gi, med_gi, low_gi


def format_gi_foods(high_gi, med_gi, low_gi):
    """Returns a formatted string with GI foods grouped by category"""

    lines = []
    #1. Check if patient gets high and med GI lists
    if len(high_gi) > 0:
        lines.append("High GI foods by category:")
        for category in high_gi:
            for name, foods in category.items():
                lines.append(f"  {name.replace('_', ' ').title()}:")
                for food, gi in foods.items():
                    lines.append(f"    - {food} (GI: {gi})")
        lines.append("")

    if len(med_gi) > 0:
        lines.append("Medium GI foods by category:")
        for category in med_gi:
            for name, foods in category.items():
                lines.append(f"  {name.replace('_', ' ').title()}:")
                for food, gi in foods.items():
                    lines.append(f"    - {food} (GI: {gi})")
        lines.append("")

    #2. Append low GI list
    #No conditional, all patient get low GI list
    lines.append("Low GI foods by category:")
    for category in low_gi:
        for name, foods in category.items():
            lines.append(f"  {name.replace('_', ' ').title()}:")
            for food, gi in foods.items():
                lines.append(f"    - {food} (GI: {gi})")
    lines.append("")

    return "\n".join(lines)

def get_formatted_foods(recs):
    """Returns formatted string of GI foods based on patient recommendations"""

    high_gi, med_gi, low_gi = classify_foods_by_gi(food_categories)

    if "Follow low-GI foods" in recs:
        return format_gi_foods([], [], low_gi)
    else:
        return format_gi_foods(high_gi, med_gi, low_gi)
    

###############################################################################
###############################################################################

#DATA

#Common international foods and glycemic indices
common_foods = {
    "White wheat bread": 75,
    "Whole wheat bread": 74,
    "Multigrain bread": 53,
    "Wheat roti": 62,
    "Chapati": 52,
    "Corn tortilla": 46,
    "White rice": 73,
    "Brown rice": 68,
    "Barley": 28,
    "Corn": 52,
    "Spaghetti": 49,
    "Rice noodles": 53,
    "Udon noodles": 55,
    "Couscous": 65
}

dairy = {
    "Whole milk": 39,
    "Skim milk": 37,
    "Soy milk": 37,
    "Rice milk": 86,
    "Ice cream": 51,
    "Yogurt": 41
}

cereals = {
    "Cornflakes": 81,
    "Rolled oat meal": 55,
    "Instant oat meal": 79,
    "Rice congee": 78,
    "Muesli": 57,
    "Millet porridge": 67,
    "Biscuits": 69
}

fruits = {
    "Apple": 36,
    "Banana": 51,
    "Dates": 42,
    "Mango": 51,
    "Orange": 43,
    "Peaches": 43,
    "Pineapple": 59,
    "Watermelon": 76
}

vegetables = {
    "Potato, boiled": 78,
    "Potato, instant mash": 87,
    "Potato, fried": 63,
    "Sweet potato": 63,
    "Carrots, boiled": 39,
    "Pumpkin, boiled": 64,
    "Plantain": 55,
    "Taro, boiled": 53,
    "Vegetable soup": 48
}

legumes = {
    "Chickpeas": 28,
    "Kidney beans": 24,
    "Lentils": 32,
    "Soy beans": 16
}

snacks = {
    "Chocolate": 40,
    "Popcorn": 65,
    "Potato chips": 56,
    "Soda": 59
}

#Dictionary of all categories
food_categories = {
    "common_foods": common_foods,
    "dairy": dairy,
    "cereals": cereals,
    "fruits": fruits,
    "vegetables": vegetables,
    "legumes": legumes,
    "snacks": snacks
}

###############################################################################
###############################################################################



def open_or_senior(data):
           
    return [
            'Senior'if (age >= 55) and (handicap > 7)    
             else 'Open'
             for (age,handicap) in data         
    ]
print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))
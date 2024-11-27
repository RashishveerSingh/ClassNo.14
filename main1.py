def total_kalkulasion(bil_very_expensive,tip_from_rich_people):
    '''herro mai naim is fanksion'''


    total = bil_very_expensive * (1 + 0.01 * tip_from_rich_people)
    total = round(total , 2)

    print(f"pls gimme your dola dolla ${total}")

print(total_kalkulasion.__doc__)

total_kalkulasion(1700,20)

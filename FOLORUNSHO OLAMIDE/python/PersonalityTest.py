optionA = []
optionB = []
invalid = []
countA = 0
countB = 0
count = 0

name = input("What is your fullname: ")

print("QUESTION 1. You regularly make new friends.\n")
noOneQuestion = input("A.Agree        B.DisAgree:").upper()
if noOneQuestion == "A":
    optionA.append("A.Agree")
    countA += 1
elif noOneQuestion == "B":
    optionB.append("B.DisAgree")
    countB += 1
else:
    invalid.append("invalid input")
    count += 1

print("QUESTION 2. Complex and novel ideas excite you more than simple and straightforward ones.\n")
noTwoQuestion = input("A.Agree        B.DisAgree:").upper()
if noTwoQuestion == "A":
    optionA.append("A.Agree")
    countA += 1
elif noTwoQuestion == "B":
    optionB.append("B.DisAgree")
    countB += 1
else:
    invalid.append("invalid input")
    count += 1

print("QUESTION 3. You usually feel more persuaded by what resonates emotionally with you than by factual arguments.\n")
noThreeQuestion = input("A.Agree        B.DisAgree:").upper()
if noThreeQuestion == "A":
    optionA.append("A.Agree")
    countA += 1
elif noThreeQuestion == "B":
    optionB.append("B.DisAgree")
    countB += 1
else:
    invalid.append("invalid input")
    count += 1

print("QUESTION 4. Your living and working spaces are clean and organized.\n")
noFourQuestion = input("A.Agree        B.DisAgree:").upper()
if noFourQuestion == "A":
    optionA.append("A.Agree")
    countA += 1
elif noFourQuestion == "B":
    optionB.append("B.DisAgree")
    countB += 1
else:
    invalid.append("invalid input")
    count += 1

print("QUESTION 5. You usually stay calm, even under a lot of pressure.\n")
noFiveQuestion = input("A.Agree        B.DisAgree:").upper()
if noFiveQuestion == "A":
    optionA.append("A.Agree")
    countA += 1
elif noFiveQuestion == "B":
    optionB.append("B.DisAgree")
    countB += 1
else:
    invalid.append("invalid input")
    count += 1

print("QUESTION 6. You find the idea of networking or promoting yourself to strangers very daunting.\n")
noSixQuestion = input("A.Agree        B.DisAgree:").upper()
if noSixQuestion == "A":
    optionA.append("A.Agree")
    countA += 1
elif noSixQuestion == "B":
    optionB.append("B.DisAgree")
    countB += 1
else:
    invalid.append("invalid input")
    count += 1

print("QUESTION 7. You prioritize and plan tasks effectively, often completing them well before the deadline.\n")
noSevenQuestion = input("A.Agree        B.DisAgree:").upper()
if noSevenQuestion == "A":
    optionA.append("A.Agree")
    countA += 1
elif noSevenQuestion == "B":
    optionB.append("B.DisAgree")
    countB += 1
else:
    invalid.append("invalid input")
    count += 1

print("QUESTION 8. People’s stories and emotions speak louder to you than numbers or data.\n")
noEightQuestion = input("A.Agree        B.DisAgree:").upper()
if noEightQuestion == "A":
    optionA.append("A.Agree")
    countA += 1
elif noEightQuestion == "B":
    optionB.append("B.DisAgree")
    countB += 1
else:
    invalid.append("invalid input")
    count += 1

print("QUESTION 9. You like to use organizing tools like schedules and lists.\n")
noNineQuestion = input("A.Agree        B.DisAgree:").upper()
if noNineQuestion == "A":
    optionA.append("A.Agree")
    countA += 1
elif noNineQuestion == "B":
    optionB.append("B.DisAgree")
    countB += 1
else:
    invalid.append("invalid input")
    count += 1

print("QUESTION 10. Even a small mistake can cause you to doubt your overall abilities and knowledge.\n")
noTenQuestion = input("A.Agree        B.DisAgree:").upper()
if noTenQuestion == "A":
    optionA.append("A.Agree")
    countA += 1
elif noTenQuestion == "B":
    optionB.append("B.DisAgree")
    countB += 1
else:
    invalid.append("invalid input")
    count += 1

print("QUESTION 11. You feel comfortable just walking up to someone you find interesting and striking up a conversation.\n")
noElevenQuestion = input("A.Agree        B.DisAgree:").upper()
if noElevenQuestion == "A":
    optionA.append("A.Agree")
    countA += 1
elif noElevenQuestion == "B":
    optionB.append("B.DisAgree")
    countB += 1
else:
    invalid.append("invalid input")
    count += 1

print("QUESTION 12. You are not too interested in discussions about various interpretations of creative works.\n")
noTwelveQuestion = input("A.Agree        B.DisAgree:").upper()
if noTwelveQuestion == "A":
    optionA.append("A.Agree")
    countA += 1
elif noTwelveQuestion == "B":
    optionB.append("B.DisAgree")
    countB += 1
else:
    invalid.append("invalid input")
    count += 1

print("QUESTION 13. You prioritize facts over people’s feelings when determining a course of action.\n")
noThirteenQuestion = input("A.Agree        B.DisAgree:").upper()
if noThirteenQuestion == "A":
    optionA.append("A.Agree")
    countA += 1
elif noThirteenQuestion == "B":
    optionB.append("B.DisAgree")
    countB += 1
else:
    invalid.append("invalid input")
    count += 1

print("QUESTION 14. Even a small mistake can cause you to doubt your overall abilities and knowledge.\n")
noFourteenQuestion = input("A.Agree        B.DisAgree:").upper()
if noFourteenQuestion == "A":
    optionA.append("A.Agree")
    countA += 1
elif noFourteenQuestion == "B":
    optionB.append("B.DisAgree")
    countB += 1
else:
    invalid.append("invalid input")
    count += 1

print("QUESTION 15. You often allow the day to unfold without any schedule at all.\n")
noFifteenQuestion = input("A.Agree        B.DisAgree:").upper()
if noFifteenQuestion == "A":
    optionA.append("A.Agree")
    countA += 1
elif noFifteenQuestion == "B":
    optionB.append("B.DisAgree")
    countB += 1
else:
    invalid.append("invalid input")
    count += 1

print("QUESTION 16. You rarely worry about whether you make a good impression on people you meet.\n")
noSixteenQuestion = input("A.Agree        B.DisAgree:").upper()
if noSixteenQuestion == "A":
    optionA.append("A.Agree")
    countA += 1
elif noSixteenQuestion == "B":
    optionB.append("B.DisAgree")
    countB += 1
else:
    invalid.append("invalid input")
    count += 1

print("QUESTION 17. You enjoy participating in team-based activities.\n")
noSeventeenQuestion = input("A.Agree        B.DisAgree:").upper()
if noSeventeenQuestion == "A":
    optionA.append("A.Agree")
    countA += 1
elif noSeventeenQuestion == "B":
    optionB.append("B.DisAgree")
    countB += 1
else:
    invalid.append("invalid input")
    count += 1

print("QUESTION 18. You enjoy experimenting with new and untested approaches.\n")
noEighteenQuestion = input("A.Agree        B.DisAgree:").upper()
if noEighteenQuestion == "A":
    optionA.append("A.Agree")
    countA += 1
elif noEighteenQuestion == "B":
    optionB.append("B.DisAgree")
    countB += 1
else:
    invalid.append("invalid input")
    count += 1

print("QUESTION 19. You prioritize being sensitive over being completely honest.\n")
noNineteenQuestion = input("A.Agree        B.DisAgree:").upper()
if noNineteenQuestion == "A":
    optionA.append("A.Agree")
    countA += 1
elif noNineteenQuestion == "B":
    optionB.append("B.DisAgree")
    countB += 1
else:
    invalid.append("invalid input")
    count += 1

print("QUESTION 20. You actively seek out new experiences and knowledge areas to explore.\n")
noTwentyQuestion = input("A.Agree        B.DisAgree:").upper()
if noTwentyQuestion == "A":
    optionA.append("A.Agree")
    countA += 1
elif noTwentyQuestion == "B":
    optionB.append("B.DisAgree")
    countB += 1
else:
    invalid.append("invalid input")
    count += 1

print(name)
print(optionA)
print(optionB)
print(invalid)
print("Total 'Agree' responses:", countA)
print("Total 'DsAgree' responses:", countB)
print("Total 'invalid input' responses:", count)

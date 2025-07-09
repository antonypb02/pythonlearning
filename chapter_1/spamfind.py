p1="hi"
p2="ads"
p3="comment"


message=input("enter ur message")

if any(p in message for p in [p1,p2,p3]):
    print("spam")

else:
    print("no spam")
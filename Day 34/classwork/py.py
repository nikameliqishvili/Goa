def newlist():
    st = "eee ladooo rogor xar"
    sia = st.split()
    new =[]
    for i in sia:
        if len(i) > 4: 
            new.append(i)
    print(new)
newlist()
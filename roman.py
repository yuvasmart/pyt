def  main():
    rom=input().upper()
    values={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    output=0
    for i in range(len(rom)):
        if i > 0 and values[rom[i]] > values[rom[i-1]]:
            output+=values[rom[i]]-2*values[rom[i-1]]
        else:
            output += values[rom[i]]
    print(output)

if __name__ == '__main__':
    main()
